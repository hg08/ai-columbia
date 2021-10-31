## A*优化

A*搜索算法的一个重要方面 is that it is optimal当它选择一个树搜索并运用可容许(admissible)评估函数(heuristics)的时候. 因此我们有this big result that states that if h(n) is admissible-- means it doesn't overestimate the path to the cause, which means 我们选取的评估函数 is
 good-- then A star using tree search is optimal.
 So this is an important result that have an intuitive meaning to it, but we are going to try to write
 the rational behind this result. So let's look closer into this statement.
 It's an if statement.
 If condition if h(n) is admissible, let's call it p,
 then 运用一个树搜索的A-star搜索算法is optimal.
 Let's call this q.
 So we have an if statement that 
$$
{\text{if}}\  \ p, {\text{then}}\ \  q
$$
that we could write as 
$$
p \Rightarrow q.
$$
为了证明这个命题我们需要用一个直接的 proof, which
 means that we are going to start from p, from the statement p,
 that h(n)是可容许的.
 And do some work until we reach the conclusion
 q, which is that A star is optimal using tree search.
 So we're going to adopt this kind of proof.
 But first of all, let's lay down what we know already
 about the domain.
 So first of all suppose we are doing a tree search.
 So since we're talking about optimality in tree search,
 and suppose we have two kinds of nodes, gold nodes.
 Suppose they did not have to be necessarily on the same level,
 but suppose we have these two goals.
 One is optimal.

 It means that it's 到达目标的最近的路径,
 such as reaching for example, the city of Calgary.
 And suppose that this one is sub-optimal.
 $G_s$ for sub-optimal, which means that this
 is another path to Calgary, but it takes longer to reach there.
 Great.
假设$G_o$是最优化的(optimal)目标.
假设$G_s$ is sub-optimal 目标.

我们将运用A-star搜索法．这个方法将利用函数f(n).

我们知道,对于结点n, f(n) 是the function the cost to n plus an estimated cost from n
 to the goal，即 
$$
f(n) = g(n) +h(n).
$$
g(n) 是到达结点n的成本.
  若我们有一个结点n,
 假设3: n是一个边缘区(fringe)中的未展开的结点,such that n 处于到达G的最短路径上.
 Means that we have a path from the root,初始结点.
 经结点n,直到到达目标G．
 结点n在is on the shortest path
 to go from the root to G.
 Then G of n would represent the cost to reach the node n.
 The path here would be G of n.
 And the estimated cost between n and $G_o$ is h of n.
 So the second part would be this one.

 That's h(n).
 That's the estimated cost from n to $G_o$
 in which we use the heuristic because we don't know.
 
 So we have this information.
 What else do we know?
 We know that we're applying the function
 f at different nodes for which A-star knows what nodes to pick.
 So 
$$
h(G_o)=0 \Rightarrow f(G_o) =g(G_o)+h(G_o) = g(G_o).
$$
 原因:我们已经在目标上了. 目标和它自己之间的估算的成本为0．下标'o'表示'最优的'(optimal).

 So we have this first result for the optimal goal.

 The function at the optimal goal is
 the cost of this optimal goal.
 So if I write it in another color--
 so it's going to be this cost here.
 Because we know the path.
 So this is the true cost to reach G
 We do the same thing for sub-optimal goal,
 for the sub-optimal goal.
 So G of s would be equal to G of s
 because the heuristic at G of s would be also equal to 0.
$$
h(G_s)=0 \Rightarrow f(G_s) =g(G_s)+h(G_s) = g(G_s).
$$
 So we have this two elements here.
 We know also for the A star algorithm,
 A star will pick the nodes the smallest function f.
 So we know that for actually A-star
 will use the fact that the function of G of s
 would be bigger than the function at G

因为$G_s$是次优的，故
$$
f(G_s) > f(G_o) = G(G_o)
$$
这还不是证明．
 But this is the first element that will help us make the proof.
 So this is from just really what we know about A star
 and what we know about being in a goal, whether it's optimal
 or not.
 

证明题：

从 "h(n)是可容许函数"开始 ，我们试图证明＂利用树搜索的A-star算法是最优的＂.
 已知： h(n) 是可容许函数(admissible). 说一个评估函数(heuristic) 是可容许函数到底意味着什么?
 So from the previous slides, we know that this means that 
$$
h(n)\le h^*(n)
$$
上式右边是到达目标的真实成本.
h(n)是可容许的, 因此我们假设: the heuristic will never overestimate
 the cost to the goal.
 So given this inequality here, 让我们在上面不等式左右两边同时加上 g(n).　因此，我们得到
$$
g(n)+h(n)  \le g(n)+h^*(n) 
$$
 左边就是 f(n)，在结点n处的一个函数．

 右边可写成g(G_o)， 因g(n)+h*(n)是从根结点到结点n的成本，加上从结点n 到 $G_o$的真实成本. 其值又等于f(G_o)．
 因此
$$
g(n) +h(n) \le g(n)+h*(n) = g(G_o) = f(G_o).
$$


这就是说：
$$
f(n) \le f(G_o).
$$
 故，我们有两个重要结论:
$$
f(G_s) > f(G_o).
$$
次优目标的f函数大于最优目标的f函数.
 And the function at n node that's actually
 on the way to which the goal is less
 or equal than f of the function at the optimal goal.
 So from this two results, one and two,
 we could conclude that actually f of g sub-optimal
 is bigger than f of n, which means that A star will never
 select a sub-optimal goal during this search
 rather than selecting n.
$$
f(G_s) > f(n).
$$
所以结点n将总是被选中before $G_s$, 这意味着 A-star将总是选择导致最优目标的结点,所以,A-star是最优的.
 Then from result one and result two
 we can conclude that f(G_s) is bigger than f(n).
 结点n，实际上是在到达$G_o$的最短路径上的一个已展开结点.
 From this result, it means that whenever
 A-star needs to decide, it applies the function on the nodes.
 It will always find that the function at the node n that's
 on the shortest path to G_o will be
 always less than the function at the sub-optimal goal.
 这就是说，A-star将不会选择$G_s$,而会选择结点n.
 即该搜索实际上是optimal,
 因为我们总会向$G_o$走，而不是向$G_s$走.






