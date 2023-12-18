import os
import requests
url="https://graph.facebook.com/{}/picture?type=large"
path = os.getcwd()

if not "fb_dps" in os.listdir(path):
    os.mkdir("fb_dps")

fbid = int(input("Enter the Facebook-id to download it's profile picture:"))
try:
    result = requests.get(url.format(fbid))
    with open("fb_dps/{}_img.jpg".format(fbid),"wb") as file:
        file.write(result.content)

except:
    print("There was some error")
