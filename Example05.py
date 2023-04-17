# while 반복문: 컴퓨터에게 귀찮은 거 시키기
# while 반복문의 형태(~할 동안에라는 뜻을 가지고 있음):
# while 조건 부분(불린 값:false가 나오면 멈춤):(들여쓰기 후) 수행 부분(반복적으로 실행하고 싶은 명령)

i = 1
while i<=3: #불린값이 true일때 print가 됨 / 불린값이 false일때 print 멈춤 #3이 아니라 100이라면 100번 출력되는 것 /i의 값이 1에서 2, 2에서 3...으로 수정되는 것이 포인트    
    print("나는 잘생겼다!")
    i += 1
    
#while 함수 예제: 100 이상인 수 중에 23의 배수인 가장 작은 수
i = 100
while i % 23 != 0:
    i += 1
print (i)

#if 함수 (만약: if, 그렇지 않으면: else / 불린 값이 true면 수행 부분이 실행, false면 else의 수행 부분이 실행)
#if 조건 부분(불린 값):(들여쓰기 후) 수행 부분 / else문은 if문 아래에 불린값이 false인 경우 어떻게 할지 쓰는 것

temperature = 16
if temperature <= 10:
    print("자켓을 입는다.")
else:
    print("자켓을 입지 않는다")
    
#elif 문: if문과 else문에서 경우의 수가 너무 많을 경우 else: if 점수가 80점 이상이다: B를 준다 >> elif 점수가 80점 이상이다: B를 준다(else 밑으로 엔터가 없음)
 