## 코드 스타일가이드 비교(before)
print(6.28*4)
print(3.14*4*4)
print(6.28*8)
print(3.14*8*8)

## 코드 스타일가이드 비교(after)
PI = 3.14 #원주율(파이) ## 상수 지정

#반지름이 r인 원의 둘레 계산
def calculate_circumference(r): ##함수가 무슨 의미인지 알 수 있음, 수식이었을 때는 의미없던 것을 의미있게, 알아들을 수 있게 디자인할 수 있음
    return 2 * PI * r

# 반지름이 r인 원의 넓이 계산
def calculate_area(r):
    return PI * r * r

radius = 4 #반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

radius = 8 #반지름
print(calculate_circumference(radius))
print(calculate_area(radius))