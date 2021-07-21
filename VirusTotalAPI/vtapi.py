import requests


def error_message():
    return "YOU HAVE PROBLEM WITH THE INTERNET"


class VirusTotal:
    def __init__(self):
        self.url = 'http://www.virustotal.com/'
        self.data = {"data": {"user_id": "vpustowit@yandex.ru", "password": "mephi1511", "forever": False}}
        self.headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)' +
                          'Chrome/78.0.3904.108 Safari/537.36'
        }
        self.params = {}

    def auth(self):
        url = self.url + 'ui/signin'
        session = requests.Session()
        req = session.post(url=url, json=self.data, headers=self.headers)
        app = req.json()
        self.params['apikey'] = app['data']['attributes']['apikey']

    def scan_file(self, file: str):
        self.auth()
        url1 = self.url + 'vtapi/v2/file/scan'
        file = {'file': (file, open('C:/users/vpust/OneDrive/Desktop/Unior/viruses/buffer/{}'.format(file), 'rb'))}
        try:
            req1 = requests.post(url1, files=file, params=self.params)
        except:
            return error_message()
        answer1 = req1.json()
        url2 = self.url + 'ui/analyses/%s' % answer1['scan_id']
        try:
            while requests.get(url2, params=self.params).json()['data']['attributes']['status'] != "completed":
                pass
            req2 = requests.get(url2, params=self.params)
        except:
            return error_message()
        answer = req2.json()
        while answer['data']['attributes']['status'] != "completed":
            pass
        return answer


def api(file: str):
    virustotal = VirusTotal()
    report = virustotal.scan_file(file=file)
    return report
