import random
import list_generator_backup
import copy

def predictive_analysis(teamA_values, teamB_values):
 total = 0
 #initializing variablies
 Probability_teamA_win=0
 Probability_teamA_draw=0
 Probability_teamA_loose=0

 Probability_teamB_win=0
 Probability_teamB_draw=0
 Probability_teamB_loose=0

 Probability_teamAwin = 0
 Probability_teamAdraw = 0
 Probability_teamAloose = 0

 Probability_teamBwin = 0
 Probability_teamBdraw = 0
 Probability_teamBloose = 0

 teamA_probability = []
 teamB_probability = []
 
 def WDL_Probability_Generator():
    for i in range(1000):
         a2 = random.randint(20,78)
         if a2 not in teamA_probability:
             if len(teamA_probability) == 0:
                 teamA_probability.append(a2)
                 continue
             elif len(teamA_probability) == 1:
                 if (teamA_probability[0] + a2 > 100):
                     continue
                 elif (teamA_probability[0] + a2 == 100):
                     teamA_probability.append(a2)
                     teamA_probability.insert(2,0)
                     break
                 elif (teamA_probability[0] + a2 < 100):
                     teamA_probability.append(a2)
                     continue
                 else:
                     continue
             elif len(teamA_probability) == 2:
                  teamA_probability.append(100 - (teamA_probability[0] + teamA_probability[1]))
             else:
                  continue
         else:
               continue

    for i in range(1000):
         b2 = random.randint(1,100)
         if b2 not in teamB_probability:
             if len(teamB_probability) == 0:
                 teamB_probability.append(b2)
                 continue
             elif len(teamB_probability) == 1:
                 if (teamB_probability[0] + b2 > 100):
                     continue
                 elif (teamB_probability[0] + b2 == 100):
                     teamB_probability.append(b2)
                     teamB_probability.insert(2,0)
                     break
                 elif (teamB_probability[0] + b2 < 100):
                     teamB_probability.append(b2)
                     continue
                 else:
                     continue
             elif len(teamB_probability) == 2:
                  teamB_probability.append(100 - (teamB_probability[0] + teamB_probability[1]))
             else:
                  continue
         else:
               continue
    return teamA_probability, teamB_probability


 lists = list_generator_backup.list_creator(WDL_Probability_Generator()[0], WDL_Probability_Generator()[1])
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
 total_interval = 10

 while(totalA <= 10000):
    if totalA == total_interval:
        total_interval = total_interval + 10
        choices = copy.deepcopy(list_generator_interval())
        lists = copy.deepcopy(list_generator_backup.list_creator(WDL_Probability_Generator()[0], WDL_Probability_Generator()[1]))
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
        d = random.randint(1,20)
        f = random.randint(1,20)
        if c == 1:
           comparison_diffrence = (random.randint(int(teamA_values[1] + teamA_values[2])-d, int(teamA_values[1] + teamA_values[2])+d) - (random.randint(int(teamB_values[9]+teamB_values[10])-f, int(teamB_values[9]+teamB_values[10])+f)))
        else:
           comparison_diffrence = (random.randint(int(teamA_values[1] + teamA_values[2])-d, int(teamA_values[1] + teamA_values[2])+d) - (random.randint(int(teamB_values[5]+teamB_values[6])-f, int(teamB_values[5]+teamB_values[6])+f)))
    elif a == choices[1]:
        c = random.randint(1,3)
        d = random.randint(1,20)
        f = random.randint(1,20)
        if c == 1:
           comparison_diffrence = (random.randint(int(teamA_values[5] + teamA_values[6])-d, int(teamA_values[5] + teamA_values[6])+d) - (random.randint(int(teamB_values[9] + teamB_values[10])-f, int(teamB_values[9]+ teamB_values[10])+f)))
        elif c == 2:
           comparison_diffrence = (random.randint(int(teamA_values[5] + teamA_values[6])-d, int(teamA_values[5] + teamA_values[6])+d) - (random.randint(int(teamB_values[5] + teamB_values[6])-f, int(teamB_values[5] + teamB_values[6])+f)))
        else:
           comparison_diffrence = (random.randint(int(teamA_values[5] + teamA_values[6])-d, int(teamA_values[5] + teamA_values[6])+d) - (random.randint(int(teamB_values[1] + teamB_values[2])-f, int(teamB_values[1]+ teamB_values[2])+f)))
    elif a == choices[2]:
        c = random.randint(1,2)
        d = random.randint(1,20)
        f = random.randint(1,20)
        if c == 1:
           comparison_diffrence = (random.randint(int(teamA_values[9] + teamA_values[10])-d, int(teamA_values[9] + teamA_values[10])+d) - (random.randint(int(teamB_values[1]+teamB_values[2])-f, int(teamB_values[1]+teamB_values[2])+f)))
        else:
           comparison_diffrence = (random.randint(int(teamA_values[9] + teamA_values[10])-d, int(teamA_values[9] + teamA_values[10])+d) - (random.randint(int(teamB_values[5]+teamB_values[6])-f, int(teamB_values[5]+teamB_values[6])+f)))
    else:
        continue
   
    comparison = comparison_diffrence

    if comparison == 0:
        total = total + 1
        continue
            

    elif comparison >= 1 and comparison <= 6:
        Draw = random.randint(1,100)
        if Draw in teamA30:
            Probability_teamA_draw = Probability_teamA_draw + 1
            totalA = totalA + 1
        elif  Draw in teamA50:
            Probability_teamA_win = Probability_teamA_win + 1
            totalA = totalA + 1
        elif Draw in teamA20:
            for i in range(1000):
              d = random.randint(1,10)
              if d not in choices:
                  continue
              elif d == choices[0]:
                  Probability_teamB_draw = Probability_teamB_draw + 1
                  totalA = totalA + 1
                  break
              elif d == choices[1]:
                  Probability_teamB_draw = Probability_teamB_draw + 1
                  totalA = totalA + 1
                  break
              elif d == choices[2]:
                  Probability_teamB_draw = Probability_teamB_draw + 1
                  totalA = totalA + 1
                  break
              elif d == choices[3]:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
    elif comparison == -1 or comparison == -2 or comparison == -3 or comparison == -4 or comparison == -5 or comparison == -6:
        Draw = random.randint(1,100)
        if Draw in teamB30:
            Probability_teamB_draw = Probability_teamB_draw + 1
            totalA = totalA + 1
        elif Draw in teamB50: 
            Probability_teamB_win = Probability_teamB_win + 1
            totalA = totalA + 1
        elif Draw in teamB20:
            for i in range(1000):
              d = random.randint(1,10)
              if d not in choices:
                  continue
              elif d == choices[0]:
                  Probability_teamA_draw = Probability_teamA_draw + 1
                  totalA = totalA + 1
                  break
              elif d == choices[1]:
                  Probability_teamA_draw = Probability_teamA_draw + 1
                  totalA = totalA + 1
                  break
              elif d == choices[2]:
                  Probability_teamA_draw = Probability_teamA_draw + 1
                  totalA = totalA + 1
                  break
              elif d == choices[3]:
                  Probability_teamA_win = Probability_teamA_win + 1
                  totalA = totalA + 1
                  break
    elif comparison > 6 and comparison < 20:
        Draw = random.randint(1,100)
        if Draw in teamA50:
            Probability_teamA_win = Probability_teamA_win + 1
        elif Draw in teamA30:
            Probability_teamA_draw = Probability_teamA_draw + 1
        elif Draw in teamA20:
            for i in range(1000):
              d = random.randint(1,10)
              if d not in choices:
                  continue
              elif d == choices[0]:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
              elif d == choices[1]:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
              elif d == choices[2]:
                  Probability_teamB_draw = Probability_teamB_draw + 1
                  totalA = totalA + 1
                  break
              elif d == choices[3]:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
    elif comparison  < -6 and comparison > -20:
        Draw = random.randint(1,100)
        if  Draw in teamB50: 
            Probability_teamB_win = Probability_teamB_win + 1
        elif Draw in teamB30:
            Probability_teamB_draw = Probability_teamB_draw + 1
        elif Draw in teamB20:
            for i in range(1000):
              d = random.randint(1,10)
              if d not in choices:
                  continue
              elif d == choices[0]:
                  Probability_teamA_win = Probability_teamA_win + 1
                  totalA = totalA + 1
                  break
              elif d == choices[1]:
                  Probability_teamA_win = Probability_teamA_win + 1
                  totalA = totalA + 1
                  break
              elif d == choices[2]:
                  Probability_teamA_draw = Probability_teamA_draw + 1
                  totalA = totalA + 1
                  break
              elif d == choices[3]:
                  Probability_teamA_win = Probability_teamA_win + 1
                  totalA = totalA + 1
                  break
            
 return (Probability_teamA_win/100), (Probability_teamA_draw/100), (Probability_teamB_win/100), (Probability_teamB_draw/100)


