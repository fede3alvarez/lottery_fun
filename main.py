#!/usr/bin/python3
import os
import pandas as pd
import analysis_checks as ch

lottery_data = 'hoosier_lottery.csv'
candidate_numbers = 'candidates.csv'

def main():
    #historic_data = get_data(lottery_data, 'data')
    #print(historic_data.head())
    ch.check_candidate(lottery_data, candidate_numbers)
    return

if __name__ == "__main__":
    main()