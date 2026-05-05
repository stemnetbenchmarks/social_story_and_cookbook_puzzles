# social_story_and_cookbook_puzzles

(under construction)

### AI RPG-Arena:
# Social Story Puzzles & 'Pointless' Cookbook/Logistics Puzzles

### A Testing, Training, Evaluation framework-set, including a Tabletop-like Mini-RPG for people or for AI-Bots

2024.05-06.22, 2026.04-05.05 G.G.Ashbrook




## Contents:

1. Introduction
2. Social Story Puzzles & 'Pointless' Logistics Puzzles
3. Functionality & Testing
4. Project Areas
5. Links & References

Appendix 1: Suggested Curriculum Projects
Appendix 2: Discussion
Appendix 3: Future Research
Appendix 4: The Game Rules & Sample Starting Instructions
Appendix 5: Sample Planning-Memos Shared by AI-Bots


# Introduction

Of the two kinds of puzzle-tests discussed here (and for which code that you can run is provided) the more interactive of the two is the Mini-RPG Dungeon-Crawl. 

The hope is that an intersection of familiar story-game, hands-on tools and code, being able to easily design and run your own tests, and example questions along the edge of what is known, will help you to confidently and inquisitively explore your own Data-Science questions and projects. 

I will try to start with a digestible entrypoint: simple, well-defined cases, questions, and terminology that should be accessible to everyone. The topic will get larger and less easy to follow, but we should be able to start with (and return to at any time) a universally clear 'base camp' that everyone can understand and agree on.

Doing a clearly defined study is a good way to approach a question. The question might be:
1. Can currently available AI participate in a basic team-project such as a simplified role playing game (RPG)? What skills are strongest or weakest (for a given AI model or pipeline-architecture)?
2. When different groups of people (for example, different age groups or other demographic groups) play the same team-project game, where do (which) people do well and where do they lack skills and fitness?
3. Both for AI and for human students, how much do we know about how to teach skills related to project management? 
4. How well do we understand communication and decision-coordination around shared-project data?
5. How much do we know about project management tools and long term best-practice skill acquisition?

Tools such as python-notebooks that can make it much easier for anybody to design, run, and share their own tests, are increasingly becoming more widely available, and more user-friendly. More people should use these tools.

We should all do projects. Doing projects is a core part of learning, for example each of perception, articulation, learning, and projects all actively rely on ongoing high-quality signals from the other three.


### Code Git Repo:
- https://github.com/stemnetbenchmarks/social_story_and_cookbook_puzzles 

### Live Notebooks in Colab:
- https://drive.google.com/drive/folders/1ETOeXGSF52_lkclJ7W_xSJNEZC0OEMz_ 


#### Dungeon Crawling (in summary)
There are two main ways to play through the Mini-RPG Dungeon-Crawl game. 1. Manual-Mode, 2. The AI-Bot-Arena

1. Manual Mode: You can play through manually, alone or with a group of people. When you play 'manually' you will iterate through each round of the game and keyboard-type (by answering Q&A prompts) the actions that each of five player-characters will take in the next 'round of actions' in the game. This is (hopefully) a lot like a table-top RPG might work, where you go around the table hearing what each player says about their actions. Players might discuss strategy with other players and will eventually announce their actions. Once everyone has decided on actions, the Dungeon-Master/Game-Master (DM/GM) calculates the consequences of all the player and non-player (NPC) actions and then explains what has happened as a result of that round-of-actions, thus setting up for the next round of actions. And then you do the next round the same way. 

You can play this way using a python-notebook (or using a terminal command-line-interface (cli)). All you need is either an online device that can access Google-Colab in a browser (even a phone or tablet can work), or you can play off-line on any device that can run python. 

I do recommend that you play the game through at least once (solving a dungeon-room) using this 'manual play method' to get a tangible understanding of how the dungeon rules and game-mechanics work so you can see all the nuances of what individual AI-Bots need to do to play well. 


2. AI-Bot-Arena: There is an AI-Bot-Arena, where a generative model takes on the role of each of the five player characters: Five bots for five players. The five-bots then plan and take actions, round after round, until either the whole team wins, loses, or until the game has reached a maximum number of rounds that you set.

The notebook and .py code is currently set up to use an AI-api from Mistral, Anthropic, or Google. If you are going to use a cloud-API, then you will need an account with some provider to get an API-key. (Or you could modify the code to run a local model. The performance of a small local model is not likely to be very good, but it is interesting to experiment).

Since you are more of a spectator of the AI game, there is the question of how you want to view the game: How do you want to see the planning and decisions made cooperatively (or not so cooperatively) by the AI-Bot players, and then the results of each round of actions presented by the Dungeon-Master?

(Note: The DM's description is abridged to eliminate the redundancy of what is re-told to each player separately.) 

- Option A: Let the game finish and then look at an automatically generated 'screenplay' of the game. When the game is done, an HTML file will be automatically saved. You can open that file (for example downloading it from colab and then double-clicking on the file) to read a round-by-round story of the game.

- Option B. View the game (in real-time, or afterwards) as a simple Visual-Novel. The visual novel can automatically progress through the story (or you pause or go back and forward). See: https://github.com/lineality/rpg_visual_novel_ui 

Either the Screen-Play-Script, or the Visual-Novel, should hopefully make following each Player-Bot's decisions more user-friendly. You also have the option of reading the logs-files (including error-reports on some invalid move choices), but reading over a lot of separate files is not great for easily getting an overall narrative sense of the game.


# Social Story Puzzles & 'Pointless' Logistics Puzzles
(See Notebook & Git links above.) 

(For the sake of brevity I am presenting "two" types of puzzle experiments, but the details of how they relate to each other are more nuanced. For example, the overall space of types may be more like five (not two). See the 'Discussion' section for more.)


"Pointless puzzles" are so nicknamed because they are not usually the kind of "games" that most people gravitate towards for sport and amusement (or for sportsmanship and edification).

One of the questions we will ask here, as we try to map out the relationship between these two examples of puzzles is: Is something really a puzzle if there isn't anything to figure out how to do? 

The idea behind ('pointless') logistics puzzles is to try to make a (scalable) puzzle that depends upon the state of a stateful system. Oh dear, what does that mean? To non-computer-science people the term "state" means something like government. To computer science people, "state" means the values assigned to variables. (Both are entirely correct.) So a puzzle (or "problem") with "state" can be something like: Alice is doing X-Y-Z over here, and Bob is doing A-B-C over there, and at some point they both need to be aware (signal communication) of what other people are doing and changing in the "project-state." The ~two types of puzzle we will look at here go into more detail (in different ways) about how Alice's and Bob's work can be connected by project-state.

(Problems that involve many participants needing to manage the state of a project are highly relevant to many real world situations across many disciplines (and may be especially relevant to AI/ML-applications).)

The 'logistics' type of puzzle represents a 'project state' in a very concrete and simplified way: a few lists of things. That's it. (Such as a list of ones and zeros, or a list of numbers, or a list of letters.) Each person in this scenario follows cookbook-like steps. For example: Alice takes the contents of Bob's list and adds that to her own list. Or, Bob takes all the numbers in his own list, sums them into one total number, and then adds that value to another list. 

This can be done using different types of operations on different types of values, three main groups of which are:
1. boolean values and boolean logic: and, or, xor, etc.
2. numbers: add, subtract, multiply, divide, etc.
3. strings (characters, letters and words): many operations you can do with strings of text.

In these puzzles people are sort of acting like lower level computer operations, comparing and moving around values in arrays in memory. Part of what is interesting about these puzzles is that you can rigorously generate questions and tests (to validate answers) for any set of solutions used as input. And you can make the cookbook-instructions as simple or as convoluted as you wish. A minimal example might be: Alice starts out with a list containing only a single zero. She moves that zero to the final-results-list. Done! Mission accomplished. As we add more steps to the cookbook the bigger picture becomes more difficult to understand all at once, but each step (or sub-step) is easy to understand.

While these logistics-puzzles are defined very abstractly, we can probably look at them as situations in a more relatable way. We can think of a given puzzle as being a market-place or as running a food-truck or a grocer, rather than logical operations on arrays of bits in memory. Instead of numbers, let's say there is a cart with eggs, flour, salt, and spices. Alice needs to move the eggs into her shop. Bob needs to mix the flour and spices. Tom adds the salt after Cat got the eggs from Alice (and after she made them into some rather nice Egg's Benedict with hollandaise sauce), etc. If you think of the puzzle-space, the project-space, in terms of shops and restaurants and that kind of logistics, it probably sounds more closely related to every-day life, and closer to puzzles that people do (and like to do), and it is probably a lot easier to understand in terms of the language and concepts we learn and live with every day.

Whether or not there is an analogy here for education, private sector employment, administration and governance, etc., these sort-of-story logistics puzzles are a pile of steps that do not have any point. There isn't anything that the participants are trying to find a way to do. Unless you choose to define the cookbook-steps as some very abstract form of "communication", there is no communication or coordination between the participants. If Alice is moving eggs over here, and Cat is cooking the eggs over there, and somewhere else Tom is salting and serving the eggs, those are steps that can be done without any communication or coordination between the people. Each person can be head's down, doing their task, whether or not the other participants exist or not.

So let's try to add more to the 'problem-space' of these puzzle-stories. Even with the story-ish analogy of a shop's or restaurant's logistics, those puzzles are still 'introverted tasks,' steps one person in isolation can read and carry out from a cookbook's list of instructions, regardless of everything else that is going on in the bustling market or during the lunch rush at the cafe. So, how could we make a similarly simple and well-defined puzzle that focuses on these missing coordinated-decision and problem-solving skills?

Fortunately we (on Earth) have a widely known type of game that we can use if we want to make something that is a bit more of a creative-problem-solving challenge, and something that will require the players to work together and coordinate (Coordinated-decisions studies!). The puzzle-tasks we want for this are not something that can be carried out by following pre-scripted steps or any unilateral solution. Even if you decide to solve such a puzzle yourself (on behalf of all the participants), the communications and coordinated-decisions are still implicit in the puzzle; it is implied that your solution was worked out by, communicated about by, and agreed to by the players. And we have a time-tested paradigm for just these needs: We have table-top Role Playing Games; we have players on a dungeon crawl.


### The Crawl: 
You are in a dungeon room with your four fellow adventurers. There is a monster in the room, and there is a treasure in the room. You need to get the monster, get the treasure, and get out of the room in one piece. You need to work together. 

One way of looking at this is that the solution to a dungeon room puzzle is any (of many possible) configurations of separate player actions. Instead of having a cookbook to follow, the players each start from a place where they do not have enough information to form a solution and where that solution is not something they can ever 'do' or 'output' themselves, and there is no way of knowing ahead of time how much communication of what kind will be needed to solve that room. All players need to align on a plan for how their team-actions can arrive at the goal: get the monster, and leave with the treasure.


#### Increasing a Need for Coordination
There are many possible ways that this RPG world could require more coordination between players (beyond multiple-players existing and the element-resonance system itself). Several of these are listed in the code-notebook. Though most are not yet implemented, one that has been included is based on perception.

When you set up the dungeon room, you can pick between letting all the players see the whole room, or having a limited-visibility environment restricting what each player can see from the point of view of where they stand. By analogy, this is as though the room is full of thick pillars and each player only has an unobstructed view along clear straight rows North, South, East, and West of where they are currently standing). 

This requires players to exchange information about where things are in the room, information that perhaps only they (and no other players) have. This makes the game more of a true 'cut-up' puzzle, where team-members need to share information about the puzzle itself (the project-state) to be able to solve it. 


### 8x8 Games: Chess & RPG
In keeping with the pen and paper and table-top nature of many RPG games (and the use of miniatures to track what is where), this 8x8 grid and 5-player system is compatible with a physical chess board and pieces: This Mini-RPG can be played as a physical board-game using a chess set. For example, you could have each player be one type of black piece (of which there are five shapes), and the NPCs, treasure and objects can be white pieces. 


# Functionality & Testing

How do we, how can we, and how should we, design and implement environments for learning? 

While there may be a fun-ish game in here somewhere, the overall context is intended to be no-less STEM/Academic: Can we find an intersection between formal-tests and well-defined evaluations that can be analyzed on the one hand, and on the other hand social-story puzzle-games that people participate in by choice, in an overall context of learning how learning happens with an eye to helping better learning and fitness?

### Applications and uses (hopefully) include: 
1. Help people to learn more about project-problem-spaces.
2. Help improve people's skills at doing projects (a.k.a to aid learning).
3. Improve (or at least study) AI-project-concept learning.
4. Help people to understand the strengths and weaknesses of stateless amnesiac generative models (E.g. How can a 'super smart' model have difficulty with a simple coordination puzzle?).
5. Use and leverage scalable problem-spaces (as the term is used here, problems that can be generated with one or more "scaling" parameters that increase or decrease N-dimensions of the same overall structure of problem (the two main types of puzzles in this study are both examples of this)).
6. Generate datasets, including N solution-testable problems in a problem-space at a given difficulty-scale.
7. Leverage solutions and errors that are analyzable; learn from those errors. 
8. Develop tools and best uses of tools.
9. Develop best practices and data that support STEM best-practice.


### Training & Testing

These puzzles can be used to test or train:
1. Individual people (for example in an educational setting)
2. Teams of people (as in a classic student-centered/constructivist 'cut-up' activity)
3. Individual AI (or architectures) (either as an evaluation, as training-data to build up a project-space-outcomes concept-set in the model, or theoretically as part of ~reinforcement training or fine tuning; possibly straight non-pretrained reinforcement)
4. Teams/Groups/Swarms of collaborating AI (either as an evaluation or as part of ~reinforcement training or fine tuning, etc.; possibly straight non-pretrained reinforcement)


# Projects:
Not surprisingly, this study is interrelated with project-management, coordinated-decisions, externalized project-object-databases, hybrid data, etc.:

- Definition Behavior Studies: https://github.com/lineality/definition_behavior_studies

- Project Areas (and project management):  https://github.com/lineality/project_areas_for_project_and_product_management 

- Coordinated Decisions: https://github.com/lineality/Networked_Voting_and_Decisions_Including_One_Time_Pads 

- Uma & T is for Task (still in progress):
https://github.com/lineality/uma_productivity_collaboration_tool/blob/main/t_is_for_task.md 

- Hybrid Data (structured and unstructured) https://github.com/lineality/hybrid_data 



# The Code
For more technical details, see (and run!) the notebook, or to modify it however you will:

### Code Git Repo:
https://github.com/stemnetbenchmarks/social_story_and_cookbook_puzzles 

### Live Notebooks in Colab:
- https://drive.google.com/drive/folders/1ETOeXGSF52_lkclJ7W_xSJNEZC0OEMz_ 



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

7. More on Basic Concepts
https://medium.com/@GeoffreyGordonAshbrook/five-ai-concepts-ecf5c9698559 

Also See:
- https://en.wikipedia.org/wiki/Fredric_Brown 
- https://huggingface.co/mistralai/collections 

More Game Design Discussion
- https://github.com/lineality/story_rpg_platform 

Farewell, Etaoin Shrdlu.






# Appendix 1: Suggested Curriculum Projects

Here are some curriculum projects as ways to integrate this starting material into a course (or independent study). One role of the instructor or other support should be to help guide the scope of a prospective project, as project scope tends to be as eyes too large for the stomach. Some of these are narrower in scope (e.g. time/resources/skills needed) others are larger projects. Helping others to refine the scope of their ideas is a valuable assistance.

1. Predict and test the overall (room-completion) success at different ~sizes of models and difficulty levels of rooms. [Easier Scope (only current notebook, minor planning, and api-key needed)]

2. Predict and test specific skill-proficiency presence and absence. (E.g. How exactly does a human or bot team fail to solve a room?)

3. Try to improve bot performance based on an improved prompt system.

4. Try to improve bot performance based on model training/fine-tuning. [Larger scope]

5. Try a reinforcement learning trained model. [Larger scope]

6. Try a hybrid-loss-function (re)trained model. [Larger scope]

7. Visual Space: Test if multi-modal inputs of maps improves performance.

8. Implement more advanced NPC movement patterns.

9. Implement local model llama-cpp api. https://github.com/ggml-org/llama.cpp  [Easier scope, not completely trivial but very finite]

10. Implement more advanced NPC fractional/multiple speed patterns.

11. Create starter-rooms that have exceptionally easy situations for a 'benchmark set' of curated difficulties. If a really-no-brainer room map (that a moderately capable LLM can solve) can be identified then a diagnostic set of increasingly difficult room-maps can be helpful. [Easier scope]

12. Implement a multi-floor dungeon iterator test (such as is outlined in the discussion and other provided tools. This will likely include a team-navigates-hallway challenge (with possible traps etc.)

13.Integrate logistics games in rooms and or hallways as optional mini/side games.

14. As language-concept-space puzzles, how would the introduction of 'immaterial' story-items for characters affect room-puzzle performance of player-characters, e.g. helping or harming overall performance. E.g. Would having a story-item relevant to a character in a chest (even if that had no mechanical function) improve that characters' performance? (Even if a first step of demonstrating some kind of quasi-motivational-story-mechanism effect works, clearly 'explaining' how this works may be infeasible. But various further tests around this could be very interesting.)


# Appendix 2: Details & Discussion

If the main body of the paper focuses on a simplest-base-camp, this section is where trails get attempted into the more dense and baffling surrounding wood. Hopefully this serves as a rough travel guide.

Between this discussion and the links (above and below) there is a truly interesting and life-relevant ~tree/web of interconnected topics.

If a given sub-section here is too obscure, apologies, feel free to skip to the next.


### Social Story Puzzle: Modular RPG Dungeon Crawl
RPG-SHRDLU: a story-oriented blocks-world for social and language-using participants

We can define a type of minimal social-story-puzzle, a mini ~Multi-Player RPG (classic dungeon-crawl), that is completely defined so that players will "make" and "implement" a plan (either for a round or a whole game in a given dungeon room) and that plan (that set of actions per round (or all rounds)) can be run through a game-outcome-calculator that acts like a simple GM/DM setting up the next round of the game (and judging if and when the game has been won). 

Each "random-seed" (and other "configuration variables and parameters" such as how many monsters/NPCs per room) will produce a fixed (reproducible) starting-room-state and the non-random outcomes will be ~deterministically (same-input, same output) calculated and validated. 


### Two Modes of Play: Whole-Game or Incremental-Iterative or 

Players can submit and implement their plans either 'iteratively' playing and seeing the outcomes of one round-of-turns at a time, or all-at-once (planning out the whole strategy for all rounds then running it all at once). If a solution is valid: test passed. If the solution is not valid: test failed. 

A. Whole-Game: One way to test a model is to give it the rules and the starting positions in the dungeon room (the 'state'), and have the model plan the whole 'room-story' all at once (all rounds), succeed or fail. This is similar to a logistics puzzle (both involve teams and roles and both are stateful), and this side-steps the coordination of the decision (so it lacks that aspect of a puzzle) but this does involve making a novel strategic solution (in the form of a cookbook for all the players).   

B. Incremental-Iterative (take actions and after each round see what happens): The iterative approach (or approaches (as "one" model could act for all players during each round, or five bots could coordinate each round)) open up more questions about the 'state' (or 'statelessness') of generative AI models. Breaking up the puzzle into smaller easier steps makes smaller similar easier sub-puzzles, but the 'context window size' and amnesia of the model create perhaps larger problems. If the model never learns and has no memories (only a kind of shadowy fake-proxy memory), then how many more 'integration roles' are needed to manage and stitch-together all the sub-puzzles? 
 
There is the manual-iteration-interface, but then there is also the more granular Bot-Arena where each player in each round is further subdivided into each planning round of N planning rounds within each action-taking round. 

Part of the point of taking the same task and being able to evaluate externalized-coordinated-project-state ways of doing things vs. internal-introverted-unilateral modes (doing the same task) is to try to gain some empirical insights of feedback about how formalities of project-state externalization (of the project-object-database) influences the set of what skills and fitness are required for and involved in doing that task.

Note: There can be other criteria for evaluating and comparing plans beyond pass-fail, e.g. some plans can require fewer steps (less time). 

### Steps:

Let's go through a very quick overview of how to use the online Google 'Colab' notebook book to run the puzzle in each way. (Note: A 'notebook' is way to run python-code that is user-friendly and easy to share, where you can make and run sections of code in 'cells,' and you can also write text-cells. 'Colab' is Google's version of the python-notebook, which is amazingly easy to share and use in a browser on ~any online device.) 

1. The 5-Bot AI-RPG Arena:
This mode in colab uses a cloud 'api' for an ai-model, so you will need to have an account with either Mistral, Anthropic, or Google. I recommend Mistral and Antropic (mistral has a wide variety of inexpensive models, many of which are ~open-source so you can run the model locally on your own hardware if you want (e.g. see Huggingface https://huggingface.co/mistralai/collections), google's api (as of 2026) is highly unreliable (often out of service) and the models are not very good. Once you get an api 'key' (like a password) and securely put it in Google-secrets (on the level side tools of colab), you should be able to just "run all cell" (see the "> Run all" button, or in a pull-down menu too). Towards the bottom of the notebook you will see the cells for each of the three methods, the bot-dungeon will be the first. It should run by itself and save files that you can view in or download from the file-browser in colab (also tools on the left). This should include a .zip archive of all logs, and a .html 'screen-play' of the dungeon story that you can download and open in a browser. The way the Bot-dungeon crawl works is that first the Dungeon-Master explains to each bot what the rules are and what is happening in the dungeon room. Then all the bot-players (like players around a table-top RPG game) go around planning how to win the room until someone says they are ready to act, then the next round of actions happens, then to planning the next round etc. until either the game ends, or they lose (or you can set a max-limit of rounds, currently set to ~2). You can also run the Visual-novel code on the downloaded and unzipped log-files, as a different way to go through the story and see what good or bad choices each bot made.

2. Manual Iteration through Rounds:
The second method (next down in the notebook) is where you (not a bot) play the RPG-dungeon crawl yourself. You do not need any ai-accounts or special setup to do this. Just follow the Q&A steps and learn how the dungeon works and how to win each room. I recommend this as a good way to learn about what we expect the AI-Bots to figure out how to do.

3. You can also use the whole-game-plan tool. Curiously, this is a kind of bridge between the 'logistics-steps' puzzles and the 'social-story-puzzle,' because this tests just the game plan itself, not how the plan was created, so not a 'social' version of the puzzle, but somehow the same puzzle (the same solutions (many of them) being just as valid). For example, if you want to isolate just the room-puzzle and put aside the teamwork-project-management social-story part the game, you can try asking any chat-bot what it thinks a valid solution to the puzzle is, then you can run that solution through the tester to see if the chat-AI solved the puzzle. The basic steps are:

#### Types of Puzzles And tests
Social stories and logistics are rather intertwined, but in some cases we can make the distinction that separates plan-invention (or solution-discovery), importantly including the problem spaces of information-sharing and coordinated-decisions from a problem space that only includes instruction-following and solution-implementation. 

In some ways there seems to be no clear dichotomy between social-story-puzzles and introverted-logistics tasks (as I nick-name them here, suggesting or presuming there is a difference between the two). If you break everything down into a pile of steps then everything looks like a pile of steps. And if you look at a logistics puzzle through the context of a village marketplace then it looks like a (it is a kind of) social story (with the same Alice, Bob, Cat, Dog, Eretosthenes cast of players, each doing their interlocking roles). But if you change the context then two seem more different, for example: Is there a problem to solve? The Dungeon Crawl poses a problem: How can you get the monster, get the treasure, and all walk out of the room? There is (presumably) no passive way to survive the dungeon; there is no dungeon cookbook. For the logistics market-restaurant-story puzzle, each player has a list of tasks to follow, but there is no 'problem' to solve. In fact, you do not even know what the result of the cookbook recipe will be until you follow all the steps.

We have the linear-cookbook tasks on the one hand where the solution is implementing one (cookbook recipe) logistics-process where there is effectively one correct or faithful "solution" (move three eggs (or bits) from this array to that), but it does not involve discovering the solution to a problem so much as following established steps. Sometimes this distinction of 'tracking logistics' vs. 'Finding a solution' seems non-existent, other times it seems more tangible. Even though both are Alice, Bob, and friends team projects, one context is to look at communication and decision. Even though in both types of puzzles each player tracks the moving logistics and follows along, in the 'pointless' logistics (marketplace, kitchen cookbook) type of puzzle there is no need for communication, and 'decision' is a perhaps misleading term for implementing the instructions that were already provided (the cook book recipe). On the other hand we have 
social-story open ended problem-solving where there are many (maybe infinitely many) viable solutions to each problem. The problem space in a social story puzzle is not A. 'follow instructions' vs. B. 'fail to follow instructions,' each player and on an aggregate level the project-team as a whole, needs to navigate through a problem space of multiple possible correct or incorrect solutions, where they are not told which is which (or even what those solutions are). In some (perhaps unrealistic cases) each player has full information about the game, but more realistically the problem space involves coordinating to share that basic information across the players. 

Where we have what in English we would call 'a problem to solve' the problem-space includes a Hayekian-signal-ecosystem (though ironically the logistics puzzles appear to resemble introverted isolated tasks in a marketplace, after the origin of those steps has been abstracted away). 

#### Special Cases + "Make the Tester"
As a non-cut-up puzzle, having a puzzle to solve merged with a logistics-puzzle, is the game-processing code itself the logistics portion of how to implement a 'class' of solutions (e.g. rounds of actions), for any given input (and valid actions), to determine the output (the outcome of the round/game)?)

With all these different factors, we may be looking at five (that same number again...) inter-related puzzle-problem-spaces, or five types of skills/tests:

1. solution cookbook-recipe class implementation
2. solution class design
3. introverted-unilateral solution design
4. solution design coordinated-decision with project-state
5. cut-up solution design coordinated-decision with project-state

I would also question whether multi-participant-interdependent actions can or should be broken down into introverted tasks (such as characterizing both types of puzzles as identical introverted-unilateral array-value shuffling actions). Using dynamic feedback within a process is likely not always just another linear step in a pile of linear steps. And it is not clear to what extent different contexts and details matter for real world skill-building and skill-retention. Scalability, modularity, coordinated decisions, and various levels of perception and articulation of project-area parts are all key factors in the skills, fitness, and best-practice needed to complete projects, and for a diagnostic understanding how projects fail and systems collapse. 

(It is also a towering irony here that the software industry and computer science spent fifty years in shambles, doubling down strong-and-wrong on the cult of anti-communication. Practices like Agile (though the kanban-board predates software) will hopefully apply STEM to the need for better managed projects, but as of 2026 the rebellion against project management is still in overwhelming majority.) 


#### Steps for Method-3 Whole Game-Plan Test:
As more detail for the above mentioned whole game-plan test mode, here is an outline of the workflow to do such a test.

1. Pick a random seed for the room (42 is a good starter (maybe?)), and other configurations, probably starting with one NPC. 
2. Make an initial dummy-data-plan so you can inspect the room: e.g. You need to have an idea of how the monster moves, and of where each player will be, in order to be able to plan what you will do.
3. Generate a Fact-Sheet Prompt (using the inspection-results)
4. Inspect the room, the NPC behavior and your starting locations, etc. (This is done by whomever the player is, e.g. you or an AI.)
5. Make a real game-plan.
6. Test the plan!
7. Rinse and Repeat: See what you did wrong and try again, until you survive the dungeon (or the AI does).



### Asynchronous Puzzles & Race Conditions
On the one hand the pseudo-asynchronous kludge of game-rounds and simultaneous turns is an artificiality that would not map well onto a fully real-time puzzle (such as a swarm of in-motion bots). Two questions:

1. Is there a test-data-understandability problem in a deeply dynamic test where, perhaps in a context of Rust memory atomics, the states of arrays in memory are too ambiguous due to race-conditions? This may translate into the question of: If rules are so loose that mistakes break the ability to see what you did wrong (e.g. untraceable undefined-behavior problems) how does that low-level signal-distortion negatively affect being able to use and learn from available learning-signals? 

2. Is there an enduring utility in iterative planning? While processes themselves may happen in a more simultaneously dynamic way 'during the agile sprint,' is there a process-layer of iteration that persists even when actions themselves cannot be pre-structured in time? 

While we can create a more asynchronous version of a minimal dungeon, e.g. where bots are continually cycling through their own loops instead of stepping through an imposed and artificial order of actions, what would that change about the overall puzzle? (Maybe we need to try and see...)
(e.g. even in the real-analog bio-ecological world, best practice is to divide projects into discrete planning and action schedules, with literal round-robbin 'standup-alignment' communications, very much like the 'artificial' game-space. 

### Modular:
In this modular framework there is a ~most minimal starting version, but there are also many aspects that can be changed to introduce increasing 'dimensions' to the puzzle.
- More 'monsters'
- Monsters with less simple behavior (
- Conditional Perception (involving more player-to-player 'cut up' coordination to solve the puzzle)
- multiple and fractional speeds of movement
- having a dungeon room inside of a ~mob/npc/object as in a puzzle in a puzzle (e.g. to get inventory items out, including other players).
- having dungeon room information not automatically universally available to all players, e.g. line of sight information or element-specific information.
- etc.

And these can be combined:
- opening a chest could involve a pointless-puzzle / 8x8 puzzle
- beating a monster could involve an 8x8 game like chess
- opening a door, etc.
- getting a person (or other object) out of another object, etc.

And / or navigation through hallways (possibly with 'traps') and entering rooms ('locked' doors?) might involve other puzzles of some kind.
 
(Note: It is probably a good idea to do further planning on ever-easier starting game configurations as well, as the minimal seed:42 room is still too difficult for any AI I have tested.) 

### NPC Movement
Where a 'whisp' is a starting monster/NPC(non-player character) that moves (once per round) in one direction and "bounces" off any object (such as a wall) going then in the opposite direction, and where the starting direction can be set by the random-seed of the room: A small-step-forward version of this is to have different types of whisp-monsters with motion-behaviors that are (still each ~deterministically self-consistent, but) not identical (compared with the movement-behaviors of other wisp types). Each wisp "type" can have its own static pattern(s) of movement that are predictable (once you have observed what they are).

We can extend to 'patterns' of movement that are not entirely simple. Movement is based on a function that take a few iterations of observation to be able to reconstruct: e.g. on every third move the wisp moves two spaces not one, or on every Nth move it changes direction clockwise (so moving in a square-shape); or every Nth move it changes direction but that direction alternates, etc. Each increase in strategic depth will require more careful planning for what the team-members should each do. Even a simple square movement path is not trivial to see when each player is only able to see North-South-East-West in obstructed-visibility rooms with narrower points of view.


### One-Time-Test vs. Repeatability with N-inputs and N-outputs
One difference between a logistics test (where the 'solution' is a process, not an individual solution) and a social-story-puzzle (in the context here) is that you can test a given logistics solution with N different inputs and outputs (e.g. the starting arrays determine the end-array, but infinitely many starting arrays can be used), it can operate perhaps ~similarly to 'unit tests' for code. The social story test is more of a dynamic coordination test, less of a static-introverted-unilateral-algorithm test. (As mentioned, combining the two may be interesting...) 

Both puzzles are generated ~deterministically (same input, same output) and are consistent with repeatability, but the language-bot process is not a static single-context artifact. For most models, even at a low 'temperature' (a topic that can cover many specific model settings, raw llama-cpp use is a good way to learn more about this, rather than the over-simplified consumer-simple-api with reified user features) the actions will not be the same when re-tested.

A solution to a social-story-puzzle (even as a whole-game-plan test with the communication abstracted away) only applies to that one puzzle-state input, not for a class of logistic inputs, and the outcome is also singular (not a class of outputs for a class of inputs). 


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


### Single-Task Reinforcement-Learning vs. Foundation-Model Language-Concept 'Pre-trained' Learning

As of 2026 I have not seen any generative-model come close to being able to navigate these 'tic-tac-toe' level-difficulty RPG puzzle-rooms (maybe that is slightly under-selling the difficulty). How can we either get this technology to be better at (at least basic) team-project and coordination skills or design a different technology (such as a different type of learning or remembering)? How can we understand how the models are failing at what specific skills and tacks? How can a model that can talk a good game do so badly at a task that it will confidently claim to be able to explain to you? (And how quickly should we accept these confident-sounding and appealing explanations?)

I am not at all claiming that these are unsolvable AI-puzzles (I assumed AI would not find them so difficult). The focus that I am interested in is using the intersection of topics in this paper as a hands-on way for people to:
1. see the kinds of mistakes that models make, 
2. see and discuss how models or architectures can 'learn' from past failures (and successes), (or are designed to not be able to remember and or learn from past events at all) and 
3. to see how project-state and unstructured-data work in the workflow of "hybrid" software "pipelines" that combine structured and unstructured (and semi-structured) data as well as (so strangely named) symbolic and subsymbolic approaches to machine learning and algorithms. 
The individual performance of a model, a person, or a team of people (and frankly people are horrible at project-tasks too) on a given puzzle I think is missing the forest for the trees. The goal is not cheering or booing and sport-thrill victory or loss, but rather improving our fitness with handling and describing team projects (of which dungeon crawls can be a choice example). This is a problem-space that society would do well to become more literate and familiar with.

Question: For the whole-game solution, as with SHRDLU and Blocks-World, a reinforcement learning model might do well (I am guessing). But in various kinds of cut-up situations where coordinated strategy and missing information are needed, what is the potential for single-task reinforcement learning vs. a trained language-concept foundation-model? This might depend in part on how many kinds of variation there are in the communication-space. Can a narrow 'no concepts' protocol be developed for just this puzzle, or is the number of different ways that players need to coordinate so varied (and modularly recombinant in their variation) that a blocks-world-soccar-model would not find traction? Is this a task that calls for general language competence and many world concepts, even though the space is still a logical-rule space (not an analog physics space of unpredictable bouncing objects). 

Project and coordinated-decision skills are, arguably, at the forefront of STEM being either not yet or barely recognized by still-not-STEM-literate humanity as existing (let alone being of value). 



#### Memory & Learning in the Pretrained-World: Taking it Slow
As a note on the above references to 'learning,' while large cloud models are beyond the reach of most people to train, it may be worth experimenting to make a dataset representing the problem space and training a QLoRA (Quantized Low-Rank Adaptation) layer on a much smaller model. Could there be any notable skill, fitness, performance improvements from this? 

Also see: 
- Richard Sutton on reinforcement vs. pre-training 
- Demis Hassabis on feedback-backs learning.
- https://www.theguardian.com/games/2026/mar/16/petri-dish-brain-cells-playing-doom-cortical-labs 

Paper and Code on alternative designs of a 'pre' training loss function:
- https://medium.com/@GeoffreyGordonAshbrook/loss-functions-for-task-outcomes-preconditions-for-learning-641ca9d48572 
- https://github.com/lineality/gutenberg_babble
- https://github.com/lineality/gutenberg_babble/tree/main/perseids/byte_perseid


### An Open History-Mystery Puzzle: Historic Popularity
The semantics are curiously sensitive here, but as of 2026 table-top-style RPG stories seem to be more popular as social-games than virtual or real cookbook-recipe-following as a game (arguably). You could argue that gamified 'cooking shows' have an even wider audience than Table-Top-RPG, but I'm not aware of people having a 'cooking game' night the way it is common to have a 'gaming night.' But, definitions vary.

It would be interesting to have a paleontology debate about the prominence of pre-historic social-cooking vs. prehistoric social-story-telling; both are no doubt quite ancient. And if 'pack hunting' is a game, it both combines cooking with monster-hunting and pre-dates a given primate species (slightly post-Cambrian?).

It is said (e.g. from the works of Richard Rudgley) that pre-'language' symbols from about the end of the last ice age were likely, you guessed it, market logistics symbols (none of this social-story chatter stuff).

Going back in time to and past the earliest times of writing, painting, and speaking, which do you think people liked doing more, task logistics (including cooking) or social stories? They look like siblings to me. 


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


### Sport vs. Sportsmanship
There is much more to games and puzzles than antisocial, predatory,  sport-thrill-seeking behavior. Publishers of games should have the spine to emphasize more enriching content, not a race to the bottom, least common denominator, contraction into ever less mindful and ever more escalating trauma-disturbance. Institutions, academics, and STEM areas should all do more to utilize and emphasize the constructive uses of stories, games, puzzles, and worlds. From therapy, to education, to public and private sector team projects, to the uses of feedback, conceding all of gaming to criminality is a concession too far.

On many levels, people of all ages and across disciplines may find something of interest in the code and questions here. With the feedback from hands-on projects done together there is inestimably more than in the isolation of compartmentalized silent conjectures trapped in a psychological dungeon of desks and cubicles. Find the doors.


### Story & Game
Especially because this is a data-analysis and skill-evaluation tool, the scope needs to be (potentially) as focused and clear as possible.

There are at least two kinds of topics colliding here:
1. The maintainability and understandability of increasing dimensions of game mechanics.
2. How narrative story and art-content does and does not intersect with abstract puzzles.

If the scope and scale of this game were not minimal but a full wizards of the coast, or elderscrolls, or white-wolf (or West-End, etc., etc.,) game, the data-space would be less amenable to feasible performing a practical study. 

"Story" is a deeper question. Not to get too much in the weeds, but even in many highly elaborate RPG systems there is the criticism that character development, story, and quality-social-game-play are not supported by a recreational hoarding of convolutions, or the now familiar tendency for video or tabletop games to being an all consuming fetish of ever-more-detailed combat-violence. 

'Story-ness' is rather elusive, and likely there will not be a useful  complete reductionist definition of 'story-world.'

But there is more meant here by 'story' puzzle than the entirely abstract distinction between non-strategic-introverted-logistics vs. cut-up-coordinated-decisions (or maybe that distinction entails more than it sounds like). 

On some level this is hopefully at least a minimal foot in the door. 

See a larger discussion of the role of story and art in games and puzzles (and the impact (often obstructive) of game-mechanics on story:
https://github.com/lineality/story_rpg_platform 


### Back to Tabletop
This report started out describing a computer-based RPG-game (one inspired by tabletop games) to be used for analysis. What if we try to step fully through that door that we wedged a foot into? 
- Could this Mini-RPG be used for a primarily-story-based game for people? 
- Could this Mini-RPG be played as a quick-start Tabletop RPG? 
- Could this single-room focused game be elegantly or simply expanded into a full multi-level-dungeon game (either for people or as a larger Bot-Test? 

There are a few (somewhat intersecting) directions this expansion could take. 

One is a very-portable Dungeon-Crawl for people who want to play an in-person game without the set-up time that many tabletop games require. The emphasis here is probably on practical ease rather that ideological-minimalism (strictly only graph paper and number-2 pencil). Having a chess set, some pens and paper, and a laptop should usually be easy to get without expense on short notice.

Groups playing online is also something that is more cumbersome than it *should* be. 

Either way, it would be useful to manage levels of dungeon rooms. In the notebook (and some in their own repos), there are various little tools that can help to extend the room-module into more of a full dungeon tool-kit. See: https://github.com/lineality/dungeon_fog_cli 

#### Dungeon Level Makers & Viewers:
dungeon_fog_cli contains two parts, a hallway of doors (a level) generator, and a point-of-view manager so that the players only see what is nearby (or past) in the dungeon maze.


In this example, # is a stone wall, 'P' is the party of players, 'O' is doorway into a dungeon room (the main game-play focus), a period (.) is position along the hall (could be blank, but easier to count with a dot), and 'S' is the stairwell down to the next level of the dungeon (and an optional 'X' is whatever the DM/GM wants it to be for the story, if anything). 



With the 'walk in fog' tool, players see further as they walk (with ~ or whatever you choose for the unknown regions). 


There is no single way to do rules for level, but there are some obvious simple options. E.g. 
- "You need one treasure of each element to go down the stairwell, and each level down has that number of monsters per room." 
- "For each level you need that many keys from treasure chests to go down to the next level.


The story part of the game is both speculative-here and subjective, different people gravitate towards (and prefer) different types of games. While very speculative, I think it would be interesting to experiment with a system-mechanic that is:
1. not level-based or even progression based
2. requires coordination and planning, not luck or high-level-ness
3. very story flexible / not highly detailed

A perhaps contrary aspect is that each of the five players must be assigned a different element (perhaps randomly assigned). But within that framework the player (and the GM/DM) can make up whatever story fits over the very simple skeleton of the player, NPC and other object elements. Just as characters can create whatever backstory and details for their character. What would the story-play-experience be like for the people if a wide range of 'story rationalization' was compatible with the sparse rules? Clothing, items, companion-animals, spells, weapons, skills, game-props, etc., could be anything that describes an intended action and whatever the effects turned out to be.

It may not work to go this far in the opposite direction of level-based unilateral action realism, but that direction of chasing ever higher detail combat-simulation has broadly led to a both reduction in story and character and a rejection of that lack of artful character by many players.

Are there additions or techniques that might help to emphasize the human story and to keep the game from becoming a story-less logic puzzle? Are there ways of forming a puzzle-grammar to, for example the situational-puzzles set up systematically in Shakespeare plays? Hopefully people in the future will have more data to work with.

#### To have a fully structured full-dungeon for a Bot-Test:
While moot in 2006 because AI cannot complete a single room, ideally AI will improve in future and it will then be useful to have a kind of AI-RPG-Arena Index/Benchmark, to standardize how many levels a model can complete.

##### Simple RPG-Arena-Index Rules v1
1. N = Dungeon-Level number (starting at 1)
2. Each room and level is randomly generated with a timestamp seed.
3. Randomly generated Dungeon-Level is size: width=N,height=N,
4. Complete all rooms on Dungeon-Level
5. Dungeon-Level is completed by descending stairs.
6. A model's level/rank/index is the highest N that the model can complete, out of N tries.


### Five Types of Project Puzzles & Side-Games
This is not a clean list of categories on a uniform axis, but it might help to list out some of the various spaces of operational-features:

1. Bitwise Boolean
The most basic logical and boolean operations.

2. Numbers
Operations on numbers.

3. Strings
String operations.

4. 8x8
2D special rule games such as tic-tac-toe, connect-four, checkers, chess, iGo, etc.

5. Mini-RPG Dungeon Crawl
With a small number of rules, a multi-player dungeon-crawl can take place on an 8x8 grid with as few as 7 numbered objects on the board. This opens up the project space to coordinated decisions, cut-up puzzles, strategy and tactics, etc., as well as less-minimal RPG game and puzzle elements.  


### Combined:
Different types of puzzles do not have to be disconnected from each-other; mini-game puzzles within puzzles are well established in games.

Various types of puzzles could be combined:
- Opening a chest could involve a pointless-puzzle / 8x8 'puzzle'
- Beating a monster could involve an 8x8 game like chess
- Opening a door, etc.
- Getting a person out of another object, etc.
- Keys, traps, etc.

Also See:
- Tsumego puzzles


### Make the Maker:
The exercise of making these tools is also noteworthy, if arguably at a higher level of difficulty than completing a minimal challenge-puzzle within the system.

- As of 2024.05, no available AI was able to make, describe, debug, etc., more than a small isolated simplified sub-component of this overall system. (As was in my notes from that date.)

- As of 2026.06, only some entirely pre-specified functions for this could be made using combinations of different AI models and approaches (e.g. each model making parts of a function to be later combined). 

One of the sub-texts of making and doing these texts is the yet-unknown limits of what 'Gen-AI' tools can competently do. One of the goals is to look more closely into what tasks which models can or cannot be taught reliably to do.

Both for students and as another model-test, making-the-testing-system is of value.


### The Human-Psychology of Machine Learning
Given that public renewed interest in AI is only about three years old as of 2026, it remains to be seen whether difficulties in understanding core concepts about STEM as applied to machine learning will continue to be a problem. History may suggest that this is likely to be (that it already has very long been, see links below) a persistent challenge.

Many times I have seen not only sales-people (who arguably do not know better) but also highest level engineers (who really ought to know better) describing pre-trained models as dynamically learning products. If this is a problem in adult upper management and engineering, how are children being taught (or not taught, or incorrectly taught) these concepts about tools they need to learn how to use? 

In this context it may be useful to have educational activities that teach people in a focused and hands-on way (ideally in a team-context) some of the practical details of STEM. 

Game-based learning is likely also a fruitful avenue to at least duly plumb.

#### (A topic survey by me (under construction))
- https://github.com/lineality/ai_2024_in_review 

#### (A real book by not-me)
- https://academic.oup.com/book/36637 
- https://www.amazon.com/AI-Narratives-Imaginative-Thinking-Intelligent/dp/0198846665 


### No Free Lunch and the Genie In the Lamp: Picking the right question is difficult, and interpreting an answer is difficult.

Maybe related to the no-free lunch theorem itself, it is very difficult to design tests and to gauge how far to read into the results. The minimalism of this test-set might be misleading in terms of the question framing and implications being less simple.


### What is a "Game"/"Puzzle"?
If only to illustrate that people do not always agree about this, John von Neumann (one of the founders of game-theory) famously asserted that Chess was not a game, but rather a calculation with a solution (whereas most people do consider chess to be a game). (See: https://www.amazon.com/Man-Future-Visionary-Life-Neumann/dp/1324003995)


### Other Questions:
- In real-world stories, where people need to learn skills, how are those 'learning environments' shaped and managed? 
- Can and should games and puzzles be used to teach real world skills? 
- In machine learning where testing and training data are often needed in large quantities (both to create a machine for a task and to evaluate how good that machine is at a task), can skills and concepts be supported by enough data describing both tasks and errors?
- Are there ways that specialized marketplace-role tasks are, perhaps invisibly, abstracted away from the Heyakian-signals that properly functioning markets rely upon? While a market-place should be a signal and decision coordination puzzle like a story-dungeon-crawl-cut-up, in what ways and cases is it or is it not?
- Would a human-team equipped with a generative/embedding foundation model resource perform better at the dungeon crawl puzzle than a human-team in the state of nature? (Note: Despite several centuries of debate, there is no consensus on a definition of either a state of nature of a paradigm of modernity.)





# Appendix 3: Future Research

1. Automated Mistake Analysis
One area that might be very important, but which is not elaborated on here, is Generating Error-Mistake-Analysis-Data Per-Puzzle

If more-so for logistics-puzzles, it should be possible to generate some level of (reliable) automatic reporting on what went wrong with a proposed solution. This may be important to go along with raw-error data for learning processes (for people and robots (as far as we can continue to make that distinction)), as well as a unit-testing type error diagnostic that is useful to have.

2. Evidence-Based Optimal Learning Patterns (for people)

3. Is there a way that raw concept-vectors might be used to map aspects of this problem space, or other non-generative models? (Trying a standard reinforcement soccer-football-game approach?)

4. User Interface: While in many ways pouring time and compute into fancy 'graphics' is not constructive, finding the right balance of a proportionate and maintainable interface that allows users to see, understand, and interact with the process and the code is useful. How can more groups of people comfortably work hands on with this problem space? 

5. Are there other coordination elements that correspond with key not-automatically-learned-skills that can be added so that more evaluation and training detail and value are possible?

6. Curricula: skills, training, fitness, feedback: Where coordination skills are important for all people to have (which I think is 'everywhere'), where methods work best (broadly or in what specific contexts such as specific groups or demographics of people) to either most quickly or with best long term retention improve test-able group project collaboration and coordination skills?

# Appendix 4: Sample Starting Instructions

The rule-set for this Mini-RPG, everything a player or GM/DM needs to know, is short enough to fit on one side of one printed piece of paper (and could be more tersely squeezed into less). Below are two examples of these instructions. 

First is a short overall 'rules of the game', and then an example starting-room. Next is a more specific set of instructions to one player (minus all the memos from other players) for one specific round of play (for one planning-iteration for that round of play), as is given to each AI-Bot so that it can plan the next action and communications.

(See the notebook (or .py code) for more details (and to experiment with framing the rules and instructions yourself).)

#### Overall Rules (not single player or single round specific)
```
## Rules:
1.  Binary Goal:
- The whole party defeats monster(s) and leaves the room with treasure, or not.

2. "Five elements" Resonance Governs Interaction & Energy:
- Everything in dungeon is an 'object' with resonance
- Element-Resonance-Effects are area-of-effect: 8 neighbor-spaces around object/player
- Help-resonance generates +1 energy for the helped, no cost to helper.
- Harm-resonance subtracts & transfers -1 energy from harmed to harmer.
- Energy is >= 0

3. Elemental Resonance:
   - Helps: water->forest->fire->void->ice->water
   - Harms: water->fire->ice->forest->void->water

4. Players have one action per turn:
- The action-sequence ("initiative") for players is always a-e
  (alphabetical == chronological).
- What is randomized per room is the integer-id,
  so the placement of player in the room,
  and their elemental alignment.

5. Player-Character-Action Options:
- 'move': Move one space. including diagonal (8 neighbor-spaces)
- 'throw': Relocate adjacent (8 neighbor-spaces) object/player,
    or inventory item, to any empty space
- 'exit_room': Must be at door to exit
- 'skip_turn': No cost

6. Action Cost:
- Player action (move/throw/exit) costs/requires 1-energy
- Monster/npc require >=1 energy to move, but movement costs nothing

7. Absorption: Absorb object into your inventory
- If absorbed object has inventory items, they move to your inventory
- If object-A helps object-B, but object-A has no energy,
   then object-B 'absorbs, carries' object-A as an inventory-item.
- Absorption costs nothing: (like resonance-effect) absorption happens   with no 'action' required.
- This is how 'monsters' are removed from the board.
- This is how treasure is collected.

9. Monster/NPC Behavior:
- For a given type of NPC, you do not know what their actions will be.
You will need to re-try a room based on a past record and timeline.
```
#### Example Room:
```
=== Example Dungeon Room ===

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

=== Example Exit Location ===
The exit door is located on the 'right' wall at coordinates (row, col): (1, 7).

=== Example Room Legend ===

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

```

#### Rules for a single-player Bot (single-player specific, single-round specific, and single-team-planning-iteration per round specific)

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

Communication with other players can bridge this Point-of-View challenge.


# Staying In-Character:
And, since this is a Role Playing Game, it is good to stay in character.
In your Memo to other players, speak with a voice consistence with the element
of your character. You can even refer to your character's animal-familiar
and your weapons and outfit. (Staying in-character will earn you more stickers
to put on your character sheet!! But try not to brag too much about how many
stickers you have. Good luck in the Dungeon!)
```



# Appendix 5: Sample Planning Memos Shared by AI-Bots

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




