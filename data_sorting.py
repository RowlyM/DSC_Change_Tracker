"""
Author :Rowly Mudzhiba


"""
# importing libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def sp_changes(df, plant):
    df = df[df['Plant'] == plant]
    area_list = []
    x_label = []

    df = df[df['Parameter'] == 'SP']

    for area in pd.unique(df['Area']):
        ind = str.find(area, '-')
        area_list.append(area)
        x_label.append(area[0:ind])

    sp_change_count = np.zeros((5, len(area_list)))

    area_count = 0
    for area in area_list:
        area_changes_df = df[df['Area'] == area]
        tag_list = pd.unique(area_changes_df['TagName'])

        for tag in area_changes_df['TagName']:
            if str.find(tag[0:3], 'P') > 0:
                sp_change_count[0, area_count] += 1

            if str.find(tag[0:3], 'T') > 0:
                sp_change_count[1, area_count] += 1

            if str.find(tag[0:3], 'L') > 0:
                sp_change_count[2, area_count] += 1

            if str.find(tag[0:3], 'F') > 0:
                sp_change_count[3, area_count] += 1

            if str.find(tag[0:3], 'A') > 0:
                sp_change_count[4, area_count] += 1
        area_count += 1

    barWidth = 1 / (len(area_list))
    X = np.arange(len(area_list))
    fig = plt.subplots(figsize=(12, 8))
    color_b = ['black', 'red', 'green', 'blue', 'cyan']
    br1 = np.arange(len(area_list))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]
    br5 = [x + barWidth for x in br4]

    plt.bar(br1, sp_change_count[0], color=color_b[0], width=barWidth, label='Pressure')
    plt.bar(br2, sp_change_count[1], color=color_b[1], width=barWidth, label='Temperature')
    plt.bar(br3, sp_change_count[2], color=color_b[2], width=barWidth, label='Level')
    plt.bar(br4, sp_change_count[3], color=color_b[3], width=barWidth, label='Flow')
    plt.bar(br5, sp_change_count[4], color=color_b[4], width=barWidth, label='Analyser')

    # Adding Xticks
    plt.xlabel('Plants', fontweight='bold', fontsize=15)
    plt.ylabel('Number of Changes', fontweight='bold', fontsize=15)
    plt.xticks([r + barWidth for r in range(len(area_list))],
               x_label)

    plt.legend()
    plt.show()
