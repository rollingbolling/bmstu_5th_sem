import matplotlib.pyplot as plt
import csv

def create_graph(algo_1, algo_2, algo_3, algo_4, seconds, length):
    fig, ax = plt.subplots()
    if algo_1 != None:
        ax.plot(seconds, algo_1[:length], label="Левенштейн не рекурсивный", marker='.', ls='-.')
    if algo_2 != None:
        ax.plot(seconds, algo_2[:length], label="Левенштейн рекурсивный", marker='v', ls='--')
    if algo_3 != None:
        ax.plot(seconds, algo_3[:length], label="Левенштейн рекурсивный с мемоизацией", marker='o', ls=':')
    if algo_4 != None:
        ax.plot(seconds, algo_4[:length], label="Дамерау-Левенштейн не рекурсивный", marker='p', ls='-')
    ax.set_ylabel("Время выполнения (секунды)")
    ax.set_xlabel("Длина строки")
    ax.legend()
    ax.grid()

    plt.show()

NoRec = []
Rec = []
RecCash = []
DamNoRec = []

with open('measure.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=';')
    
    for ROWS in plotting:
        NoRec.append(float(ROWS[1]))
        Rec.append(float(ROWS[2]))
        RecCash.append(float(ROWS[3]))
        DamNoRec.append(float(ROWS[4]))

Sec1 = [i for i in range(1, len(NoRec) + 1)]
create_graph(NoRec, Rec, RecCash, DamNoRec, Sec1, len(Sec1))

NoRec = []
Rec = []
RecCash = []
DamNoRec = []

with open('measure_long.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=';')
    
    for ROWS in plotting:
        NoRec.append(float(ROWS[1]))
        Rec.append(float(ROWS[2]))
        RecCash.append(float(ROWS[3]))
        DamNoRec.append(float(ROWS[4]))

Sec2 = [i * 25 for i in range(1, len(NoRec) + 1)]
create_graph(NoRec, None, RecCash, DamNoRec, Sec2, len(Sec2))