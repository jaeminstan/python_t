'''

모듈(module)설치
pip install 모듈이름
matplotlib

2.모듈 가져오기
import 모듈이름 as 단축어

3.모둘 사용하기
모듈이름.변수
모듈이름.함수()

as plt

'''
'''
import matplotlib.pyplot as plt
plt.figure()

plt.plot([50,40,60],[150,120,170],'go')

plt.ylabel("height")
plt.xlabel("weight")
plt.show()
'''


'''
import matplotlib.pyplot as plt
plt.figure()

plt.plot([0,1,2,3,4,5],[5,8,11,14,17,20],'r')

plt.ylabel("y")
plt.xlabel("x")
plt.show()
'''



'''
import matplotlib.pyplot as plt

xvalues=[0,1,2,3,4,5]
yvalues=[5,8,11,14,17,20]

plt.figure()

plt.plot(xvalues,yvalues,'go')

plt.ylabel("height")
plt.xlabel("weight")
plt.show()
'''

'''
import matplotlib.pyplot as plt

xvalues=[]
yvalues=[]
for i in range(-100,100):
    xvalues.append(i)
    yvalues.append(i**5)


plt.figure()

plt.plot(xvalues,yvalues,'g')

plt.ylabel("y")
plt.xlabel("x")
plt.show()

'''
import matplotlib.pyplot as plt

xvalues=[]
yvalues1=[]
yvalues2=[]
yvalues3=[]
for i in range(-10,10):
    xvalues.append(i)
yvalues1.append(i)
yvalues2.append(i*i)
yvalues3.append(i*i*i)

plt.figure()

plt.plot(xvalues,yvalues1,'r',xvalues,yvalues2,'g',xvalues,yvalues3,'b')

plt.ylabel("y")
plt.xlabel("x")
plt.show()

