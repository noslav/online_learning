#how the occupation affects socialness, learning online, paying for courses, coworking

import csv
import matplotlib.pyplot as plt
import numpy as np

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 13}

plt.rc('font', **font)
data=[]

ifile  = open('survey.csv', "r", )
read = csv.reader(ifile)
for row in read :
    data.append(row)

#deleting the questions
del data[0]

#scaling 13
for i in range(len(data)):
    if(data[i][13]=="Everyday"):
        data[i][13]=5
    if(data[i][13]=="Two or three times a week"):
        data[i][13]=4
    if(data[i][13]=="Not at all"):
        data[i][13]=0
    if(data[i][13]=="Two, three times a month"):
        data[i][13]=2
    if(data[i][13]=="Once a few months"):
        data[i][13]=1
    if(data[i][13]=="Once a week"):
        data[i][13]=3


#scaling 12
for i in range(len(data)):
    data[i][12]=float(data[i][12])
    
#scale 16
for i in range(len(data)):
    if(data[i][16]=="Yes"):
        data[i][16]=1
    else:
        data[i][16]=0
#scale 19
for i in range(len(data)):
    if(data[i][19]=="Yes"):
        data[i][19]=1
    else:
        data[i][19]=0
#scale 8
for i in range(len(data)):
    if(data[i][8]=="Yes"):
        data[i][8]=1
    else:
        data[i][8]=0
    

block = [[[] for x in range(5)] for x in range(15)]

for i in range(len(data)):
    if(data[i][6]=="Consulting"):
        block[0][0].append(float(data[i][13])* float(data[i][14]))
        block[0][1].append(data[i][16])
        block[0][2].append(data[i][19])
        block[0][3].append(1)  
        block[0][4].append(data[i][8])
    if(data[i][6]=="Education"):
        block[1][0].append(float(data[i][13])* float(data[i][14]))
        block[1][1].append(data[i][16])
        block[1][2].append(data[i][19])
        block[1][3].append(1)      
        block[1][4].append(data[i][8])
    if(data[i][6]=="Entrepreneurship"):
        block[2][0].append(float(data[i][13])* float(data[i][14]))
        block[2][1].append(data[i][16])
        block[2][2].append(data[i][19])
        block[2][3].append(1)
        block[2][4].append(data[i][8])
    if(data[i][6]=="Management"):
        block[3][0].append(float(data[i][13])* float(data[i][14]))
        block[3][1].append(data[i][16])
        block[3][2].append(data[i][19])
        block[3][3].append(1)
        block[3][4].append(data[i][8])
    if(data[i][6]=="Law"):
        block[4][0].append(float(data[i][13])* float(data[i][14]))
        block[4][1].append(data[i][16])
        block[4][2].append(data[i][19])
        block[4][3].append(1)
        block[4][4].append(data[i][8])
    if(data[i][6]=="Software Development"):
        block[5][0].append(float(data[i][13])* float(data[i][14]))
        block[5][1].append(data[i][16])
        block[5][2].append(data[i][19])
        block[5][3].append(1)
        block[5][4].append(data[i][8])
    if(data[i][6]=="Marketing & PR"):
        block[6][0].append(float(data[i][13])* float(data[i][14]))
        block[6][1].append(data[i][16])
        block[6][2].append(data[i][19])
        block[6][3].append(1)
        block[6][4].append(data[i][8])
    if(data[i][6]=="Design"):
        block[7][0].append(float(data[i][13])* float(data[i][14]))
        block[7][1].append(data[i][16])
        block[7][2].append(data[i][19])
        block[7][3].append(1)
        block[7][4].append(data[i][8])
    if(data[i][6]=="Sales"):
        block[8][0].append(float(data[i][13])* float(data[i][14]))
        block[8][1].append(data[i][16])
        block[8][2].append(data[i][19])
        block[8][3].append(1)
        block[8][4].append(data[i][8])
    if(data[i][6]=="Lifestyle"):
        block[9][0].append(float(data[i][13])* float(data[i][14]))
        block[9][1].append(data[i][16])
        block[9][2].append(data[i][19])
        block[9][3].append(1)
        block[9][4].append(data[i][8])
    if(data[i][6]=="Music"):
        block[10][0].append(float(data[i][13])* float(data[i][14]))
        block[10][1].append(data[i][16])
        block[10][2].append(data[i][19])
        block[10][3].append(1)
        block[10][4].append(data[i][8])
    if(data[i][6]=="Healthcare"):
        block[11][0].append(float(data[i][13])* float(data[i][14]))
        block[11][1].append(data[i][16])
        block[11][2].append(data[i][19])
        block[11][3].append(1)
        block[11][4].append(data[i][8])
    if(data[i][6]=="Finance"):
        block[12][0].append(float(data[i][13])* float(data[i][14]))
        block[12][1].append(data[i][16])
        block[12][2].append(data[i][19])
        block[12][3].append(1)
        block[12][4].append(data[i][8])
    if(data[i][6]!="Finance" and data[i][6]!="Healthcare" and data[i][6]!="Music" and data[i][6]!="Lifestyle" and data[i][6]!="Sales" and data[i][6]!="Design" and data[i][6]!="Marketing & PR" and data[i][6]!="Software Development" and data[i][6]!="Law" and data[i][6]!="Management" and data[i][6]!="Education" and data[i][6]!="Entrepreneurship" and data[i][6]!="Consulting"):
        block[13][0].append(float(data[i][13])* float(data[i][14]))
        block[13][1].append(data[i][16])
        block[13][2].append(data[i][19])
        block[13][3].append(1)
        block[13][4].append(data[i][8])

signi=[]
social=[]
online=[]
pay=[]
cowork=[]

for i in range(len(block)):
    for j in [0,1,2,4]:
        block[i][j]=np.average(block[i][j])
        
    block[i][0]=block[i][0]/(35)
    block[i][3]=np.sum(block[i][3])/48
    signi.append(block[i][3])
    social.append(block[i][0])
    online.append(block[i][1])
    pay.append(block[i][2])
    cowork.append(block[i][4])


fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(131)

xsize = 14
ysize= 5

Z=np.array([signi,social,online,pay,cowork])

im = ax.imshow(Z,origin='lower',extent=[0, xsize, 0, ysize],vmax=abs(Z).max(),vmin=0)

x = np.arange(0,xsize)+0.5
y = np.arange(0,ysize)+0.5


xlabels = ['Consulting','Education','Entrepreneurship','Management','Law','Software Development','Marketing and HR','Design','Sales','Lifestyle','Music','Healthcare','Finance','Other']
ylabels=['relative Significance','Socialness','learning online','payed for course','coworking']
plt.xticks(x, xlabels,rotation='vertical')
plt.yticks(y, ylabels,rotation='horizontal')

data = np.arange(xsize * ysize).reshape((xsize, ysize))

x_start = 0
x_end = xsize
y_start = 0
y_end = ysize

extent = [x_start, x_end, y_start, y_end]

jump_x = (x_end - x_start) / (2.0 * xsize)
jump_y = (y_end - y_start) / (2.0 * ysize)
x_positions = np.linspace(start=x_start, stop=x_end, num=xsize, endpoint=False)
y_positions = np.linspace(start=y_start, stop=y_end, num=ysize, endpoint=False)

for y_index, y in enumerate(y_positions):
    for x_index, x in enumerate(x_positions):
        label = round(Z[y_index, x_index],3)
        text_x = x + jump_x
        text_y = y + jump_y
        ax.text(text_x, text_y, label, color='black', ha='center', va='center')
plt.show()
