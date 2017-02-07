#!coding=utf-8
from enum import Enum
import matplotlib.pyplot as plt
from matplotlib.path import Path

sample="L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2"

a =sample.split(", ")
print a

class Direction(Enum):
    N = 0
    W = 1
    S = 2
    E = 3

#def checkIntersect():

print Direction(2)
print Direction.S
print Direction('E')
#print Direction.1
# class Move():
#     def __init__(self):
#         self.facing = Direction(0)
#         self.pos = (0,0)
#         self.path = []

#     def turnR(self):
#         self.facing = Direction((self.facing.value - 1) % 4)

#     def turnL(self):
#         self.facing = Direction((self.facing.value + 1) % 4)
    
#     def move(self,steps):
#         if self.facing == Direction.N:
#             temp = self.pos
#             self.pos = ( self.pos[0] , self.pos[1] + steps )
#             self.path.append((temp,self.pos))
#         elif self.facing == Direction.W:
#             temp = self.pos
#             self.pos = ( self.pos[0] - steps , self.pos[1] )
#             self.path.append((temp,self.pos))
#         elif self.facing == Direction.S:
#             temp = self.pos
#             self.pos = ( self.pos[0] , self.pos[1] - steps )
#             self.path.append((temp,self.pos))
#         elif self.facing == Direction.E:
#             temp = self.pos
#             self.pos = ( self.pos[0] + steps , self.pos[1] )
#             self.path.append((temp,self.pos))

#     def run(self):
#         for i in a:
#             if i[0] == "L":
#                 print "Turning Left"
#                 self.turnL()
#             else:
#                 print "Turning Right"
#                 self.turnR()
#             print "Moving ",int(i[1:])," steps."
            
#             self.move(int(i[1:]))
#             for (x,y) in self.path:
#                 if 
#                 print (x,y)
#             # else:
#             #     print "Collision",self.pos
#             #     print self.path
#             #     return
#             #break
#         print self.pos
#         print type(self.pos)
#         #print self.path
# Move().run()

