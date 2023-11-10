import platform
if platform.system() == "Windows":
    pathToHosts=r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Linux":
    pathToHosts=r"/etc/hosts"

websites=["https://www.facebook.com"]

with open(pathToHosts,'r+') as file:
    content=file.readlines()
    file.seek(0)
    for line in content:
        if not any(sites in line for site in websites):
            file.write(line)
    file.truncate()
