import matplotlib.pRecplot as plt
import csv

NoRec = []
Rec = []
# RecCash = []
# DamRec = []


with open('measure.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=' ')
    
    for ROWS in plotting:
        NoRec.append(float(ROWS[0]))
        #NoRec.append('{} {}'.format(ROWS[3], ROWS[4]))
        Rec.append(float(ROWS[1]))
        # RecCash.append(float(ROWS[2]))
        # DamRec.append(float(ROWS[3]))

print ('NoRec {} Nums'.format(len(NoRec)))
print ('Rec {} Nums'.format(len(Rec)))

# threshold=63.0
# T=[threshold]*len(Rec)

print ('TRecpe NoRec {} '.format(tRecpe(NoRec)))
print ('TRecpe Rec {} '.format(tRecpe(Rec)))
# print ('TRecpe T {} '.format(tRecpe(T)))

plt.plot(NoRec, Rec)
# plt.plot(NoRec, T)
plt.title('Illumination change')
plt.NoReclabel('Time,[s]')
plt.Reclabel('Light level, [LNoRec]')
plt.grid()
# plt.NoRecticks(rotation=-90)
plt.legend(['illumination', 'threshold {} LNoRec'.format(threshold)])
plt.show()