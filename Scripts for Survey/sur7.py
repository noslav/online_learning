#General Results
#15Have you used any of the following platforms? Please select all that apply.
#18What are you biggest problems learning online? (Choose at max 3)
#9What describes best your motivation to learn? (Choose at max 3)
#13How do you learn? (Select at max 3)

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
s=" "

plat=[]
for i in range(len(data)):
    plat.append(data[i][15])


plat2=(s.join(plat)) 

how=[]

for i in range(len(data)):
    how.append(data[i][13])

how2=(s.join(how)) 


mot=[]

for i in range(len(data)):
    mot.append(data[i][9])


mot2=(s.join(mot))

prob=[]

for i in range(len(data)):
    prob.append(data[i][18])


prob2=(s.join(prob))

plat=["Youtube","Duolingo","Khan Academy","Kaggle","University","Coursera","Codecademy","Babbel","Google","Udemy","FutureLearn"]
platc=[0] *len(plat)

how=["Online","Youtube","University","Reading articles","Learning groups","Reading code","Reading books","Asking people","Wikipedia","Live Courses","Googling"]
howc=[0] *len(how)

mot=["Career Development","Friends & colleagues","Career Change","Help others","Personal Development","Trending topics & tech","Personal Curiosity","Role Model","Social Pressure"]
motc=[0] *len(mot)

prob=["Social","Too hard","No community","Too Easy","Lack of resources","Iteractivity","One-on-One Feedback","Cost","Lack of time","Support","Motivation","Missing Information",]
probc=[0] *len(prob)

for i,n,m in zip([plat,how,mot,prob],[plat2,how2,mot2,prob2],[platc,howc,motc,probc]):
    for j in range(len(i)):
        m[j]=n.count(i[j])

for i,n,m in zip([plat,how,mot,prob],[platc,howc,motc,probc],["Plattform",'How do you learn?','Motivation','Problems']): 
    y=n[:]
    x=np.arange(0,len(n))
    plt.figure(m)
    plt.title(m)
    plt.bar(x,y)
    plt.xticks(x,i,rotation='vertical')
    plt.show()



