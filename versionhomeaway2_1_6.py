#introduction of breaks and reducing biasness
import random
import list_generator_backup
import copy

def predictive_analysis(teamA_values, teamB_values, homematches, awaymatches):
 total = 0
 #initializing variablies
 Probability_teamA_win=0
 Probability_teamA_draw=0
 Probability_teamA_loose=0

 Probability_teamB_win=0
 Probability_teamB_draw=0
 Probability_teamB_loose=0

 lists = list_generator_backup.list_creator(homematches, awaymatches)
 teamA50 = lists[0]
 teamA30 = lists[1]
 teamA20 = lists[2]
 teamB50 = lists[3]
 teamB30 = lists[4]
 teamB20 = lists[5]
 
 def list_generator_interval():
  choice = []
  for i in range(100):
   x = random.randint(1,10)
   if len(choice) == 3:
     break
   elif x not in choice:
     choice.append(x)
   elif x in choice:
     continue
   else:
     continue

  return choice

 choices = copy.deepcopy(list_generator_interval())
 totalA = 0
 total_interval = 5

 while(totalA <= 1000000):
    if totalA == total_interval:
        total_interval = total_interval + 5
        choices = copy.deepcopy(list_generator_interval())
        lists = list_generator_backup.list_creator(homematches, awaymatches)
        teamA50 = lists[0]
        teamA30 = lists[1]
        teamA20 = lists[2]
        teamB50 = lists[3]
        teamB30 = lists[4]
        teamB20 = lists[5]
    else:
        a = random.randint(1,10)

    a = random.randint(1,10)
    if a not in choices:
        continue
    elif a == choices[0]:
        c = random.randint(1,2)
        d = random.randint(1,10)
        f = random.randint(1,10)
        if c == 1:
           comparison_diffrence = (random.randint(teamA_values[0]-d, teamA_values[0]+d) - random.randint(teamB_values[2]-f, teamB_values[2]+f))
        else:
           comparison_diffrence = (random.randint(teamA_values[0]-d, teamA_values[0]+d) - random.randint(teamB_values[1]-f, teamB_values[1]+f))
    elif a == choices[1]:
        c = random.randint(1,3)
        d = random.randint(1,10)
        f = random.randint(1,10)
        if c == 1:
           comparison_diffrence = (random.randint(teamA_values[1]-d, teamA_values[1]+d) - random.randint(teamB_values[2]-f, teamB_values[2]+f))
        elif c == 2:
           comparison_diffrence = (random.randint(teamA_values[1]-d, teamA_values[1]+d) - random.randint(teamB_values[1]-f, teamB_values[1]+f))
        else:
           comparison_diffrence = (random.randint(teamA_values[1]-d, teamA_values[1]+d) - random.randint(teamB_values[0]-f, teamB_values[0]+f))
    elif a == choices[2]:
        c = random.randint(1,2)
        d = random.randint(1,10)
        f = random.randint(1,10)
        if c == 1:
           comparison_diffrence = (random.randint(teamA_values[2]-d, teamA_values[2]+d) - random.randint(teamB_values[0]-f, teamB_values[0]+f))
        else:
           comparison_diffrence = (random.randint(teamA_values[2]-d, teamA_values[2]+d) - random.randint(teamB_values[1]-f, teamB_values[1]+f))
    else:
        continue
   
    if comparison_diffrence == 0:
        total = total + 1
        continue
            

    elif comparison_diffrence <= -1 and comparison_diffrence >= -4:
        a = random.randint(1,101)
        if a in teamB30:
            Probability_teamB_draw = Probability_teamB_draw + 1
            totalA = totalA + 1
        elif a in teamB50:
            Probability_teamB_win = Probability_teamB_win + 1
            totalA = totalA + 1
        elif a in teamB20:
            for i in range(10000):
              d = random.randint(1,101)
              if d in teamA20:
                  continue
              elif d in teamA30:
                  Probability_teamA_draw = Probability_teamA_draw + 1
                  totalA = totalA + 1
                  break
              elif d in teamA50:
                  Probability_teamA_win = Probability_teamA_win + 1
                  totalA = totalA + 1
                  break
              else:
                  continue
                
    elif comparison_diffrence >= 1 and comparison_diffrence <= 4:  
        a = random.randint(1,101)
        if a in teamA30:
            Probability_teamA_draw = Probability_teamA_draw + 1
            totalA = totalA + 1
        elif a in teamA50:
            Probability_teamA_win = Probability_teamA_win + 1
            totalA = totalA + 1
        elif a in teamA20:
            for i in range(1000):
              d = random.randint(1,101)
              if d in teamB20:
                  continue
              elif d in teamB30:
                  Probability_teamB_draw = Probability_teamB_draw + 1
                  totalA = totalA + 1
                  break
              elif d in teamB50:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
              else:
                  continue

    elif comparison_diffrence > 4 and comparison_diffrence <= 10:
        a = random.randint(1,101)
        if a in teamA50:
            Probability_teamA_win = Probability_teamA_win + 1
            totalA = totalA + 1
        elif a in teamA30:
            Probability_teamA_draw = Probability_teamA_draw + 1
            totalA = totalA + 1
        elif a in teamA20:
            for i in range(10000):
              d = random.randint(1,101)
              if d in teamB20:
                  continue
              elif d in teamB30:
                  Probability_teamB_draw = Probability_teamB_draw + 1
                  totalA = totalA + 1
                  break
              elif d in teamB50:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
              else:
                  continue
              
    elif comparison_diffrence < -4 and comparison_diffrence >= -10:
        a = random.randint(1,101)
        if a in teamB50:
            Probability_teamB_win = Probability_teamB_win + 1
            totalA = totalA + 1
        elif a in teamB30:
            Probability_teamB_draw = Probability_teamB_draw + 1
            totalA = totalA + 1
        elif a in teamB20:
            for i in range(10000):
              d = random.randint(1,101)
              if d in teamA20:
                  continue
              elif d in teamA30:
                  Probability_teamA_draw = Probability_teamA_draw + 1
                  totalA = totalA + 1
                  break
              elif d in teamA50:
                  Probability_teamA_win = Probability_teamA_win + 1
                  totalA = totalA + 1
                  break
              else:
                  continue

 return (Probability_teamA_win/10000), (Probability_teamA_draw/10000), (Probability_teamB_win/10000), (Probability_teamB_draw/10000)
