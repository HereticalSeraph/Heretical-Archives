    #importing the necessary modules
import requests
import shutil
import ctypes

    #grabbing the image from the url
image_url = "https://www.clipartkey.com/mpngs/m/122-1222244_fat-yoshi-transparent-fat-yoshi-transparent-background.png"

    #store the original file name as a variable for later use
filename = image_url.split("/")[-1]

    #open the image, return stream contents
r = requests.get(image_url, stream = True)

    #check if the image was correctly retrieved from the URL
if r.status_code == 200:
    r.raw.decode_content = True
    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
else:
    print('whoops')

    #change the wallpaper to the downloaded image
ctypes.windll.user32.SystemParametersInfoW(20,0,filename,0)
