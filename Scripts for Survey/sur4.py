#yes no questions for socials and antisocials

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
        data[i][11]=24
    if(data[i][11]=="18 - 23"):
        data[i][11]=18
    if(data[i][11]=="31 - 40"):
        data[i][11]=31
    if(data[i][11]=="40 - 60"):
        data[i][11]=40
    if(data[i][11]=="Under 18"):
        data[i][11]=16

#for social
counter=0
paidforcourse=0
coworking=0
learnedon=0

for i in range(len(data)):
    if(data[i][11]>3 and data[i][12]>4):
        counter=counter+1
        if(data[i][17]=="Yes"):
            paidforcourse=paidforcourse+1
        if(data[i][7]=="Yes"):       
            coworking=coworking+1
        if(data[i][14]=="Yes"):        
            learnedon=learnedon+1
            
print(paidforcourse/counter)
print(coworking/counter)
print(learnedon/counter)

#for antisocial
counter=0
paidforcourse=0
coworking=0
learnedon=0
for i in range(len(data)):
    if(data[i][11]<=3 or data[i][12]<=4):
        counter=counter+1
        if(data[i][17]=="Yes"):
            paidforcourse=paidforcourse+1
        if(data[i][7]=="Yes"):       
            coworking=coworking+1
        if(data[i][14]=="Yes"):        
            learnedon=learnedon+1

print(paidforcourse/counter)
print(coworking/counter)
print(learnedon/counter)








