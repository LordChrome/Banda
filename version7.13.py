result = [0, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 0, 0, -1, -1, -1, 0, 0, 1, -1, 0, 1, -1, 1, 1, 0, 0, 0]
versionhdtohdresults = [[34.1542, 19.5584, 23.1611, 23.1264],[11.7211, 29.4055, 22.0569, 36.8166],[41.6948, 17.5004, 23.728, 17.0769],[55.2905, 13.3779, 18.951, 12.3807],[27.6117, 23.0181, 19.6124, 29.7579],[28.9507, 18.5105, 33.3283, 19.2106],[17.8347, 13.3165, 52.7615, 16.0874],[27.0974, 17.8818, 35.5279, 19.493],[62.2644, 17.7636, 6.639, 13.3331],[41.492, 14.1164, 29.3259, 15.0658],[11.7332, 18.5247, 43.9451, 25.7971],[14.2693, 14.2492, 53.6616, 17.82],[66.9562, 0.0, 33.0439, 0.0],[24.9696, 31.2328, 12.5426, 31.2551],[16.7842, 12.9918, 54.9566, 15.2675],[6.5212, 12.6635, 57.8457, 22.9697],[67.0486, 0.0, 32.9515, 0.0],[22.4756, 22.6307, 27.4771, 27.4167],[0.0, 26.8265, 31.4379, 41.7357],[22.805, 20.7543, 32.3766, 24.0642],[34.4273, 17.2343, 32.2114, 16.1271],[23.2877, 16.842, 42.3474, 17.523], [36.9601, 24.957, 19.0361, 19.0469],[30.0677, 23.0853, 24.8562, 21.9909],[39.9897, 0.0, 60.0104, 0.0],[40.5, 14.3463, 30.4646, 14.6892],[23.059, 16.0773, 40.277, 20.5868],[44.8125, 12.3194, 30.6163, 12.2519]]
versionhomeawayresults = [[22.5709, 13.5877, 39.9126, 23.9289],[22.9707, 23.0578, 24.2324, 29.7392],[27.5409, 31.5574, 24.7189, 16.1829],[32.5335, 8.1987, 29.6771, 29.5908],[19.65, 17.35, 31.5403, 31.4598],[28.8149, 12.8716, 42.1582, 16.1554],[29.3966, 14.2679, 24.2977, 32.0379],[48.1893, 8.5157, 39.0295, 4.2656],[37.0688, 18.4958, 8.9166, 35.5189],[28.0129, 27.9504, 26.1497, 17.8871],[16.5416, 32.4757, 32.6757,18.3071],[34.0518, 14.929, 25.4986, 25.5207],[25.3227, 15.9246, 48.7233, 10.0295],[21.3213, 28.6863, 33.3801, 16.6124],[42.5172, 25.5344, 18.9665, 12.982],[26.0786, 12.567, 20.1674, 41.1871],[37.9384, 11.5179, 32.1118, 18.432],[34.0492, 19.7281, 40.8195, 5.4033],[21.8845, 35.5978, 25.2375, 17.2803],[33.1102, 25.4384, 27.3225, 14.129],[34.6837, 26.1001, 29.2167, 9.9996],[36.5913, 4.7015, 40.3569, 18.3504],[38.38, 26.3223, 22.5222, 12.7746],[6.6868, 31.3867, 20.3681, 41.5585],[30.857, 6.5267, 27.8938, 34.7226],[18.0749, 37.441, 22.2353, 22.2489],[43.3486, 21.2854, 24.9841, 10.382],[31.5612, 20.889, 35.5056, 12.0443]]

def possible_results():                
  possible_results = []
  
  for k in list(range(10,100)):
        for j in list(range(10,100,2)):
            algorithm_combination = str(k) + "-" + str(j)
            if algorithm_combination[::-1] in possible_results:
               continue
            elif algorithm_combination not in possible_results:
               possible_results.append(algorithm_combination)
            else:
               continue
                    
  return possible_results

percentage_combination = possible_results()

for item23 in percentage_combination:
  results = []
  success_probability = 0
  win_success_probability = 0
  success_probability_percentage = 0
  win_success_probability_percentage = 0
  a = int(item23[0]+item23[1])
  b = int(item23[3]+item23[4])
  d = a+b
  for (item1, item3) in zip(versionhdtohdresults, versionhomeawayresults):
        version1_winA = item1[0]*(a/d)
        version1_drawA = item1[1]*(a/d)
        version1_winB = item1[2]*(a/d)
        version1_drawB = item1[3]*(a/d)
        version3_winA = item3[0]*(b/d)
        version3_drawA = item3[1]*(b/d)
        version3_winB = item3[2]*(b/d)
        version3_drawB = item3[3]*(b/d)
        teamA_win = version1_winA + version3_winA
        teamA_draw = version1_drawA + version3_drawA
        teamB_win = version1_winB + version3_winB
        teamB_draw = version1_drawB + version3_drawB
        if teamA_win > teamA_draw:
            if teamA_win > teamB_win:
                if teamA_win > teamB_draw:
                    output = []
                    output.append(1)
                    output.append(0)
                    results.append(output)
                else:
                    output = []
                    output.append(0)
                    output.append(1)
                    results.append(output)
            else:
                if teamB_win > teamB_draw:
                    output = []
                    output.append(-1)
                    output.append(0)
                    results.append(output)
                else:
                    output = []
                    output.append(0)
                    output.append(-1)
                    results.append(output)
        else:
            if teamA_draw > teamB_win:
                output = []
                output.append(0)
                output.append(-1)
                results.append(output)
            else:
                if teamB_win > teamB_draw:
                    output = []
                    output.append(-1)
                    output.append(0)
                    results.append(output)
                else:
                    output = []
                    output.append(0)
                    output.append(-1)
                    results.append(output)

  for (item, items) in zip(result, results):
        if item in items:
          success_probability = success_probability + 1
          if item == items[0]:
            win_success_probability = win_success_probability + 1
          else:
            continue
        else:
            continue

  success_probability_percentage = (success_probability/len(result)*100)
  win_success_probability_percentage = (win_success_probability/len(result)*100)

  if success_probability_percentage >= 75:
        print("Succes Probability Percentage " + str(success_probability_percentage))
        print("Win Success Probability Percentage " + str(win_success_probability_percentage))
        print(item23)
  else:
        continue
