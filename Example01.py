print(6 // 4)
print(round(3.1415926535, 2))
print("hello" * 3)
print("Hello" + "world")
print("3"+"5")
print("I'm excited to learn Python!")
print("건이는 말했다. \"현주야 밥 먹었어?\"")

#형 변환
#int: 소수형을 정수형으로 변환
print(int(3.8))
#float: 정수형을 소수형으로 변환
print(float(3))
#int:문자형을 숫자형으로 변환(int는 정수형이라는 뜻이라서 숫자라는 뜻도 있음)
print(int("2")+int("5"))
#str(string):숫자형을 문자형으로 전환
print(str(2) + str(5))
# %는 나머지를 구하는 것
print(4 % 2)
# //는 버림 나눗셈(몫이 소수형으로 나왔을 때 소숫점 아래를 버림)

age = 7
print("제 나이는" + str(age) + "살입니다")
#str을 쓰지 않았을 경우 문자형+숫자형+문자형이기 때문에 이어질 수 없음

year = 2023
month = 4
day = 4

#문자열 포맷팅 .format() : 형태를 잡아주는 것
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))
print(date_string.format(year, month, day+1))