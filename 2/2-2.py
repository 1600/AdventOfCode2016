#!coding=utf-8

current_xy = (-2,0)
numpad = {'1':(0,2),'2':(-1,1),'3':(0,1),'4':(1,1),'5':(-2,0),'6':(-1,0),'7':(0,0),'8':(1,0),'9':(2,0),'A':(-1,-1),'B':(0,-1),'C':(1,-1),'D':(0,-2)}
switcher_dict = { 'U':(0,1) , 'R':(1,0) , 'D':(0,-1) , 'L':(-1,0) }


def will_violate_constraint(coordinate):
    try:
        assert coordinate[1] <= coordinate[0] + 2
        assert coordinate[1] >= coordinate[0] - 2
        assert coordinate[1] <= -coordinate[0] + 2
        assert coordinate[1] >= -coordinate[0] - 2
    except:
        return True
    return False
    
def coordinate_change(instruction):
    return switcher_dict.get(instruction)


def moveSteps(line):
    '''每走一行得到一个坐标（和对应的数字）
    '''
    global current_xy
    for instruction in line:
        temp = current_xy
        current_xy = tuple(map(sum, zip(current_xy, coordinate_change(instruction))))
        if will_violate_constraint(current_xy):
            current_xy = temp


def acquireCodes():
    with open('puzzle2.txt','r') as f:
        for line in f.readlines():
            moveSteps(line[:-1])
            for num in numpad:
                if current_xy == numpad[num]:
                    print 'Falls in ',num

acquireCodes()