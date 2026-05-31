# [Buggy Code] 쇼핑몰 할인 계산기
# 에러는 없는데 가끔 사장님이 화냄

def calculate_final_price(price, discount):
    # discount가 20%면 0.2를 넣어야 하는데...
    # 사용자가 정수 20을 넣으면 어떻게 될까?
    final = price - (price * discount)
    return final

# 테스트
print(calculate_final_price(10000, 0.2)) # 정상: 8000
print(calculate_final_price(10000, 20))  # 버그: -190000 (돈을 주고 물건을 팖)
