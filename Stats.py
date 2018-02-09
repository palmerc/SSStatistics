#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'font.serif': 'Palatino',
                     'font.sans-serif': 'Helvetica',
                     'text.usetex': True})

def sus(data):
    pos = list(range(1, 13))
    bounds = [0, 100]
    width = 0.25

    fig = plt.figure(300)
    ax = fig.add_subplot(111)
    ax.bar([p - width for p in pos], data.Usability, width, label='Usability')
    ax.bar([p for p in pos], data.SUS, width, label='SUS')
    ax.bar([p + width for p in pos], data.Learnability, width, label='Learnability')
    ax.set_xticks(data.Candidate)
    ax.set_ylim(bounds)

    plt.title('System Usability Scale')
    plt.xlabel('Candidate')
    plt.ylabel('Score')
    plt.legend()
    plt.savefig('sus_scores.eps', bbox_inches='tight', format='eps', dpi=1000)
    plt.show()

def time(data):
    group1Data = pd.DataFrame(data[data.Group == 1], columns=['SS_Time', 'US_Time'])
    group2Data = pd.DataFrame(data[data.Group == 2], columns=['SS_Time', 'US_Time'])
    largestValue = max([data.SS_Time.values.max(), data.US_Time.values.max()])
    upperbound = int((largestValue + 99) // 100 * 100)
    bounds = [0, upperbound]

    fig = plt.figure(100)
    ax = fig.add_subplot(111)
    ax.plot(bounds, bounds, color='k', linestyle='-', linewidth=1)
    ax.scatter(group2Data.US_Time, group2Data.SS_Time, label='Ultrasound First')
    ax.scatter(group1Data.US_Time, group1Data.SS_Time, label='SmartScan First')
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(bounds)
    ax.set_ylim(bounds)

    plt.title('Time Spent in Seconds')
    plt.xlabel('Ultrasound')
    plt.ylabel('SmartScan')
    plt.legend()
    plt.savefig('time_spent.eps', bbox_inches='tight', format='eps', dpi=1000)
    plt.show()


def score(data):
    group1Data = pd.DataFrame(data[data.Group == 1], columns=['SS_Score', 'US_Score'])
    group2Data = pd.DataFrame(data[data.Group == 2], columns=['SS_Score', 'US_Score'])
    bounds = [0, 6]

    fig = plt.figure(200)
    ax = fig.add_subplot(111)
    ax.plot(bounds, bounds, color='k', linestyle='-', linewidth=1)
    ax.scatter(group2Data.US_Score, group2Data.SS_Score, label='Ultrasound First')
    ax.scatter(group1Data.US_Score, group1Data.SS_Score, label='SmartScan First')
    axes = plt.gca()
    axes.set_aspect('equal', adjustable='box')
    axes.set_xlim(bounds)
    axes.set_ylim(bounds)

    plt.title('Average Score')
    plt.xlabel('Ultrasound')
    plt.ylabel('SmartScan')
    plt.legend()
    plt.savefig('score_average.eps', bbox_inches='tight', format='eps', dpi=1000)
    plt.show()

def compareSS(data):
    bounds = [0, 6]
    pos = list(range(1, 13))
    data['ss_err'] = abs(data.SS_Avg_HD - data.SS_Avg_OC) / 2

    fig = plt.figure(300)
    ax = fig.add_subplot(111)

    colors = ['CF', 'C1', 'C0']
    labels = ['CF', 'SmartScan First', 'Ultrasound First']

    groups = data.groupby(data.Group)

    ax.errorbar([p for p in pos], data.SS_Avg, yerr=data.ss_err, capsize=2, ls='none', color='black', elinewidth=1, label='', zorder=-1)
    for x, group in groups:
        name = labels[x]
        color = colors[x]
        ax.scatter(group.Candidate, group.SS_Avg, marker='s', c=color, label=name)
    ax.set_xticks(data.Candidate)
    ax.set_ylim(bounds)

    plt.title('SmartScan Scoring')
    plt.xlabel('Candidate')
    plt.ylabel('Score')

    plt.legend()
    plt.savefig('compare_ss_score_average.eps', bbox_inches='tight', format='eps', dpi=1000)
    plt.show()

def compareBoth(data):
    bounds = [0, 6]
    pos = list(range(1, 13))
    data['us_err'] = abs(data.US_Avg_HD - data.US_Avg_OC) / 2
    data['ss_err'] = abs(data.SS_Avg_HD - data.SS_Avg_OC) / 2

    fig = plt.figure(300)
    ax = fig.add_subplot(111)

    colors = ['CF', 'C1', 'C0']
    labels = ['CF', 'SmartScan First', 'Ultrasound First']

    groups = data.groupby(data.Candidate)

    ax.errorbar([p-0.1 for p in pos], data.US_Avg, yerr=data.us_err, capsize=2, ls='none', color='black', elinewidth=1, label='', zorder=-1)
    ax.errorbar([p+0.1 for p in pos], data.SS_Avg, yerr=data.ss_err, capsize=2, ls='none', color='black', elinewidth=1, label='', zorder=-1)
    for x, group in groups:
        ax.scatter(group.Candidate-0.1, group.US_Avg, marker='s', c='C0', label='')
        ax.scatter(group.Candidate+0.1, group.SS_Avg, marker='s', c='C1', label='')
    ax.set_xticks(data.Candidate)
    ax.set_ylim(bounds)

    plt.title('Scoring')
    plt.xlabel('Candidate')
    plt.ylabel('Score')

    plt.legend()
    plt.savefig('compare_score_averages.eps', bbox_inches='tight', format='eps', dpi=1000)
    plt.show()

def compareUS(data):
    bounds = [0, 6]
    pos = list(range(1, 13))
    data['us_err'] = abs(data.US_Avg_HD - data.US_Avg_OC) / 2

    fig = plt.figure(300)
    ax = fig.add_subplot(111)

    colors = ['CF', 'C1', 'C0']
    labels = ['CF', 'SmartScan First', 'Ultrasound First']

    groups = data.groupby(data.Group)

    ax.errorbar([p for p in pos], data.US_Avg, yerr=data.us_err, capsize=2, ls='none', color='black', elinewidth=1, label='', zorder=-1)
    for x, group in groups:
        name = labels[x]
        color = colors[x]
        ax.scatter(group.Candidate, group.US_Avg, marker='s', c=color, label=name)
    ax.set_xticks(data.Candidate)
    ax.set_ylim(bounds)

    plt.title('Ultrasound Scoring')
    plt.xlabel('Candidate')
    plt.ylabel('Score')

    plt.legend()
    plt.savefig('compare_us_score_average.eps', bbox_inches='tight', format='eps', dpi=1000)
    plt.show()

data = pd.read_csv('/Users/palmerc/Documents/NTNU/SmartScan/Data/SmartScan Score Summary.csv', sep=';', decimal=',')
compareBoth(data)
# compareSS(data)
# compareUS(data)
# time(data)
# score(data)
# sus(data)