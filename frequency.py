import os
import datetime
import pandas as pd
import analysis_checks as ch

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

lottery_data = 'hoosier_lottery.csv'
lottery_data = 'test.csv'
candidate_numbers = 'candidates.csv'
test_data_file = 'test_data.csv'

def main():
    historic_data = ch.get_data(lottery_data, 'data')
    x = find_freq(historic_data)

    return

def find_freq(df, ball_range=46):
    ball_range += 1

    for ball in range(ball_range):

        ball_header = "Ball_" + str(ball)
        df[ball_header] = 0
        df.loc[df['0'] == ball, ball_header] = 1
        df.loc[df['1'] == ball, ball_header] = 1
        df.loc[df['2'] == ball, ball_header] = 1
        df.loc[df['3'] == ball, ball_header] = 1
        df.loc[df['4'] == ball, ball_header] = 1
        df.loc[df['5'] == ball, ball_header] = 1

    return df

"""
# ---------------------------
# Time Periodicity
# ---------------------------

fft = tf.signal.rfft(df['T (degC)'])
f_per_dataset = np.arange(0, len(fft))

n_samples_h = len(df['T (degC)'])
hours_per_year = 24*365.2524
years_per_dataset = n_samples_h/(hours_per_year)

plt.figure(6)
f_per_year = f_per_dataset/years_per_dataset
plt.step(f_per_year, np.abs(fft))
plt.xscale('log')
plt.ylim(0, 400000)
plt.xlim([0.1, max(plt.xlim())])
plt.xticks([1, 365.2524], labels=['1/Year', '1/day'])
_ = plt.xlabel('Frequency (log scale)')

# Print outputs
plt.show()
"""

if __name__ == "__main__":
    main()