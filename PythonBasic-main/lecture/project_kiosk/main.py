###########################
## Project: 별다방조선
## Writer: Silverbird
## Company: 조선대학교
## Reg_date: 2024.10.14
## Update_date: 2024.10.14
## License:
## Contents: 콘솔 프로그래밍을 활용한 커피 전문점에서 사용하는 키오스크

# 키오스크

# 1. 메인 메뉴 출력(커피, 스무디, 베이커리)
# 2. 메인 메뉴 선택(사용자)
# 3. 서브 메뉴 출력(커피 or 스무디 or 베이커리)
# 4. 서브 메뉴 선택(사용자)
# 5. 고객 주문 메뉴 목록에 저장(선택한 서브 메뉴)
# 6. 추가 주문 여부?(yes or no)
# 7-1. yes: 1번으로 보내기
# 7-2. no: 최종주문 내역으로 보내기
# 8. 최종주문 내역 출력

from service_kiosk import print_menu,select_menu

####################
## 1. 메뉴 만들기 ##
####################
main_menu = {
    1:"커피",
    2:"스무디",
    3:"베이커리"
}

coffee_menu = {
    1:"에스프레소",
    2:"아메리카노"
}
coffee_price = {
    1:3500,
    2:4000
}
smoothie_menu = {
    1:"딸기 스무디",
    2:"오렌지 스무디",
    3:"블루베리 스무디",
    4:"망고 스무디"
}
smoothie_price = {
    1:4000,
    2:3500,
    3:4000,
    4:4500
}
bakery_menu = {
    1:"조각 케이크",
    2:"크로플",
    3:"마카롱"
}
bakery_price = {
    1:7000,
    2:8000,
    3:3000
}

order_list = []  # 고객 주문 기록 #[[메뉴, 가격],[메뉴,가격],[메뉴,가격],...]


while True:
    ## 1. 메인메뉴 출력
    print("★" * 50)
    print("★★ 별다방 조선")
    print_menu(main_menu,3)

    ## 2. 메인메뉴 선택
    order = select_menu(3)
   

    ## 3. 서브메뉴 출력 및 선택
    if order == 1:    # 커피
        print_menu(coffee_menu,2)
        sub_order= select_menu(2)
        # [[메뉴, 가격],[메뉴, 가격]]
        order_list.append((coffee_menu[sub_order],coffee_price[sub_order]))
    elif order == 2:  # 스무디
        print_menu(smoothie_menu,4)
        sub_order= select_menu(4)
        order_list.append(smoothie_menu[sub_order],smoothie_price[sub_order])     
    elif order == 3:  # 베이커리
        print_menu(bakery_menu,3)
        sub_order= select_menu(3)
        order_list.append(bakery_menu[sub_order],bakery_price[sub_order])
   
   # 아래 숙제
   # 6번 추가 주문하시겠습니까? -> input()
   # 결과: y/n 
   # y: 1번으로 이동
   # n: 출력("주문 페이지로 이동합니다.")
print(">> MSG : 추가주문하시겠습니까?")
while True:
    yn = input(">> y/n: ").lower()
    
    
    if yn == "y":
        break
    elif yn =="n":
        break
    else:
        print(">> WARNING: 올바른 값을 입력하세요.")
    
    
    # 7.추가주문 y/n 선택
    if yn == "y":
        continue   # 추가 주문(다음 반복으로 넘기기)
    elif yn == "n":
        # 8.주문 내역 출력하기!
        print(f"== 주문 내역 ==")
        total = 0
        for item in enumerate(order_list):
            total += item[1]
            # item -> [메뉴, 가격] / item[0]:메뉴 / item[1]: 가격           
            print(f"{i+1}.{item[0]}({item[1]}원)")     # 1.아메리카노(3000원)
        print(f"고객님이 주문하신 메뉴는 총 {len(order_list)}건으로")
        print(f"결제금액은 {total}원입니다.")
        print("이용해주셔서 감사합니다.")
        
            
#완성본 clc에 있음 -> 확인해라

    
    
    
   

        





