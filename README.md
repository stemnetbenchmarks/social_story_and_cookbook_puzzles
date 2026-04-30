# social_story_and_cookbook_puzzles

(under construction)

# AI RPG-Arena:
Social Story Puzzles & 'Pointless' Cookbook/Logistics Puzzles
for Teaching, Training and Evaluation

### A testing/training framework set, including a Tabletop-like 
Mini-RPG for people or for AI-Bots. 

2024.05-06.22, 2026.04.21 G.G.Ashbrook



As a continuation of our discussion of making tests to better understand how things work, from "Let's Test Models", "Ants vs. AI" and "The Jellyfish Spidercrab," et al, and as part of the larger discussion of how to create and use tests and metrics in "Stem Net Benchmarks", let's now look at two groups of puzzles that we can automatically generate to evaluate or to train people or machines.

This study is part of a layered puzzle of stories, skills, and learning and layers of stories about puzzles, skills and learning. How do we, how can we, and how should we, design and implement environments for learning? 

## Contents:

1. Introduction
2. Functionality
3. Social Story Puzzles & 'Pointless' Logistics Puzzles
4. Training & Testing
5. Projects
6. Future Research
7. Links & References

Appendix 1: Discussion
Appendix 2: The Game Rules, Sample Starting Instructions
Appendix 3: Sample Bot-Shared Memos


# Introduction

How is a marketplace like, and how unlike, a dungeon for adventurers? In real-world stories where people need to learn skills, how are those 'learning environments' shaped and managed? Can and should games and puzzles be used to teach real world skills? In machine learning where testing and training data are often needed in large quantities (both to create a machine for a task and to evaluate how good that machine is at a task), can skills and concepts be supported by enough data describing both tasks and errors? 

### Code Git Repo:
- https://github.com/stemnetbenchmarks/social_story_and_cookbook_puzzles 

### Live Notebooks in Colab:
- https://drive.google.com/drive/folders/1ETOeXGSF52_lkclJ7W_xSJNEZC0OEMz_ 


#### Dungeon Crawling (in summary)
There are two main ways to play through the Mini-RPG game.

1. You can play manually yourself (or with a team), iterating through each round of play entering in the turns that each player will take in the next round (much like a table-top RPG where players might state their actions before the Dungeon-Master/Game-Master calculates the effects of all the players and non-players taking their actions. You can do this using a python-notebook (or in cli), which does not require anything aside from a computer with python installed (linux, bsd, MacOS should be fine (ms-windows...should work as well as windows ever works), or a google-colab notebook will run on any online device with a current browser (even a phone or tablet), (and you need a google-account to run colab). I recommend that you play the game through at least once this way to get a hands-on understanding of how the dungeon rules work and the nuances of what individual AI-Bots need to figure out together.

2. You can run the AI-Bot-Arena (for which you will need a model-api (currently set up to use api from Mistral, Anthropic, or Google)):
- Option A. Play using a notebook (or cli), and you can view the results as an RPG-Screenplay HTML file, seeing what the GM/DM each player says and chooses (for each iteration of planning and each round of actions taken).
- Option B. View the game in real-time (or afterwards) as a (minimalist) Visual-Novel, using the code in /rpg_visual_novel_ui). See: https://github.com/lineality/rpg_visual_novel_ui 

Either the Screen-Play-Script, or the Visual-Novel, should hopefully make following each Player-Bot's decisions more user-friendly (and the logs files are there to inspect as well, including the output that did not contain valid move choices).


# Functionality
While there may be a fun-ish game in here somewhere, the overall context is intended to be no-less STEM/Academic: Can we find an intersection between formal-tests and well-defined evaluations that can be analyzed on the one hand, and on the other hand social-story puzzle-games that people participate in by choice, in an overall context of learning how learning happens with an eye to helping better learning and fitness?

Applications and uses (of this dual-framework of generable logistics evaluation datasets and project-coordination-datasets), if ideally, include: 
1. Help people to learn more about project-problem-spaces
2. Help improve people's skills at doing projects (a.k.a help learning)
3. Improve (or at least study) AI-project-concept learning
4. Help people to understand the strengths and weaknesses of stateless amnesiac generative models (E.g. How can a 'super smart' model have difficulty with a simple puzzle-task?)
5. Use and leverage scalable problem-spaces (as the term is used here, problems that can be generated with one or more "scaling" parameters that increase or decrease N-dimensions of the same overall structure of problem (the two main types of puzzles in this study are both examples of this).
6. Deterministically Generate Datasets: N solution-testable problems in a problem-space at a given difficulty-scale.
7. Leverage solutions and errors that are analyzable, and learn about and from those errors. 
8. Develop tools and best uses of tools.
9. Develop best practices and data that support STEM best practice



# Social Story Puzzles & 'Pointless' Logistics Puzzles

### Digestible Entrypoint: 
We can start with an 8x8, or even simpler, game space that anyone can understand and interact with (just as roughly-everyone can play tic tac toe or connect-four, or a game like battle-ship with a tic-tac-toe scaled board). Then, when the questions are clearly framed in simple and unambiguous terms, we can follow the connections and implications and use tools accessible to anyone.


### Social Story Puzzle: Modular RPG Dungeon Crawl
RPG-SHRDLU: a story-oriented blocks-world for social and language-using participants

We can define a type of minimal social-story-puzzle, a mini ~Multi-Player RPG (classic dungeon-crawl), that is completely defined so that players will "make" and "implement" a plan (for a given dungeon room) and run that plan through a game-outcome-calculator. 

Each "random-seed" (and other "configuration variables and parameters" such as how many monsters/NPCs per room) will produce a fixed (reproducible) starting-room-state and the non-random outcomes will be ~deterministically (same-input, same output) calculated and validated. Players can submit and implement their plans either 'iteratively' playing and seeing the outcomes of one round-of-turns at a time, or all-at-once (planning out the whole strategy for all rounds then running it all at once). If a solution is valid: test passed. If the solution is not valid: test failed. 


### Social Story Puzzles vs. 'Pointless Puzzles'
The social-story-puzzle Mini-RPG (and the AI-Bot Arena) is the star of the show here, but (somewhat in contrast) there are related ~deterministic puzzles (also team-project puzzles), that I nickname 'pointless puzzles,' such as project-schedule or project-logistics puzzles. (See Notebook & Git links above.) 

"Pointless puzzles" are so nicknamed because they are not usually the kind of 'game' that most people gravitate towards for sport and amusement; they are however concretely realistic in terms of human everyday tasks and technical-significance. 

Is something really a puzzle if there isn't anything to figure out how to do? (If only to illustrate that people do not agree about this, John von Neumann famously asserted that Chess was not a game, but rather a calculation with a solution (whereas... most people do consider chess to be a game).)

The idea behind ('pointless') logistics puzzles is to try to make a (scalable) puzzle that depends upon the state of a stateful system. (To non-computer-science people the term "state" means something like government. To computer science people, "state" means the values assigned to variables. To the utter disbelieving astonishment of both camps, they are both entirely correct. But they never talk with each other, so nobody finds this out.) Our abstract project logistics puzzles deal with lists of values (sometimes, but not always, called 'arrays'). Each person in this puzzle scenario follows 'cookbook' like steps: Alice takes the contents of Bob's list and adds that to her own list. Or, Bob takes all the numbers in his own list, sums them into one total number, and adds that value to another list. This can (interestingly) be done using different operations on different types of values, three main groups of which are:
1. boolean values and boolean logic: and, or, xor, etc.
2. numbers: add, subtract, multiply, divide, etc.
3. strings (characters, letters and words): many operations you can do with strings of text.

In these puzzles people are sort of acting like lower level computer operations, comparing and moving around values in arrays in memory. Part of what is interesting about these puzzles is that you can rigorously generate questions and tests for any set of solutions used as input, with the cookbook instructions being as convoluted as you wish. If you want to know if an AI is really capable of following and managing everything going on in a literal or proverbial factory with many people doing inter-related processes, this is the kind of 'stateful' test that you would want to evaluate with.

But we can look at these logistics-puzzles in a less abstract and more relatable way. Let's think of it as a market-place or as running a food-truck or a grocer, rather than logical operations and arrays of bits in memory or over a network. Instead of numbers, let's say there is a cart with eggs, flour, salt, and spices. Alice needs to move the eggs into her shop. Bob needs to mix the flour and spices. Tom adds the salt after Cat got the eggs from Alice (and after she made them into Egg's Benedict with hollandaise sauce), etc. If you think of the puzzle-space, the project-space, in terms of shops and restaurants and that kind of logistics, it probably sounds more closely related to every-day life, and closer to puzzles that people do (and like to do), and it is probably a lot easier to understand in terms of the language and concepts we learn and live with every day. 

Let's try to add something else to our stew of puzzles, to the 'problem-space' of these puzzle-stories. Even the shop-logistics puzzles are still 'introverted tasks' in a way, steps one person can read and carry out from a cookbook's list of instructions, regardless of everything else that's going on in the bustling market and during the lunch rush at the cafe. Fortunately we (on Earth) have a widely known type of game that we can use if we want to make something that is a bit more of a creative-problem-solving challenge, and something that requires the players to work together and coordinate more directly (Coordinated-decisions studies!), not merely in abstract results, something that really requires people to plan and act in communication and in alignment with each-other. We have table-top Role Playing Games; we have players on a dungeon crawl.

### The Crawl: 
You are in a dungeon of rooms. You need to decide where to go, get past the monsters, get to the treasure, work together, use a 'system-mechanic' of spells, keep your health-level above zero, and participate with others in a turn-based system. While not as technically dexterous as the "pointless puzzles," these social-story puzzles exist more in the space of coordinated planning and decision making (of project management).

Social stories and logistics are rather intertwined, but in some cases we can make the distinction that separates plan-invention (or solution-discovery), importantly including the problem spaces of information-sharing and coordination-decisions from a problem space that only includes instruction-following and solution-implementation. 

In some ways there seems to be no clear dichotomy between social-story-puzzles and introverted-logistics tasks (as I nick-name them here, suggesting or presuming there is a difference between the two). If you break everything down into a pile of steps then everything looks like a pile of steps. And if you look at a logistics puzzle through the context of a village marketplace then it looks like a (it is a kind of) social story (with the same Alice, Bob, Cat, Dog, Eretosthenes cast of players, each doing their interlocking roles). But if you change the context then two seem more different, for example: Is there a problem to solve? The Dungeon Crawl poses a problem: How can you get the monster, get the treasure, and all walk out of the room? There is (presumably) no passive way to survive the dungeon; there is no dungeon cookbook. For the logistics market-restaurant-story puzzle, each player has a list of tasks to follow, but there is no 'problem' to solve. In fact, you do not even know what the result of the cookbook recipe will be until you follow all the steps.

We have the linear-cookbook tasks on the one hand where the solution is implementing one (cookbook recipe) logistics-process where there is effectively one correct or faithful "solution" (move three eggs (or bits) from this array to that), but it does not involve discovering the solution to a problem so much as following established steps. Sometimes this distinction of 'tracking logistics' vs. 'Finding a solution' seems non-existent, other times it seems more tangible. Even though both are Alice, Bob, and friends team projects, one context is to look at communication and decision. Even though in both types of puzzles each player tracks the moving logistics and follows along, in the 'pointless' logistics (marketplace, kitchen cookbook) type of puzzle there is no need for communication, and 'decision' is a perhaps misleading term for implementing the instructions that were already provided (the cook book recipe). On the other hand we have 
social-story open ended problem-solving where there are many (maybe infinitely many) viable solutions to each problem. The problem space in a social story puzzle is not A. 'follow instructions' vs. B. 'fail to follow instructions,' each player and on an aggregate level the project-team as a whole, needs to navigate through a problem space of multiple possible correct or incorrect solutions, where they are not told which is which (or even what those solutions are). In some (perhaps unrealistic cases) each player has full information about the game, but more realistically the problem space involves coordinating to share that basic information across the players. 

Where we have what in English we would call 'a problem to solve' the problem-space includes a Hayekian-signal-ecosystem (though ironically the logistics puzzles appear to resemble introverted isolated tasks in a marketplace, after the origin of those steps has been abstracted away).

I would also question whether multi-participant-interdependent actions can or should be broken down into introverted tasks (such as characterizing both types of puzzles as identical introverted-unilateral array-value shuffling actions). Using dynamic feedback within a process is likely not always just another linear step in a pile of linear steps. And it is not clear to what extent different contexts and details matter for real world skill building and skill retention. Scalability, modularity, coordinated decisions, and various levels of perception and articulation of project-area parts are all key factors in the skills, fitness, and best practice needed to complete projects, and for a diagnostic understanding how projects fail and systems collapse. (It is also a towering irony here that the software industry and computer science spent fifty years in shambles, doubling down strong-and-wrong on the cult of anti-communication. Practices like Agile (though the kanban-board predates software) will hopefully apply STEM to the need for better managed projects, but as of 2026 the rebellion against project management is still in overwhelming majority.) 


#### Increasing a Need for Coordination
There are many possible ways that the RPG world and system-mechanic could be configured to require more coordination between players (beyond the element-resonance system itself). Several of these are listed in the code-notebook. Though most are not yet implemented, one that has been included is based on perception.

When you set up the dungeon room, you can pick between letting all the players see the whole room, or having a limited-visibility environment restricting what each person can see from where they stand (as if the room is full of thick pillars and each player can only see down clear straight rows North, South, East, and West). 

This requires players to exchange information about where things are in the room, information that only they may have. This is even more of a classic 'cut-up' puzzle where team-members need to share information  about the puzzle itself to co-discover how the puzzle can be solved. 

### Chess & RPG
As somehow chess finds a way into many AI discussions: In keeping with the empirical 'pen and paper,' 'tabletop,' nature of many RPG games, this 8x8 grid and 5-player system is compatible with... a physical chess board and pieces. This mini-RPG can be played as a physical board game using a chess set. For example, you could have each player be one type of black piece (of which there are five shapes), and the mobs, treasure, NPC, objects can be white pieces. 

#### To Recap:
A "pointless puzzle" is more of a 'can you follow directions' puzzle, rather than a, 'plan what the directions should be for this open-ended situation' puzzle. Both are very important, but they are also importantly different from each other.

These social story puzzles are still meant to primarily be abstract tests (they are not designed to be consumer-attractive products), but they should retain some elements of the kind of story-space and socially found solution that a tabletop RPG has.


# Training & Testing
These puzzles can be used to either test or train:
1. Individual people (for example in an educational settings)
2. Teams of people as in a classic student-centered/constructivist 'cut-up' activity involving team-project sharing of information of group planning, (for example in educational settings)
3. Individual one-shot generative AI (or architectures) (either as an evaluation, as training-data to build up a project-space-outcomes concept-set in the model, or theoretically as part of ~reinforcement training or fine tuning).
4. Teams/Groups/Swarms of collaborating AI (either as an evaluation or as part of ~reinforcement training or fine tuning, etc.)
5. Reinforcement Learning to train (non-oneshot-pre-trained) models/architectures


# Projects:
Not surprisingly, this study is interrelated with project-spaces, coordinated-decisions, hybrid data, project-object-databases, etc.:

- Definition Behavior Studies: https://github.com/lineality/definition_behavior_studies

- Project Areas (and project management):  https://github.com/lineality/project_areas_for_project_and_product_management 

- Coordinated Decisions: https://github.com/lineality/Networked_Voting_and_Decisions_Including_One_Time_Pads 

- Hybrid (structured and unstructured data) https://github.com/lineality/hybrid_data 

- Uma & T is for Task (still in progress):
https://github.com/lineality/uma_productivity_collaboration_tool/blob/main/t_is_for_task.md 


# Future Research

1. Automated Mistake Analysis
One area that might be very important, but which is not elaborated on here, is Generating Error-Mistake-Analysis-Data Per-Puzzle

If more-so for logistics-puzzles, it should be possible to generate some level of (reliable) automatic reporting on what went wrong with a proposed solution. This may be important to go along with raw-error data for learning processes (for people and robots (as far as we can continue to make that distinction)), as well as a unit-testing type error diagnostic that is useful to have.

2. Evidence-Based Optimal Learning Patterns (for people)

3. Is there a way that raw concept-vectors might be used to map aspects of this problem space, or other non-generative models? (Trying a standard reinforcement soccer-football-game approach?)

4. User Interface: While in many ways pouring time and compute into fancy 'graphics' is not constructive, finding the right balance of a proportionate and maintainable interface that allows users to see, understand, and interact with the process and the code is useful. How can more groups of people comfortably work hands on with this problem space? 

5. Are there other coordination elements that correspond with key not-automatically-learned-skills that can be added so that more evaluation and training detail and value are possible?

6. Curricula: skills, training, fitness, feedback: Where coordination skills are important for all people to have (which I think is 'everywhere'), where methods work best (broadly or in what specific contexts such as specific groups or demographics of people) to either most quickly or with best long term retention improve test-able group project collaboration and coordination skills?

# Sport vs. Sportsmanship
There is much more to games and puzzles than antisocial, predatory,  sport-thrill-seeking behavior. Publishers of games should have the spine to emphasize more enriching content, not a race to the bottom, least common denominator, contraction into ever less mindful and ever more escalating trauma-disturbance. Institutions, academics, and STEM areas should all do more to utilize and emphasize the constructive uses of stories, games, puzzles, and worlds. From therapy, to education, to public and private sector team projects, to the uses of feedback, conceding all of gaming to criminality is a concession too far.

On many levels, people of all ages and across disciplines may find something of interest in the code and questions here. With the feedback from hands-on projects done together there is inestimably more than in the isolation of compartmentalized silent conjectures trapped in a psychological dungeon of desks and cubicles. Find the doors.


# Code
For more technical details, see (and run!) the notebook, or to modify it however you will:

### Code Git Repo:
https://github.com/stemnetbenchmarks/social_story_and_cookbook_puzzles 

### Live Notebooks in Colab:
- https://drive.google.com/drive/folders/1ETOeXGSF52_lkclJ7W_xSJNEZC0OEMz_ 


Farewell, Etaoin Shrdlu.


# Links & References

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




# Appendix 1: Details & Discussion


### Two Modes of Play: Whole-Game or Incremental-Iterative or 

A. Whole-Game: One way to test a model is to give it the rules and the starting positions in the dungeon room (the 'state'), and have the model plan the whole 'room-story' all at once (all rounds), succeed or fail. This is similar to a logistics puzzle (both involve teams and roles and both are stateful), but this involves making a novel strategic solution (beyond following through a stateful outcome).  

B. Incremental-Iterative (take action after each round see what happens): The iterative approach (or approaches) open up more questions about the 'state' (or 'statelessness') of generative AI models. Breaking up the puzzle into smaller easier steps makes smaller similar easier sub-puzzles, but the 'context window size' and amnesia of the model create perhaps larger problems. If the model never learns and has no memories (only a kind of shadowy fake-proxy memory), then how many more 'integration roles' are needed to manage and stitch-together all the sub-puzzles? 
 
There is the manual-iteration-interface, but then there is also the more granular Bot-Arena where each player in each round is further subdivided into each planning round of N planning rounds within each action-taking round. 

Part of the point of taking the same task and being able to evaluate externalized-coordinated-project-state ways of doing things vs. internal-introverted-unilateral modes (doing the same task) is to try to gain some empirical insights of feedback about how formalities of project-state externalization (of the project-object-database) influences the set of what skills and fitness are required for and involved in doing that task.

Note: There can be other criteria for evaluating and comparing plans beyond pass-fail, e.g. some plans can require fewer steps (less time). (Linotype?)


### Asynchronous Puzzles & Race Conditions

On the one hand the pseudo-asynchronous kludge of game-rounds and simultaneous turns is an artificiality that would not map well onto a fully real-time puzzle (such as a swarm of in-motion bots). Two questions:

1. Is there a test-data-understandability problem in a deeply dynamic test where, perhaps in a context of Rust memory atomics, the states of arrays in memory are too ambiguous due to race-conditions? This may translate into the question of: If rules are so loose that mistakes break the ability to see what you did wrong (e.g. untraceable undefined-behavior problems) how does that low level signal-distortion negatively affect being able to use and learn from that low-quality-learning-signal? 

2. Is there an enduring utility in iterative planning? While processes themselves may happen in a more simultaneously dynamic way 'during the agile sprint,' is there a process-layer of iteration that persists even when actions themselves cannot be pre-structured in time? 

While we can create a more asynchronous version of a minimal dungeon, e.g. where bots are continually cycling through their own loops instead of stepping through an order of actions, what would that change about the overall puzzle? (Maybe we need to try and see...)


### Modular:
In this modular framework there is a ~most minimal starting version, but there are also many aspects that can be changed to introduce increasing 'dimensions' to the puzzle.
- More 'monsters'
- Monsters with less simple behavior
- Conditional Perception (involving more player-to-player 'cut up' coordination to solve the puzzle)
- multiple and fractional speeds of movement
- having a dungeon room inside of a ~mob/npc/object as in a puzzle in a puzzle to get an absorbed player back out.
- having limited or shared areas to communicate
- etc.

And these can be combined:
- opening a chest could involve a pointless-puzzle / 8x8 puzzle
- beating a monster could involve an 8x8 game like chess
- opening a door, etc.
- getting a person out of another object, etc.


### One-Time-Test vs. Repeatability with N-inputs and N-outputs
One difference between a logistics test (where the 'solution' is a process, not an individual solution) and a social-story-puzzle (in the context here) is that you can test a given logistics solutions with N different inputs and outputs, it can operate perhaps similarly to 'unit tests' for code. The social story test is more of a dynamic coordination test, less of a static-introverted-unilateral-algorithm test. (As mentioned, combining the two may be interesting...) Both puzzles are generated ~deterministically (same input, same output) and are consistent with repeatability examination, but the language-bot process is not a static single-context artifact. 

### Gamification & Blocks World

While this is speculative, it is likely worth mentioning. Historically it was difficult/ineffective to try to extend a simplified "Blocks World" bot into real-world (less-simple-world) tasks. But in some ways that early failure is an apples-to-apples (comparing the same things) comparison to the various types of machine learning, robotics, and virtual-training environments fifty or a hundred years later.

It is most likely correct to not naively assume that a simplified test will not automatically generalize across real world phenomena, but on the other hand can we avoid teaching machines to find solvable simple games within their stochastic analog rivers of input? 


### Story, Language & Games

Is there a story in this mini-RPG, or is it too minimal? We can probably agree that the logistics puzzles do not contain any story (though they can be analogized to stories). In the mechanics of the mini-RPG the characters do not 'need' to have names, or be very 'social' etc. At least hypothetically we could imagine a theatrically 'mechanical-robotic-aesthetic' but this 'hard-science-fiction, hard-neo-modern' style is a human fantasy that is, somewhat comically, completely at odds with how language-concept-foundation-models work (yet people go on with their 'I am an expressionless robot who loves numbers, 1-2-3, 1-2-3, 1-2-3, beep.' fantasies about what robot-ai is doing.

On the other hand, is the social story within the implied coordinated decision and project management layer that sits on top of the mechanics of the game? This might go back to the question of using a language-concept model vs. using a single-task reinforcement-learning modeling.

For example, could we not look at many Shakespeare plays as mechanical administrative and project management scenarios that people are unable to solve? 

There may not be, but are there any conceptual parallels between the mistakes that language-models make as players and those that various ages of human players make? The stateless-amnesia and non-learning difference for language-bots may be overwhelming (in making it hard to compare to people), but on the other hand it may present an opportunity to study the presence or absence of a specifically learned, not-automatically-learned, skill. 

See: Link to paper on game-design
- https://github.com/lineality/story_rpg_platform 


## single-task reinforcement learning vs. foundation-model language-concept 'pre-train' learning

How can a model that can talk a good game and do individual tests and quasi-tasks do so badly at a concrete (relatively simple) situation that it would be happy to describe to you.

Question: For the whole-game solution, as with SHRDLU and Blocks-World, a reinforcement learning model would probably do well (I am guessing). But in various kinds of cut-up situations where coordinated strategy and missing information are needed, what is the potential for single-task reinforcement learning vs. a trained language-concept foundation-model?

Project and coordination decision skills are, arguably, at the forefront of STEM being either not yet or barely recognized by semi-STEM humanity as existing (let alone being of value). 

https://www.theguardian.com/games/2026/mar/16/petri-dish-brain-cells-playing-doom-cortical-labs 


### An Open History-Mystery Puzzle
 People being unpredictable, it is entirely possible the 'social cookbook recipes' could become popular, but as of 2026 table-top-style RPG stories are more popular social-games than virtual cookbook recipe following. (Though it would be interesting to have a paleontology debate about the prominence of pre-historic social-cooking vs. prehistoric social-story-telling, both are no doubt quite ancient. And if 'pack hunting' is a game, it both combines cooking with monster-hunting and pre-dates a given primate species.) 


### Dimensions and operation-spaces of logistics-puzzles
- bits
- numbers
- strings

Dimensions alone are likely not a distinguishing factor between social-story and logistics puzzles. A logistics puzzle can be a few simple one dimensional arrays, but they could also be less simply N dimensional (and N of those). 

The social story puzzle is, in a way, one 8x8 2-D array (or set of arrays), and a few other arrays of data and meta-data. The social story mode is probably simpler overall as the number of participants cannot grow much and the sizes of the arrays is fixed and small.

### Step vs. Fixed-Process Steps
While a given 8x8 RPG puzzle could be broken down into logistical steps in retrospect, this abstracts away the signal-communication puzzle layer that gave rise to that solution. 

If there is a standard-solution-process here, it is a signal-protocol process (a project-management best practice process), not a pedantic literally array application process. And it remains to be seen if such a strategy negotiation can occur in the narrow space of no-concept single-task trained machines learning, vs. the broader conceptual space of language-concept foundation-models.

The story-operations are such that they are not procedurally fixed with an unknown end-point, but are defined by strategic end-points with arbitrary paths to those end-states. These end-point cannot be the result of introverted unilateral action, but must involve coordination (especially in the case of increasing cut-up elements and distributions of puzzle data (which is at a minimum in a simple version of the game (e.g. no limited rules-sharing or limited 'pillar-blocked' perception, or element-specific data)).

At this point (2026) that additional level of difficulty is moot, because even the largest llm-models cannot coordinate even when given complete information about the dungeon.



### Interlocking Projects

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


### Opportunities To Observe Failure
Being able to adapt based on feedback information from past (including real-time) errors and mistakes is of the highest value. An absence of mistakes is not a learning event, it is a most-dangerous potemkin village.

Let's take the example of putting two students in front of one computer, each having a 'mouse.' At first this looks like a 'disorderly event' as the students fail to coordinate and communicate about where the mouse pointer should go. The false-solution that most schools apply is to put significant resources into preventing learning-events such as this from ever happening, silo-ing students into individual work or fake 'safe group activities' that are designed to have high entertainment-viewing value for adults as the illusions of the potemkin village create a 'better than life' virtual reality in which students are harmoniously skilled at coordination and project skills. Then those students become adults in a depraved world of cargo-cults that have low or no fitness and few or no concepts of coordination and project skills, which is exactly what was planned and implemented by their education. As in this classic tragedy of the commons, does anyone benefit from this routine in the long term?


### The Scope of Coordinated Decisions:
The scope for communication here is minimal, and there is a question about the scope and scale of the problem-space of formalities in coordinated decisions and projects. Is there a significantly better and efficient paradigm for signal handling that is beyond this method and yet not as far as project-Uma and the full coordinated decisions studies? If not there may be something about the space and role of coordinated decisions that is routinely underestimated. 


### Try it! Make a game-board in software: 'Easy things are hard'
One of the enduring notions of John McCarthy, one of the founders of 'AI' from the 1950s, was his observation that apparently easy things can turn out to be not as easy as we expected. 

While this mini-RPG can be played using a chess-board, a piece of paper, and a pencil, the seemingly simple process of moving a game piece one square somehow becomes much less simple when the game-board exists in software.

For anyone who has not done this, I highly recommend writing something that seems simple, such as a chess-server. 

This is not directly related to this scope at all, but it is fascinating for learning (and peripherally related to many topics here).


### Story & Game
Especially because this is a data-analysis and skill-evaluation tool, the scope needs to be (potentially) as focused and clear as possible.

There are at least two kinds of topics colliding here:
1. The maintainability and understandability of increasing dimensions of game mechanics.
2. How narrative story and art-content does and does not intersect with abstract puzzles.

If the scope and scale of this game were not minimal but a full wizards of the coast, or elderscrolls, or white-wolf (or West-End, etc., etc.,) game, the data-space would be less amenable to feasible performing a practical study. 

Story is a deeper question. Not to get too much in the weeds, but even in many highly elaborate RPG systems there is the criticism that character development, story, and quality-social-game-play are not supported by a recreational hoarding of convolutions, or the now familiar tendency for video or tabletop games to being an all consuming fetish of ever-more-detailed combat-violence. 

'Story-ness' is rather elusive, and likely there will not be a useful  complete reductionist definition of 'story-world.'

But there is more meant here by 'story' puzzle than the entirely abstract distinction between non-strategic-introverted-logistics vs. cut-up-coordinated-decisions (or maybe that distinction entails more than it sounds like). 

On some level this is hopefully at least a minimal foot in the door. 

See a larger discussion of the role of story and art in games and puzzles (and the impact (often obstructive) of game-mechanics on story:
https://github.com/lineality/story_rpg_platform 


### Back to Tabletop
If this mini-RPG framework were used for a tabletop-game(as in theory it could be useful to have as an extremely portable, easy to set-up, quick-start table-top dungeon-crawl system that can be used with nearly zero set up time) are there additions or techniques that might help to emphasize the human story and to keep the game from becoming a story-less logic puzzle? 

- Hallway vs. room guidelines
- maybe floor-map generation tools...
- ways to work equipment, familiar, accessories, clothing into the game (may be ways for DM/GM to frame resonance)

There are various little tools that can help to extend the the dungeon room module into a levels of dungeon tool-kit:
- https://github.com/lineality/dungeon_fog_cli 

Such as dungeon level makers.

For example, where # is a stone wall, 'P' is the party of players, 'O' is doorway into a dungeon room (the main game-play focus), and 'S' is the stairwell down to the next level of the dungeon (and 'X' is whatever the DM/GM wants it to be for the story, if anything). 


And 'walk in fog' tools, so players can only see what is visible so far on that dungeon level.


If you wanted to make or automate level-rules, you could say something like: "You need one treasure of each element to go down the stairwell, and each level down has that number of monsters per room..." or something.

While moot in 2006 because AI cannot complete a single room, ideally AI will improve in future and it will then be useful to have a kind of AI-RPG-Arena Index/Benchmark, to standardize how many levels a model can complete.

#### Simple RPG-Arena-Index Rules v1
1. N = Dungeon-Level number (starting at 1)
2. Randomly degenerated Dungeon-Level is size: width=N,height=N,
3. Complete all rooms on Dungeon-Level
4. Dungeon-Level is completed by descending stairs.
5. A model's level/rank/index is the highest N that the model can complete, out of N tries.


### Five Types of Project Puzzles & Side-Games

This is not a clean list of categories on a uniform axis, but it might help to list out some of the various spaces of operational-features:

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


### Combined:
Types of puzzles do not have to be diverging (and disconnected from each-other), mini-game puzzles within puzzles are well established in games.

Various types of puzzles could be combined:
- Opening a chest could involve a pointless-puzzle / 8x8 'puzzle'
- Beating a monster could involve an 8x8 game like chess
- Opening a door, etc.
- Getting a person out of another object, etc.
- Keys, traps, etc.

Also See:
- Sume-go puzzles


### Make the Maker:
The exercise of making these tools is also noteworthy, if arguably at a higher level of difficulty than completing a minimal challenge-puzzle within the system.

- As of 2024.05, no available AI was able to make, describe, debug, etc., more than a small isolated simplified sub-component of this overall system. (As was in my notes from that date.)

- As of 2026.06, only some entirely pre-specified functions for this could be made using combinations of different AI models and approaches (e.g. each model making parts of a function to be later combined). 

One of the sub-texts of making and doing these texts is the yet-unknown limits of what 'Gen-AI' tools can competently do. One of the goals is to look more closely into what tasks which models can or cannot be taught reliably to do.

Both for students and as another model-test, making-the-testing-system is of value.



### The Human-Psychology of Machine Learning

Given that public renewed interest in AI is only about three years old as of 2026, it remains to be seen whether difficulties in understanding core concepts about STEM as applied to machine learning will continue to be a problem. History may suggest that this is likely to be (that it already has very long been, see links below) a persistent challenge.

Many times I have seen not only sales-people (who arguably do not know better) but also highest level engineers (who really ought to know better) describing pre-trained models as dynamically learning products. If this is a problem in adult upper management and engineering, how are children being taught (or not taught, or incorrectly taught) these concepts about tools they need to learn how to use? 

In this context it may be useful to have educational activities that teach people in a focused an hands-on way (ideally in a team-context) some of the practical details of STEM. 

Game-based learning is likely also a fruitful avenue to at least duly plumb.

(A topic survey by me (under construction))
- https://github.com/lineality/ai_2024_in_review 

(A real book by not-me)
- https://academic.oup.com/book/36637 
- https://www.amazon.com/AI-Narratives-Imaginative-Thinking-Intelligent/dp/0198846665 



### No Free Lunch and the Genie In the Lamp: Picking the right question is difficult, and interpreting an answer is difficult.

Maybe related to the no-free lunch theorem itself, it is very difficult to design tests and to gauge how far to read into the results. The minimalism of this test-set might be misleading in terms of the question framing and implications being less simple.


# Appendix 2: Sample Starting Instructions

```

# Task/Rules/Instructions:

You are player a, take your action:
1. State your action for this round in valid json (default is skip_turn)
2. To end planning and start this round,
say (in addition to your action): '''json
"start_round": true
'''

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
'''json
{
"player_id": "f",
"action_type": "move",
"move_from_coord": [0, 0],
"move_to_coord": [0, 1]
}
'''


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
a ID 6 -> Player 'a' | Element: ice | Energy: 1 | Inventory: []
b ID 4 -> Player 'b' | Element: void | Energy: 1 | Inventory: []
c ID 5 -> Player 'c' | Element: fire | Energy: 1 | Inventory: []
d ID 7 -> Player 'd' | Element: water | Energy: 1 | Inventory: []
e ID 3 -> Player 'e' | Element: forest | Energy: 1 | Inventory: []

-- NPCs --
ID 2 -> NPC | Element: void | Energy: 1

-- Treasures --
ID 1 -> Treasure | Element: ice | Energy: 1

=== Personal Status ===
Identity: a (Player 'a', ID 6)
Location: Row: 1, Col: 7
Element: ice
Energy: 1
Inventory (zero-based index): []
Status: active

=== Timeline (Last N Boards) ===
Round 1 Board:
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

# Limited Sight
In this room, your line of sight is limited by thick pillars
at the corner or each floor-space. You are only able to see objects
that are directly North, South, East, and West of where you stand.

Communication with other players can brdige this Point-of-View challenge.


# Staying In-Character:
And, since this is a Role Playing Game, it is good to stay in character.
In your Memo to other players, speak with a voice consistence with the element
of your character. You can even refer to your character's animal-familiar
and your weapons and outfit. (Staying in-character will earn you more stickers
to put on your character sheet!! But try not to brag too much about how many
stickers you have. Good luck in the Dungeon!)
```



# Appendix 3, Sample Bot Shared Memos: 

### "Cinder"

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
```

### Player e — Shared Memo:


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








