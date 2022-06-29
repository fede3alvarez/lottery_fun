#!/usr/bin/python3
import os
import pandas as pd
import analysis_checks as ch

lottery_data = 'hoosier_lottery.csv'
candidate_numbers = 'candidates.csv'
test_data_file = 'test_data.csv'

def main():
    historic_data = ch.get_data(lottery_data, 'data')
    historic_2 = historic_data.copy()
    candidate = ch.get_data(candidate_numbers)
    test_data = ch.get_data(test_data_file)
    print("This is a test.")
    #print(historic_data.head())
    #
    #ch.check_candidate(lottery_data, candidate_numbers)
    #x = ch.check_single_number(historic_data , 33)
    #x = ch.check_multiple_numbers(historic_data, 33, 35)
    x = ch.number_subset(historic_data, historic_2, 5)
    #x = ch.check_number(historic_data, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    #x = ch.check_number(historic_data, 6, 33)
    print(x)
    return

if __name__ == "__main__":
    main()