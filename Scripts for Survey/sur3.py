#how long those socials and antisocials learn online

import csv
import matplotlib.pyplot as plt
import numpy as np

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

#scaling 21
for i in range(len(data)):
    if(data[i][21]=="Everyday"):
        data[i][21]=5
    if(data[i][21]=="Two or three times a week"):
        data[i][21]=4
    if(data[i][21]=="Not at all"):
        data[i][21]=0
    if(data[i][21]=="Two, three times a month"):
        data[i][21]=2
    if(data[i][21]=="Once a few months"):
        data[i][21]=1
    if(data[i][21]=="Once a week"):
        data[i][21]=3
    if(data[i][21]==""):
        data[i][21]=0

#histo of 21
a21ur=[]
a21el=[]
   
for i in range(len(data)):
    if(data[i][11]>3 and data[i][12]>4):
        a21ur.append(data[i][21])      
    if(data[i][11]<=3 or data[i][12]<=4):
        a21el.append(data[i][21])   

x=np.array(a21ur)
n, bins, patches = plt.hist(x,50, facecolor='green', alpha=0.75,label='social')

plt.xlabel('How often do you learn online')
plt.ylabel('Probability')
plt.xticks([0.5,4.5],['never','everyday'])
plt.legend()
plt.title('social')

plt.show()

x=np.array(a21el)
n, bins, patches = plt.hist(x+0.1, 50, facecolor='red', alpha=0.75,label='asocial')

plt.xlabel('How often do you learn online')
plt.ylabel('Probability')
plt.xticks([0.5,4.5],['never','everyday'])
plt.title('')
plt.legend()

plt.show()

for i in range(len(a21ur)):
    a21ur[i]=a21ur[i]/5
for i in range(len(a21el)):
    a21el[i]=a21el[i]/5



