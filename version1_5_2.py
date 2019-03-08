import random
import copy
import list_generator_backup

def predictive_analysis(teamA_values, teamB_values):
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

 teamA_probability = [50, 30, 20]
 teamB_probability = [50, 30, 20]


 def list_generator():
    choice = []
    for i in range(100):
        x = random.randint(1,10)
        if len(choice) == 4:
           break
        elif x not in choice:
            choice.append(x)
        else:
            continue

    return choice

 choices = copy.deepcopy(list_generator())
 teamA50 = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability)[0])
 teamA30 = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability)[1])
 teamA20 = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability)[2])
 teamB50 = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability)[3])
 teamB30 = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability)[4])
 teamB20 = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability)[5])

 totalA = 0
 total_interval = 10
 total_total_interval = 250000
 g = 3
 h0 = -1
 h1 = -1
 while(totalA <= 1000000):
    if totalA == total_interval:
        total_interval =+ 10
        choices = copy.deepcopy(list_generator())
        teamA50 = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability)[0])
        teamA30 = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability)[1])
        teamA20 = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability)[2])
        teamB50 = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability)[3])
        teamB30 = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability)[4])
        teamB20 = copy.deepcopy(list_generator_backup.list_creator(teamA_probability, teamB_probability)[5])
        if totalA == total_total_interval:
            g = 5
            
    else:
        a = random.randint(1,10)
        
    a = random.randint(1,10)
    
    if a not in choices:
        continue
    elif a == choices[0]:
        c = random.randint(1,2)
        d = random.randint(1,g)
        f = random.randint(1,g)
        if c == 1:
           comparison_diffrence = (random.randint(teamA_values[0]-d, teamA_values[0]+d) - random.randint(teamB_values[2]-f, teamB_values[2]+f))
           totalA = totalA + 1
        else:
           comparison_diffrence = (random.randint(teamA_values[0]-d, teamA_values[0]+d) - random.randint(teamB_values[1]-f, teamB_values[1]+f))
           totalA = totalA + 1
    elif a == choices[1]:
        c = random.randint(1,3)
        d = random.randint(1,10)
        f = random.randint(1,10)
        if c == 1:
           comparison_diffrence = (random.randint(teamA_values[1]-d, teamA_values[1]+d) - random.randint(teamB_values[2]-f, teamB_values[2]+f))
           totalA = totalA + 1
        elif c == 2:
           comparison_diffrence = (random.randint(teamA_values[1]-d, teamA_values[1]+d) - random.randint(teamB_values[1]-f, teamB_values[1]+f))
           totalA = totalA + 1
        else:
           comparison_diffrence = (random.randint(teamA_values[1]-d, teamA_values[1]+d) - random.randint(teamB_values[0]-f, teamB_values[0]+f))
           totalA = totalA + 1
    elif a == choices[2]:
        c = random.randint(1,2)
        d = random.randint(1,10)
        f = random.randint(1,10)
        if c == 1:
           comparison_diffrence = (random.randint(teamA_values[2]-d, teamA_values[2]+d) - random.randint(teamB_values[0]-f, teamB_values[0]+f))
           totalA = totalA + 1
        else:
           comparison_diffrence = (random.randint(teamA_values[2]-d, teamA_values[2]+d) - random.randint(teamB_values[1]-f, teamB_values[1]+f))
           totalA = totalA + 1
    else:
        continue


    if comparison_diffrence == 0:
        continue

    elif comparison_diffrence <= h0 and comparison_diffrence >= h1:
        a = random.randint(1,100)
        if a in teamB50:
            Probability_teamB_draw = Probability_teamB_draw + 1
            totalA = totalA + 1
        elif a in teamB30:
            Probability_teamB_win = Probability_teamB_win + 1
            totalA = totalA + 1
        elif a in teamB20:
            d = random.randint(1,10)
            for i in range(1000):
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
                
    elif comparison_diffrence >= 1 and comparison_diffrence <= 3:
        
        a = random.randint(1,100)
        if a in teamA50:
            Probability_teamA_draw = Probability_teamA_draw + 1
            totalA = totalA + 1
        elif a in teamA30:
            Probability_teamA_win = Probability_teamA_win + 1
            totalA = totalA + 1
        elif a in teamA20:
            d = random.randint(1,10)
            for i in range(1000):
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
    elif comparison_diffrence > 3 and comparison_diffrence <= 5:
        a = random.randint(1,100)
        if a in teamA50:
            Probability_teamA_win = Probability_teamA_win + 1
            totalA = totalA + 1
        elif a in teamA30:
            Probability_teamA_draw = Probability_teamA_draw + 1
            totalA = totalA + 1
        elif a in teamA20:
            d = random.randint(1,10)
            for i in range(1000):
              if d not in choices:
                  continue
              elif d == choices[0]:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
              elif d == choices[1]:
                  Probability_teamB_draw = Probability_teamB_draw + 1
                  totalA = totalA + 1
                  break
              elif d == choices[2]:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
              elif d == choices[3]:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
    elif comparison_diffrence < -3 and comparison_diffrence >= 5:
        a = random.randint(1,100)
        if a in teamB50:
            Probability_teamB_win = Probability_teamB_win + 1
            totalA = totalA + 1
        elif a in teamB30:
            Probability_teamB_draw = Probability_teamB_draw + 1
            totalA = totalA + 1
        elif a in teamA20:
            for i in range(1000):
              d = random.randint(1,10)
              if d not in choices:
                  continue
              elif d == choices[0]:
                  Probability_teamA_win = Probability_teamA_win + 1
                  totalA = totalA + 1
                  break
              elif d == choices[1]:
                  Probability_teamA_draw = Probability_teamA_draw + 1
                  totalA = totalA + 1
                  break
              elif d == choices[2]:
                  Probability_teamA_win = Probability_teamA_win + 1
                  totalA = totalA + 1
                  break
              elif d == choices[3]:
                  Probability_teamB_draw = Probability_teamB_draw + 1
                  totalA = totalA + 1
                  break
                
    elif comparison_diffrence > 5:
        a = random.randint(1,100)
        if a in teamA50:
            Probability_teamA_win = Probability_teamA_win + 1
            totalA = totalA + 1
        elif a in teamA20:
            Probability_teamA_draw = Probability_teamA_draw + 1
            totalA = totalA + 1
        elif a in teamA30:
            d = random.randint(1,10)
            for i in range(1000):
              if d not in choices:
                  continue
              elif d == choices[0]:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
              elif d == choices[1]:
                  Probability_teamB_draw = Probability_teamB_draw + 1
                  totalA = totalA + 1
                  break
              elif d == choices[2]:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
              elif d == choices[3]:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
    elif comparison_diffrence < -5:
        a = random.randint(1,100)
        if a in teamB50:
            Probability_teamB_win = Probability_teamB_win + 1
            totalA = totalA + 1
        elif a in teamB20:
            Probability_teamB_draw = Probability_teamB_draw + 1
            totalA = totalA + 1
        elif a in teamB30:
            d = random.randint(1,10)
            for i in range(1000):
              if d not in choices:
                  continue
              elif d == choices[0]:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
              elif d == choices[1]:
                  Probability_teamB_draw = Probability_teamB_draw + 1
                  totalA = totalA + 1
                  break
              elif d == choices[2]:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break
              elif d == choices[3]:
                  Probability_teamB_win = Probability_teamB_win + 1
                  totalA = totalA + 1
                  break


 return (Probability_teamA_win/10000), (Probability_teamA_draw/10000), (Probability_teamB_win/10000), (Probability_teamB_draw/10000)
