This project is written in python 3.8. Currently the only method to run it is to navigate to the hsBattleGrounds and run

python3.8 cli.py

To run the test suite:

python3.8 -m pytest

Running this with a python version prior to 3.8 will fail because earlier python versions lack walruses.
This project in written in 3.8 in appreciation of the [majestic walrus](https://i.redd.it/iat5vyqabtzx.jpg). := := :=
---

This project is intended to simulate battles in Hearthstone Battlegrounds, primarily for the purpose of working out exactly how unlucky you were when you lost to that board.

This is not intended to be a fully accurate remaking of the Hearthstone engine - such a project would take planning time to ensure everything worked properly. Rather, this just needs to work well enough, without being too much of a hassle to update.

Currently, there is only a very basic command line interface. In the future, this will be scaled up to either a web interface, or something else graphical.

Battles are handled through the GameManager object, which much be initialised with an instance of a MinionRepository. Minions can be added to either players board using the assign_minion_to_board method.

Battles can either be run in full using the run_full_combat method, or step by step using combat_step and combat_substep methods.

---

Heathstone uses stack method for resolving game events, similar to Magic the Gathering. However, due to the digital nature of the game, there are some notable differences:
  - Stacks rarely grow beyond two or three events, since the stack must be cleared before any new action can be taken by a player
  - In magic, if two events would simultaneously enter the stack, their controller can choose which order they enter in. In Heathstone, this is entirely determined programatically.
    - I am currently unsure of the full rules for e.g. deathrattle order resolution in Battlegrounds. Currently, these are corner cases, but over time the simulation should become more accurate
  
Events can be added to the stack at almost any time, such as:
  - When any minion attacks,
  - When a specific minion attacks,
  - When a minion is attacked,
  - When a minion deals damage,
  - When a minion receives damage,
  - When a minion dies,
  - When a minion kills another minion,
  - When a minion kills another minion with more damage than its current health,
  - When a minion enters the battlefield,
  - When a minion of a specific tribe enters the battlefield,

Etc., etc.,

---

In Battlegrounds, the player has no direct control over the battles their minions fight. Rather, the gameplay loop involves building and managing their army in between rounds, then watching the sparks fly. Minions take turns attacking one at a time, alternating between each player. The attack order for minions is, on the face of it, simple: they attack from left to right. However, there are some complications involved when new minions enter the battlefield.
  - If minions enter the battlefield to the left of the most recent attacker, they will not attack until the attack order wheels back round to them
  - If they enter to the right, they will attack when the attack order reaches them
  - If the most recent attacking minion caused some minions to enter the battlefield, those minions will attack next.
This turned out to be more difficult to implement than I imagined - the attack order needs to look at specific minions and their ancestry to determine attack order.
Since minions will always spawn minions directly to the right of themselves (or, if the spawning minion dies, in its place), it can be assumed that, if that minion is the most recent attacker, the next attacker will be its left-most child.

There are some notable complications to be accounted for, involving the secrets [Venomstrike Trap](https://hearthstone.gamepedia.com/Venomstrike_Trap), [Snake Trap](https://hearthstone.gamepedia.com/Snake_Trap) and [Splitting Image](https://hearthstone.gamepedia.com/Splitting_Image), and the minion [The Beast](https://hearthstone.gamepedia.com/The_Beast).
  - Venomstrike trap and snake trap will spawn their minions on the right of the battlefield. To avoid these minions potentially missing their attacks if they are spawned in during the previous rightmost minions attacks, any minion which is spawned on the right of the board is immediately added to the "next potential attackers" list the MinionBoard object uses to determine the next attacker.
  - Splitting image, unlike the other two secrets, spawns its minion directly to the right of the minion it is attacking. This can be accounted for by treating the new minion as a child of the minion it is copying.
  - "The Beast", upon death, summons a minion for its owners opponent. As this minion spawns in on the right of the board, it can be handled in the same manner as Venomstrike and snake traps.

---

There are some rules complications involving exactly when minions die which need to be clarified. A notable example is with the minion [Security Rover](https://hearthstone.gamepedia.com/Security_Rover).
Upon taking damage, Security Rover will spawn a minion to its right. This occurs even when it takes lethal damage (Though not if it is destroyed without taking damage). If the board is full (7 minions is the most a player board can hold), it will fail to spawn a minion.

The notable part is that, if it takes lethal damage while being on a full board, it will try and fail to spawn a minion, and then die.
This is a notable difference to Magic the Gathering, where Security Rover would always die before its minion spawning ability resolved. The inference here is that minions are not checked for death after every ability is resovled. Currently, I am unsure of the exact times hearthstone checks for minion deaths, but this adds complications to resolving the combat stack (as checking for death after each event resolution will not work).
