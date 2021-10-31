# 4.4 随机游戏

 Last thing I wanted to address in this adversarial search
 lecture is to talk a little bit about stochastic games,
 or non-deterministic games.
 These are games in which we have some random element
 of occurring during the game.
 It could be throwing a die, or a dice,
 or actually shuffling cards.
 So this can include the chance node in the search.
 We don't have anymore on the max and min.
 We also have nodes for a chance to occur between the two
 players.
 So an example of a game is that backgammon
 that actually is the one of the very, very-- one of the oldest
 board games combining skills and chance of the players.
 The goal is that-- given a board like this one,
 the goal is that each player needs to get rid of his pieces
 as soon as possible before the other one does.
 So I'm not going to go into the details of how the game works
 but I wanted to show you that in this case
 the game tree is actually slightly
 different from the previous--
 what we have seen so far for tic-tac-toe and for our toy
 examples.
 And also, for chess where there is no chance factor occurring.
 So in this case we're going to have
 alternate and alternation between max, chance, min,
 chance, max, et cetera.
 So we're to have our regular max and min working and playing,
 but also we have this element of chance occurring
 in the middle between them.
 So we're going to actually have--
 in the case of backgammon we are actually
 rolling two dice, which means that we're
 going to have each die, each numbers on the die
 occurring with some probability.
 So we could have one occurring with the probability
 of throwing over 36, so we have six faces on each of the die.
 So for the backgammon, the search space
 is no longer max and min playing just by themselves.
 There would be an element of chance
 in the middle that actually is symbolized here
 by the yellow circles.
 And each of the yellow circles has some branching factor
 that actually shows the possible outcomes
 of rolling or die, or rolling dice, or shuffling a card.
 So for example, for the backgammon game
 we are going to have an outcome on the two dice
 that actually could be either 1, 1,
 with the probability of 1 over 36, or 1, 2, or 2, 1,
 with probability of 1 divided by 18, and so on and so forth.
 So I'm going to put all the possible outcomes weighted
 by the probability of the event for happening.
 So we need to take into consideration this new element
 in the search game in order to find
 the best solutions for max.
 So the algorithm that could handle
 this randomness in the game is called expectiminimax
 that actually generalizes the minimax algorithm to handle
 the chance nodes as follows.
 So this is a very similar function
 that we have seen for minimax in which we're going to have--
 if this state is a max we're going to call expectiminimax
 on all the successors or all the children of the state.
 If the state is a min, we are going
 to call again all the expectiminimax
 for all the successor of the state to minimize for min.
 But if the state has a chance state then
 we're going to call expectiminimax and return
 the average of the value of the successor
 so we know that there would be a chance to get different--
 with different probability we have different outcomes
 So we're going to weigh that by the probability of each outcome
 to happen and get the expected value of those outcomes.
 So let's take a very simple example with coin flipping.
 So suppose we have an unbiased coin.
 So we flip it, we get a head with the probability of 0.
 We get a tail with the probability of 0.
 So suppose we have max playing here and min playing here,
 and we have this terminal state here with this values.
 So the way that expectiminimax would work
 is to first of all get the--
 so this is the min value.
 So we're going to get at this point the value of 
 For this one we're going to get 
 For this min value we're going to get 2, and for this one
 we're going to get 
 So remember that we're going to have
 max pick the maximum value of its children,
 but it is actually-- we have the chance in the middle here
 that actually gives the chance of getting this outcome here
 with a 50%, and the chance of getting this outcome here
 with 50%.
 So we're going to use a weighted sum of these two outcomes
 here and do the average of 4 and 6,
 which really does to actually 
 So I get 5 here, and here it's going
 to be 2 plus 1 is 3, divided by 
 So this is the average of the outcome weighted
 by the probability here of 0.5 for each
 of the outcomes of the flipping of the coin.
 And we would have a value of 
 And then the max will take them, the maximum value of this two
 outcome and we'll end up with 
 So this is how we are going to weight actually
 the min value that is being sent back by min from the leaves
 by this chance nodes.
 And we're going to, of course, use--
 so this is a simple example with coin flipping,
 so you could imagine with rolling
 a die we have different probabilities depending
 on the different outcomes we get.
 This is just to give you a flavor of what
 stochastic games would look like,
 and how we would change the minimax algorithm to handle
 that randomness in the search.
 The function expectiminimax in this case
 would look like the minimax function,
 with the exception that we are going
 to introduce a third condition here in which we consider
 the case for change.
 If it's a chance node then we're going
 to calculate the weighted sum of the probability of the outcomes
 for this node, just as we did now.
 So we take the weighted average of the expected value
 of the outcomes of the nodes starting from this position.
 We are reaching now the end of the adversarial search
 lecture in which we have seen that games
 are modeled in AI as search problems,
 and use your stick to be able to evaluate the game.
 So it's a complicated problem for AI,
 but it has proven to be actually a problem that's
 solvable for many complex games such as chess or Go.
 So we have good algorithms for those.
 We have seen that the minimax algorithm chooses the best--
 sorry, it should be here-- move, the best
 move given the optimal play from the opponent.
 Minimax goes all the way down into the leaves,
 which is impractical given time constraints.
 And often we use strategies such as alpha-beta pruning that
 allow us to reduce the search space in the game tree
 by pruning parts of it.
 This will allow us to go deeper in the tree with the same time
 constraints, which actually turn out
 to make a big difference when we search a tree for the best
 possible strategy to solve the problem.
 We could also use, besides pruning, some bookkeeping,
 some evaluation heuristics, node reordering, and also IDS,
 or iterative depth search techniques
 has proven to be not only effective, but also efficient
 within the time constraints in practice.
 And that's why we have seen lots of progress in the last years
 in solving games that are very complex
 and such as chess, Go, extra.
 I wanted to finish by saying that games
 is an exciting and fun topic for artificial intelligence
 because devising adversarial search agent
 is challenging because of the huge state space.
 So it pushes the boundary of the research in AI,
 and this could be applicable in other domains besides games.
 We have for-- in this lecture we have just scratched
 the surface of this topic.
 Further topic could be explored, and this
 includes partially observable games in which we don't have.
 We have partial information, for example, if you play poker,
 or bridge, you don't have--
 you don't know what are the cards in your opponent's hand
 so you don't have full visibility of the game.
 As compared to chess in which you could see the whole board.
 Another point to mention about games and AI
 is that except for robot football, known
 as soccer in the US, there was not much interest
 in AI in modeling physical games,
 such as tennis or other ones.
 So I invite you to check this website robocup.org in which
 you are going to see really cute games played--
 soccer games, played by robots.
 Finally, if you're interested in chess,
 check out the evaluation functions
 于Claude Shannon的论文中.
 非常有趣，值得读.
 

And the last point is that you will
 have a chance to implement a game in your homework
 assignment.