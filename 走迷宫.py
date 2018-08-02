
# coding: utf-8

# 【走迷宫】你的手里有一张迷宫地图。现在，你想知道从迷宫入口到走出迷宫有多少条路？迷宫地图如下图所示：

# 01111
# 
# 00001
# 
# 10101
# 
# 10001
# 
# 11100

# 每个迷宫地图都是个n*m（n行，m列）的矩阵。迷宫入口在左上角-坐标（0，0），迷宫出口在右下角-坐标（n-1，m-1）。其中，地图上的数字0表示可以走路的地方，数字1表示迷宫障碍。在迷宫里，你只能往上下左右四个方向移动（不能斜着走）。
# 
# 每条迷宫路线是不能走回头路的————这意味着每个数字0只能被经过一次。
# 
# （我们能够很轻松的看出来，上面这个迷宫地图，一共有两条出路）
# 
# 好了，接下来，各个小组发挥聪明才智，用程序来解决这道问题吧！
# 
# （提示：迷宫地图存在成了一个csv文件("./map.csv")，可以通过python的pandas包读取）

# In[21]:


import pandas as pd

Map = pd.read_csv("./map.csv",index_col=0)
Map


# In[39]:


route_stack = [[0,0]]

route_history = [[0,0]]

def up(location):

    if location[1] == 0:

        return False

    else:

        new_location = [location[0],location[1]-1]

        if new_location in route_history:

            return False

        elif Map[new_location[0]][new_location[1]] == 1:

            return False

        else:

            route_stack.append(new_location)

            route_history.append(new_location)

            return True

 

def down(location):

    if location[1] == 4:

        return False

    else:

        new_location = [location[0],location[1]+1]

        if new_location in route_history:

            return False

        elif Map[new_location[0]][new_location[1]] == 1:

            return False

        else:

            route_stack.append(new_location)

            route_history.append(new_location)

            return True

 

def left(location):

    if location[0] == 0:

        return False

    else:

        new_location = [location[0]-1,location[1]]

        if new_location in route_history:

            return False

        elif Map[new_location[0]][new_location[1]] == 1:

            return False

        else:

            route_stack.append(new_location)

            route_history.append(new_location)

            return True

 

def right(location):

    if location[0] == 4:

        return False

    else:

        new_location = [location[0]+1,location[1]]

        if new_location in route_history:

            return False

        elif Map[new_location[0]][new_location[1]] == 1:

            return False

        else:

            route_stack.append(new_location)

            route_history.append(new_location)

            return True


# In[41]:


lo = [0,0]

while route_stack != [15,15]:

    if up(lo):

        lo = route_stack

        continue

    if down(lo):

        lo = route_stack

        continue

    if left(lo):

        lo = route_stack

        continue

    if right(lo):

        lo = route_stack

        continue

    route_stack.pop()

    lo = route_stack

