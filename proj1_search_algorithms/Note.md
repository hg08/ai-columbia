BFS的步骤，可参考：

https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/



How can I add items to an empty set in python？

https://stackoverflow.com/questions/17511270/how-can-i-add-items-to-an-empty-set-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa



想对队列用"in测试"，就不得不对队列定义一个容器方法" \__contains__．否则，你将会遇到一个错误"TypeError: argument of type 'Queue' is not iterable"

https://docs.python.org/2/reference/datamodel.html#emulating-container-types

输入输出：

https://docs.python.org/3/tutorial/inputoutput.html

关于A*算法的文献：
第一部分：https://www.cnblogs.com/chnhideyoshi/p/Dijkstra.html

第二部分：http://www.cnblogs.com/chnhideyoshi/p/AStar.html



## BFS算法：

TravelSearch_BFS(G,S,E)
    创建空队列容器Q
    将S置为已访问并加入Q
    While(Q不为空)
        从Q中取出一个节点P
        对P的所有邻居n
            若n未被访问过
                若n==E，则找到终点E，算法结束
                将n置为已访问并加入Q
    算法结束，未能找到终点E



## DFS算法

TravelSearch_DFS(G,S,E)
    创建空栈容器Q
    将S置为已访问并加入Q
    While(Q不为空)
        从Q中取出一个节点P
        对P的所有邻居n
            若n未被访问过
                若n==E，则找到终点E，算法结束
                将n置为已访问并加入Q
    算法结束，未能找到终点E





## A*算法的一个典型例子（方格阵列中一点到另一点）

TravelSearch_BestFirst(G,S,E)
    创建空堆容器Q
    将S置为已访问并加入Q
    While(Q不为空)
        从Q中取出一个节点P(即P是Q中距离E**最近**的格子)
        对P的所有邻居n
            若n未被访问过
                若n==E，则找到终点E，算法结束
                将n置为已访问并加入Q
    算法结束，未能找到终点E



## A*算法的普遍形式（与Dijkstra算法绝类）

Function_AStar(图Graph,起点S,终点E)
 初始化f数组为MAX。
 初始化g数组为MAX。
 初始化previus数组为-1。
 初始化flagsmap_close数组为false。
 初始化开启列表Q。
 初始化g[S]=0。
 初始化f[S]=h(S)。
 将S加入Q。
 While(Q不为空)算法结束，若进行到此步则说明未找到终点E
   P=Q.ExtractMin()，即找到Q中f值最小的点P。
   flagsmap_close[P]=true，即设置P为关闭状态（A类节点）。
   若P==E
       找到终点，算法结束。
   对P的所有邻接点n
    　若n为关闭状态(A类节点），即有flagsmap_close[n]==true
        　continue继续循环。
   　 否则
        　从S通过P到n的路径长度：
　　　　　　　distancePassP=g[P]+Weight(P,n)。
    　若n为B类节点，即有f[n]!=MAX
        　若distancePassP<g[n]
            　将g[n]更新为distancePassP。
            　将f[n]更新为distancePassP+h(n)。
            　将previous[n]更新为P。
            　若容器为堆则找到n在堆中的位置并调整之。
   　　否则n为C类节点，即f[n]==MAX
        　将g[n]更新为distancePassP。
        　将f[n]更新为distancePassP+h(n)。
        　将previous[n]更新为P。
        　将n加入Q。
 算法结束，若进行到此步则说明未找到终点E



## Dijkstra算法

Function_Dijkstra(图Graph,起点S,终点E)
 初始化distance数组为MAX。
 初始化previus数组为-1。
 初始化flagsmap_close数组为false。
 初始化集合Q。
 初始化distance[S]=0。
 将S加入Q。
 While(Q不为空)算法结束，若进行到此步则说明未找到终点E
     P=Q.ExtractMin()，即找到Q中Distance值最小的点P。
     flagsmap_close[p]=true，即设置P为A类节点。
     若P==E
         找到终点，算法结束。
     对P的所有邻接点n
         若n为A类节点，即有flagsmap_close[n]==true
             continue继续循环。
         否则
             计算从S通过P到n的路径长度：
　　　　　　　　  distancePassP=distance[P]+Weight(P,n)。
             若n为B类节点，即有distance[n]!=MAX
                 若distancePassP<distance[n]
                     将distance[n]更新为distancePassP。
                     将previous[n]更新为P。
                     若容器为堆则找到n在堆中的位置并调整之。
             否则n为C类节点，即distance[n]==MAX
                 将distance[n]更新为distancePassP。
                 将previous[n]更新为P。
                 将n加入Q。
 算法结束，若进行到此步则说明未找到终点E



## A*算法的Wiki版本

function A*(start,goal)
     closedset := the empty set                 //已经被估算的节点集合    
     openset := set containing the initial node //将要被估算的节点集合
     came_from := empty map
     g_score[start] := 0                        //g(n)
     h_score[start] := heuristic_estimate_of_distance(start, goal)    //h(n)
     f_score[start] := h_score[start]            //f(n)=h(n)+g(n)，由于g(n)=0，所以……
     while openset is not empty                 //当将被估算的节点存在时，执行
         x := the node in openset having the lowest f_score[] value   //取x为将被估算的节点中f(x)最小的
         if x = goal            //若x为终点，执行
             return reconstruct_path(came_from,goal)   //返回到x的最佳路径
         remove x from openset      //将x节点从将被估算的节点中删除
         add x to closedset      //将x节点插入已经被估算的节点
         foreach y in neighbor_nodes(x)  //对于节点x附近的任意节点y，执行
             if y in closedset           //若y已被估值，跳过
                 continue
             tentative_g_score := g_score[x] + dist_between(x,y)    //从起点到节点y的距离

             if y not in openset          //若y不是将被估算的节点
                 add y to openset         //将y插入将被估算的节点中
                 tentative_is_better := true     
             elseif tentative_g_score < g_score[y]         //如果y的估值小于y的实际距离
                 tentative_is_better := true         //暂时判断为更好
             else
                 tentative_is_better := false           //否则判断为更差
             if tentative_is_better = true            //如果判断为更好
                 came_from[y] := x                  //将y设为x的子节点
                 g_score[y] := tentative_g_score
                 h_score[y] := heuristic_estimate_of_distance(y, goal)
                 f_score[y] := g_score[y] + h_score[y]
     return failure