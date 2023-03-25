
# import matplotlib.pyplot as plt
# x=[]
# y=[]
# y2=[]
# for i in range(-10,11):
#     x.append(i)
#     y.append(-i**2)
#     y2.append(i**2)
# print(x)
# print(y)
# plt.figure()
# plt.plot(x,y,x,y2)
# plt.show()



# import matplotlib.pyplot as plt
# x=[]
# y1=[]
# y2=[]
# y3=[]
# y4=[]
# for i in range(-5,6):
#     x.append(i)
#     y1.append(5)
#     y2.append(-5)
#     y3.append(i*5+10)
#     y4.append(-i*5+1+10)
# print(x)
# print(y1)
# plt.figure()
# plt.plot(x,y1,x,y2,x,y3,x,y4)
# plt.show()


import matplotlib.pyplot as plt
subjects=["UZB","KZ","KGY"]
score=[60,90,70]
figure,axes=plt.subplots(2,2)
x=[]
y=[]
y2=[]
y3=[]
bar_color=["black"]
barh_color=["green"]
barhh_color=["red","blue","green"]
barr_color=["chocolate","darkblue","snow"]
for i in range(-10,11):
    x.append(i)
    y.append(i**2)
    y2.append(-i**2)
    y3.append(i**3)

axes[0,0].plot(x,y,'go',x,y2,'ro')
axes[0,1].bar(subjects,score,color=barhh_color)
axes[1,0].barh(subjects,score,color=barr_color)
axes[1,1].plot(x,y3)






plt.show()























