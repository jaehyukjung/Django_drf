import os, requests, json

import speech_recognition as sr
# os.environ.setdefault("DJANGO_SETTINGS_MODULE","drfProject.settings")

# import django
# django.setup()

# from mainApp.models import Coffee

def my_fun():

    def kakao_stt(app_key, stype, data):
        if stype == 'file':
            filename = data
            with open(filename, "rb") as fp:
                audio = fp.read()
        else:
            audio = data

        headers = {
            "Content-Type": "application/octet-stream",
            "Authorization": "KakaoAK " + app_key,
        }

        # 카카오 음성 url
        kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
        # 카카오 음성 api 요청
        res = requests.post(kakao_speech_url, headers=headers, data=audio)
        # 요청에 실패했다면,
        if res.status_code != 200:
            text = ""
            print("error! because ", res.json())
        else:
            result = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}') + 1]
            text = json.loads(result).get('value')

        return text


    # 함수 호출부
    KAKAO_APP_KEY = '14eb9391acd95f167100f637cd776d71'


    def get_speech():
        # 마이크에서 음성을 추출하는 객체
        recognizer = sr.Recognizer()

        # 마이크 설정
        microphone = sr.Microphone(sample_rate=16000)

        # 마이크 소음 수치 반영
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            print("소음 수치 반영하여 음성을 청취합니다. {}".format(recognizer.energy_threshold))

        # 음성 수집
        with microphone as source:
            print("Say something!")
            result = recognizer.listen(source)
            audio = result.get_raw_data()

        return audio
    audio = get_speech()
    text = kakao_stt(KAKAO_APP_KEY, "stream", audio)

    arr = text.split()

    lst = []
    coffee_list = ["아메리카노", "카페 라떼", "바닐라 라떼", "카푸치노", "카라멜 마키야또", "돌체 라떼", "에스프레소", "아포가토", "콜드브루", "콜드브루 라떼"]
    
    ans_dic = {}
    for i in coffee_list:
        ans_dic[i] = 0

    
    for ans in ans_dic.keys():
        if ans in text:
            ans_dic[ans] += 1

    for ans in ans_dic:
        if ans_dic[ans] != 0:
            lst.append(ans)

    return lst
lst = my_fun()
print(lst)