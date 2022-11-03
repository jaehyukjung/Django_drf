import requests, key

# 자신의 REST_API_KEY를 입력하세요!
REST_API_KEY = key.REST_API_KEY


class KakaoTTS:
    def __init__(self, text, API_KEY=REST_API_KEY):
        self.resp = requests.post(
            url="https://kakaoi-newtone-openapi.kakao.com/v1/synthesize",
            headers={
                "Content-Type": "application/xml",
                "Authorization": f"KakaoAK {API_KEY}"
                },
            data=f"<speak>{text}</speak>".encode('utf-8')
        )

    def save(self, filename="output.mp3"):
        with open(filename, "wb") as file:
            file.write(self.resp.content)


if __name__ == '__main__':
    tts = KakaoTTS(" 메뉴를 선택해주세요. 선택된 음료는 좌측 하단의 장바구니에서 확인하실 수 있습니다. ")
    tts.save("일반1.mp3")
 


