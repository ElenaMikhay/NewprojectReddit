import requests
import requests.auth


class RedditTests:
    def __init__(self, login, password, client_id, client_secret):
        self._url = 'https://reddit.com'
        self._login = login
        self._password = password

        # client_id и client_secret надо сгенерировать на странице https://www.reddit.com/prefs/apps
        # создав новый dev application для скрипта
        # "Script for personal use. Will only have access to the developers accounts"
        self._client_id = client_id
        self._client_secret = client_secret

        # инициируем новую сессиию, которая будет у нас использована по всему классу
        self._session = requests.session()

        # как оказалось, в API reddit.com, наличие заголовока User-Agent обязательно.
        # Почему так хитро добавлен? В именах переменных нельзя использовать "-", это ошибка. А так как headers.update
        # принимает на вход **kwargs (key=value), а в key у нас есть "-", тогда мы можем воспользоваться распаковковкой
        # https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
        # https://stackoverflow.com/a/5710402
        # Тогда при каждом запросе, у нас автоматически данный заголовок будет подставлятся в запрос
        self._session.headers.update(**{"User-Agent": "TestForJob/0.0.1"})

    def check_availability_reddit(self):
        """Открытие сайта Reddit"""

        resp = requests.get(self._url)
        resp.raise_for_status()
        if resp.status_code == 200:
            # А если статус 301, тогда метод вернет None и мы получим ошибку если что-то попытаемся извлечь из ответа.
            # Для проверки доступности самого сайта думаю хватит raise_for_status, если ошибка не выскочила, то значит
            # работает
            return resp.status_code

    def auth(self):
        """Аутентификация на сайте"""

        # создаем объекты для аутентификации на reddit.com
        auth_hdr = requests.auth.HTTPBasicAuth(self._client_id, self._client_secret)
        data = {'grant_type': 'password', 'username': self._login, 'password': self._password}

        # запрашиваем токен, он понадобится для работы с API
        resp = self._session.post(f'{self._url}/api/v1/access_token', auth=auth_hdr, data=data)
        # проверяем возвращаемый статус от reddit.com, если часто запрашивать токен, то вернется статус 429
        resp.raise_for_status()

        # у нас всё работает, тогда декодируем json в словарь (dict())
        resp_data = resp.json()

        # добавляем в заголовки нашей сессии, заголовок Authorization чтобы не добавлять это в каждый наш запрос
        self._session.headers.update(Authorization=f"{resp_data['token_type']} {resp_data['access_token']}")

        # после того, как получили токен и добавили его в заголовки можем перейти к API-запросам


if __name__ == '__main__':
    rt = RedditTests("TestForJob", "!qaz2wsx", "client_id", "client_secret")
    rt.auth()
# всегда в конце файла должна быть пустая строка
