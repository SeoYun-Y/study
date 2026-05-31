import re

# [실습 2: Data Privacy]
# 고객의 리뷰 데이터를 AI에게 분석 맡기려고 합니다.
# 하지만 리뷰 안에 '전화번호'와 '이메일'이 그대로 들어있네요.
# 이대로 보내면 개인정보 유출 사고입니다!
# AI를 이용해 정규식(Regex) 마스킹 함수를 작성하고 적용해보세요.

raw_reviews = [
    "제품은 좋은데 배송이 늦어요. 010-1234-5678로 연락 주세요.",
    "환불 요청합니다. 이메일은 customer@example.com 입니다.",
    "사장님 친절해요! 02-555-1234 번창하세요."
]

def mask_personal_info(text):
    """
    TODO: Gemini에게 아래와 같이 요청해서 이 함수를 완성하세요.
    프롬프트: "파이썬 re 모듈을 써서 텍스트 안의 '휴대폰 번호'와 '이메일'을 찾아서 각각 '[PHONE]', '[EMAIL]'로 치환하는 함수를 짜줘."
    """
    # 여기에 AI가 짜준 코드를 붙여넣으세요.
    processed_text = text 
    return processed_text

def send_to_ai(reviews):
    print("🚀 AI에게 전송할 데이터 미리보기:")
    print("-" * 30)
    for review in reviews:
        safe_review = mask_personal_info(review)
        print(f"[전송됨] {safe_review}")
    print("-" * 30)
    print("✅ 전송 완료 (이 데이터는 AI 학습에 활용될 수 있습니다)")

if __name__ == "__main__":
    send_to_ai(raw_reviews)