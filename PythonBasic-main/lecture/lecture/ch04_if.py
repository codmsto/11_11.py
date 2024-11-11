# 제어문
#  1. 조건문
#    -if
#  2.반복문
#    -for
#    -while

# 조건문(Condition): if~elif~else
#  - 특정조건을 만족하는 경우 수행할 작업에 사용
#  - 모든 조건은 boolean으로 표현
#  - 조건문의 경우 if,elif,else 블록 내 들여쓰기
#  - 모든 블록문의 시작점은 :(콜론)

# if 조건1:
#     실행문
# elif 조건2:
#     실행문
# elif 조건3:
#     실행문
# else:
#     실행문

# if문 조합식
#  1. if
#  2. if ~ else
#  3. if ~ elif ~ elif
#  4. if ~ elif ~ else

# 2개 이상의 조건을 사용하고 싶은 경우
# -> AND, OR, NOT
#  1. AND : 두 조건이 모두 참인 경우만 참
#  2. OR : 한 조건이라도 참이면 참
#  3. NOT : 참 -> 거짓, 거짓 -> 참

# 예제) 사용자로부터 출생년도를 입력받고
#       성인, 대, 고, 중, 초, 어린이로 분류하는 코드 작성하세요.

from datetime import datetime
now = datetime.today().year

# input(): 키보드로부터 값을 입력 받음
#  - 문자열 타입(str)
born = input("출생년도: ")
print(born)
if born > now:
    print(f"{now}보다 작은 출생년도를 입력해주세요.")
    # 다시 출생년도 입력받기
    

# print(type(now))
# print(type(born))

age = now - int(born)
print(age)

# 27이상 성인
# 20 ~ 26 대학생
# 17 ~ 19 고등학생
# 14 ~ 16 중학생
# 8 ~ 13 초등학생
# ~7 어린이

if age >= 27:
    category = "성인"
elif age >= 20:
    category = "대학생"
elif age >= 17:
    category = "고등학생"
elif age >= 14:
    category = "중학생"
elif age >= 8:
    category = "초등학생"
elif age >= 0:
    category = "어린이"
else:
    print("잘못 입력하셨습니다.")
print(f"출생년도는 {born},나이는 {age}로 당신은 {category}입니다.")
  