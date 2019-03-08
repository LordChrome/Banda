import version4_1_2
import version4_1_3
import version4_1_4

def Results_Generator(teamA_values, teamB_values):
    version4_1_2_results = version4_1_2.predictive_analysis(teamA_values, teamB_values)
    version4_1_3_results = version4_1_3.predictive_analysis(teamA_values, teamB_values)
    version4_1_4_results = version4_1_4.predictive_analysis(teamA_values, teamB_values)
    
    teamA_win = version4_1_2_results[0] + version4_1_3_results[0] + version4_1_4_results[0]
    teamA_draw = version4_1_2_results[1] + version4_1_3_results[1] + version4_1_4_results[1]
    teamB_win = version4_1_2_results[2] + version4_1_3_results[2] + version4_1_4_results[2]
    teamB_draw = version4_1_2_results[3] + version4_1_3_results[3] + version4_1_4_results[3]

    if teamA_win > teamA_draw:
        if teamA_win > teamB_win:
            if teamA_win > teamB_draw:
                return 1
            else:
                return 0
        else:
            if teamB_win > teamB_draw:
                return -1
            else:
                return 0
    else:
        if teamA_draw > teamA_win:
            if teamA_draw > teamB_win:
                if teamA_draw > teamB_draw:
                    return 0
                else:
                    return 0
            else:
                if teamB_win > teamB_draw:
                    return -1
                else:
                    return 0
        else:
            return 1
