hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

websites = ["www.youtube.com","youtube.com","www.facebook.com","facebook.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("Access denied Website")
        with open(hostsPath,'r+') as file:
            content = file.read()
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(redirect + "" + "\n")
    else:
        with open(hostsPath,'r+') as file:
            content = file.readlines()
        file.seek(0)

    for line in content:
        if not any(site in line for site in websites):
            file.write(line)
        file.truncate()
    print("Allowed access!")
time.sleep(5)


