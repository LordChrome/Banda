import random
import copy
import list_generator_backup

def predictive_analysis(teamA_values, teamB_values, teamA_probability, teamB_probability):
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

 def list_generator():
    choice = []
    for i in range(1000):
        x = random.randint(1,10)
        if len(choice) == 4:
           break
        elif x not in choice:
            choice.append(x)
        else:
            continue

    return choice

 choices = copy.deepcopy(list_generator())
 probabilities = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability))
 teamA50 = probabilities[0]
 teamA30 = probabilities[1]
 teamA20 = probabilities[2]
 teamB50 = probabilities[3]
 teamB30 = probabilities[4]
 teamB20 = probabilities[5]
 totalA = 0
 total_interval = 5
 
 while(totalA <= 1000000):
    if totalA == total_interval:
        total_interval =+ 5
        choices = copy.deepcopy(list_generator())
        probabilities = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability))
        teamA50 = probabilities[0]
        teamA30 = probabilities[1]
        teamA20 = probabilities[2]
        teamB50 = probabilities[3]
        teamB30 = probabilities[4]
        teamB20 = probabilities[5]
    else:
        a = random.randint(1,10)
        
    a = random.randint(1,10)
    
    if a not in choices:
        continue
    elif a == choices[0]:
        c = random.randint(1,10)
        comparison_value_teamA = random.randint(teamA_values[0]-c, teamA_values[0]+c)
    elif a == choices[1]:
        c = random.randint(1,10)
        comparison_value_teamA = random.randint(teamA_values[1]-c, teamA_values[1]+c)
    elif a == choices[2]:
        c = random.randint(1,10)
        comparison_value_teamA = random.randint(teamA_values[2]-c, teamA_values[2]+c)
    elif a == choices[3]:
        c = random.randint(1,10)
        comparison_value_teamA = ((random.randint(teamA_values[0]-c, teamA_values[0] + c) + random.randint(teamA_values[1]-c, teamA_values[1] + c) + random.randint(teamA_values[2]-c, teamA_values[2]+c)//3))
    else:
        continue


    b = random.randint(1,10)
    if b not in choices:
        continue
    elif b == choices[0]:
         c = random.randint(1,10)
         comparison_value_teamB = random.randint(teamB_values[0]-c, teamB_values[0]+c)
    elif b == choices[1]:
         c = random.randint(1,10)
         comparison_value_teamB = random.randint(teamB_values[1]-c, teamB_values[1]+c)
    elif b == choices[2]:
         c = random.randint(1,10)
         comparison_value_teamB = random.randint(teamB_values[2]-c, teamB_values[2]+c)
    elif b == choices[3]:
         c = random.randint(1,10)
         comparison_value_teamB = ((random.randint(teamB_values[0]-c, teamB_values[0] + c) + random.randint(teamB_values[1]-c, teamB_values[1] + c) + random.randint(teamB_values[2]-c, teamB_values[2]+c)//3))
    else:
        continue


    comparison_diffrence = comparison_value_teamA - comparison_value_teamB

    if comparison_diffrence == 0:
        continue

    elif comparison_diffrence <= -1 and comparison_diffrence >= -3:
        a = random.randint(1,101)
        if a in teamB50:
            Probability_teamB_draw = Probability_teamB_draw + 1
            totalA = totalA + 1
        elif a in teamB30:
            Probability_teamB_win = Probability_teamB_win + 1
            totalA = totalA + 1
        elif a in teamB20:
            for i in range(1000):
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
                
    elif comparison_diffrence >= 1 and comparison_diffrence <= 3:  
        a = random.randint(1,101)
        if a in teamA50:
            Probability_teamA_draw = Probability_teamA_draw + 1
            totalA = totalA + 1
        elif a in teamA30:
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
                  Probability_teamB_win= Probability_teamB_win + 1
                  totalA = totalA + 1
                  break

    elif comparison_diffrence > 3 and comparison_diffrence < 10:
        a = random.randint(1,101)
        if a in teamA50:
            Probability_teamA_win = Probability_teamA_win + 1
            totalA = totalA + 1
        elif a in teamA30:
            Probability_teamA_draw = Probability_teamA_draw + 1
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
              
    elif comparison_diffrence < -3 and comparison_diffrence > -10:
        a = random.randint(1,101)
        if a in teamB50:
            Probability_teamB_win = Probability_teamB_win + 1
            totalA = totalA + 1
        elif a in teamB30:
            Probability_teamB_draw = Probability_teamB_draw + 1
            totalA = totalA + 1
        elif a in teamB20:
            for i in range(1000):
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

 return (Probability_teamA_win/10000), (Probability_teamA_draw/10000), (Probability_teamB_win/10000), (Probability_teamB_draw/10000)
