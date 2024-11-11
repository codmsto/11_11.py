# 주차 타워(엘리베이터)
#  - 5층으로 제한
#  - 1층마다 차량 1대만 입고
#  - 차량번호는 숫자 4자리 ex) 1528

# 기능
#   1. 차량입고
#   2. 차량 출고
#   3. 차량 조회
#   4. 종료

# 1. 공통 설정
max_car = 5  # 최대 주차 차량수
cnt_car = 0  # 현재 주차되어 있는 차량 수 (count)

# 2. 주차 타워 생성 -> list[] -> "" 빈칸
#tower = ["","","","",""]  # 방법1. 하드코딩(절대 지양)
# 방법2. for 문 활용
#tower = []
#for i in range(max_car):
#    tower.append("")
    

# 방법3: 리스트 컴프리헨슨
# - 모든 for 문을 리스트 컴프리헨슨 변경 불가(심플만 가능)
tower = ["" for i in range(max_car)]


# 3. 메뉴 출력
print("=" * 50)
print("== 주차 타워 시스템 ver 1.0 ==")
print("=" * 50)
print("= 1. 차량 입고")
print("= 2. 차량 출고")
print("= 3. 차량 조회")
print("= 4. 종료")
print("=" * 50)


# 4. 메뉴 선택
# 사용자는 1~4번까지 입력받는 코드 작성
# 사용자가 입력한 값은 select_num 변수에 저장
# 사용자가 1~4 이외의 값을 넣으면 경고메세지 출력 후 다시 입력받기
while True:
    select_num = int(input(">> 번호:"))
    if 4 >= select_num >= 1:
        break
    else:
        print("올바른 값을 입력하세요.")



# 5. 메뉴 서비스
# select_num이 1,2,3,4인 경우
if select_num == 1:
    # 도메인 지식 -> 비즈니스 로직
    # 1. 주차공간 유무 확인
    #   y: 다음 스텝
    #   n: "만차입니다."
    if max_car > cnt_car:
        pass
    # 2. 차량번호 입력
    #   + 유효성체크(숫자, 4자리수) -> 정규식(re)
    num_car = input(">> 차량번호: ") 
    # 3. 주차타워 입고(tower[]에 저장)
    #   + 주차타워 비어있는 공간 서치
    #   + 비어있는 공간에 값 저장  
    # 4. 현재 주차수 최신화 -> cnt_car + 1
    for i in range(max_car):
        if tower[i] == "":     
            tower[i] = num_car
            cnt_car += 1
            break
    else:
    
        print("만차입니다.")
    

      
    
elif select_num ==2:  # 숙제
    # 1. 출고 차량 번호 입력 ex) 5789
    # > cnt_car == 0 -> "현재 주차된 차량이 없습니다."
    # 2. 입력한 번호로 주차타워 검색
    #    y: 다음 스텝
    #    n: "주차되지 않은 차량번호입니다."
    # 3. 차량 출고 -> tower[] -> ""
    # 4. 현재주차수 -1
elif select_num ==3:
    # range(시작,끝,인터벌) -> range(0, 5, 1) = 0,1,2,3,4
    #                      -> range(4,-1,-1) = 4,3,2,1,0
    for i in range(max_car-1, -1, -1):
        print(f"{i+1}층: {tower[i]}")
elif select_num ==4:
    print("프로그램을 종료합니다.")
    exit()

    

# 21일 4시에 시험
#여기랑 20명넘으면 옆반에서 
#시험문제 15문제
# 하나 안에 자투리있는 문제 있을수도
#이론 + 코드(손코딩은 아니고 구구단짜세요 이런거 아니고 오류났을때 해결 , 빈칸에 출력 나올라면 뭐 들어감 이런거 )

