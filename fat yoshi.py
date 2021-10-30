#import modules
import requests
import shutil
import ctypes
import os
import image_paths
import random

#grab image from URL
image_url = random.choice(image_paths.IMAGES)
print(image_url)

#set file name
filename = 'temp.png'

#open image from the URL, return stream contents
r = requests.get(image_url, stream = True)

#check if image was successfully retrieved from the URL
if r.status_code == 200:
    r.raw.decode_content = True
    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
else:
    print('whoops')

global_path = os.path.join(os.path.dirname(__file__), filename)

#set wallpaper to downloaded image
ctypes.windll.user32.SystemParametersInfoW(20,0,global_path,0)