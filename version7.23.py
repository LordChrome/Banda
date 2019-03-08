result = [0, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 0, 0, -1, -1, -1, 0, 0, 1, -1, 0, 1, -1, 1, 1, 0, 0, 0, -1, -1, -1, -1]
versionlastmatchesresults = [[15.60979, 11.98324, 49.3273, 23.07935],[18.52341, 26.0543, 32.00508, 23.41722],[20.3091, 28.15507, 34.08247, 17.45337],[24.52438, 17.63329, 27.20142, 30.64092],[16.93745, 15.46465, 35.07462, 32.52329],[25.04644, 16.5034, 43.20367, 15.2465],[14.28927, 21.04971, 32.31608, 32.34495],[34.50583, 10.41082, 45.79414, 9.28922],[30.12647, 17.34442, 29.36858, 23.16054],[19.39908, 28.25337, 33.36973, 18.97783],[12.2645, 29.23973, 43.86714, 14.62864],[25.03673, 12.50883, 34.90416, 27.55029],[19.78197, 11.6819, 55.00464, 13.5315],[18.86779, 24.30114, 35.23795, 21.59313],[33.31764, 18.40156, 41.12778, 7.15303],[21.72376, 11.90943, 39.64171, 26.72511],[31.49122, 7.49999, 39.84178, 21.16702],[21.97849, 19.70286, 45.2709, 13.04768],[24.71539, 24.70695, 33.18972, 17.38795],[23.01261, 20.83027, 29.32485, 26.83228],[34.93636, 19.18103, 32.31527, 13.56735],[30.70514, 9.99379, 40.54692, 18.75416],[39.84702, 21.90959, 26.3607, 11.8827],[13.96906, 25.35521, 27.1877, 33.38804],[25.33274, 9.03709, 37.63469, 27.99549],[7.42573, 32.42723, 30.07803, 30.06902],[33.86358, 18.07587, 32.02497, 16.03559],[31.607, 12.20366, 44.6782, 11.51115],[24.09074, 11.42616, 48.16131, 16.3218],[19.19771, 23.18397, 38.92698, 18.69135],[7.6403, 18.56371, 46.14988, 27.64612],[26.14511, 15.239, 35.36367, 23.25223]]
versionhomeawayresults = [[22.5709, 13.5877, 39.9126, 23.9289],[22.9707, 23.0578, 24.2324, 29.7392],[27.5409, 31.5574, 24.7189, 16.1829],[32.5335, 8.1987, 29.6771, 29.5908],[19.65, 17.35, 31.5403, 31.4598],[28.8149, 12.8716, 42.1582, 16.1554],[29.3966, 14.2679, 24.2977, 32.0379],[48.1893, 8.5157, 39.0295, 4.2656],[37.0688, 18.4958, 8.9166, 35.5189],[28.0129, 27.9504, 26.1497, 17.8871],[16.5416, 32.4757, 32.6757,18.3071],[34.0518, 14.929, 25.4986, 25.5207],[25.3227, 15.9246, 48.7233, 10.0295],[21.3213, 28.6863, 33.3801, 16.6124],[42.5172, 25.5344, 18.9665, 12.982],[26.0786, 12.567, 20.1674, 41.1871],[37.9384, 11.5179, 32.1118, 18.432],[34.0492, 19.7281, 40.8195, 5.4033],[21.8845, 35.5978, 25.2375, 17.2803],[33.1102, 25.4384, 27.3225, 14.129],[34.6837, 26.1001, 29.2167, 9.9996],[36.5913, 4.7015, 40.3569, 18.3504],[38.38, 26.3223, 22.5222, 12.7746], [6.6868, 31.3867, 20.3681, 41.5585],[30.857, 6.5267, 27.8938, 34.7226],[18.0749, 37.441, 22.2353, 22.2489],[43.3486, 21.2854, 24.9841, 10.382],[31.5612, 20.889, 35.5056, 12.0443],[33.7859, 6.5197, 39.5618, 20.1327],[26.0916, 26.0697, 35.74, 12.0988],[7.8783, 15.8031, 44.7894, 31.5293],[40.0805, 15.7112, 22.1399, 22.0685]]

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
  for (item2, item3) in zip(versionlastmatchesresults, versionhomeawayresults):
        version2_winA = item2[0]*(a/d)
        version2_drawA = item2[1]*(a/d)
        version2_winB = item2[2]*(a/d)
        version2_drawB = item2[3]*(a/d)
        version3_winA = item3[0]*(b/d)
        version3_drawA = item3[1]*(b/d)
        version3_winB = item3[2]*(b/d)
        version3_drawB = item3[3]*(b/d)
        teamA_win = version2_winA + version3_winA
        teamA_draw = version2_drawA + version3_drawA
        teamB_win = version2_winB + version3_winB
        teamB_draw = version2_drawB + version3_drawB
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

  if success_probability_percentage >= 65:
        print("Succes Probability Percentage " + str(success_probability_percentage))
        print("Win Success Probability Percentage " + str(win_success_probability_percentage))
        print(item23)
  else:
        continue
