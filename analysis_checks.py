import os
import pandas as pd
import itertools as it

# Assuming all files read will be csv formay.
def get_data(filename, directory = None):
    base_folder = os.path.dirname(__file__)

    if directory is None:
        filename = os.path.join(base_folder, filename)
    else:    
        filename = os.path.join(base_folder, directory, filename)
    
    df = pd.read_csv(filename)
    return df

# Checks candidate numbers against historic data
def check_candidate(lottery_data, candidate_numbers):
    candidates = get_data(candidate_numbers)
    historic_data = get_data(lottery_data, 'data')
    
    print("-----------------------------")
    print(" Checking Candidate Numbers")
    print("-----------------------------")
    print("")
    '''
    print(candidates.shape[0])
    print(candidates.loc[0, '0'])

    '''
    for attempt in range(candidates.shape[0]):
        print("Candidate #", attempt)
        print(candidates.loc[[attempt]].to_string(index=False, header=False))
        results = check_number( historic_data,
                                candidates.loc[attempt, '0'],
                                candidates.loc[attempt, '1'],
                                candidates.loc[attempt, '2'],
                                candidates.loc[attempt, '3'],
                                candidates.loc[attempt, '4'],
                                candidates.loc[attempt, '5'])
        #result = historic_data[historic_data['Year'] == 1994]
        print("")

        if (results.empty):
            print("Number Set has not been drawn!")       
        else:
            print(results)

        print("-----------------------------")
        #df_employees['salary'] > 45000
        #p = events.where((events['s1_held'] == 0.0) & (events['s2_held'] == 0.0))
    


    
    return

# Assumes columns are named 0, 1, 2, 3, 4, 5
def check_number(df_input, a, b = None, c = None, d = None, e = None, f = None):

    # If value is None, set it equal to a
    if (b == None): b = a
    if (c == None): c = a
    if (d == None): d = a
    if (e == None): e = a
    if (f == None): f = a

    # Interrogate df
    # If value is not define, it will be equal to a, make the calculation redundant
    df_output = df_input[((df_input['0'] == a) | (df_input['1'] == a) | (df_input['2'] == a) |    # Ball a 
                          (df_input['3'] == a) | (df_input['4'] == a) | (df_input['5'] == a)) &
                         ((df_input['0'] == b) | (df_input['1'] == b) | (df_input['2'] == b) |    # Ball b
                          (df_input['3'] == b) | (df_input['4'] == b) | (df_input['5'] == b)) & 
                         ((df_input['0'] == c) | (df_input['1'] == c) | (df_input['2'] == c) |    # Ball c
                          (df_input['3'] == c) | (df_input['4'] == c) | (df_input['5'] == c)) & 
                         ((df_input['0'] == d) | (df_input['1'] == d) | (df_input['2'] == d) |    # Ball d
                          (df_input['3'] == d) | (df_input['4'] == d) | (df_input['5'] == d)) & 
                         ((df_input['0'] == e) | (df_input['1'] == e) | (df_input['2'] == e) |    # Ball e
                          (df_input['3'] == e) | (df_input['4'] == e) | (df_input['5'] == e)) & 
                         ((df_input['0'] == f) | (df_input['1'] == f) | (df_input['2'] == f) |    # Ball f
                          (df_input['3'] == f) | (df_input['4'] == f) | (df_input['5'] == f))]
    return df_output


def number_subset(df_historic_data, df_candidates = None, num = 6):
    
    # If df_candidates is None, set it equal to df_input
    if (df_candidates == None): df_candidates = df_historic_data

    # Initialize empty result df
    results = pd.DataFrame()

    for attempt in range(df_candidates.shape[0]):
        #print("Candidate #", attempt)
        #print(candidates.loc[[attempt]].to_string(index=False, header=False))

        attempt_numbers = df_candidates.loc[attempt, ['0', '1', '2', '3', '4', '5']]
        attempt_comb = it.combinations(attempt_numbers, num)

        #print(attempt_numbers)
        #print(list(attempt_comb))

        for comb in attempt_comb:
            print(comb)
    pass