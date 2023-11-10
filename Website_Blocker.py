import platform

if platform.system() == "Windows":
    pathToHosts=r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Linux":
    pathToHosts=r"/etc/hosts"

redirect="127.0.01"
websites=["https://www.websitename.com"]

with open(pathToHosts,'r+') as file:
    content=file.read()
    for site in websites:
        if site in content:
            pass
        else:
            file.write(redirect+" "+site+"\n")
