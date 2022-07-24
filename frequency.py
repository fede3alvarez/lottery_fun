import os
import datetime
import numpy as np
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
#lottery_data = 'test.csv'
candidate_numbers = 'candidates.csv'
test_data_file = 'test_data.csv'

def main():
    historic_data = ch.get_data(lottery_data, 'data')
    x = find_freq(historic_data, graph=True)

    return

def find_freq(df, ball_range=46, graph=False):
    ball_range += 1

    for ball in range(1, ball_range):

        ball_header = "Ball_" + str(ball)
        df[ball_header] = 0
        df.loc[df['0'] == ball, ball_header] = 1
        df.loc[df['1'] == ball, ball_header] = 1
        df.loc[df['2'] == ball, ball_header] = 1
        df.loc[df['3'] == ball, ball_header] = 1
        df.loc[df['4'] == ball, ball_header] = 1
        df.loc[df['5'] == ball, ball_header] = 1

        if graph:
            # Get Fourrier Transform
            fft = tf.signal.rfft(df[ball_header])
            print("----------------")
            print(fft)
            print("----------------")
            #do nothing
            index = np.arange(0, len(fft))

            #n_samples_h = len(df['T (degC)'])
            #hours_per_year = 24*365.2524
            #years_per_dataset = n_samples_h/(hours_per_year)


            plt.figure(ball)

            plt.plot(index, fft)

            #X = [x.real for x in cnums]
            #Y = [x.imag for x in cnums]
            #plt.scatter(X,Y, color='red')
            #plt.show()

            #f_per_year = f_per_dataset/years_per_dataset
            #plt.step(f_per_year, np.abs(fft))
            #plt.xscale('log')
            #plt.ylim(0, 400000)
            #plt.xlim([0.1, max(plt.xlim())])
            #plt.xticks([1, 365.2524], labels=['1/Year', '1/day'])
            #_ = plt.xlabel('Frequency (log scale)')

            plt.title(ball_header)
            plt.ylim(0, 50)
            plt.xlim(0, 100)
            plt.grid()

            base_folder = os.path.dirname(__file__)
            jpg_file = ball_header + ".jpg"
            #jpg_file_loc = os.path.join(base_folder, 'freq', 'jpg', jpg_file)
            #jpg_file_loc = os.path.join(base_folder, 'freq', 'below_100', jpg_file)
            jpg_file_loc = os.path.join(base_folder, 'freq', 'imaginary', jpg_file)

            plt.savefig(jpg_file_loc)

            plt.clf()
            x = df[ball_header]
            y = np.arange(0, len(x))
            plt.title(ball_header)
            
            plt.bar(y, x, 0.5)
            plt.xlim(0, 1500)
            plt.grid()

            jpg_num_loc = os.path.join(base_folder, 'freq', 'raw', jpg_file)
            #plt.savefig(jpg_num_loc)
            
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