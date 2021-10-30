import requests
import shutil
image_url = "https://www.clipartkey.com/mpngs/m/122-1222244_fat-yoshi-transparent-fat-yoshi-transparent-background.png"
filename = image_url.split("/")[-1]
r = requests.get(image_url, stream = True)
if r.status_code == 200:
    r.raw.decode_content = True
    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
else:
    print('whoops')
import ctypes
ctypes.windll.user32.SystemParametersInfoW(20,0,filename,0)