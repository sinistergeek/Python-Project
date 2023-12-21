import subprocess

data = (subprocess.check_out(["netsh","wlan","show","profiles"]).decode("utf-8").split("\n"))
profile=[i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    result=(subprocess.check_output(["netsh","wlan","show","profile",i,"key=clear"]).decode("utf-8").split("\n"))
