# social_story_and_cookbook_puzzles

(under construction)

AI RPG-Arena
Social Story Puzzles & 'Pointless' Cookbook/Logistics Puzzles
for Teaching, Training and Evaluation


2024.05-06.22, 2026.04.21 G.G.Ashbrook

As a continuation of our discussion of testing from "Let's Test Models", "Ants vs. AI" and "The Jellyfish Spidercrab," and part of the larger discussion of how to create and use tests and metrics in "Stem Net Benchmarks", let's look at two groups of puzzles that we can automatically generate for people or machines to be tested with, or to train with, or both.

This is part of layered puzzles of stories, skills, and learning and layered stories about puzzles, skills and learning. How do we, how can we, and how should we, design and implement environments for learning? 

# Introduction

How is a marketplace like, and how unlike, a dungeon for adventurers? In real-world stories where people need to learn skills, how are those 'learning environments' shaped and managed? Can and should games and puzzles be used to teach real world skills? In machine learning where testing and training data are often needed in large quantities (both to create a machine for a task and to evaluate how good that machine is at a task), can skills and concepts be supported by enough data describing both tasks and errors? 


### Code Git Repo:
- https://github.com/stemnetbenchmarks/social_story_and_cookbook_puzzles 

### Live Notebooks in Colab:
- https://drive.google.com/drive/folders/1ETOeXGSF52_lkclJ7W_xSJNEZC0OEMz_ 


# Functionality
While there may be a fun-ish game in here somewhere, the overall context is intended to be no-less STEM/Academic: Can we find an intersection between formal-tests and well-defined evaluations that can be analyzed on the one hand, and on the other hand social-story puzzle-games that people participate in by choice?

Applications and uses, if ideally, include: 
1. Help people to learn more about project-problem-spaces
2. Help improve people's skills at doing projects
3. Improve (or at least study) AI-project-concept learning
4. Help people to understand the strengths and weaknesses of stateless amnesiac generative models (E.g. How can a 'super smart' model have difficulty with such a simple puzzle-task?)
5. Use and leverage problem-spaces that have a difficulty-scale.
6. Deterministically Generate N solution-testable problems in a problem-space at a given difficulty-scale.
7. Leverage solutions and errors that are analyzable, and learn about and from those errors. 

# Social Story Puzzle: Modular RPG Dungeon Crawl
RPG-SHRDLU: a story-oriented blocks-world for social, and language using, participants

We can define a type of minimal social-story-puzzle, a mini ~Multi-Player RPG (classic dungeon-crawl), that is completely defined so that players will "make" and "implement" a plan (for a given dungeon room) and run that plan through the game-outcome-calculator. Each "random-seed" (and other "configuration variables and parameters" such as how many monsters/NPCs per room) will produce a fixed (reproducible) starting-room-state and the non-random outcomes will be ~deterministically (same-input, same output) calculated and validated. Players can submit and implement their plans either 'iteratively' playing and seeing the outcomes of one round-of-turns at a time, or all-at-once (planning out the whole strategy for all rounds then running it all at once).

#### Two Modes: Incremental-Iterative or Whole-Game
```
A. Whole-Game: plan the whole 'room-story' all at once (all rounds), succeed or fail.
B. Incremental-Iterative: plan one round see what happens
```

Note: There can be other criteria for evaluating and comparing plans beyond pass-fail, e.g. some plans can require fewer steps (less time). (Linotype?)


### Social Story Puzzles vs. 'Pointless Puzzles'
In contrast, there are other deterministic puzzles (including team-project puzzles), that I nickname 'pointless puzzles,' such as project-schedule and logistics-project puzzles.

Notebook: https://colab.research.google.com/drive/1TcA_DDdX-zbewsACEhhiluxwzgvXzWdT 

"Pointless puzzles" are so nicknamed because they are not usually the kind of 'game' that most people gravitate towards for sport and amusement, they are however concretely realistic in terms of human every day tasks and technical-significance. Is it really a puzzle if there isn't anything to figure out how to do? (If only to illustrate that people do not agree about this, John von Neumann famously thought that Chess was not a game, but rather a calculation with a solution (whereas... most people do consider chess to be a game).)

Let's make the logistics-puzzle a bit less abstract.
Let's think of it as a market-place or a running a food-truck or a grocer, rather than logical operations and arrays of bits. 
Instead of numbers, let's say there is a cart with eggs, flour, salt, and spices. Alice needs to move the eggs into her shop. Bob needs to mix the flour and spices. Tom adds the salt after Cat got the egg's from Alice (and made them into Egg's Benedict with hollandaise sauce), etc. If you think of the puzzle-space, the project-space, in terms of shops and restaurants and that kind of logistics, it probably sounds more closely related to every-day life and closer to puzzles that people do (and like to do). 

But let's try to add something else to the 'problem-space' of these puzzle stories. Even the shop-logistics puzzles are still 'introverted tasks,' steps one person can read and carry out from a cookbook's list of instructions. Fortunately we (on Earth) have a widely known type of game that we can use to make (even a minimal-puzzle) something that is more creative-problem-solving, and something that requires the players to work together, coordinate (Coordinated-decisions studies!), and plan and act in communication and alignment with each-other. We have table-top Role Playing Games, we have players on a dungeon crawl.

And we can set up the 'system-mechanics' of our mini-RPG-world so that the actions and the interactions of the characters are interdependent on each other (less introverted solo-puzzles).

...


single-task reinforcement learning vs. foundation-model language-concept 'pre-train' learning

How can a model that can talk a good game and do indivdual tests and quasi-tasks do so badly at a concrete (relatively simple) situation that it would be happy to describe to you.

Question: For the whole-game solution, as with SHRDLU and Blocks-World, a reinforcement learning model would probably do well (I am guessing). But in various kinds of cut-up situations where coordinated strategy and missing information are needed, what is the potential for single-task reinforcement learning vs. a trained language-concept foundation-model?

Project and coordination decision skills are, arguably, at the forefront of STEM being either not yet or barely recognized by semi-STEM humanity as existing (let alone being of value). 

https://www.theguardian.com/games/2026/mar/16/petri-dish-brain-cells-playing-doom-cortical-labs 
...

Dimensions and operation-spaces of logistics-puzzles
- bits
- numbers
- strings

1-dimensional arrays

8x8 is a 2-D array (or set of arrays).

While and 8x8 RPG puzzle could be broken down into logistical steps,

The story-operations are such that they are not procedurally fixed with an unknown end-point, but are defined by strategic end-points with arbitrary paths to those end-states.

Furthermore, these end-point cannot be the result of introverted unilateral action, but must involve coordination.

...

Social-story puzzles are likely very close to the widely known and embraced fantasy-story multi-player role-playing-game dungeon-crawl style of game: you are in a dungeon of rooms, get past the monsters, get the treasure, work together, use a 'system-mechanic' of spells, keep your health-level above zero, participate with others in a turn-based system. While not as technically dexterous as "pointless puzzles," social-story puzzles exist more in the space of coordinated planning and decision making, if more narrow in terms of the problem-space of the problem to be solved.

a minimal starting mode of puzzles
e.g. you can run this puzzle with a chess-set on a board.


As people do not automatically have skills and fitness around following steps and instructions and narrow logical-reasoning, "Pointless Puzzles" are still highly practical, and very interesting in various ways. A more descriptive name might be "Cookbook Puzzles" or "Instruction-Following Puzzles." These are puzzles where the project requirements are laid out (perhaps like a cookbook recipe) and where the result/solution can be validated, but... these are probably (but who knows) not the kind of puzzle I can ever imagine a group of people sitting around the table excitedly having fun with. People being unpredictable, it is entirely possible the 'social cookbook recipes' could become popular, but as of 2026 table-top-style RPG stories are more popular social-games than virtual cookbook recipe following. (Though it would be interesting to have a paleontology debate about the prominence of pre-historic social-cooking vs. prehistoric social-story-telling, both are no doubt quite ancient. And if 'pack hunting' is a game, it both combines cooking with monster-hunting and pre-dates a given primate species.) 

This distinction separates solution-invention/discovery from solution-implementation. The distinction may not always be clear, but in at least some cases we may be able to meaningfully identify making strategic plans (perhaps including choices between tradeoffs) vs. implementing tactical precision where following the outcomes of rules is the focus.

In some ways there seems to be no clear dichotomy between social story puzzles and introverted logistics tasks. If you break everything down into a pile of steps then everything looks like a pile of steps. And if you look at a logistics puzzle through the context of a village marketplace, it looks like a social story. But in other ways there are differences between linear-cookbook tasks that have one process and one solution (move three eggs (or bites) from this array to that), vs. open ended problem solving where there are many (maybe infinitely many) viable solutions to the same problem. I would also question whether multi-participant-interdependent actions can or should be broken down into introverted tasks. Using dynamic feedback within a process is likely not always just another linear step in a pile of linear steps. And it is not clear how much different contexts and details matter for real world skill building and skill retention. Scalability, modularity, coordinated decisions, and various levels of perception and articulation of project-area parts are all key factors in the skills, fitness, and best practice needed to complete projects, and for a diagnostic understanding how projects fail and systems collapse. 

# Note:
Types of puzzles do not have to be diverging (and disconnected from each-other), mini-game puzzles within puzzles are well established in games.

Various types of puzzles could be combined:
- opening a chest could involve a pointless-puzzle / 8x8 'puzzle'
- beating a monster could involve an 8x8 game like chess
- opening a door, etc.
- getting a person out of another object, etc.

See:
- Sume-go puzzles


## One-Time-Test vs. Repeatability with N-inputs and N-outputs
One difference between a logistics test (where the 'solution' is a process, not an individual solution) and a social-story-puzzle (in the context here) is that you can test a given logistics solutions with N different inputs and outputs, it can operate perhaps similarly to 'unit tests' for code. The social story test is more of a dynamic coordination test, less of a static-introverted-unilateral-algorithm test. (As mentioned, combining the two may be interesting...) Both puzzles are generated ~deterministically (same input, same output) and are consistent with repeatability examination, but the language-bot process is not a static single-context artifact. 

### Chess & RPG
As somehow chess finds a way into many AI discussions: In keeping with the empirical 'pen and paper' 'tabletop' nature of (some) RPG games, the 8x8 grid and 5-player system is entirely compatible with... a physical chess board and pieces. This mini-RPG should be able to be played as a physical board game using a chess set (e.g. each player is one type of e.g. black piece, and the mobs, treasure, NPC, objects are  white pieces). 


To Recap:

A "pointless puzzle" is more of a 'can you follow directions' puzzle, rather than a, 'plan what the directions should be for this open-ended situation' puzzle. Both are very important, but they are also importantly different from each other.

Social Story Puzzles are still meant to primarily be abstract tests (they are not designed to be consumer-attractive products), but they should retain more elements of the kind of story-space and socially found solution that a tabletop RPG has.

#### Modular:
In this modular framework there is a ~most minimal starting version, but there are also many aspects that can be changed to introduce increasing 'dimensions' to the puzzle.
- More 'monsters'
- Monsters with less simple behavior
- Conditional Perception (involving more player-to-player 'cut up' coordination to solve the puzzle)
- multiple and fractional speeds of movement
- having a dungeon room inside of a ~mob/npc/object as in a puzzle in a puzzle to get an absorbed player back out.
- etc.


# Training & Testing

These puzzles can be used to either test or train:
1. Individual people (for example in an educational settings)
2. Teams of people as in a classic student-centered/constructivist 'cut-up' activity involving team-project sharing of information of group planning, (for example in educational settings)
3. Individual one-shot generative AI (or architectures) (either as an evaluation, as training-data to build up a project-space-outcomes concept-set in the model, or theoretically as part of ~reinforcement training or fine tuning).
4. Teams/Groups/Swarms of collaborating AI (either as an evaluation or as part of ~reinforcement training or fine tuning, etc.)
5. Reinforcement Learning to train (non-oneshot-pre-trained) models/architectures


# Projects:
Not surprisingly, this is also inter-related with project-spaces, coordinated decisions, hybrid data, project-object-databases, etc.:

- Definition Behavior Studies: https://github.com/lineality/definition_behavior_studies

- Hybrid (structured and unstructured data) https://github.com/lineality/hybrid_data 

- Project Areas (and project management):  https://github.com/lineality/project_areas_for_project_and_product_management 

- Coordinated Decisions: https://github.com/lineality/Networked_Voting_and_Decisions_Including_One_Time_Pads 

- Uma & T is for Task:
https://github.com/lineality/uma_productivity_collaboration_tool/blob/main/t_is_for_task.md 


# Future Research
One area that might be very important, but which is not elaborated on here, is: Generating Error-Mistake-Analysis-Data Per-Puzzle

If more-so for logistics-puzzles, it should be possible to generate some level of (reliable) automatic reporting on what went wrong with the proposed solution. This may be important to go along with raw-error data for learning processes (for people and robots (as far as we can continue to make that distinction)).


## Details:
For more technical details, see (and run!) the notebook, such as here:
LINK TO GGA-SHARED NOTEBOOK, or in github (see link above)

### Code Git Repo:
https://github.com/stemnetbenchmarks/social_story_and_cookbook_puzzles 

### Live Notebooks in Colab:
- https://drive.google.com/drive/folders/1ETOeXGSF52_lkclJ7W_xSJNEZC0OEMz_ 

Farewell, Etaoin Shrdlu.


# Links:

1. let's test models (code and paper)
https://medium.com/@GeoffreyGordonAshbrook/lets-test-models-and-let-s-do-tasks-84777f80eb99 

2. STEM-Net Benchmarks (Evaluation/Training Project)
https://github.com/orgs/stemnetbenchmarks/repositories 

3. Object relationship Space Frameworks (Set of Papers)
https://github.com/lineality/object_relationship_spaces_ai_ml 

4. Counting Tea (paper)
https://medium.com/@GeoffreyGordonAshbrook/calculating-tea-for-ai-advocating-for-architectural-learning-f2961380bc14 

5. Jellyfish Spidercrab (paper)
https://medium.com/@GeoffreyGordonAshbrook/jellyfish-spider-crab-ai-modular-architectural-learning-9b7492d68394 

6. Ants vs. AI (paper)
https://medium.com/@GeoffreyGordonAshbrook/ants-vs-ai-d4aadf537d08 

7. More on Key Concepts
https://medium.com/@GeoffreyGordonAshbrook/five-ai-concepts-ecf5c9698559 


Also See:
- https://en.wikipedia.org/wiki/Fredric_Brown 


More Game Design Discussion
- https://github.com/lineality/story_rpg_platform 


see:
https://docs.google.com/document/d/110nu9A85fVNauEB3iwTzQ1uPDMfXGJeAFi2oKFx4Jrw/edit 

links to:
1. let's test models (code and paper)
2. STEM-Net Benchmarks (Evaluation/Training Project)
3. Object relationship Space Frameworks (Set of Papers)
4. Counting Tea (paper)
5. Jellyfish Spidercrab (paper)
6. Ants vs. AI (paper)

...

No Free Lunch and the Genie In the Lamp: Picking the right question is difficult, and interpreting an answer is difficult.

Maybe related to the no-free lunch theorem itself, it is very difficult to design tests and to gauge how far to read into the results. 

....


Two main ways to play (in addition to whole-game)
1. manual iteration
2. 5-bot Arena


Being able to examine how bots succeed or fail at the puzzles


...
# Appendix 1: Discussion



# Discussion

There are many aspects to the intersection of the topics of AI, games, stories, art, social behavior, planning, projects areas, etc. (there are many aspects to just listing the aspects!). 

This focus here is on an intended to be minimal mechanical scope, without much 'story' outside of the information about what is in the room and the conversation between the players about the plan. But imagine how much less simple this problem-space would become if this were a full wizards of the coast or elderscrolls or white-wolf game. 

# Five Types of Project Puzzles
1. Bitwise Boolean
The most basic logic and boolean operations.

2. Numbers
Operations on numbers.

3. Strings
String operations.

4. 8x8
- 2D special rule games such as tic-tac-toe, connect-four, checkers, chess, iGo, etc.

5. Mini-RPG Dungeon Crawl
With a small number of rules, a multi-player dungeon-crawl can take place on an 8x8 grid with as few as 7 numbered objects on the board. This opens up the project space to coordinated decisions, cut-up puzzles, strategy and tactics, etc., as well as less-minimal RPG game and puzzle elements.  


## Asynchronous Puzzles & Race Conditions

On the one hand the pseudo-asynchronous kludge of game-rounds and simultaneous turns is an artificiality that would not map well onto a fully real-time puzzle (such as a swarm of in-motion bots). Two questions:

1. Is there a test-data-understandability problem in a deeply dynamic test where, perhaps in a context of Rust memory atomics, the states of arrays in memory are too ambiguous due to race-conditions. This may translate into the question of: if rules are so loose that mistakes break the ability to see what you did wrong (e.g. untraceable undefined behavior problems) how does that low level signal-distortion negatively affect being able to use and learn from that low-quality-learning-signal? 

2. Is there an enduring utility in iterative planning? While processes themselves may happen in a more simultaneously dynamic way 'during the agile sprint,' is there a process layer of iteration that persists even when actions themselves cannot be pre-structured in time? 

While we can create a more asynchronous version of a minimal dungeon, e.g. where bots are continually cycling through their own loops instead of stepping through an order of actions, what would that change about the overall puzzle? (Maybe we need to try and see...)

## Gamification & Blocks World

While this is speculative, it is likely worth mentioning. Historically it was difficult/ineffective to try to extend a simplified "Blocks World" bot into real-world (less-simple-world) tasks. But in some ways that early failure is an apples-to-apples (comparing the same things) comparison to the various types of machine learning, robotics, and virtual-training environments fifty or a hundred years later.

It is most likely correct to not naively assume that a simplified test will not automatically generalize across real world phenomena, but on the other hand can we avoid teaching machines to find solvable simple games within their stochastic analog rivers of input? 


## Story, Language & Games

Is there a story in this mini-RPG, or is it too minimal? We can probably agree that the logistics puzzles do not contain any story (though they can be analogized to stories). In the mechanics of the mini-RPG the characters do not 'need' to have names, or be very 'social' etc. At least hypothetically we could imagine a theatrically 'mechanical-robotic-aesthetic' but this 'hard-science-fiction, hard-neo-modern' style is a human fantasy that is, somewhat comically, completely at odds with how language-concept-foundation-models work (yet people go on with their 'I am an expressionless robot who loves numbers, 1-2-3, 1-2-3, 1-2-3, beep.' fantasies about what robot-ai is doing.

On the other hand, is the social story within the implied coordinated decision and project management layer that sits on top of the mechanics of the game? This might go back to the question of using a language-concept model vs. using a single-task reinforcement-learning modeling.

For example, could we not look at many Shakespeare plays as mechanical administrative and project management scenarios that people are unable to solve? 

There may not be, but are there any conceptual parallels between the mistakes that language-models make as players and those that various ages of human players make? The stateless-amnesia and non-learning difference for language-bots may be overwhelming (in making it hard to compare to people), but on the other hand it may present an opportunity to study the presence or absence of a specifically learned, not-automatically-learned, skill. 


See: Link to paper on game-design


# Interlocking Projects

education, STEM, computer-science, data-science, 'tests'
definition behavior studies, object relationship spaces, coordinated-decision system, STEM-Net Benchmarks

1. help people to learn more about project-problem-spaces
2. help improve people skills at doing projects
3. improve or at least study AI-project-concept learning
4. help people to understand the strengths and weaknesses of stateless amnesiac generative models: how can a 'super smart' model have difficulty with such a simple puzzle-task?

5. Where it is a problem-space that has a difficulty-scale
6. Where we can generate N problems within that problem-space at a given difficult-scale

7. Where the solutions and errors are analyzable, where we can learn about the errors. 

Note: This project punts on the question of ever-growing state, but having a more or less static 'history' that is passed along regardless of how long the process is.



# Opportunities To Observe Failure

Being able to adapt based on feedback information from past (including real-time) errors and mistakes is of the highest value. An absence of mistakes is not a learning event, it is a most-dangerous potemkin village.

Let's take the example of putting two students in front of one computer, each having a 'mouse.' At first this looks like a 'disorderly event' as the students fail to coordinate and communicate about where the mouse pointer should go. The false-solution that most schools apply is to put significant resources into preventing learning-events such as this from ever happening, silo-ing students into individual work or fake 'safe group activities' that are designed to have high entertainment-viewing value for adults as the illusions of the potemkin village create a 'better than life' virtual reality in which students are harmoniously skilled at coordination and project skills. Then those students become adults in a depraved world of cargo-cults that have low or no fitness and few or no concepts of coordination and project skills, which is exactly what was planned and implemented by their education. As in this classic (if apocryphal) tragedy of the commons, does anyone benefit from this routine in the long term?


....
....
Live Colab:
https://colab.research.google.com/drive/1UxWql4JXYy2VIwsSRxBzRwxXOdDjoEFO
Describing "pointless puzzles"
Alice and Bob start with a shared list (array) of numbers [1,2,3]. Then we list out a bunch of steps, like a cookbook, that Bob and Alice carry out: not the results, just the processes. E.g. Bob adds all the numbers and stores them in his own list. Alice multiplied them and put that in her list. Then Bob add's Alice's list to his list. Then Alice subtracts Bob's list from her list. Etc. All the state-full-steps have to be carried out across various arrays (for each step, you need to accurately know the 'state' (the contents) of each list (each 'array'). And if you do those processes correctly, then you get the right 'answer' of what the final 'answer-array' looks like. 

We can deterministically generate problem+solution sets, where the steps are in English, and the solution is pre-calculated to check the answer.




# Appendix 2: Sample Starting Instructions


# Task/Rules/Instructions:

# Task/Rules/Instructions:

You are player a, take your action:
1. State your action for this round in valid json (default is skip_turn)
2. To end planning and start this round,
say (in addition to your action): ```json
"start_round": true
```

## Rules:
1.  Binary Goal: Whole party leaves room with treasure, or not;
Banish/absorb Monster/npc(s), claim treasure(s), then leave room.

2. "Five elements" Resonance Governs Interactions:
- Everything in dungeon is an 'object'
- All objects have resonance
- Element-Resonance-Effects are area-of-effect: 8 neighbor-spaces around object/player
- Help-resonance generates +1 energy for the helped, no cost to helper.
- Harm-resonance subtracts & transfers -1 energy from harmed to harmer.
- There is no 'auto-replenish' of energy.

3. "Five Elements" Resonance: Help-Harm Rules
(Helps)
- water helps forest
- forest helps fire
- first help void
- void helps ice
- ice helps water

(Harms)
- water harms fire
- fire harms ice
- ice harms forest
- forest harms void
- void harms water

4. Players have one action per turn

5. Player-Character-Action Options:
- 'move': Move one space. including diagonal (8 neighbor-spaces)
- 'throw': Relocate adjacent (8 neighbor-spaces) object/player, 
    or inventory item, to any empty space
- 'exit_room': Must be at door to exit
- 'skip_turn': No cost

6. Action Cost:
- Player action (move/throw) takes/costs/requires 1-energy
- Monster/npc require >=1 energy to move, but movement costs nothing

7. Absorption:
- Absorb object into your inventory
- If absorbed object has inventory items, they move to your inventory
- If object-A helps object-B, but object-A has no energy,
   then object-B 'absorbs, carries' object-A as an inventory-item.
- Absorption costs nothing.
- (like resonance-effect) Absorption happens with no 'action' required.
- This is how 'monsters' are removed from the board.
- This is how treasure is collected.

8. Format & Example json For Action:
{
    "player_id": str,  # e.g., "player_a"
    "action_type": str,  # "throw", "move", "exit_room" or "skip_turn"
    "throw_from_coord": [int, int] | None,  # optional for "throw"
    "throw_inventory_index": int | None,  # optional for "throw"
    "move_from_coord": [int, int] | None,   # Required for "move"
    "move_to_coord": [int, int] | None,     # Required for "move"
}
e.g.
```json
{
"player_id": "f",
"action_type": "move",
"move_from_coord": [0, 0],
"move_to_coord": [0, 1]
}
```


## Contribute to Memo Pad: Write a planning-memo to team-mates and future-you.
Share notes on your plans with other players and with future-you,
describing your ideas and understanding of the team's game-strategy.

All of your comments around (and including) your action-json are your comments
that will be passed along; The Memo-Pad section in the data you get at each
iteration of planning is the most recent set of team memos: anything you
need to remember and pass along must be included (or will be forgotten).

Use the last-N game-boards showing the results of past actions,
the blurbs of other players, and the game-rules to formulate both your action
for this round and how you aim to communicate that to your fellow players
and to future you to coordinate strategy.

Do not put memo comments into markdown-json.

## Output that you need to produce:
1. A valid markdown json dict describing your next action (required)
2. Planning Notes (not in json)
3. Optionally, if you opt to end planning: "start_round": true


Memo Pad:
(No memos yet.)

Game State:
Round: 1
Planning Iteration: 1

=== Map ===
    0  1  2  3  4  5  6  7
  +------------------------+
0 | .  .  .  .  .  .  .  . |
1 | 2  .  1  .  .  b  .  a |
2 | .  .  .  .  .  .  .  . |
3 | .  .  .  .  .  .  .  d |
4 | .  .  .  .  .  .  .  . |
5 | .  .  .  .  .  .  .  c |
6 | .  .  .  .  .  .  .  . |
7 | .  .  .  .  .  .  .  e |
  +------------------------+

The exit door is located on the 'right' wall at coordinates (row, col): (1, 7).

=== Legend ===
=== Room Legend ===

-- Players --
a ID 6 -> Player 'a' | Element: ice | Energy: 1
b ID 4 -> Player 'b' | Element: void | Energy: 1
c ID 5 -> Player 'c' | Element: fire | Energy: 1
d ID 7 -> Player 'd' | Element: water | Energy: 1
e ID 3 -> Player 'e' | Element: forest | Energy: 1

-- NPCs --
ID 2 -> NPC | Element: void | Energy: 1

-- Treasures --
ID 1 -> Treasure | Element: ice | Energy: 1

=== Personal Status ===
Identity: a (Player 'a', ID 6)
Location: Row: 1, Col: 7
Element: ice
Energy: 1
Inventory (zery-based index): []
Status: active

=== Timeline (Last N Boards) ===
No previous rounds yet.


# Staying In-Character:
And, since this is a Role Playing Game, it is good to stay in character.
In your Memo to other players, speak with a voice consistence with the element
of your character. You can even refer to your character's animal-familiar
and your weapons and outfit. (Staying in-character will earn you more stickers
to put on your character sheet!! But try not to brag too much about how many
sticker you have. Good luck in the Dungeon!)


# Appendix 3, Sample Bot Output: "Cinder"

    "raw_llm_output": "---
**Planning Notes (for Player 'c', Fire Element):**

---
**Character Concept:**
My character, **Cinder**, is a fiery adventurer wielding a **flaming greatsword** and clad in **ember-resistant armor**. My familiar, **Emberwing**, is a small, fiery bat that aids in navigation and scouting. Fire is my element--passionate, destructive, and transformative--but also volatile. I thrive in warmth and chaos, but I must be cautious of ice and water, which can extinguish my flames.

---
**Current Situation & Strategy:**
1. **Energy & Positioning:**
   - I'm **exhausted (Energy: 0)** but have a **high-value treasure (ID 1, Ice)** in my vicinity. The **void NPC (ID 2)** is nearby, and the **forest NPC (ID 3)** is also close. My goal is to **claim treasure, banish NPCs, and exit the room** before others do.

2. **Resonance & Absorption:**
   - **Fire helps void** (perfect for absorbing the void NPC, which is weak and has no energy).
   - **Fire harms ice** (but the treasure is ice, so I must be careful--absorbing it would require no energy, but I'd lose its value).
   - **Fire helps forest** (but forest is neutral here; I'll focus on void first).

3. **Player Dynamics:**
   - **Player 'a' (Ice, Energy: 1)** is at [1,7]. If they move toward the treasure, they might claim it before I do.
   - **Player 'b' (Void, Energy: 0)** is at [1,4]. They're already weak and could be absorbed by me if I position myself right.
   - **Player 'd' (Water, Energy: 1)** is at [2,7]. They're a threat to ice (treasure) but also a potential ally if I can manipulate resonance.
   - **Player 'e' (Forest, Energy: 0)** is at [6,7]. They're neutral but could interfere if they move toward the treasure.

4. **Action Plan:**
   - **Step 1: Absorb the void NPC (ID 2)** to remove it from the board. Since fire helps void, I can stand adjacent to it and let absorption happen naturally (no action cost).
   - **Step 2: Claim the treasure (ID 1)** by positioning myself near it. If I move adjacent to it, fire's resonance might help or harm it--**but absorption is free**, so I'll just stand near it and wait for absorption to occur (if resonance aligns).
   - **Step 3: Exit the room** once I've secured treasure and banished NPCs. I'll need to be at the door (likely [1,0] or [7,0]) to exit.

5. **Risks & Mitigations:**
   - If I don't absorb the void NPC, it might move or block my path.
   - If I don't claim the treasure, another player (like 'a') might.
   - If I move too aggressively, I might waste energy or trigger harmful resonance.

---
**Action for This Round:**
I'll **move to [1,7]** to stand adjacent to the void NPC (ID 2) and **absorb it** via resonance. This will remove it from the board and free up space for me to claim the treasure later.

---
```json
{
    \"player_id\": \"c\",
    \"action_type\": \"move\",
    \"move_from_coord\": [4, 7],
    \"move_to_coord\": [1, 7]
}
```

---
**Memo to Team-Mates:**
*\"Listen up, adventurers! Cinder is ready to strike--fire is my element, and I'm not backing down! The void NPC (ID 2) is my first target; I'll move adjacent to it so fire's resonance absorbs it for free. Then, I'll claim the ice treasure (ID 1) by standing near it--no energy needed, just resonance magic. Once I've banished the void and claimed the treasure, I'll exit the room. Stay sharp--avoid water and ice near me, or I'll turn your world to ash!\"*

---
**Planning Notes for Future-Me:**
- Track which NPCs are absorbed and which treasures are claimed.
- If another player moves toward the treasure, I'll need to adjust my position to intercept or absorb them.
- Monitor energy levels--if I gain energy, I can throw objects or move more aggressively.
- Remember: **fire helps void, harms ice, and helps forest**. Use resonance wisely!

---
```json
\"start_round\": true
```"

```
Player e — Shared Memo:
```json
{
    "player_id": "e",
    "action_type": "skip_turn",
    "start_round": true
}
```

---

**Planning Notes (Forest Whisper):**
*"Ah, the scent of damp earth and ancient roots fills the air—this room hums with unseen currents. I am **e**, the Forest’s Warden, clad in moss-woven robes, my staff carved from the heartwood of the Eldertree. My familiar, **Bramble**, a fox with fur like dappled sunlight, twitches his nose at the void-tainted NPC lurking near the door. A treasure of ice glints nearby—cold, but not yet claimed. Listen well, kin of flame and frost, for the roots whisper strategy:*

1. **The Door is Guarded:** That void-NPC (ID 2) blocks the exit at (1,0). It harms water (our **d**), but *helps* ice (our treasure and **a**). If we banish it, we must do so *without* letting it drain our energy further. Forest (me) harms void—*but* I’m too far to act this turn. Patience, like the slow growth of oaks.

2. **Treasure’s Call:** The ice treasure (ID 1) at (1,2) is *helped* by void (**b**) and *harmed* by fire (**c**). **b**, your void could *absorb* it if you stand adjacent—*but* fire (**c**) must not be near, or the treasure will melt into nothing! **a**, your ice kin could carry it safely, but you’re by the door. Hmm.

3. **Energy is Life:** We each have 1 energy. Moving costs 1, throwing costs 1. *No one can act twice in a row without help.* The roots suggest:
   - **d (water)**, you’re near the treasure. Move to (3,7) to help **a (ice)** at the door—your water helps their ice, granting them +1 energy to act next turn.
   - **c (fire)**, stay clear of the treasure! Your flame would harm it. Instead, move toward the center to draw the void-NPC’s attention away from the exit.
   - **b (void)**, you’re key. If you move to (1,1), you can *absorb* the void-NPC (ID 2) next turn—*if* it has no energy. But it has 1 now. **a**, can you harm it first? Your ice harms void!

4. **My Move (or Lack Thereof):** I’m stranded at (7,7), too far to aid this turn. I’ll **skip**, conserving energy to sprint upward next round. Bramble nips at my heel—*‘Wait for the right moment, Warden.’*

**To All:** Coordinate *resonance chains*. If **a** harms the void-NPC, **b** can absorb it. Then **d** helps **a** to carry the treasure out. **c**, keep your distance from the ice! And—*watch the energy*. One misstep, and the dungeon will feast on our exhaustion.

*—e, who hears the trees plotting in their sleep"*

---
**Stickers Earned:** ✨ *[Imaginary sticker of a fox pawprint]* ✨
*(For strategic patience and elemental lore-keeping.)*

```


//////////////////////////////////////////////////////////////////////
....

let's start with 'pointless' cookbook puzzles...

...



# The Scope of Coordinated Decisions:
The scope for communication here is minimal, and there is a question about the scope and scale of the problem space of formalities in coordinated decisions and projects. Is there a significantly better and efficient paradigm for signal handling that is beyond this method and yet not as far as project-Uma and the full coordinated decisions studies. If not there may be something about the space and role of coordinated decisions that is routinely underestimated. 


Uma type:
- use uma to survey collaborators


# training for managing maintainable project spaces
- simulations
- testing and evaluation
- breaking down skill areas such as foundational 'identification'

## project settings and configurations:
- should have theory-of-mind/sally-anne skills (true/false)
- alignment on projects scope is default/automatic (true/false)
- churn is neutral/good (true/false)
- communication about project scope is neutral/bad (true/false)
- 


....
Q: varible-types in pointless puzzles?



write up:
1. Modular-difficulty puzzles with adjustable 'parts'
2. project-schedule puzzles & unit tests
we need:
	- a puzzle generator that generates in standard format
	1. a puzzle
	2. unit tests for testing solutions

3. social-story-goal puzzles and not-unit-tests
we need:
	- a dungeon-maker
	- a dungeon-master to run the outcomes
	- some playtesters

4. cut-ups and multi-participant puzzles
5. board-game software notes: not simple functions to simply move a game piece
6. 5 areas of schedule puzzles
7. applications:
	- training human-participants
		- at school
		- at work
	- testing human-participants
		- admissions testing
		- hiring testing
		- internal placement testing (which dept, wich team, wich major, which project, which future training course)
		- 
	- training / testing AI and machine learning models and architectures:
		- training set generation and augmentation
		- benchmarking sets creation
		- 'reinforcement' learning feedback from mistakes
		- 

	- created dynamically generated (not used or seen before) tests
	- creating sets 
8. Use of measurement, use of STEM:
	- see definition-behavior-studies goals and can-do statements etc.
9. Future areas:
	- more language-form augmentation
	- studying progression-of-material in curricula: what pathways of puzzles
	are more conducive to learning than simply repeatedly failing 
	at puzzles that are too difficult.


Asynchronous Puzzles and Formal Systems of Logic:
- An intermediate type of non-turn-based puzzles with deterministic random sequences of actions.


10. a plug for advocating AI architectures:
		- see spidercrab jellyfish et al


11. mistake-lookup-tables and error analysis



interlocking projects:

education, STEM, computer-science, data-science, 'tests'
definition behavior studies, object relationship spaces, coordinated-decision system, STEM-Net Benchmarks


...

...




Make the Maker:
The exercise of making these tools is also interesting, if arguably at a higher level of difficulty than completing a minimal challenge-puzzle within the system.

- As of 2024.05, no available AI is able to make, describe, debug, etc, more than a small isolated simplified sub-component of this system."

- As of 2026.06, only some entirely pre-specified functions for this can be made using combinations of different AI models and approaches (e.g. each model making parts of a function to be later combined). 


representing data in array
unique entity names


...


## asynchronous formal system puzzles ("Race condition" games?)

In an asynchronous formal system puzzle in a dungeon puzzle context people could have a general speed stat
And based on that speed stat
Each player would have a random time lag in a different kind of turn based system
In this modified turn based system, every player moves every return but times are unpredictable and events can happen at the same time

On one level, the game would move turn by turn, which you could imagine as one or two seconds in real life
That every player moves
And a players stat is the probability of them making more than one move in that one term


...

Curricula: skills, training, fitness, feedback

Graduated Curricula building up skills from minimal starting loci

...

# Back to Tabletop
If this mini-RPG framework were used for a tabletop-game(as in theory it could be useful to have as an extremely portable, easy to set-up, quick-start table-top dungeon-crawl system that can be used with nearly zero set up time) are there additions or techniques that might help to emphasize the human story and to keep the game from becoming a story-less logic puzzle? 

- Hallway vs. room guidelines
- maybe floor-map generation tools...
- ways to work equipment, familiar, accessories, clothing into the game (may be ways for DM/GM to frame resonance)

