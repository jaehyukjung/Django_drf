import requests

# 자신의 REST_API_KEY를 입력하세요!
REST_API_KEY = '14eb9391acd95f167100f637cd776d71'


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
    tts = KakaoTTS("  주문이 완료되셨습니다. 저희 매장을 이용해 주셔서 감사합니다. ")
    tts.save("[4단계]_완료_1.mp3")
