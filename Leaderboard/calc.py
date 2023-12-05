import json
import sys
from datetime import date

NAME_IDX = 'name'
STARS_DATA_IDX = 'completion_day_level'
USER_ID_IDX = 'id'
STARS_IDX = 'stars'
STARS_GET_TIME_IDX = 'get_star_ts'

def get_problem_list():
    d0 = date(2022, 11, 30)
    d1 = date.today()
    delta = d1 - d0

    limit = min(delta.days, 25)
    result = []
    for i in range(1,limit+1):
        result.append(str(i)+'.1')
        result.append(str(i)+'.2')
    
    return result

def to_data_table(users): 
    problem_list = get_problem_list()

    header = ['USER_NAME', 'STARS', 'POINTS'] + problem_list

    data = []

    for user_id,user in users.items():
        datum = [
            user['name'] if user['name'] != None else "anonymous user #" + str(user['user_id']),
            user['stars'],
            user['points'],
        ]

        for problem in problem_list:
            datum.append(user['points_detailed'][problem] if problem in user['points_detailed'] else 0)
        
        data.append(datum)
    data.sort(key = lambda a: a[2], reverse=True)
    return [ header ] + data

def to_csv(users, file_name): 
    data = to_data_table(users)

    with open(file_name, 'w') as file:
        for datum in data:
            file.write(', '.join([str(i) for i in datum])+"\n")
        file.close()

def main(argc, argv):
    dataset = {}
    file = open(argv[1], 'r')
    dataset = json.load(file)
    file.close()
    
    members = dataset['members']

    solutions_rank = {}
    users = {}
    for user_id in members.keys():
        results = members[user_id][STARS_DATA_IDX]

        user = {
            'name': members[user_id][NAME_IDX],
            'user_id': members[user_id][USER_ID_IDX],
            'stars': members[user_id][STARS_IDX],
            'points': 0,
            'points_detailed': {},
            'results': {}
        }

        for problem_id in results.keys():
            problem_result = results[problem_id]
            user['results'][problem_id] = {}

            for star_id in problem_result.keys():
                rank_key = str(problem_id) + '.' + str(star_id)
                if rank_key not in solutions_rank:
                    solutions_rank[rank_key] = []

                user['results'][problem_id][star_id] = problem_result[star_id][STARS_GET_TIME_IDX]
                solutions_rank[rank_key].append((user['user_id'], problem_result[star_id][STARS_GET_TIME_IDX]))
        
        users[user['user_id']] = user
    
    for rank_key in solutions_rank.keys():
        solutions_rank[rank_key].sort(key = lambda a: a[1])

        rank = solutions_rank[rank_key]

        for idx,entry in enumerate(rank):
            users[entry[0]]['points'] += len(users) - idx
            users[entry[0]]['points_detailed'][rank_key] = len(users) - idx

    to_csv(users, 'data/result.csv')

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)