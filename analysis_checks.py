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
        results = check_multiple_numbers(historic_data,
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
       
    return


# Assumes columns are named 0, 1, 2, 3, 4, 5
# Checks for instances of a single number on a df with draws / sets
def check_single_number(df, a):
    df = df[((df['0'] == a) | 
             (df['1'] == a) | 
             (df['2'] == a) | 
             (df['3'] == a) | 
             (df['4'] == a) | 
             (df['5'] == a))]

    return df


# Checks for instances of a multiple numbers on a df with draws / sets
def check_multiple_numbers(df, *args):

    # Limit entries to a max of 6
    entries = min(len(args), 6)

    for entry in range(entries):
        df = check_single_number(df, args[entry])

    return df


# Based on a set / draw (included in df_candidates) 
#       gets all the subsets / combinations of size "size"
#       and finds all combinations in df_historic data
def number_subset(df_historic_data, df_candidates, size = 6):

    # Initialize empty result df
    results = pd.DataFrame()

    # Iterate throught every entry
    for entry in range(df_candidates.shape[0]):

        # Remove entry from df_historic_data
        entry_index = df_historic_data[ (df_historic_data['0'] == df_candidates.loc[entry, '0'].item())         &
                                        (df_historic_data['1'] == df_candidates.loc[entry, '1'].item()) &
                                        (df_historic_data['2'] == df_candidates.loc[entry, '2'].item()) &
                                        (df_historic_data['3'] == df_candidates.loc[entry, '3'].item()) &
                                        (df_historic_data['4'] == df_candidates.loc[entry, '4'].item()) &
                                        (df_historic_data['5'] == df_candidates.loc[entry, '5'].item())
                                      ].index

        df_historic_data.drop(entry_index, inplace=True)

        # Get entry and find combinations / subsets of numbers
        entry_numbers = df_candidates.loc[entry, ['0', '1', '2', '3', '4', '5']]

        entry_comb = it.combinations(entry_numbers, size)

        # Iterate throught every combination of a single entry
        for comb in entry_comb:
            #results = pd.concat([check_multiple_numbers(df_historic_data, *comb), results], axis=0)
            result = check_multiple_numbers(df_historic_data, *comb)

            if not(result.empty):
                results = pd.concat([results, df_candidates.iloc[[entry]]], axis=0)
                results = pd.concat([results, result], axis=0)

    return results