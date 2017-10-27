#Find Angle MBC

import math

AB = int(input())
BC = int(input())
MCB = math.atan2(AB,BC)
MBC = MCB
MBC_deg = int(round(math.degrees(MBC)))
print str(MBC_deg)+"°"