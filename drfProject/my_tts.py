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
    tts = KakaoTTS(" 메뉴를 선택해주세요. 선택된 음료는 우측 하단의 장바구니에서 확인하실 수 있습니다. ")
    tts.save("일반1.mp3")
    tts = KakaoTTS(" 음료 상세옵션을 선택해주세요 ")
    tts.save("일반2.mp3")
    tts = KakaoTTS(" 드시고 가시나요? ")
    tts.save("결제적립_1.mp3")
    tts = KakaoTTS(" 결제는 어떻게 하세요? ")
    tts.save("결제적립_2.mp3")
    tts = KakaoTTS(" 적립 도와드릴까요? ")
    tts.save("결제적립_3.mp3")
    tts = KakaoTTS(" 결제하기 버튼을 눌러주세요. ")
    tts.save("결제적립_4.mp3")
    tts = KakaoTTS(" 신용카드를 투입구에 넣어주세요. 결제가 완료될 때 까지 카드를 빼지 마세요! ")
    tts.save("결제적립_5.mp3")
    tts = KakaoTTS(" 결제 되었습니다. ")
    tts.save("결제완료.mp3")
    tts = KakaoTTS(" 주문이 완료되었습니다. 저희 매장을 이용해주셔서 감사합니다. ")
    tts.save("마무리.mp3")


