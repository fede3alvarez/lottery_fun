import os
import pandas as pd

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
    print("Checking Candidate Numbers...")
    print("")
    
    for attempt in range(candidates.shape[0]):
        print(attempt)
        print(candidates.loc[[attempt]].to_string(index=False, header=False))
        print("")
        print(historic_data['0' == 7])
        print("")

        #df_employees['salary'] > 45000
        #p = events.where((events['s1_held'] == 0.0) & (events['s2_held'] == 0.0))
    


    print("-----------------------------")
    return