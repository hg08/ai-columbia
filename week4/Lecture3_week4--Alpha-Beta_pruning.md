# 4.3 Alpha-Beta剪枝

## 4.3.1 alpha-beta剪枝  

为了去掉一部分树，剪枝(Pruning)是最流行的方法之一．
最常用的剪枝方法称为alpha-beta剪枝．
Let's take an example with a two-ply game tree,
just as follows.
This game is a two-ply in which we have,
Max takes one turn and Min takes one turn.
So we have the different actions of Max given in these edges,
and the actions for Min given in these edges.
So Max is trying to maximize again,
and Min is trying to minimize.
So we go all the way down the tree so we reach 3,
the min would be 
Then we find 12, then min will not change.
And we find 8, then min will not change.
So the answer for this node here will be 
For this one we are going to do a similar fashion.
So we are going to explore 2, and then 4, and then 
The min here will be 
And then finally here the min would be 
So at the end of the game so we are
going to have 3, 2, 2 for Min at this ply here.
And then Max would pick the maximum of this 3 value
is going to be 
The question here is whether we need to really explore
all those nodes in order to find this value 3 that represents
the maximum utility for Max.
And the answer is no.
So for example maybe these x, y,
here are not that really needed to calculate that
So let's check it out.
So we're going to check the minimax at the root.
The minimax will be the maximum of the minimum value at 3,
12, 8, the minimum of 2, x, y, and the medium of 14, 5, and 
So this minimum will be 
This minimum will be 
And this minimum has to be less or equal than 2
because we have 2 in the list.
So the minimum 2, x, y, depending on x, y.
It's going to be 2 or less if x and y are less than 
So this will bring us to a place--
actually the value of minimum 2, x,
y, by z, where z is less or equal than 
This means that actually given that we are calculating
the maximum and then that the z is less or equal than 2,
we want even to know what's z because we already have
3 that is maximum in this case.
So the maximum is 3 and we didn't even
need to look at x and y to decide that 3 is the maximum.
So many minimax decisions are independent of the values
of x and y, which means that we can just
not even explore them, and just get rid of them by pruning.
Based on this observation let's devise the algorithm
alpha-beta pruning, that you might have guessed that it
is actually a DFS algorithm.
So just like minimax a strategy is DFS.
However, we need to carry parameters that are actually
the alpha and beta of the algorithm from which
the name is actually inspired.
So we're going to use a DFS, but we're
going to use two parameters that are two bounds.
The alpha represents the largest value for Max.
This is the largest seen value for Max among the children.
In other words, it is the current lower bound
on Max's outcome.
Beta is for Min.
It is the lowest value of mean across the seen children, which
is actually the current upper bound on the Min outcome.
So we're going to carry this alpha-beta along the search
tree, and we're going to initialize them
by putting alpha to minus infinity.
This is like the worst case scenario,
you want to find the largest value,
and so far there is no largest value so it's minus infinity.
For beta it's the other way around.
So it's going to be plus infinity because you are trying
to find the minimum, for now we don't know yet
what's the minimum.
So the propagation is also very important.
As we explore the search tree we are
going to send alpha and beta down the tree.
So we're going to update alpha and beta values
about propagating the upward--
propagating upward the values of terminal nodes.
So how about the pruning.
The putting happened for any remaining branches whenever
we have alpha bigger or equal than beta, which
means that actually we're going to have alpha and beta starting
from minus infinity, plus infinity, right.
And both of them will be moving--
one is moving-- alpha is going to go higher,
beta is going to go smaller because remember Min is trying
to minimize, Max is trying to maximize.
So whenever these two values will cross each other,
it means that there is no hope for alpha,
for Max to find a smaller value than alpha,
and there is no hope likewise for Min
to find a larger value than beta.
So whenever this happens we are going to stop the search.
It's not needed to search anymore.
So alpha-beta pruning could be also explained
through these two diagrams.
The left one is for Max, the right one is for Min.
So for Max, if we have alpha as the best choice for Max then,
a, down the tree, then Max will simply
avoid deploying or exploring that branch and prune it.
Similarly, so it works similarly for Min.
For Min if we have a beta that is actually
a best choice for Min, and there is another b that's actually
a worst choice for Min, then Min will simply
avoid exploring that branch here and prune it.
So this is the idea for both Max and Min
doing the pruning based on their alpha and beta values.
So the alpha-beta pruning algorithm
is best if seen first through an example.
So let's take again our two-ply example
in which we have Max playing first
and then Min playing second.
So just remember, stage 1 we're going to go through
all the way deep in the tree.
So we're going to pick 3, then pick 12, then go up to 8,
and then the Min would be in this case 
And then we're going to go through the second mean value c.
We're going to explore 2, and we want
to avoid exploring these two notes here.
And finally, we are going to go through the last node, explore
14, 5, and 
So let's see for this specific example
how these two nodes here are actually
pruned from the search.
So let's start with the initial values for alpha and beta being
minus infinity for alpha, and beta being plus infinity.
We're going to first send this down the tree
as we do the search.
So suppose we didn't do the search yet.
So it's more common to write it this way,
so as you could see the values as I run the algorithm.
So we're going to send alpha and beta down.
So alpha would be equal to minus infinity,
and beta equal to plus infinity.
The Min node here will explore it's children.
The first child is 3, then beta will change its mind.
The value is no longer plus infinity,
we have a better min value for Min, which would
be, in this case, equal to 
The second child explored would be 
Now, 12 is not better than 3 for Min
and 8 is not better than 3 for Min.
So in this case, Min declares that its minimum value
based on its children is 
And we will send back this 3 value to the Max
that's called the child its first child.
So great, so we have 3 that's going back into Max.
What does Max do with it?
So remember, Max is taking the maximum value
among it's children.
So far the maximum value for alpha
fall we started with minus infinity,
so we have a better choice now, it's 
So we're going to change this into 
We're going to start again over with the node c here.
So in this case we're going to send down the alpha equals 3,
and beta equals plus infinity in this case
because we have a better choice for alpha, as I said.
The max value among these children is so far 
Then the mean will start exploring its children.
The children are starting with 2,
so b will say, OK so I found a smaller
value than plus infinity, one more time.
So I'm going to change my beta into 2, which we
makes in this case, we have--
warning, we have alpha bigger or equal than 
The alpha beta cross which means that we are not
going to find anything better than 3
in any subsequent children of the mean node.
So the 3 we found is really the better choice
than any of these nodes here, because this will return
2 or less than 2 in this case.
So we're going to just cut these two nodes, here and return
the value of alpha, beta here.
So we're going to send the two back.
So remember the Max is doing the maximum of the children,
so it has 3, it's seen 2, so it's keeping 
All right.
Last, it's going to again, send--
we are going to send down alpha equal 3 and beta equal
plus infinity to this node.
The Min node will explore its children.
So in this case we're going to have alpha
is 3 and beta plus infinity.
So when we explore the
14, The beta will update it's--
the Min will update it's beta.
It's going to be 
Afterwards, the beta sees 5, the next child is 
So it's going to change the 14 to 5,
and finally change the 5 to 
So we're going to have--
Min will update it's beta to 2, and send the value back,
which is 
OK, so again here Max is taking the maximum of it's children.
It has 3, 2, and now it's c, 
So it is two sides going to keep the value of 
That's how, actually, Max picks its value
using the alpha-beta strategy, so we end up
with this configuration of minimax value for each
of the nodes.
We know that this one is 
This is the final answer we had, this one is for sure 
This one is less than or equal than 2
because we didn't bother to explore these two.
We know that it is not going to be helping us in getting
the maximum value for Max.
And this one is 
So now, here's the alpha-beta pruning algorithm
that's looks very similar to, as you can see,
to minimax algorithm.
We have again a decision function
that we used to call the maximize function,
but this time we carry alpha and beta, minus infinity
and plus infinity for the parameters.
The maximize function we try to maximize
for Max, the minimize we try to minimize for Min.
With the exceptions that actually
as compared to minimax, what we're going to do
is to add two different things to each of the functions.
One of them is to actually check b for beta,
whether we need to cut or not, and update the alpha.
And also, we need to check similarly
for the minimized function and check whether we should
actually update the beta.
So basically, this is for whether we
need to cut the search space because we found actually
alpha bigger than beta, which is maximum utility that we
find for this child.
If the utility of this child is bigger than beta then
we need to cut.
If the maximum utility is bigger than alpha
that means that we find a new alpha.
Then we need to update alpha.
So remember, alpha is updated only by Max
and beta is only updated by the Min.
So this is update beta, and this is also
cut in case we have alpha bigger or equal than the minimum
utility of the child.
So if it happens, then we are going to skip this child
and check the next child.
So we're going to cut this branch for this child.
So a similar algorithm, but we need again
to do the balance of between maximize and minimize,
but we carry these alphas and we check them,
and whenever alpha is bigger or equal than beta,
this is the condition to prune for actually
both maximize and minimize function.
So this was the alpha-beta pruning strategy.



## 4.3.2 Alpha-Beta剪枝的移动顺序

 Another important aspect in alpha-beta algorithm
 is the move ordering.
 It does matter as it actually affects the effectiveness
 of alpha and beta.
 For example, if you remember in this example we started with--
 we were exploring this node here.
 We
 sent as alpha 3, and we sent beta of plus infinity.
 So when node d-- this is a min-- it's exploring the children,
 it started with 
 So which led that min update the beta to 
 And afterwards it explored 5, it updated the beta to 
 And at the end it explored 2, so it updated the beta to 
 So you could imagine that if we had a 14 and 15 after 2,
 we could have simply avoided explaining 14 and 
 In this case we could have started with the value of--
 if we had-- so we had plus infinity, if we saw 2 first,
 we could have changed beta to 
 And then since alpha is bigger or equal than 2,
 then we could have dropped these two nodes if that were--
 assuming they were actually on the other side of the number
 of the children of the node d.
 So we could not proven any successor
 of d, because the worst successors were actually of min
 were actually generated first.
 If the third one, again, the leaf 2
 was actually generated first, we would
 have pruned the two others, 14 and 5, earlier.
 So the idea of ordering is to examine
 the first successors that are likely best
 and explore those first.
 Chances are that you're going to get the best first
 and then you are going to prune a large space in the tree.
 The worst order for alpha-beta pruning
 is why no pruning can happen at all.
 This happens when the best moves are simply
 on the right side of the game tree, which
 means that we have to go through those,
 explore the bad moves first before reaching the best
 moves on the right.
 The complexity of the alpha-beta pruning in this case
 is similar to minimax, which is a big o of b to the m.
 The ideal ordering for alpha-beta pruning
 is when a lot of pruning happens and the best moves are actually
 on the left of the game trees.
 So remember, it's a DFS search, which
 means that we're going to get the best moves first,
 which means that when we go to the right-hand side of the game
 tree it's going to be the worst moves
 and we're not going to explore them because we
 have better alphas and betas.
 So in this case, this solves the tree
 twice as deep as minimax in the same amount of time.
 And we know that when we go deeper,
 we are going to have a better chance to play better.
 So the complexity in this case is in practice an o
 of b to the m divided by 
 The search can go deeper which is great.
 So the question is how to find a good ordering?
 There are different strategies to do that.
 So first of all, we can remember the best moves
 from the shallowest nodes.
 So it means that the actions can, you know,
 be just reproduced based on what we have observed
 in the shallowest nodes.
 We can order the nodes as the best are checked first.
 We could use some domain knowledge,
 For example, for chess, we could try the order captures,
 then captures first, then threads, then forward moves,
 the backward moves, et cetera.
 So this gives us a sequence of actions
 we could prioritize those.
 And finally, we could bookkeep the states because many of them
 may repeat, and we don't necessarily need to
 recalculate the whole host of trees
 if we have them already in memory.
 So if we bookkeep and we do use some domain knowledge to explore
 the actions in some order we can
 maybe provide a good ordering
 and have an interesting pruning happening in the tree,
 and hence go deeper into the game tree
 while we are searching.
 So minimax, alpha-beta pruning, and move ordering
 help us do a better exploration of the search space.
 However, minimax still needs to generate the entire game search
 space to search in it.
 Alpha-beta algorithm, in the best case scenario,
 reach double the depth of minimax,
 but still needs to go all the way down to the leaves, which
 is actually impractical in real time
 games in which we have to move in a reasonable amount of time.
 A solution to that would be to bound the depth of the search
 by doing a cut-off search as suggested by Shannon in 1
 In which we are going to replace the utility function
 s with an eva function that actually is an evaluation
 function, or heuristic, to estimate
 the value of the current board configuration.
 So in this case--
 the idea of Shannon is to say that given the search space,
 instead of going all the way to the leaves
 to find the true utility of the terminal state,
 let's stop earlier and have an estimation of the value
 of the board at that node here.
 So this is what actually helped solve many games, complex games
 such as chess and Go.
 Is to stop earlier, try to go as deep as we can,
 but to stop earlier in the search space.
 A value of s at some state s is actually
 a heuristic function that could be
 used based on domain knowledge.
 For example, for Othello we could
 take the difference between the white pieces
 and the black pieces.
 For chess we could take the difference
 between the value of the white pieces
 versus the value of the black pieces, which we take--
 which we actually turn non-terminal nodes
 into terminal leaves, which is great.
 So we can stop the search earlier rather
 than going all the way down into a depth of 
 An ideal evaluation function would drag, actually,
 the terminal state in the same way
 as the true utility function, but it must be fast.
 That's why we are using actually this evaluation functions.
 It's typical to define those features
 and make a function that actually
 is a linear way to some of the features.
 And use the domain knowledge to craft
 the best possible features for the domain
 So how does it work
 f1, f2 and fn
 so for example select first some useful features
 For example, for chess we could take the number
 of pieces on the board.
 Feature two could be, for example,
 the values of one piece, like pound,
 one for a pound, three for B sharp, et cetera.
 So we could devise using domain knowledge
 and our longtime experience using playing chess,
 all kinds of features that we could put together using
 a weighted linear function.
 So eval of s would be the sum of the wif
 i of s, which means that we're going to put a weight to each
 of those features and have the evaluation function at a state
 s being the weighted sum of those features.
 So going to be able to learn the weight using machine learning.
 This is what we're going to see in the next lectures.
 So we are going to have a set of examples to learn from,
 the previews matches for example.
 And we can, using these functions,
 devise the weights, learn the weights,
 that can actually give us the best evaluation
 function for chess.
 So just as an example, deep blue has used over 6,000 features
 to as a function that we've combined together
 to evaluate the game and stop earlier in the search tree.


