#推箱子
#辣鸡蹦蹦蹦夏活推箱子卡我半天

#0:people
#1:box
#2;board
#3:slip_board
#4;barrier

#输入地图
Map=[[0,2,2,2,2,2,2,2],
     [2,2,2,2,2,2,2,2],
     [2,2,2,2,2,2,2,2],
     [2,2,2,2,2,2,2,2]]

def people(code):
    if code==0:
        return 1
    else:
        return 0

def box(code):
    if code==1:
        return 1
    else:
        return 0

def isBoard(code):
    if code==2:
        return 1
    else:
        return 0

def isSlipBoard(code):
    if code==3:
        return 1
    else:
        return 0

def isBarrier(code):
    if code==4:
        return 1
    else:
        return 0

#def getplace(Map): #获取人物坐标
#    for x in range(9):
#        for y in range(8):
#            if Map[x][y]==0:
#                return x,y
def getplace(Map): #获取人物坐标
    for x in range(4):
        for y in range(8):
            if Map[x][y]==0: #list index out of range仍未解决
                return x,y

def willgo(x,y):  #便于理解
    return Map[x][y]
def move(standnow=2):
    import random
    num=random.randint(0,3)
    x,y=getplace(Map)
    a=x
    b=y
    if   num==0 and x+1>=0:
        x+=1
        act="↓"#向下
    elif num==1 and x-1>=0:
        x-=1
        act="↑"#向上
    elif num==2 and y+1>=0:
        y+=1
        act="→"#向右
    elif num==3 and y-1>=0:
        y-=1
        act="←"#向左
    else:
        move()
    t=willgo(x,y) #t用于保存将要前往的格子的属性，离开该格子后，该格子属性由0变为原属性
#    if willgo(x,y)==0: #x,y未改变
#        move()                 这两句用上面else取代
    if willgo(x,y)==4: #遇到障碍
        move()
    Map[x][y]=0
    Map[a][b]=standnow  #离开该格子后，该格子属性由0变为原属性
    return t,act
#    elif willgo(x,y)==4: #遇到障碍
#       move()
#    elif willgo(x,y)==3: #滑块

def goto(x,y):
    a,b=getplace(Map)
    cnt=0
    t=2
    Step=""
    while a!=x or b!=y:
        t,step=move(t)
        cnt+=1
        Step+=step
        a,b=getplace(Map)
    return cnt,Step


Min=99999
for i in range(10000):
    Map=[[0,2,2,4,2,2,2,2],
         [4,4,2,4,2,4,4,2],
         [2,4,2,4,2,2,4,2],
         [2,2,2,2,2,4,2,2]]
    try:
        cnt,Step=goto(3,2)
    except:
        cnt=100
        Step=""
    if cnt<Min:
        Min=cnt
        Step0=Step
        Map0=Map
print(Min,Step0)
print(Map0)

#极待添加：滑块，推箱子等动作


        
#有待添加:
#用户图形界面
#用户输入界面

#缺点：模块间耦合度高





    

