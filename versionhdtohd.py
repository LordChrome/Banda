import versionhdtohd2_1_6
import versionlast6matches2_1_6
import versionhomeaway2_1_6

teamA_name = input("Enter Home Team Name : ")
teamA_values = []
for item in ['Attack', 'MidField', 'Defend']:
    value = int(input("Enter value for " + item + " : "))
    teamA_values.append(value)
teamB_name = input("Enter Away Team Name : ")
teamB_values = []
for item in ['Attack', 'MidField', 'Defend']:
    value = int(input("Enter value of " + item + " : "))
    teamB_values.append(value)

teamA_probability=[]
for item in ['win_probability_Home_team_hd_to_hd', 'Draw_probability_Home_team_hd_to_hd', 'loose_probability_Home_team_hd_to_hd']:
    value = int(input("Enter value of " + item + " : "))
    teamA_probability.append(value)

teamB_probability = []
for item in ['win_probability_Away_team_hd_to_hd', 'Draw_probability_Away_team_hd_to_hd', 'loose_probability_Away_team_hd_to_hd']:
    value = int(input("Enter value of " + item + " : "))
    teamB_probability.append(value)

last6matcheshome = []
for item in ['win_probability_Home_team_last6matches', 'Draw_probability_Home_team_last6matches', 'loose_probability_Home_team_last6matches']:
    value = int(input("Enter value of " + item + " : "))
    last6matcheshome.append(value)

last6matchesaway = []
for item in ['win_probability_Away_team_last6matches', 'Draw_probability_Away_team_last6matches', 'loose_probability_Away_team_last6matches']:
    value = int(input("Enter value of " + item + " : "))
    last6matchesaway.append(value)

homematches = []
for item in ['win_probability_Home_team_matches', 'Draw_probability_Home_team_matches', 'loose_probability_Home_team_matches']:
    value = int(input("Enter value of " + item + " : "))
    homematches.append(value)

awaymatches = []
for item in ['win_probability_Away_team_matches', 'Draw_probability_Away_team_matches', 'loose_probability_Away_team_matches']:
    value = int(input("Enter value of " + item + " : "))
    awaymatches.append(value)

versionhdtohd2_1_6_results = versionhdtohd2_1_6.predictive_analysis(teamA_values, teamB_values, teamA_probability, teamB_probability)
versionlast6matches2_1_6_results = versionlast6matches2_1_6.predictive_analysis(teamA_values, teamB_values, last6matcheshome, last6matchesaway)
versionhomeaway2_1_6_results = versionhomeaway2_1_6.predictive_analysis(teamA_values, teamB_values, homematches, awaymatches)

print(versionhdtohd2_1_6_results)
print(versionlast6matches2_1_6_results)
print(versionhomeaway2_1_6_results)
