#Using team positions
import random

def matches_generator():
 matches_played = []
 totalA = 1
 while(totalA <= 576):

   a = random.randint(1,24)
   b = random.randint(1,24)
 

   if a == b:
      continue
   else:
      match = str(a) + "-" + str(b)
      if match not in matches_played:
          matches_played.append(match)
          totalA = totalA + 1
      else:
          continue

 return matches_played
    
