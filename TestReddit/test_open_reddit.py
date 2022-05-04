import requests

class RedditTests:
    def __init__(self, login, password):
        self._url = "https://reddit.com/"
        self._login = login
        self._password = password

    def check_availability_reddit(self):
        """Открытие сайта Reddit"""

        resp = requests.get(self._url)
        resp.raise_for_status()
        if resp.status_code == 200:
            return resp.status_code

    def auth(self):
        """Аутентификация на сайте"""

        session = requests.session()
        url = self._url+'login'
        params = {
            'csrf_token': 'ac0a1b8d7a4490a9103282269372ae6784fce79d',
            'otp': '',
            'password': '!QAZ2wsx',
            'dest': f'{self._url}',
            'username': 'TestForJob'
        }
        r = session.post(url, params)
        print(r.text)

               #
        #    # url https://www.reddit.com/login
        #    # POST
        #    # Headers:
        #    # Body:csrf_token=ac0a1b8d7a4490a9103282269372ae6784fce79d&otp=&password=!QAZ2wsx&dest=https%3A%2F%2Fwww.reddit.com&username=TestForJob
        #    # content-type: application/x-www-form-urlencoded
        #    # accept:*/*
        #    # accept-encoding:gzip, deflate, br
        #    # accept-language: ru,en;q=0.9
        #    #На выходе получить токен
        #    #login: TestForJob Password: !QAZ2wsx
        #
        #    def search_thread(self):
        #        """Поиск треда по ключевым словам"""
        #
        #       url: https: // oauth.reddit.com / api / subreddit_autocomplete_v2.json?query = museum & raw_json = 1 & gilding_detail = 1
        #
        #
        #
        #
        #    def add_comment(self):
        #        """Добавление комментария в тред"""
        #        https: // oauth.reddit.com / api / comment.json?rtj = only & emotes_as_images = true & redditWebClient = desktop2x & app = desktop2x - client - production & raw_json = 1 & gilding_detail = 1
        ## accept:*/*
        ## accept-encoding:gzip, deflate, br
        ## accept-language: ru,en;q=0.9
        ##POST
        ##Headers: authorization: Bearer...из метода authtorization
        ##content-type:application/x-www-form-urlencoded
        ##Body: api_type=json&return_rtjson=true&thing_id=t3_u4nxjk&text&richtext_json=%7B%22document%22%3A%5B%7B%22e%22%3A%22par%22%2C%22c%22%3A%5B%7B%22e%22%3A%22text%22%2C%22t%22%3A%22fgdfgd%22%7D%5D%7D%5D%7D
        ##
        ##Зафиксировать name
        #
        #
        #    def delete_comment(self):
        #        """Удаление ранее оставленного комментария"""
        ##https://oauth.reddit.com/api/del?redditWebClient=desktop2x&app=desktop2x-client-production&raw_json=1&gilding_detail=1
        ## accept:*/*
        ## accept-encoding:gzip, deflate, br
        ## accept-language: ru,en;q=0.9
        ##POST
        ##Headers: authorization: Bearer...из метода authtorization
        ##content-type:application/x-www-form-urlencoded
        ##Body: id=t1_i75mgb4     id=add_comment.name
        #
        #
        #    def log_out_of_the_user(self):
        #        """Выйти из авторизованного пользователя"""
        #      https://www.reddit.com/logoutproxy
        #    # POST:
        #    # accept:*/*
        #    # accept-encoding:gzip, deflate, br
        #    # accept-language: ru,en;q=0.9
        #    # POST
        #    # Headers: authorization: Bearer...из метода authtorization
        #    # content-type:application/x-www-form-urlencoded
        #    #Body:  access_token = 1736311588263 - UbABTB48P2bWPyF6xrphWB7b1sf7Nw ????

if __name__ == '__main__':
    rt = RedditTests("TestForJob", "!qaz2wsx")
    rt.auth()