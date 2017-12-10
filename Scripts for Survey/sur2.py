#plotting the density of how social people are via two questions

import csv
import matplotlib.pyplot as plt
import numpy as np
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 20}

plt.rc('font', **font)
data=[]

ifile  = open('survey.csv', "r", )
read = csv.reader(ifile)
for row in read :
    data.append(row)

#deleting the questions
del data[0]
    
#scaling 11
for i in range(len(data)):
    if(data[i][11]=="Everyday"):
        data[i][11]=5
    if(data[i][11]=="Two or three times a week"):
        data[i][11]=4
    if(data[i][11]=="Not at all"):
        data[i][11]=0
    if(data[i][11]=="Two, three times a month"):
        data[i][11]=2
    if(data[i][11]=="Once a few months"):
        data[i][11]=1
    if(data[i][11]=="Once a week"):
        data[i][11]=3


#scaling 12
for i in range(len(data)):
    data[i][12]=float(data[i][12])
    

#array and plot for 11/12
a11=[]
a12=[]

for i in range(len(data)):     
    a11.append(data[i][11])
    a12.append(data[i][12])


x = np.array(a11)
y = np.array(a12)

h = plt.hist2d(x, y, bins=(6,7))
plt.xlabel('How often do you interact with someone who is learning the same topics as you are?')
plt.ylabel('How important is social interaction while learning for you?')
plt.title('Socialness')
plt.xticks([0.5,4.5],['never','everyday'])
plt.yticks([1.5,6.5],['not at all','very important'])
plt.colorbar(h[3])
plt.show()