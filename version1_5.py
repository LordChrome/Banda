import random

def predictive_analysis(teamA_values, teamB_values):
 Probability_teamA_win=0
 Probability_teamA_draw=0
 Probability_teamA_loose=0

 Probability_teamB_win=0
 Probability_teamB_draw=0
 Probability_teamB_loose=0
 for i in range(0, 1000000):
    a = random.randint(1,4)
    if a == 1:
        comparison_value_teamA = random.randint(teamA_values[0]-3, teamA_values[0]+2)
    elif a == 2:
        comparison_value_teamA = random.randint(teamA_values[1]-3, teamA_values[1]+2)
    elif a == 3:
        comparison_value_teamA = random.randint(teamA_values[2]-3, teamA_values[2]+2)
    else:
        comparison_value_teamA = ((random.randint(teamA_values[0]-3, teamA_values[0] + 2) + random.randint(teamA_values[1]-3, teamA_values[1] + 2) + random.randint(teamA_values[2]-3, teamA_values[2]+2)//3))


    b = random.randint(5,8)
    if b == 5:
         comparison_value_teamB = random.randint(teamB_values[0]-3, teamB_values[0]+2)
    elif b == 6:
         comparison_value_teamB = random.randint(teamB_values[1]-3, teamB_values[1]+2)
    elif b == 7:
         comparison_value_teamB = random.randint(teamB_values[2]-3, teamB_values[2]+2)
    elif b == 8:
         comparison_value_teamB = ((random.randint(teamB_values[0]-3, teamB_values[0] + 2) + random.randint(teamB_values[1]-3, teamB_values[1] + 2) + random.randint(teamB_values[2]-3, teamB_values[2]+2)//3))


    comparison_diffrence = comparison_value_teamA - comparison_value_teamB

    if comparison_diffrence == 0:
        continue
    
    elif comparison_diffrence == 1 or comparison_diffrence == 2:
        Draw = random.randint(1,4)
        if Draw == 1 or Draw == 2:
            Probability_teamA_draw = Probability_teamA_draw + 1
        elif Draw == 3:
            Probability_teamA_win = Probability_teamA_win + 1
        else:
            x = random.randint(1,4)
            if x == 1 or x == 2:
                Probability_teamB_draw = Probability_teamB_draw + 1
            elif x == 3:
                Probability_teamB_win = Probability_teamB_win + 1
            elif x == 4:
                continue
                
    elif comparison_diffrence == -1 or comparison_diffrence == -2:
        Draw = random.randint(1,4)
        if Draw == 1 or Draw == 2:
            Probability_teamB_draw = Probability_teamB_draw + 1
        elif Draw == 3:
            Probability_teamB_win = Probability_teamB_win + 1
        else:
            x = random.randint(1,4)
            if x == 1 or x == 2:
                Probability_teamA_draw = Probability_teamA_draw + 1
            elif x == 3:
                Probability_teamA_win = Probability_teamA_win + 1
            else:
                continue
                
    elif comparison_diffrence < -2 and comparison_diffrence >= -5:
        teamB_win = random.randint(1,10)
        if teamB_win == 1 or teamB_win == 2 or teamB_win == 3 or teamB_win == 4 or teamB_win == 5:
            Probability_teamB_win = Probability_teamB_win + 1
        elif teamB_win == 6 or teamB_win == 7 or teamB_win == 8:
            Probability_teamB_draw = Probability_teamB_draw + 1
        elif teamB_win == 9 or teamB_win == 10:
            x = random.randint(1,10)
            if x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
                Probability_teamA_win  = Probability_teamA_win + 1
            elif x == 6 or x == 7 or x == 8:
                Probability_teamA_draw = Probability_teamA_draw + 1
            elif x == 9 or x == 10:
                continue
            
    elif comparison_diffrence > 2 and comparison_diffrence <= 5:
        teamA_win = random.randint(1,10)
        if teamA_win == 1 or teamA_win == 2 or teamA_win == 3 or teamA_win == 4 or teamA_win == 5:
            Probability_teamA_win = Probability_teamA_win + 1
        elif teamA_win == 6 or teamA_win == 7 or teamA_win == 8:
            Probability_teamA_draw = Probability_teamA_draw + 1
        elif teamA_win == 9 or teamA_win == 10:
            x = random.randint(1,10)
            if x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
                 Probability_teamB_win = Probability_teamB_win + 1
            elif x == 6 or x == 7 or x == 8:
                Probability_teamB_draw = Probability_teamB_draw + 1
            elif x == 9 or x  == 10:
                continue

 return (Probability_teamA_win/10000), (Probability_teamA_draw/10000), (Probability_teamB_win/10000), (Probability_teamB_draw/10000)

