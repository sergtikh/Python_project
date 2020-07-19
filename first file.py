from requests import Session
from credentials import *
import time

session = Session()

friend_id = '484950266'

response = session.post(
    url='http://5.178.83.92/' + id + '/' + auth_key + '/package',
    data={
        'requests': '[{"params":{"friend":"' + friend_id + '","vote":"2"},"ts":' + str(time.time()) + ',"request":"vote_send"}]'
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
