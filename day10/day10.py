'''
딕셔너리(dictionary)

-python에서 사용하는 자료구조 중 하나
-key와 value의 쌍으로 이루어져 있다.
-중괄호와 :를 이용해 작성
ex){"손흥민":"축구","류현진":"야구"}

-indexing 가능(key를 이용),(get method 이용해도 됨)
indexing을 이용한 추가 또는 update method를 이용해 value를 바꿀 수 있음,value 쌍을 추가할 수 있다.

-"key in dictionary" 질문에 T/F로 확인 가능하다는 정보를 우리는 얻어낼 수 있다.

리스트=[177,200,,125,101]

ыфваыоваовыоычдяюязййщзуцзхывдысвьыьлфдавллылысьывлысвддыфршысьйхвыддль
ييبسسسسسسسبمممممممممخخخعثصةيةصءءمحص

'''


height={"용규":177,"자민":200,"재민":125,"준영":101}
print(type(height))

튜플=(177,200,125,101)
리스트=[177,200,125,101]


print(리스트[1])
print(튜플[1])
print(height["자민"])
print('jamin say,"what?"')
리스트.pop
print(height.keys())
print(height.values())
print(height["준영"])
print(height.get("준영"))
리스트[1]=150
print(리스트)
height["자민"]=150
print(height)
height.update({"자민":149.9})
print(height)
2
height["선생님"]=180
print(height)

height.update({"손흥민":185})
print(height)

del height["선생님"]
del height["손흥민"]
print(height)

print("용규" in height)

print("손흥민" in height)

for i in range(10):

    fruits={"orange":30,"banana":40,"apple":20}
fruit=input("THis is fruit store. what do you want?:")
if fruit in fruits:
    print(f"we have{fruit},{fruits[fruit]}left")
else:
    print(f"sorry,we don't have {fruit}")






