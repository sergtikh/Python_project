from requests import Session
from credentials import *
import time

session = Session()

class abc:
    def artobstrel(self, friend_id):
        response = session.post(
            url='http://5.178.83.92/' + id + '/' + auth_key + '/package',
            data={
                'requests': '[{"params":{"friend":"' + friend_id + '","vote":"2"},"ts":' + str(
                    time.time()) + ',"request":"vote_send"}]'
            },
            headers={
                'Accept': '*/*',
                'Content-Type': 'application/x-www-form-urlencoded',
                'DNT': '1',
                'Host': '5.178.83.92',
                'Origin': 'null',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 YaBrowser/20.7.1.70 Yowser/2.5 Safari/537.36',
                'X-Requested-With': 'ShockwaveFlash/32.0.0.403'
            }
        )

        print(str(time.time()))
        print(response.text)

    def boezapas(self, friend_id):
        response = session.post(
            url='http://5.178.83.92/' + id + '/' + auth_key + '/package',

            data={"requests": '[{"request": "vote_send","ts": ' + str(time.time()) + ',"params": {"friend":' + friend_id + ', "vote": "4"}}]'},
            headers={
                'Accept': '*/*',
                'Content-Type': 'application/x-www-form-urlencoded',
                'DNT': '1',
                'Host': '5.178.83.92',
                'Origin': 'null',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 YaBrowser/20.7.1.70 Yowser/2.5 Safari/537.36',
                'X-Requested-With': 'ShockwaveFlash/32.0.0.371'
            }
        )
        print(str(time.time()))
        print(response.text)

    def snabzhenie(self, friend_id):
        response = session.post(
            url='http://5.178.83.92/' + id + '/' + auth_key + '/package',
            data={
                "requests": '[{"params": {"present": "1", "sign": "f417877e2db41d2c0b7bc0a04170dc27","friend": ' + friend_id + '}, "request": "present_send", "ts": "" + str(time.time()) + ""}]'
            },
            headers={
                'Accept': '*/*',
                'Content-Type': 'application/x-www-form-urlencoded',
                'DNT': '1',
                'Host': '5.178.83.92',
                'Origin': 'null',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 YaBrowser/20.7.1.70 Yowser/2.5 Safari/537.36',
                'X-Requested-With': 'ShockwaveFlash/32.0.0.371'
            }
        )
        print(str(time.time()))
        print(response.text)


friend_id = '39638147'
test = abc()
#test.artobstrel(friend_id)
test.boezapas(friend_id)
#test.snabzhenie(friend_id)

