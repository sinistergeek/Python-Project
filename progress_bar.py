import random, time

BAR = chr(9608)
def main():
    print('Progressbar')
    bytesDownload = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        bytesDownload += random.randint(0,100)
        barStr = getProgressBar(bytesDownloaded,downloadSize)
        print(barStr,end='',flush = True)
