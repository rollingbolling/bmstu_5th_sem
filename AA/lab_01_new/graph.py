import matplotlib.pyplot as plt
import csv

def create_graph(algo_1, algo_2, algo_3, algo_4, seconds, length):
    fig, ax = plt.subplots()
    if algo_1 != None:
        ax.plot(seconds, algo_1[:length], label="Левенштейн итеративный", marker='', ls='-.')
    if algo_2 != None:
        ax.plot(seconds, algo_2[:length], label="Левенштейн рекурсивный", marker='', ls='--')
    if algo_3 != None:
        ax.plot(seconds, algo_3[:length], label="Левенштейн рекурсивный с кэшем", marker='', ls=':')
    if algo_4 != None:
        ax.plot(seconds, algo_4[:length], label="Дамерау-Левенштейн рекурсивный", marker='', ls='--')

    ax.legend()
    ax.grid()

    plt.show()

Sec1 = [float(i) for i in range(0, 13)]
Sec2 = [float(i) % 1000 for i in range(1000-1)]
NoRec = []
Rec = []
RecCash = []
DamRec = []

with open('measure.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=' ')
    
    for ROWS in plotting:
        NoRec.append(float(ROWS[0]))
        Rec.append(float(ROWS[1]))
        RecCash.append(float(ROWS[2]))
        DamRec.append(float(ROWS[3]))

create_graph(NoRec, Rec, RecCash, DamRec, Sec1, 13)

create_graph(NoRec, None, RecCash, None, Sec2, 1000)