import time
import requests


session = requests.Session()
headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 YaBrowser/21.6.0.616 Yowser/2.5 Safari/537.36'
}
session.headers.update(headers)
persons = None
info = []
def authorizate():
    try:
        url = 'https://findclone.ru/login'
        datas = {
            'phone': '+79168460149',
            'password': '65l50k5l45',
        }
        loging = session.post(url, data = datas).json()
        headers.update({'session-key': str(loging['session_key']), 'user-id': str(loging['userid'])})
        print('Авторизация завершена')
    except Exception as e:
        print("Не получилось авторизоваться",e)

tlist = []
def upload_foto(file):
    try:
        tlist.clear()
        url1 = 'https://findclone.ru/upload2'
        files = {'uploaded_photo': ('photo.png', open(file, 'rb'), 'image/png')}
        session.headers.update(headers)
        upload = session.post(url1, files=files).json()
        persons  = upload['Total']
        info = upload['data']
        print(f'Поиск завершен, найдено {persons} похожих людей')
        for person in info:
            try:
                score = person['score']
            except:
                score = "Не получилось"
            try:
                firstame = person['firstname']
            except:
                firstame = "Имя очень странное"
            try:
                age = person['age']
            except:
                age = "Возраст не указан"
            try:
                city = person['city']
            except:
                city = "Город не указан"
            try:
                userid = f'https://vk.com/id{person["userid"]}'
            except:
                userid = "Noname"
            text = f"""
Точность совпадения: {score}
Имя:  {firstame }
Возраст:  {age}
Город:  {city}
Ссылка на страницу ВКонтакте:  
{userid}
            """
            tlist.append(text)
        return tlist


    except Exception as e:
        print('Не получилось найти',e)

def main():
    authorizate()
    upload_foto(file)
if __name__ == '__main__':
    main()