import requests
import requests.auth


class RedditTests:
    def __init__(self, login, password, client_id, client_secret):
        self._url = 'https://reddit.com'
        self._login = 'TestForJob'
        self._password = '!QAZ2wsx'
        self._client_id = 'aITM_HsCi-HNExzJfGdCwQ'
        self._client_secret = 'PO0n6ijLOLm96CkEAYMCAYNfWi4qVg'
        self._session = requests.session() # инициируем новую сессиию, которая будет у нас использована по всему классу
        self._session.headers.update(**{"User-Agent": "TestForJob/0.0.1"}) # добавляем заголовок User-Agent

    def check_availability_reddit(self):
        """Проверка доступности Reddit"""

        resp = requests.get(self._url)
        resp.raise_for_status()

    def auth(self):
        """Аутентификация на reddit"""

        auth_hdr = requests.auth.HTTPBasicAuth(self._client_id, self._client_secret)
        data = {'grant_type': 'password', 'username': self._login, 'password': self._password}
        resp = self._session.post(f'{self._url}/api/v1/access_token', auth=auth_hdr, data=data)
        resp.raise_for_status()
        resp_data = resp.json()
        self._session.headers.update(Authorization=f"{resp_data['token_type']} {resp_data['access_token']}")

    def search_for_a_thread(self):
        """Поиск треда по ключевому слову"""

        params = {'limit': limit, 'q': subreddit}
        response = self._get(f'url={self._url}/search', params=params, expected_codes=expected_code)

        return response.json()

    def add_new_comment_for_thread(self):

        params = {'thing_id': thread_id, 'text': comment}

        response = self._post(url=f'{self._url}/api/comment', params=params, expected_codes=expected_code)

        return response.json()

    def delete_comment_in_thread(self):

        params = {'id': comment_id}
        response = self._post(url=f'{self._url}/api/del', params=params,expexted_codes=expected_code)

        return response.json()


if __name__ == '__main__':
    rt = RedditTests("TestForJob", "!qaz2wsx", "client_id", "client_secret")
    rt.auth()

