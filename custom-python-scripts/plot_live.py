import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import math
import yaml
import csv

with open('dict.txt','r') as f:
    dict1=f.read()

dict = yaml.load(dict1)

with open('gait.txt','w+') as j:
    j.write('')
with open('gait1.txt','w+') as j:
    j.write('')
with open('gait2.txt','w+') as j:
    j.write('')

def total_theta(oblu, number):
    theta = 0
    for i in range (number):
        theta += dict[i][oblu-1][3]
    return theta

def totalof(oblu, whose, number):
    v = 0
    if whose==0:
        for i in range (1,number+1):
            v += dict[i][oblu-1][4]*math.sin(total_theta(oblu, i))
            print 'ss'
    else:
        for i in range (1,number+1):
            v += dict[i][oblu-1][4]*math.cos(total_theta(oblu, i))
    return v

for counter in range (8):
    with open('gait.txt','a+') as j:
        a=(dict[counter][1][0] + dict[counter][0][0])/2.0
        b=(dict[counter][1][1] + dict[counter][0][1])/2.0
        j.write(str(a)+','+str(b)+'\n')

for counter in range (8):
    with open('gait1.txt','a+') as j:
        a=dict[counter][1][0]
        b=dict[counter][1][1]
        j.write(str(a)+','+str(b)+'\n')

for counter in range (8):
    with open('gait2.txt','a+') as j:
        a=dict[counter][0][0]
        b=dict[counter][0][1]
        j.write(str(a)+','+str(b)+'\n')

# # for counter in range (8):
# #     with open('gait.txt','a+') as j:
# #         a=(dict[counter][0][0] + dict[counter][0][0])/2.0
# #         b=(dict[counter][0][1] + dict[counter][0][1])/2.0
# #         j.write(str(a)+','+str(b)+'\n')

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)

# def animate(i):
#     pullData = open("gait.txt","r").read()
#     dataArray = pullData.split('\n')
#     xar = []
#     yar = []
#     for eachLine in dataArray:
#         if len(eachLine)>1:
#             x,y = eachLine.split(',')
#             xar.append(float(x))
#             yar.append(float(y))
#     ax1.clear()
#     ax1.plot(xar,yar,'r')

# def animate1(i):
#     pullData = open("gait.txt","r").read()
#     dataArray = pullData.split('\n')
#     xar = []
#     yar = []
#     for eachLine in dataArray:
#         if len(eachLine)>1:
#             x,y = eachLine.split(',')
#             xar.append(float(x))
#             yar.append(float(y))
#     ax1.clear()
#     ax1.plot(yar,xar,'b')

# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.hold(True)
# ani2 = animation.FuncAnimation(fig, animate1, interval=1000)
# plt.show()






x = []
y = []

with open('gait.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x,y, label='dual mounted config',color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.hold(True)

plt.plot(x,y, label='dual mounted config',color='b')
plt.show()