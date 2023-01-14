'''
조건문2(while)

반복할 떄 사용

<문법>
while 조건:
    실행할 코드 작성

특징

1.조건이 참이면 코드가 실행
2.조건이 거짓이면 while이 종료

예제

a=0

while a<3:
    print("안녕")

다음과 같이 적을 시 안녕이 무한으로 나옴.


while True:
    print("안녕")

이렇게 해도 다음과 똑같이 나옴.

'''




'''
a=0

while True:
    print("안녕")
    a+=1
    '''


#1
a=1
while a<11:
        print(a)
        a+=1

#2

a=1

while a<11:
    if a%2==0:
        print(a)
    a+=1

#3

a=1
sum=0
while a<21:
    if a%4!=0:
        sum+=a    
    a+=1
print(sum)
        
#4        

a=50

while a<101:
    if a%2==0:
        if a%3==0:
            print(a)
    a+=1

#5

a=1

Mul=1

Sum=0

while a<11:
    if a%3==0:
        Mul*=a

    if a%2==0:
        Sum+=a
    a+=1
print(Mul-Sum)
    