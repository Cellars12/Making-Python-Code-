import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    try:
        short_url = s.tinyurl.short(url)  # TinyURL을 사용하여 URL 단축
        return short_url
    except Exception as e:
        return f"URL 단축 중 오류 발생: {e}"

if __name__ == "__main__":
    url = input("단축할 URL을 입력하세요: ")
    short_url = shorten_url(url)
    print("단축된 URL:", short_url)
