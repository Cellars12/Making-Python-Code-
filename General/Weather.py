import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']

        print(f"도시: {city}")
        print(f"온도: {temperature} °C")
        print(f"기압: {pressure} hPa")
        print(f"습도: {humidity}%")
        print(f"날씨 설명: {description.capitalize()}")
    else:
        print("날씨 정보를 가져오지 못했습니다. 도시 이름을 확인하세요.")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # OpenWeatherMap API
    city = input("날씨를 검색할 도시 이름을 입력하세요: ")
    get_weather(city, api_key)
