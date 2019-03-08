import copy
import result_generator

Home_Teams = ["[86, 88, 83]", "[83, 84, 79]", "[87, 82, 83]", "[89, 83, 81]", "[85, 83, 82]", "[86, 80, 80]", "[76, 75, 77]", "[79, 79, 79]", "[82, 76, 79]", "[76, 76, 76]", "[77, 78, 76]", "[78, 76, 77]", "[80, 78, 77]", "[77, 78, 77]", "[76, 76, 76]", "[74, 73, 76]", "[75, 77, 72]", "[71, 71, 70]", "[73, 74, 71]", "[73, 73, 75]"]
Away_Teams = copy.deepcopy(Home_Teams)
def matches_generator():
 matches_played = []
 First_List = list(range(1,21))

 for j in First_List:
    for k in list(range(1,21)):
        if j == k:
             continue
        else:
             match = str(j) + "-" + str(k)
             matches_played.append(match)

 return matches_played

matches = matches_generator()
expe = {}
for item in matches[0:1]:
    for i in list(range(0,10)):
        teamA_values = Home_Teams[int(item[0])]
        teamB_values = Away_Teams[int(item[2])]
        results = result_generator.Results_Generator(teamA_values, teamB_values)
        if i == 1:
            expe["one"] = "str(results[0])"
        elif i == 2:
            expe["two"] = "str(results[0])"
        elif i == 3:
            expe["three"] = "str(results[0])"
        elif i == 4:
            expe["Four"]  = "str(results[0])"
        elif i == 5:
            expe["five"] = "str(results[0])"
        elif i == 6:
            expe["six"] = "str(results[0])"
        elif i == 7:
            expe["seven"] = "str(results[0])"
        elif i == 8:
            expe["eight"] = "str(results[0])"
        elif i == 9:
            expe["nine"] = "str(results[0])"
        elif i == 10:
            expe["Ten"] = "str(results[0])"

print(expe)
