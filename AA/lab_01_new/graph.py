import matplotlib.pyplot as plt
import csv

X = []
Y = []

with open('measure.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=' ')
    
    for ROWS in plotting:
        X.append(float(ROWS[3]))
        #X.append('{} {}'.format(ROWS[3], ROWS[4]))
        Y.append(float(ROWS[1]))

print ('X {} Nums'.format(len(X)))
print ('Y {} Nums'.format(len(Y)))

# threshold=63.0
# T=[threshold]*len(Y)

print ('Type X {} '.format(type(X)))
print ('Type Y {} '.format(type(Y)))
print ('Type T {} '.format(type(T)))

plt.plot(X, Y)
plt.plot(X, T)
plt.title('Illumination change')
plt.xlabel('Time,[s]')
plt.ylabel('Light level, [Lx]')
plt.grid()
# plt.xticks(rotation=-90)
plt.legend(['illumination', 'threshold {} Lx'.format(threshold)])
plt.show()