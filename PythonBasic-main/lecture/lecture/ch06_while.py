# While
#  - 조건이 참인 경우 반복 실행
#  - 조건이 거짓인 경우 반복 중단
#  - 조건이 True(boolean) -> 무한 반복
#    (break문과 함께 사용) 

# for, while에서 사용할 수 있는 키워드
#  1. break:    즉시 반복문 종료
#  2. continue: 즉시 다음 반복으로 넘어가기

# while 조건:
#    실행문

while True:
    print("test")
    if True:
        break
    
print("Hello")

# 숙제: for문으로 작성한 구구단 2단을 while문으로 작성해보세요.
for i in range(1, 10):
    print(f"2x{i}={2*i}")
    