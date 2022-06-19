#!/usr/bin/python3
import os
import pandas as pd

lottery_data = 'hoosier_lottery.csv'

def main():
    historic_data = get_data(lottery_data)
    print(historic_data.head())
    return

# Assuming all files read will be csv formay.
def get_data(filename, directory='data'):
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, directory, filename)
    
    df = pd.read_csv(filename)
    return df

if __name__ == "__main__":
    main()