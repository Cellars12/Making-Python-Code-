import nltk
from nltk.chat.util import Chat, reflections
import requests
from datetime import datetime

# 대화 쌍을 정의합니다.
pairs = [
    [
        r"안녕|안녕하세요|여보세요",
        ["안녕하세요!", "안녕! 어떻게 도와드릴까요?"]
    ],
    [
        r"내 이름은 (.*)",
        ["반갑습니다, %1님!", "안녕하세요, %1님!"]
    ],
    [
        r"날씨 어때?",
        ["어디의 날씨를 알고 싶으신가요?"]
    ],
    [
        r"날씨는 (.*)",
        ["날씨를 확인하는 중입니다. 잠시만 기다려 주세요..."]
    ],
    [
        r"기분이 어때?|기분이 좋지 않아",
        ["괜찮으신가요? 제가 도와드릴 수 있는 게 있을까요?"]
    ],
    [
        r"계산해줘 (.*)",
        ["계산 결과는: %1입니다."]  # 이 부분은 계산 로직이 추가되어야 합니다.
    ],
    [
        r"시간이 몇 시야?|현재 시간은?",
        ["현재 시간은: " + datetime.now().strftime("%H:%M:%S")]
    ],
    [
        r"퀴즈 해볼래?|퀴즈",
        ["좋아요! 퀴즈를 시작합니다. 문제: '서울의 수도는?'"]
    ],
    [
        r"서울",
        ["정답입니다! 잘 하셨습니다."]
    ],
    [
        r"끝내고 싶어|그만할게",
        ["알겠습니다. 다음에 또 봐요!", "안녕히 가세요!"]
    ],
    [
        r"(.*)",
        ["죄송합니다, 잘 모르겠어요.", "다시 한 번 말씀해 주시겠어요?"]
    ]
]

# 날씨 정보를 가져오는 함수
def get_weather(city):
    api_key = 'YOUR_API_KEY'  # 여기에 자신의 API 키를 입력하세요
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=kr&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"{city}의 현재 날씨는 {weather}이며, 기온은 {temp}도입니다."
    else:
        return "죄송합니다, 해당 도시의 날씨를 찾을 수 없습니다."

# 간단한 계산기 기능
def calculate(expression):
    try:
        result = eval(expression)
        return f"계산 결과는: {result}"
    except Exception:
        return "계산할 수 없습니다. 올바른 수식을 입력해 주세요."

# 사용자 입력 처리
def process_input(user_input):
    for pattern, responses in pairs:
        match = nltk.re.match(pattern, user_input)
        if match:
            if pattern == r"날씨는 (.*)":
                city = match.group(1)
                return get_weather(city)
            elif pattern == r"계산해줘 (.*)":
                expression = match.group(1)
                return calculate(expression)
            return responses[0]  # 첫 번째 응답을 반환
    return "죄송합니다, 잘 모르겠어요."

# 챗봇과 대화 시작
def start_chat():
    print("챗봇과 대화를 시작하세요! (종료하려면 '끝내고 싶어'라고 입력하세요.)")
    print("사용 방법:")
    print("1. 인사: '안녕' 또는 '안녕하세요'")
    print("2. 이름 설정: '내 이름은 [이름]'")
    print("3. 날씨 요청: '날씨는 [도시 이름]'")
    print("4. 기분 상태: '기분이 어때?'")
    print("5. 계산: '계산해줘 [수식]'")
    print("6. 현재 시간: '시간이 몇 시야?'")
    print("7. 퀴즈: '퀴즈 해볼래?'")
    print("8. 종료: '끝내고 싶어' 또는 '그만할게'")
    
    while True:
        user_input = input("당신: ")
        if user_input.lower() in ['끝내고 싶어', '그만할게']:
            print("챗봇: 알겠습니다. 다음에 또 봐요!")
            break
        response = process_input(user_input)
        print(f"챗봇: {response}")

if __name__ == "__main__":
    start_chat()
