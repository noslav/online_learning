#age for socials

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
    

#scaling 2
for i in range(len(data)):
    if(data[i][2]=="24 - 30"):
        data[i][2]=24
    if(data[i][2]=="18 - 23"):
        data[i][2]=18
    if(data[i][2]=="31 - 40"):
        data[i][2]=31
    if(data[i][2]=="40 - 60"):
        data[i][2]=40
    if(data[i][2]=="Under 18"):
        data[i][2]=16


#histo of 2
a2ur=[]
a2el=[]
   
for i in range(len(data)):
    if(data[i][11]>3 and data[i][12]>4):
        a2ur.append(data[i][2])      
    if(data[i][11]<=3 or data[i][12]<=4):
        a2el.append(data[i][2])  

x=np.array(a2ur)
n, bins, patches = plt.hist(x,50, facecolor='green', alpha=0.75)

plt.xlabel('How old are you?')
plt.ylabel('Probability')
plt.title('Social')

plt.show()
plt.figure()
x=np.array(a2el)
n, bins, patches = plt.hist(x, 50,facecolor='green', alpha=0.75)

plt.xlabel('How old are you?')
plt.ylabel('Probability')
plt.title('Not Social')

plt.show()





