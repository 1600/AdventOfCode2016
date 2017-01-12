#!coding=utf-8

current_xy = (0,0)

numpad = {'1':(-1,1),'2':(0,1),'3':(1,1),'4':(-1,0),'5':(0,0),'6':(1,0),'7':(-1,-1),'8':(0,-1),'9':(1,-1)}

def violate_constraint(coordinate,instruction):
    '''
    默认九宫格，起点位于(0,0)
    检测是否处于边界，例如如果向上，则当y=1时无法进行U操作。
    '''
    # print 'current coordinate is >> ',current_xy
    # print 'want to move toward ',instruction
    deny_dict = { 'U': (1,1) ,'R':(0,1),'D':(1,-1),'L':(0,-1) }
    cond = deny_dict.get(instruction)
    if coordinate[cond[0]] == cond[1]:
        return True
    return False

    

def coordinate_change(instruction):
    '''定义了走一步所需改变的坐标量
    '''
    switcher_dict = { 'U':(0,1) , 'R':(1,0) , 'D':(0,-1) , 'L':(-1,0) }
    if violate_constraint(current_xy,instruction):
        return (0,0)
    return switcher_dict.get(instruction)


def moveSteps(line):
    '''每走一行得到一个坐标（和对应的数字）
    '''
    global current_xy
    for instruction in line:
        current_xy = tuple(map(sum, zip(current_xy, coordinate_change(instruction))))


def acquireCodes():
    with open('puzzle2.txt','r') as f:
        for line in f.readlines():
            moveSteps(line[:-1])
            for num in numpad:
                if current_xy == numpad[num]:
                    print 'Falls in ',num

acquireCodes()