import random
import copy

def list_creator(teamA_probability,teamB_probability):
 teamA_values_win = []
 teamA_values_draw = []
 teamA_values_loose = []
 teamB_values_win = []
 teamB_values_draw = []
 teamB_values_loose = []

 total = 0
 teamA = list(range(1,((teamA_probability[0]*100) + (teamA_probability[1]*100) + (teamA_probability[2]*100)+1)))
 teamB = list(range(1,((teamB_probability[0]*100) + (teamB_probability[1] *100)+ (teamB_probability[2]*100)+1)))
 
 def outer_range(teamA, teamB):
   if (teamA_probability[0] + teamA_probability[1] + teamA_probability[2]) == (teamB_probability[0] + teamB_probability[1] + teamB_probability[2]):
     f = (teamA_probability[0] + teamA_probability[1] + teamA_probability[2])
   elif (teamA_probability[0] + teamA_probability[1] + teamA_probability[2]) > (teamB_probability[0] + teamB_probability[1] + teamB_probability[2]):
     f = (teamA_probability[0] + teamA_probability[1] + teamA_probability[2])
   elif (teamA_probability[0] + teamA_probability[1] + teamA_probability[2] ) < (teamB_probability[0] + teamB_probability[1] + teamB_probability[2]):
     f = (teamB_probability[0] + teamB_probability[1] + teamB_probability[2])

   return f

 while ((len(teamA_values_win) != teamA_probability[0])):
    x = random.randint(1, outer_range(teamA, teamB))
    if x in teamA:
       teamA.remove(x)
       if len(teamA_values_win) <= teamA_probability[0]:
           if x not in teamA_values_win:
               teamA_values_win.append(x)
    else:
        continue

 while ((len(teamA_values_draw) != teamA_probability[1])):
     if teamA_probability[2] == 0:
        teamA_values_draw = copy.deepcopy(teamA)
        teamA_values_loose = []
        teamA =[]
     else:
       x = random.randint(1, outer_range(teamA, teamB))
       if x in teamA:
        teamA.remove(x)
        if len(teamA_values_draw) <= teamA_probability[1]:
           if x not in teamA_values_draw:
               teamA_values_draw.append(x)
       else:
         continue

 totalA = 0 
 while (totalA == 0 ):
    teamA_values_loose = copy.deepcopy(teamA)
    totalA = totalA + 1

 while ((len(teamB_values_win) != teamB_probability[0])):
    x = random.randint(1, outer_range(teamA, teamB))
    if x in teamB:
       teamB.remove(x)
       if len(teamB_values_win) <= teamB_probability[0]:
           if x not in teamB_values_win:
               teamB_values_win.append(x)
    else:
        continue

 while ((len(teamB_values_draw) != teamB_probability[1])):
    if teamB_probability[2] == 0:
        teamB_values_draw = copy.deepcopy(teamB)
        teamB_values_loose = []
        teamB = []
    else:
     x = random.randint(1, outer_range(teamA, teamB))
     if x in teamB:
        teamB.remove(x)
        if len(teamB_values_draw) <= teamB_probability[1]:
           if x not in teamB_values_draw:
               teamB_values_draw.append(x)
     else:
        continue

 totalB = 0
 while (totalB == 0 ):
    teamB_values_loose = copy.deepcopy(teamB)
    totalB = totalB + 1

 return teamA_values_win, teamA_values_draw, teamA_values_loose, teamB_values_win, teamB_values_draw, teamB_values_loose, outer_range(teamA, teamB)
