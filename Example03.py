#불(불린) 대수의 진리값: True, False밖에 없음 / and 연산: 둘 다 true여야 함, or연산: 둘 중 하나만 true여도 괜찮 / not연산: 반대로 뒤집어줌. t는 f로, f는 t로
#불린은 따옴표 없이 씀
print(True and True)
print(False and False)
print(True or False) #False or False만 False로 출력, 나머지는 다 True
print(not True) #not True: False, not False: True
# ==는 같다, !는 not을 의미(~하지 않다)
print(3 >= 3)
print(2 == 2)
print(2 != 2)
print(2>1 and "Hello" == "Hello")

#type: 무슨 형(정수형, 소수형, 문자형)인지 알아볼 수 있게 하는 함수
print(type(3)) #class 'int'
print(type(3.0)) #class 'float'
print(type("3")) #class 'str'

def hello():
    print("Hello world!")

print(type(hello)) #class 'function'
print(type(print)) #class 'builtin_function_or_method'

#지정연산자 = 오른쪽에 있는 값을 왼쪽 변수에 넣으라는 의미(결론: x의 값을 1늘려준 것)
x = 7
x = 7 + 1

#return문 효과 하나 더: 함수 즉시 종료: return 뒤에 뭔가를 더 쓰는 건 의미없는일
def square(x):
    print("함수 시작")
    return x * x

print(square(3))
print("Hello World!")

# 다음 두 줄은 같습니다(x +=1의 경우에 x가 1만큼 더해진다)
x = x + 1
x += 1

# 다음 두 줄은 같습니다
x = x + 2
x += 2

# 다음 두 줄은 같습니다
x = x * 2
x *= 2

# 다음 두 줄은 같습니다
x = x - 3
x -= 3

# 다음 두 줄은 같습니다
x = x / 2
x /= 2

# 다음 두 줄은 같습니다
x = x % 7
x %= 7