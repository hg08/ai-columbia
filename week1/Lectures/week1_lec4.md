# week 1 lecture4

So maybe enough for now about AI history and AI applications and foundation.

Let's talk a little bit now about our course **logistics**.

So this course is an artificial intelligence course at the masters level.　(研究生层次的课程)

Which means that you can expect some challenge in completing the course,

it's going to challenge you and you learn a lot from it.

As of the perquisites you are required to have some knowledge of **programming** and

understanding of **probability**.

**Python** is the programming choice of language for this course.

Whether it's 2 or 3.

Will accommodate both versions.

Assignments that would be two counts of assignments.

Quizzes or conceptual assignments that will test your understanding of the lectures.

Here please **make sure you read the instructions and**

**questions very carefully before you hit submit of your assignment**.

There will also be some **project assignments** or programming assignments.

The course offers an excellent opportunity for students to dive in Python programming

while solving AI problems and learning its applications.

So dive in course materials which recommend but do not require this book,

which is the main reference in the field, *Artificial Intelligence,*

*A Modern Approach* from Stuart Russell and Peter Norvig.

This is like the encyclopedia of AI, and represent an excellent reference for

whoever wants to learn about the history of AI, the techniques AI and applications.

I use it as the main reference from my lectures.

And you could find in this in the book website and large number of

resources that you could also look into it as you follow the lectures in this course.

We're going also to post a large number of reading materials and

let useful links as we go in the course for each of the topics that we cover.

What you'll learn in this course is an introduction to artificial intelligence,

the history of AI, building intelligent agent in search,

games, logic, and constraint satisfaction problems.

Machine learning algorithm is also a topic in this course where we dive into

several machine learning methodologies.



Applications of AI to natural language processing, robotics, and

vision would be at the end of this course.

**We will learn how to solve AI problems through programming in Python.**



# 本课程结构

Our course roadmap is as follows:

We start for the first with the notion of rational intelligent agents followed by

different kinds of agents including search agents in an *uninformed search*（盲目搜索） and

informed search（提示性搜索／启发性搜索）, adversarial search (对抗搜索) or games,

followed by **machine learning algorithms**.

We tackle then *constraints satisfaction problems* or CSPs,

and *logical agents* through propositional logic (命题逻辑), and first order logic.



The second topic is about **Markov decision processes and reinforcement learning**.

And we will finish the course with a set of applications through natural

language processing, vision, and robotics.

Now let's take a tour over all of these topics.

So first of all, rational intelligent agents.

This school is about designing intelligent agents

where an agent *perceives* (感知到) its own environment

and acts upon that environment to achieve some task.

An agent could be seen as a function F, that actually goes from the set of percent

or whatever the agent is perceiving from its environment to a set of actions, A,

in which the agent acts in that environment.

So this is a way to see agents as a function.

We care specifically about rational agencies,

our agencies that do the right thing.

We'll define what is doing the right thing in the next lecture.

Do the right things.

Rationality is relative to how to act to maximize a performance measure that actually tell us how the agent is doing.

AI aims to design the best agents or the programs that achieve the best performance given the computational limitations.

An important aspect of agent is to see it as a bunch of hardware and

a bunch of software so we care about the software part of the program agent's part in this course.



## 第一个agent

Our first agents will be **search agents** in  which we design search agents that work toward the goal.

The agent consider the impact of its actions on future states. Which means that

the agent is thinking about what to do to achieve its goal.

The agent’s job is then to identify the action,

or series of actions that we could call a path, that lead to the goal.

A path comes in different costs and depths.

We see two kinds of search. *Uninformed search* use not *domain knowledge* and

includes techniques such as *Breadth First Search*, *Depth First Search*,

Uniform Cost Search, etc.

The *Informed search* through some heuristic or

information or *rule of thumbs*(经验法则) about how to reach the goal faster and

this include techniques such as *greedy search*,　 A*,　 etc.

So you go through this different techniques and

you get a chance to implement some of them.

Example of *sort agents* include the **eight queen problem** in which

on the chess board we want to place eight queens so

that no queens attacks another one either horizontally, vertically or diagonally.

This is a search problem, they're going to search for

possible configuration that actually such as no queen attacks another one.

A typical example of search agents is what we call a **route finding**.

So given a set of cities in North America for example and we have a map of it,

the map is represented by a graph in which the nodes represent the cities and

the edges represent the possible roads.

You have the distance between the two cities that is actually highlighted

on the edge.

So suppose you want to go from the city of Las Vegas to the city of Calgary

There are different ways to do it.

So we're going to explore the possibilities. The aim of the agent is

to do some exploration, and possible exploration would be to go for example,

taking this path here or go through this path here or take this path, etc.

So the paths have different cost, and

this cost is a sum of the number of kilometers on the edges.

So the role of search agent here is to find you a solution to go from city

of Las Vegas to Calgary, but also to find your the optimal solution, and

we find, we see different ways of how we can perform this kind of search.

So once this path is found the agent can execute the path to each destination.



Another important part of AI is **adversarial search or games**.

That have been several games that actually were solved in AI. We have seen chess, Go,

and Jeopardy before. So, another example is the **checkers**.

Chinook for example which is a computer program

ended 40 years reign of human world champion Marion Tinsley in 1994.

Checkers is considered as solved. It can, the computer, or

Chinook, can actually beat any human on chess.

Assuming the human is also playing an optimal play.

So adversarial search other name is games.

An adversarial means that there is an opponent who we can't control.

So how about game versus search.

Game is also a search problem but

the optimal solution is not a sequence of actions off pad that lead to the goal.

But it's a strategy or policy that actually help us win the game.

In other words if the opponent is doing A then we do B,

if the opponent is doing C then we do D.

It can be maybe tempting to write this as rules or hard code that but

it is tedious and for fragile.

So the idea is to write search agent that can play games and against opponents.

So the concept and method that you will learn in this part of the course

include the **mini max algorithm**, **alpha beta pruning** and **stochastic games**.



A section of this course is devoted to machine learning.

This is the current trend of AI today.

So I'm going to talk about some methodologies which won’t cover

all the aspects of machine learning but

consider it as a baby machine learning part in this AI course.

So according to **Tom Riccio** which is one of the eminent researchers

in machine learning.

**Machine learning is about how to create computer programs that improves our**

**experience, and these are experienced comes from observations or data**.

So you want to be able to teach the computer how to learn and how to

actually improve with experience and this is at the core of machine learning.

When I just different kinds of learning.

First a **supervised learning** is when you have a label.

In other words you have an input, as input a set of examples

are instances or objects or points.

And these examples have labels, they are tagged with some label, for

example, this food described by XYZ is a banana.

So we have a set of examples that actually have some features, and have some labels.

So this is the tag or the label attached to each of the instances.

And the label Y is actually part of a small set of values which is discrete.

So it could be banana, not banana.

It could be minus one, plus one, or zero one.

So we talk here about *binary classification*.

And the output we want to build is a function age that goes from the set of inputs or

description of the instances to the set of outputs.

For example, supposed we have data about customers in the bank and

we have all the information about the customers, their age,

their gender, their occupation, their salary, etc.

And we have some label for each of the customers that said whether he was

approved credit yes or no, whether for emails whether it's a spam or not spam.

So on and so forth.

So we have what you call positive examples and negative examples or two classes and

the idea is to find this function agent help us map the inputs or

the descriptions of the customers to their

credit status.

Okay?

So you could represent that—suppose we are talking about two features, feature one and

feature two.

We could put the examples as positive or negative on this **two dimensional space** or

positive examples are those who got credit.

They're going to example how the of those who are denied credit and

the idea is to find this **decision boundary** that actually separates here

positive from the negative example.

So this is typically a typical example in supervised learning so

remember this term **supervised learning**.

Why it is supervised?

Because there is someone who tells us which is which,

which is a positive example which is a negative example.

Because of any method that you learn here include supervised learning,

**classification**, **K-nearest neighbors perceptions**, **neural networks**,

**linear regression**, **boosting**, to cite a few.



The second kind of learning is called **unsupervised**.

And the unsupervised learning means that we don't have to label. 非监督学习中，我们不必做标签

So without label, we have examples without label.

We have for example the populations or the customers but we don't have

any information about any kinds of label, no label is attached to them.

So given these data points can we find clusters of data points of instances?

We are **seeking to find a function F that maps the inputs X**.

To a set of clusters and this is actually completely unsupervised,

we *don't* have any information about the label.

We have different methods for unsupervised learning and

this includes **clustering with K means** and also as association rules among others.



Our next topic will be **constrained satisfaction problems** in which we

talk about another kind of search problems,

it's a search problems in which we *don't care about the path*.

To achieve the the goal but we care about the goal itself such as solving a game.

All part of the same depth and

the problem is generally formulated using variables instead of states.

So use variables, there domains and

some constraint that tells us how to solve the problem.

Solving the CSP is then to find the assignment that has satisfy

all the constraints.

We're going to learn concepts and methods including a **problem familiarization** of

CSP's, **backtracking search**, our consistency and so on and so forth.

A typical example in constraint satisfaction problem is **Sudoku** so

you all probably played the game Sudoku, in which you have a grid of nine

by nine cells and you want to actually fill the grid with numbers such that each

three by three grid has numbers, digits between 1 and 9 with no repetitions.

The lines have also all that digits between 1 and 9 and the columns and

also digits between 1 and 9.

Let's call this **lines** and this **columns**, lines go between 1 and 9.

And columns go between one and nine, right?

So you could express that as a CSP

by putting the variable by each of the cells so

each of the cell is a **variable**, XLC.

This is X one two.

And the constraints on this variables are that all three by three grid, row, or

column must contain one to nine digits and all of them.

The solution is then to find the assignment to the variables

that satisfy all of these constraints or

filling the blanks in all the words fill the blanks that actually were missing

such as all the digits in the line columns and three by three metrics are different.

This is a typical CSP and you will get a chance to play with these kinds of

problems in your programming assignments.



Our next topic is **logical agent**,

in which logic can be used by an agent to model the world.

Sentences in what we call propositional logic invented by **Boole** a long time ago,

and **first-order logic** have a fixed syntax.

And we use **symbols** and

**connectives** to model the word with logical expressions of sentences.

For example if it's hot and sunny then we're going to the beach or the pool.

This is a logical expression using connective such as the and, the or

and the implications and also uses symbols such as pool, beach, sunny, and

hot that represent different statements about the world.

**Syntax and semantic** represents two important components.

And just don't aspect in logic.

So the goal in using logic in artificial intelligence is to do inference and

inference is given a knowledge base something you know about

the environment a set of sentences in logic.

And given a query for example, I wonder where they should go to the beach or not.

Output whether the knowledge based

entails alpha, so can we infer that we should do Alpha

based on what we know.

And what we know is represented as I said in terms of sentences in logic.

So in this topic you will learn new concepts and

methods including **Modus Ponens**, which is an inference rule,

sound and complete inference, horn clauses, etc.



**Reinforcement learning** is our next topic in which we design agent that evolves in

a stochastic or in certain environment.

Agents learn from reinforcement or delayed reward.

It's another kind of learning besides a supervised and unsupervised.

Learning approaches for decision making in situation where outcome are stochastic,

involves an agent that continued to plan and learn to effect its environment.

Reinforcement learning agents are driven by maximizing the reward

on the long run and we'll see those agents in the next topic of this course.



Finally, we'll go through some applications of artificial intelligence to

**natural language processing**, in which we are concerned with the interaction between

computers and human languages, vision or perceptions that is concerned with

image processing and building computers vision AI agents, and

the goal is information extraction from task.

For task such as manipulation, navigation, and **objects recognition**.



Finally robotics that's concerned with intelligent

agents that manipulate the physical world.

Different aspects would be seen such as planning a robot motion,

vision, and object of recognition.

I wanted also to have a historical moment today.

And dedicate this lecture to Alan Turing, who is the famous British mathematician

and the code breaker during the World War II.

He proposed an operational test for

intelligence that we have seen today called **The Imitation Game**.

He also proposed in his article in 1950, **Computing Machinery** and

Intelligence, major components of AI, including language,

reasoning, learning, and understanding.

So I invite you a to go through this archive and

check his article, it's a wonderful read.



## 今日总结

So let's summarize for today.

We have said AI is a hard topic, it's hard because it involves different aspects,

including compositional complexity, languages, division etc.

It's also a broad topic with high impact on humanity and society.

What AI can do for us and

we have seen several application is just already amazing.

AI system, remember, do not have to model human or nature.

But can act like or be inspired by human or nature.

How human think is actually beyond the scope of this course and

it's another branch of AI.

And finally the aspect rationale agents, **the agent that do the right thing,**

**is the central approach of the central idea in this course**.

Note here though that the rationality is not always possible

in complicated environment but we still will aim for to build a rationale agents.

A recurrent question in the media and

public opinion is whether AI is a threat to our human kind.

Indeed AI may raise some feeling of uncertainty about the future, and

whether living people wonder whether they will keep their jobs, and

whether AI systems would take over the word an exterminate the human race.

This comes from different kinds of peoples at all levels in the society

including Professor Stephen Hawkins who told the BBC that the development of

full artificial intelligence could spell the end of the human race.

So he's in a good position to see how

powerful are AI systems as he's using AI systems to communicate.

In my opinion AI is a flourishing and

exciting field where everyone can contribute.

We can contribute at the policy level, at the research level,

computing level, privacy preserving level, nature level and so on and so forth.

So we can be actors other than consumers of AI and

AI is a part of our lives anyway.

This is all what this course is about giving you the principle and

practice of artificial intelligence.



I wish you all an excellent learning journey together.

Thanks very much for being part of this course.