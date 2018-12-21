# Using discrete math to solve turning
#      0            N
#    3   1   -->  W   E
#      2            S
def turn(LR,current_dir):
  if(LR=="L"):
    current_dir += 3;
  else:
    current_dir += 1;
  return current_dir%4;

#pre: string N/E/S/W
#post: an integer representation
def parseDir(direction):
  return ("NESW").find(direction)

# pre: an integer 0,1,2,3
# post: a string representation
def getDir(val):
  return ("NESW")[val];

# return new location (x,y) after moving in direction
def move(spaces,curDir,curLoc):
  newloc = [curLoc[0], curLoc[1]];
  if curDir == 0:
    newloc[1] += int(spaces);
  elif curDir == 2:
    newloc[1] -= int(spaces);
  elif curDir == 1:
    newloc[0] += int(spaces);
  elif curDir == 3:
    newloc[0] -= int(spaces);
  return newloc;

