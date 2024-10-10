import itertools
import random
from operator import itemgetter, attrgetter



def sampling_algorithm_e(gruppa_e, result_e_power_random, place_result_e):
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

    power_commands_e = dict(reversed(sorted(result_e_power_random.items(), key=lambda match_e: match_e[1])))

    min_place_e = 1
    for place in enumerate(power_commands_e):
        for place_result in place_result_e:
            if place[1] == place_result:
                place_result_e[place_result] = min_place_e
                min_place_e += 1
    return power_commands_e




def sampling_algorithm_d(gruppa_d, result_place_commands, result_power_d):
    played_matches = list(itertools.combinations(gruppa_d, 2))
    for match in played_matches:
        first_team, second_team = match

        scores_all_teams = gruppa_d[first_team] + gruppa_d[second_team]  
        p1 = gruppa_d[first_team] / scores_all_teams


        if random.random() < p1:
            result_power_d[first_team] += 3
        else: 
            result_power_d[second_team] += 3
    

    power_commands = (dict(reversed(sorted(result_power_d.items(), key=lambda st: st[1]))))
    print(power_commands)


    min_place = 1
    #this code add place command in empty dict judging by his result
    for place in enumerate(power_commands):
        for second_place in result_place_commands:
            if second_place == place[1]:
                result_place_commands[second_place] = min_place
                min_place += 1
    return power_commands



def determination_semi_final_pair(place_result_e, result_place_commands):
    semi_final_pair_1 = list(place_result_e.keys())[list(place_result_e.values()).index(1)]

    semi_final_pair_2 = list(place_result_e.keys())[list(place_result_e.values()).index(2)]

    semi_final_pair_3 = list(result_place_commands.keys())[list(result_place_commands.values()).index(1)]


    semi_final_pair_4 = list(result_place_commands.keys())[list(result_place_commands.values()).index(2)]

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
    return list_finalists,third_place


def determing_world_championship_medalist(list_finalists, third_place, power_commands, power_commands_e):
    #who is winner in that go to winner
    #who is second pl ...
    power_finalists = {}
    power_third_finalists = {}

    winner = {'Франция':0,'Дания':0,'Австралия':0,'Тунис':0,'Германия':0,'Япония':0,'Испания':0,'Коста-Рика':0}
    second_pl = {'Франция':0,'Дания':0,'Австралия':0,'Тунис':0,'Германия':0,'Япония':0,'Испания':0,'Коста-Рика':0}
    third_pl = {'Франция':0,'Дания':0,'Австралия':0,'Тунис':0,'Германия':0,'Япония':0,'Испания':0,'Коста-Рика':0}
    # this code return combination of semifianal_pais
    for finanalist, power in power_commands.items():
        for winner_1 in list_finalists:
            if winner_1 == finanalist:
                power_finalists[finanalist] = power
    for finanalist_2, power_2 in power_commands_e.items():
        for winner_1 in list_finalists:
            if winner_1 == finanalist_2:
                power_finalists[finanalist_2] = power_2
    for thirdplace, power_3 in power_commands.items():
        for player in third_place:
            if player == thirdplace:
                power_third_finalists[thirdplace] = power_3
    for thirdplace, power_4 in power_commands_e.items():
        for player in third_place:
            if player == thirdplace:
                power_third_finalists[thirdplace] = power_4
    print(f"Finalists is {list_finalists}")
    print(f"Third place:{third_place}")
    #add finalist in dict winner
    list_points_finalists = list(power_finalists.values())
    for winners in range(1, len(power_finalists)):
        bigger_point = list_points_finalists[0]
        if list_points_finalists[winners] > bigger_point:
            bigger_point = list_points_finalists[winners]


    for name_command, points_command in power_finalists.items():
        print(name_command,points_command)
        if points_command == bigger_point: 
            winner[name_command] = bigger_point

    #add second and third place
    max_points = max(power_third_finalists.values())
    winner_team = [name for name,points in power_third_finalists.items() if points == max_points]
    for team in winner_team:
        second_pl[team] = max_points
    return winner, second_pl, third_pl



def application_of_resampling_on_all_tournament(gruppa_d, gruppa_e):
    #this code will work for all tournament not like before!!
    result_d_e = {'Германия':0,'Япония':0,'Испания':0,'Коста-Рика':0,'Франция':0,'Дания':0,'Австралия':0,'Тунис':0}
    winner = {'Франция':0,'Дания':0,'Австралия':0,'Тунис':0,'Германия':0,'Япония':0,'Испания':0,'Коста-Рика':0}
    second_pl = {'Франция':0,'Дания':0,'Австралия':0,'Тунис':0,'Германия':0,'Япония':0,'Испания':0,'Коста-Рика':0}
    third_pl = {'Франция':0,'Дания':0,'Австралия':0,'Тунис':0,'Германия':0,'Япония':0,'Испания':0,'Коста-Рика':0}
    played_matches_e = list(itertools.combinations(gruppa_e, 2))
    played_matches_d = list(itertools.combinations(gruppa_d, 2))
    for matches_e in played_matches_e:
        #here we used a variables below as iteration variable for next manipulations on line 75
        command_e_1, command_e_2 = matches_e
        sum_commands = gruppa_e[command_e_1] + gruppa_e[command_e_2]
        p1 = gruppa_e[command_e_1] / sum_commands
        if random.random() > p1:
            result_d_e[command_e_1] += 3
        else:
            result_d_e[command_e_2] += 3

    for matches_d in played_matches_d:
        #here we used a variables below as iteration variable for next manipulations on line 75
        command_e_1, command_e_2 = matches_d
        sum_commands = gruppa_d[command_e_1] + gruppa_d[command_e_2]
        p1 = gruppa_d[command_e_1] / sum_commands
        if random.random() > p1:
            result_d_e[command_e_1] += 3
        else:
            result_d_e[command_e_2] += 3
    combination_e_d = dict(reversed(sorted(result_d_e.items(), key=lambda match_e: match_e[1])))


    # max_points = max(combination_e_d.values())
    # winner_team = [name for name, points in combination_e_d.items() if points==max_points]
    # for winners in winner_team:
    #     winner[winners] = max_points
    for name,points_ in combination_e_d.items():
        for name,points in winner.items():
            if combination_e_d[name] == winner[name]:
                winner[name] = points_
    return  combination_e_d,winner
  



    



def main():
    gruppa_d = {
    'Франция':56,
    'Дания':45,
    'Австралия':90,
    'Тунис':11
    }
    gruppa_e = {
     'Германия': 0.85,'Япония': 0.65,'Испания': 0.85,'Коста-Рика': 0.55
    }
    
    result_e_power_random = {'Германия': 0,
      'Япония': 0,
      'Испания': 0,
      'Коста-Рика': 0}

    place_result_e = {'Германия': 0,'Япония': 0,'Испания': 0,'Коста- Рика': 0}

    result_power_d = {'Франция':0,'Дания':0,'Австралия':0,'Тунис':0}
    result_place_commands = {'Франция':0,'Дания':0,'Австралия':0,'Тунис':0}
    power_commands = sampling_algorithm_d(gruppa_d, result_place_commands, result_power_d)
    power_commands_e = sampling_algorithm_e(gruppa_e, result_e_power_random, place_result_e)
    list_finalists, third_place = determination_semi_final_pair(place_result_e, result_place_commands)

    determing_world_championship_medalist(list_finalists, third_place, power_commands, power_commands_e)
    result_all_commands = {}
    result_all_commands = application_of_resampling_on_all_tournament(gruppa_d, gruppa_e)
    print(result_all_commands)
    



if __name__ == "__main__":
    main()


