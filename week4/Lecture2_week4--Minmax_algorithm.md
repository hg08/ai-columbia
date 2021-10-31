# 4.2 Minimax算法

 Minimax算法递归地实现minimax函数的思想：寻找从x开始的最好的移动以是utility最大化.
记住: Max 和 Min都在相互对抗, 且它们都在最优地玩着该游戏.
 The minimax algorithm implements the minimax function we just
 saw as a recursive algorithm that actually allows
 to find the best move for max.
 Remember that both max and min are playing optimally, which
 means that max is trying his best to find
 the maximum utility in the leaves,
 while the min is trying to find the minimum utility
 in the leaves.
 So this is a recursive function that's  three pieces.
 The function decision that's actually--
 the main function, that's actually
 the main function, the function maximize, and the function
 minimize.
 Initially we start with max, so we are going
 to call the function maximize.
 The function maximize() finds the state
 with the highest utility.
 This is max's job.
 And the function minimize() will try
 to find the child with the lowest utility.
 This is min's job.
 All right, so the function max.
 Initially we start with the initial stage we call max.
 If it's a terminal test then we are going to end the function.
 Otherwise, we are going to look for--
 in the children, for those for the maximum utility children,
 right.

 So we're going to pick the maximum child
 among the children by doing a recursive call.
 So this function is going to call maximize() because we're
 going to give a turn to Min, and Min
 is going to give a turn to Max, and so on.
 So it's going to call minimize(), and 函数minimize()
 做的是相同的事.
 It's going to check if it's a terminal.
 Otherwise we're going to 探索叶子结点
 and take the leaf, or the node
 with the minimum utility.
 Again, it's going to search here for 最小的utility.
 It's going to 将其放进一个元组.
 All of them are using a tuple.
 Max child max utility for maximize.
 Min child min utility for minimize.
但是，记住:one is trying
 to find the child with the highest utility, the other one
 with 最低的utility.
 There's going to be bounce enough between maximize,
 minimize.
 因此，直到我们到达叶子结点, in which case
 we're going to return these values up to the node
 that's the root.
 So basically, the function at the end
 would return the child with the highest utility for max
 after recursive execution is done,
 which means that we went all the way deep into the leaves,
 and we reached the leaves.
 That's how minimax algorithm works.
 因其递归本质，通过一个例子来解释Minimax算法更简单. 
 例如： a game tree in which we have max
 and min taking turns.
 从Max开始.
Max 常常用正三角形来表示.
 Each of these lines 称为一个回合(ply).

这是一个multi-ply游戏树,注意, 它是利用的**DFS**.
 We have to go **all the way** through the leaves
 to reach the utility values at the leaves,
 and then bring them back up.
 So the utility-- the terminal values
 or the utility of the leaves is given by these numbers here.
 Max will take a turn-- will actually
 bring up the value between 2 and 9, he will pick the value 
 Between 7 and 4 it will pick the value 
 So it's going to maximize-- **take the child that**
 **actually maximizes the utility**.
 So the values would be 9, 7, 9, and 
 Min will try to not let max
 get the maximum of the leaves.
 So it's going to take the minimum of the leaves.
 So the min in this case will pick 7 among the 9 and 
 Will pick 5 among 9 and 7 and 
 At the end, max will have the choice between 7 and 
 So it will pick the maximum value of 7 in this case.
 So the edges, or the arrows, here
 are actually representing the actions taken by max and min
 successively.
 So max will start by picking up this action.
 After thinking about going all the way in the leaves
 and bringing this value up, max will pick this action,
 min will pick this action, and then
 max would pick this action.
 This is the-- when both of them play optimally
 this is the best choice for max to get maximum utility.
 And the child with the maximum utility in this case
 is this child with a value 
 So how about the minimax algorithm property?
 So first of all, it is **optimal**.
 Assuming that both opponents are playing optimally
 the algorithm is optimal.
 It's also **complete.**
 **It will find a solution if it exists**, in finite trees.

 Minimax, it performs a DFS, so it has DFS time and space
 complexities where b is the brunching factor,
 and m is the maximum depth of the game tree.
 So as examples, let's check tic-tac-toe, chess,
 and Go to see what would--
 this time and space complexity represent.
 So for tic-tac-toe which is one of the simplest
 games out there, we saw that actually it's
 even on the board we can't really
 draw the whole search space.
 This is because we have about a branching factor
 of 5, which is the average legal number of moves.
 With total of 9 moves, which means
 that we have a 9 plys to fill the-- actually
 the tic-tac-toe board.
 This represents 5 to the 
 This is the complexity in time, which
 represents about 2 million of nodes that we need to explore.
 Regarding this number of terminal nodes,
 we have about 9 factorial.
 This is the number of terminal on nodes
 that we could reach tic-tac-toe.
 So tic-tac-toe is an easy game for AI, let's say it this way.
 As compared to chess that actually
 has a branching factor that's an average of 
 And that's actually typically the games
 in chess reach 100-ply, which means that we have a b to the d
 which is 10 to 154 nodes that actually represent its time
 complexity not to export the full search space.
 This is pretty much impossible.
 That's why there have been many heuristics that
 were designed in order to search at chess
 and not having to go all the way to a depth of 
 For Go we have a branching factor
 that starts at 391, which may seem like a hopeless AI
 to build for the Go.
 For 19 by 19 we have a branching factor of 
 You could imagine what would be the search space size.
 It's absolutely huge.
 But it was still solved by alpha Go,
 so there is always progress, which makes actually games
 really a challenge for AI to solve.
 Such a huge search space, or state space,
 represent actually a big problem to implement for real games
 because we are limited in time.
 We really can't wait forever for our opponents
 to make a move on the chess board for example.
 So it's impossible to really search
 the leaves because of the depth and the branching factor
 of those real games.
 And to be practical, and run in a reasonable amount of time,
 minimax can only search to some depth.
 So it's not reasonable to get into a depth of 100,
 for example, for chests.
 But we know also that more plys make a big difference.
 If you can really think ahead and go as deep in your thinking
 about and think about your opponent's actions
 and then the consequences of the actions by your own actions,
 and so on, and so forth, more plys make a big difference
 because you can plan better when you know more
 about the different consequences of those choices of actions.
 The solution for this big problem
 is to replace terminal utilities with an evaluation function
 for non-terminal positions.
 So remember, Shannon had suggested initially
 to cut the search earlier because there is no way, again,
 we can get all the way down to the leaves.
 So that's stop earlier and have an evaluation function
 tells us roughly how this position is actually
 doing in terms of evaluation function.
 And then, also, 我们可以利用**迭代加深搜索**(IDS, iterative deepening search): 我们将go try to go deeper, deeper, deeper,
 and when the time is off, what we can do
 is to take the solution that comes
 in the previous iteration.
最终, 我们可以运用剪枝，因为我们有一个巨大的搜索空间.
也许,剪枝且不必探索每一个结点.
因此，如果我们可以消除large part of the tree
 we can go in the same amount of time deeper in the game tree.





### 附录

 

**sys.setrecursionlimit(limit)**
Set the maximum depth of the Python interpreter stack to limit. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python.

The highest possible limit is platform-dependent. A user may need to set the limit higher when they have a program that requires deep recursion and a platform that supports a higher limit. This should be done with care, because a too-high limit can lead to a crash.

If the new limit is too low at the current recursion depth, a RecursionError exception is raised.

Changed in version 3.5.1: A RecursionError exception is now raised if the new limit is too low at the current recursion depth.



