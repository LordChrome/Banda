result = [0, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 0, 0, -1, -1, -1, 0, 0, 1, -1, 0, 1, -1, 1, 1, 0, 0, 0]
versionhdtohdresults = [[34.1542, 19.5584, 23.1611, 23.1264],[11.7211, 29.4055, 22.0569, 36.8166],[41.6948, 17.5004, 23.728, 17.0769],[55.2905, 13.3779, 18.951, 12.3807],[27.6117, 23.0181, 19.6124, 29.7579],[28.9507, 18.5105, 33.3283, 19.2106],[17.8347, 13.3165, 52.7615, 16.0874],[27.0974, 17.8818, 35.5279, 19.493],[62.2644, 17.7636, 6.639, 13.3331],[41.492, 14.1164, 29.3259, 15.0658],[11.7332, 18.5247, 43.9451, 25.7971],[14.2693, 14.2492, 53.6616, 17.82],[66.9562, 0.0, 33.0439, 0.0],[24.9696, 31.2328, 12.5426, 31.2551],[16.7842, 12.9918, 54.9566, 15.2675],[6.5212, 12.6635, 57.8457, 22.9697],[67.0486, 0.0, 32.9515, 0.0],[22.4756, 22.6307, 27.4771, 27.4167],[0.0, 26.8265, 31.4379, 41.7357],[22.805, 20.7543, 32.3766, 24.0642],[34.4273, 17.2343, 32.2114, 16.1271],[23.2877, 16.842, 42.3474, 17.523],[36.9601, 24.957, 19.0361, 19.0469],[30.0677, 23.0853, 24.8562, 21.9909],[39.9897, 0.0, 60.0104, 0.0],[40.5, 14.3463, 30.4646, 14.6892],[23.059, 16.0773, 40.277, 20.5868],[44.8125, 12.3194, 30.6163, 12.2519]]
versionlastmatchesresults = [[15.60979, 11.98324, 49.3273, 23.07935],[18.52341, 26.0543, 32.00508, 23.41722],[20.3091, 28.15507, 34.08247, 17.45337],[24.52438, 17.63329, 27.20142, 30.64092],[16.93745, 15.46465, 35.07462, 32.52329],[25.04644, 16.5034, 43.20367, 15.2465],[14.28927, 21.04971, 32.31608, 32.34495],[34.50583, 10.41082, 45.79414, 9.28922],[30.12647, 17.34442, 29.36858, 23.16054],[19.39908, 28.25337, 33.36973, 18.97783],[12.2645, 29.23973, 43.86714, 14.62864],[25.03673, 12.50883, 34.90416, 27.55029],[19.78197, 11.6819, 55.00464, 13.5315],[18.86779, 24.30114, 35.23795, 21.59313],[33.31764, 18.40156, 41.12778, 7.15303],[21.72376, 11.90943, 39.64171, 26.72511],[31.49122, 7.49999, 39.84178, 21.16702],[21.97849, 19.70286, 45.2709, 13.04768],[24.71539, 24.70695, 33.18972, 17.38795],[23.01261, 20.83027, 29.32485, 26.83228],[34.93636, 19.18103, 32.31527, 13.56735],[30.70514, 9.99379, 40.54692, 18.75416],[39.84702, 21.90959, 26.3607, 11.8827],[13.96906, 25.35521, 27.1877, 33.38804],[25.33274, 9.03709, 37.63469, 27.99549],[7.42573, 32.42723, 30.07803, 30.06902],[33.86358, 18.07587, 32.02497, 16.03559],[31.607, 12.20366, 44.6782, 11.51115]]

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
  for (item1, item2) in zip(versionhdtohdresults, versionlastmatchesresults):
        version1_winA = item1[0]*(a/d)
        version1_drawA = item1[1]*(a/d)
        version1_winB = item1[2]*(a/d)
        version1_drawB = item1[3]*(a/d)
        version2_winA = item2[0]*(b/d)
        version2_drawA = item2[1]*(b/d)
        version2_winB = item2[2]*(b/d)
        version2_drawB = item2[3]*(b/d)
        teamA_win = version1_winA + version2_winA 
        teamA_draw = version1_drawA + version2_drawA
        teamB_win = version1_winB + version2_winB
        teamB_draw = version1_drawB + version2_drawB
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

  if success_probability_percentage >= 69:
        print("Succes Probability Percentage " + str(success_probability_percentage))
        print("Win Success Probability Percentage " + str(win_success_probability_percentage))
        print(item23)
  else:
        continue
