#!/usr/bin/python3
'''
This module objective is to analyse odd / even odd
A bit of math / background first:
    We have this lottery  is a 6 (selections) / 46 (balls), therefore:

'''
import math
import pandas as pd
import analysis_checks as ch

def main():
    historic_data = ch.get_data('hoosier_lottery.csv', 'data')
    z = add_evens_and_odds(historic_data)
    print(z)
    '''
    n = 45
    k = 6
    x =even_odds(n, k)
    print(x)
    '''

def add_evens_and_odds(df, header=-1):
    # Initialize parameters
    df["Even"] = 0
    df["Odd"] = 0
    
    if (header == -1):
        header = ["0" ,"1" ,"2" ,"3" ,"4" ,"5"]
    
    #for number in header:
    df.loc[(df['0'] % 2) == 0, 'Even'] = df['Even'] + 1
    df.loc[(df['0'] % 2) == 1, 'Odd'] = df['Odd'] + 1
    #df.loc[df['c1'] == 'Value', 'c2'] = 10
    return df

def even_odds(n, k):
    # Initialize parameters
    results = list()
    total = math.comb(n, k)
    total_evens =  n // 2
    total_odds = n - total_evens

    # Appends probability of getting even & odd
    # In a list with template (even, odd, prob)
    for even in range(k+1):
        even_prob = math.comb(total_evens, even)
        odd_prob = math.comb(total_odds, k - even)
        results.append([even, k - even, even_prob * odd_prob / total])

    # Return data as a pandas pd
    results_df = pd.DataFrame(results)
    results_df.columns = ["Evens", "Odds", "Prob"]

    return results_df


if __name__ == "__main__":
    main()