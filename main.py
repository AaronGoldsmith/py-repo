#!/usr/bin/env python
"""main.py: Runs the main function to compute routes ."""
__author__ = "Aaron Goldsith"
__email__ = "aargoldsmith@gmail.com"
__status__ = "Development"

import helpers


# 1.  Domain-specific language (how to contextualize the route)

# Parse each direction using pipes
# Expect two integers for arg0 and arg1 representing start x,y
# Expect a direction N/E/S/W and a distance as arg2
# All other possible steps must be one of: a numerical only value
# A character followed by a numeral, representing direction + distance
# A single character , representing Left or Right

#   data should be stored in the smallest possible format
#   an integer will take up less space in memory than a string, (each character represents an 8bit ascii code)  
#   If we store two tuples, the start and end locations, the remaining information could be a string representing the 
#   "instruction set" i.e path to get from (start loc) --> (finish loc). 
#   
#   PK    START     END         Path                       Final Destination
#   ---   -----     --------    -----------------------   -----------------
#    1    [0,0]     [100,20]    0|0|ABC|DEF|GHI|JKL|MNO    "New York City"
#    2    [0,0]     [50,40]     0|0|ABD|DGF|AHI|JKL|MNO    "Statue Of Liberty"
#    3    [0,4]     [20,1]      0|4|TUV|RUV|MNO|XYZ|STV    "Six Flags discovery kingdom"

# with a design like this, popular routes could easily be ranked in a separate table
# Additionally, this structure allows for various graph representations which could be utilized to find useful information
# For example, Kruskal's MST algorithm could be used to find the path with the fewest number of "steps"  
# or likewise, if a new path can be represented using two or more exisiting paths. 


def parse_route(route):
  loc = (0,0)
  try: 
    stepList = route.split('|');
    loc = (int(stepList[0]),int(stepList[1]))
  except: 
    print("Could not parse string")
  finally: 
    del stepList[0]
    del stepList[0]
    count = 0
    facing = "";

    print('----\nStarting at ('+ str(loc[0])+','+str(loc[1])+')\n')
    # "walk" the route to determine the end location (and to ensure we stay on our map)
    for step in stepList:
      if(loc[0]>=0):
        if count>0:
          print('\tfacing ' + facing + '\n');

        print('Step: ' + str(count+1))
        result = parse_path(step,loc,facing)
        print("\tLocation: " + '('+str(result[0][0])+","+str(result[0][1])+')');
      else: 
        print('you ran off the map')
        break;
      count+=1
      loc = result[0];
      facing = result[1];
    print('---')
    print('facing: ' + facing);
    print('final loc at: ('+ str(loc[0])+","+str(loc[1])+")");

# if the first character is a digit, the whole string is a number
# if the entire instruction is one character, it is a turn left/right
# if the string consists of only alpha characters, the instruction is a landmark  
# if the string is none of those, it is a direction and a distance

# note: there are 2 cases that apply to the rule ('all characters to be a string')
#       the 'special' case is when the length of the string is 1 

# pre: string path, tuple loc, int direction 
# post: return  (loc,dir) after following path
def parse_path(path,myloc,direction):
  newloc = [myloc[0],myloc[1]];
  curDir = helpers.parseDir(direction);
  if path[0].isdigit(): 
      print('\tContinue for ' + str(path[0] + " blocks"))
      newloc = helpers.move(path,curDir,myloc)
  elif len(path)==1:
    curDir = helpers.turn(path,curDir);
    print('\tTurn: ' + path);
  elif path.replace(' ','').isalpha():
    print('\tContinue straight until you reach the ' + path);
  else:
    new_dir = helpers.parseDir(path[0])
    newloc = helpers.move(path[1:],new_dir,myloc)
    print('\tHead ' + path[0] + ' for ' +path[1:]+ " blocks")

  return (newloc,helpers.getDir(curDir));

# MAIN FUNCTION that will be ran
try:
  file = open("routes.txt", "r")
except:
  print('error reading file')
finally:
  for line in file:
    parse_route(line)
  file.close()




  




