import requests
from pprint import pprint
import time
with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()
with open('token_dick.txt', 'r') as file_object:
    token_dick = file_object.read().strip()
URL = 'https://api.vk.com/method/photos.getAll/'
params = {
    # 'user_ids': '3',
    'owner_id': '15800001',
    'access_token': token,
    'v':'5.131',
    'extended': 'likes',
    'album_id': 'profile',
}
res = requests.get(URL, params=params,).json()
# pprint(res)
qwe = res['response']['items']
for n in qwe:
    # pprint(n)
    likes = n['likes']['count'] # количество лайков
    date = n['date'] # дата фото
    photo_url = n['sizes'][-1]['url'] # сылка фото
    # print(photo_url)
    photo_list = {'likes': likes, 'date': date, 'url': photo_url}


    class YaUploader:
        def __init__(self, token: str):
            self.token = token_dick

        def upload(self, file_path: str):

            file_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

            headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token_dick}'}
            params = {'path': f' {photo_list["likes"]}.jpeg', 'overwrite': 'true'}
            response = requests.get(file_url, headers=headers, params=params).json()
            href = response.get('href', '')
            res = requests.put(href)
            if res.status_code == 201:
                print('Загрузка прошла успешно!')
            else:
                print(f'Ошибка загрузки! Код ошибки: {res.status_code}')


    if __name__ == '__main__':
        path_to_file = photo_list['url']  # сылка на картинку
        token = token_dick
        uploader = YaUploader(token)
        result = uploader.upload(path_to_file)
