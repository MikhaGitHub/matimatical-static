import itertools
import random
from operator import itemgetter, attrgetter



def sampling_algorithm_e(gruppa_e, result_e_power_random, place_result_e):
    #combinations matches(Grmany,Spain)
    played_matches_e = list(itertools.combinations(gruppa_e, 2))
    for matches_e in played_matches_e:
        #here we used a variables below as iteration variable for next manipulations on line 75
        command_e_1, command_e_2 = matches_e
        sum_commands = gruppa_e[command_e_1] + gruppa_e[command_e_2]
        p1 = gruppa_e[command_e_1] / sum_commands
        if random.random() > p1:
            result_e_power_random[command_e_1] += 3
        else:
            result_e_power_random[command_e_2] += 3
#string of code for applying places from 1
    power_commands_e = dict(reversed(sorted(result_e_power_random.items(), key=lambda match_e: match_e[1])))
    min_place_e = 1
    for place in enumerate(power_commands_e):
        print(place[0], place[1])
        for place_result in place_result_e:
            if place[1] == place_result:
                place_result_e[place_result] = min_place_e
                min_place_e += 1
    print(place_result_e)
    # # # # buiding semi-final pairs grupps e




def sampling_algorithm_d(gruppa_d, result_place_commands):
    # same code as before
    error in cf
    played_matches = list(itertools.combinations(gruppa_d, 2))
    for match in played_matches:
        first_team, second_team = match

        scores_all_teams = gruppa_d[first_team] + gruppa_d[second_team]  
        p1 = gruppa_d[first_team] / scores_all_teams


        if random.random() < p1:
            result_place_commands[first_team] += 3
        else: 
            result_place_commands[second_team] += 3
    

    power_commands = (dict(reversed(sorted(result_place_commands.items(), key=lambda st: st[1]))))


    min_place = 1
    #this code add place command in empty dict judging by his result
    for place in enumerate(power_commands):
        print(place[0], place[1])
        for second_place in result_place_commands:
            if second_place == place[1]:
                result_place_commands[second_place] = min_place
                print(power_commands)
                min_place += 1
    print(result_place_commands)

    




def determination_semi_final_pair(place_result_e, result_place_commands):
    semi_final_pair_1 = list(place_result_e.keys())[list(place_result_e.values()).index(1)]
    print(semi_final_pair_1)
    semi_final_pair_2 = list(place_result_e.keys())[list(place_result_e.values()).index(2)]
    print(semi_final_pair_2)
    semi_final_pair_3 = list(result_place_commands.keys())[list(result_place_commands.values()).index(1)]
    print(semi_final_pair_3)

    semi_final_pair_4 = list(result_place_commands.keys())[list(result_place_commands.values()).index(2)]
    print(semi_final_pair_4)
    list_finalists = []

    third_place=[]

    winner_first_place = place_result_e[semi_final_pair_1] + result_place_commands[semi_final_pair_4] / place_result_e[semi_final_pair_1]
    winner_first_place_2 = place_result_e[semi_final_pair_2] + result_place_commands[semi_final_pair_3] / place_result_e[semi_final_pair_2]
    if random.random() > winner_first_place:
        list_finalists.append(semi_final_pair_4)
        third_place.append(semi_final_pair_1)
            
    else:
        list_finalists.append(semi_final_pair_1)
        third_place.append(semi_final_pair_4)


    if random.random() > winner_first_place_2:
        list_finalists.append(semi_final_pair_3)
        third_place.append(semi_final_pair_2)

    else:
        list_finalists.append(semi_final_pair_2)
        third_place.append(semi_final_pair_3)
    print(list_finalists)
    print(third_place)




def main():

    gruppa_d = {
    'Франция':56,
    'Дания':45,
    'Австралия':90,
    'Тунис':11
    }
    gruppa_e = {
     'Германия': 0.85,'Япония': 0.65,'Испания': 0.85,'Коста- Рика': 0.55
    }
    
    result_e_power_random = {'Германия': 0,
      'Япония': 0,
      'Испания': 0,
      'Коста- Рика': 0}

    place_result_e = {'Германия': 0,'Япония': 0,'Испания': 0,'Коста- Рика': 0}

    result_place_commands = {'Франция':0,'Дания':0,'Австралия':0,'Тунис':0}
    sampling_algorithm_d(gruppa_d, result_place_commands)
    sampling_algorithm_e(gruppa_e, result_e_power_random, place_result_e)
    determination_semi_final_pair(place_result_e, result_place_commands)

if __name__ == "__main__":
    main()




















# # # # its code for approximately the same result
# sum_ = 0
# for i in range(100):
#  	sum_ += random.random()
# print(sum_/100)
#  #applying multiple sampling
# for element in result_place_commands.values():
#     element=+sum_
#     print(element)
# print(result_place_commands)







# print(result_e_power_random)


# print(power_commands_e)







#buiding semi-final pairs grupps d





# print(result_place_commands)
# print(place_result_e)




# check_winner = place_result_e[semi_final_pair_1]+ result_place_commands[semi_final_pair_4] / result_place_commands[semi_final_pair_4]
# check_winner_2 = place_result_e[semi_final_pair_2] + result_place_commands[semi_final_pair_3] / result_place_commands[semi_final_pair_3]






# for command in list_finalists:
#     for command_2 in result_place_commands:
#         if command_2 in result_place_commands and command == result_place_commands[command]:
#             print(command,"yeah")

#     if command in place_result_e and command == place_result_e[command]:
#         print(command, "yaeah")
        




# power_list_finalists = [result_place_commands[list_finalists[0]] or result_place_commands[list_finalists[1]] or place_result_e[list_finalists[0]] or place_result_e[list_finalists[1]]]
# print(power_list_finalists)

winner = {'Франция':0,'Дания':0,'Австралия':0,'Тунис':0,'Германия':0,'Япония':0,'Испания':0,'Коста-Рика':0}
second_pl = {'Франция':0,'Дания':0,'Австралия':0,'Тунис':0,'Германия':0,'Япония':0,'Испания':0,'Коста-Рика':0}
third_pl = {'Франция':0,'Дания':0,'Австралия':0,'Тунис':0,'Германия':0,'Япония':0,'Испания':0,'Коста-Рика':0}


