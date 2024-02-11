import random, time

BAR = chr(9608)
def main():
    print('Progressbar')
    bytesDownload = 0
    downloadSize = 4096
    while bytesDownload < downloadSize:
        bytesDownload += random.randint(0,100)
        barStr = getProgressBar(bytesDownload,downloadSize)
        print(barStr,end='',flush = True)
        time.sleep(0.2)
        print('\b' * len(barStr), end ='',flush=True)

def getProgressBar(progress,total,barWidth=40):
    progressBar = ''
    progressBar += '['

    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    numberOfBars = int((progress / total) * barWidth)
    progressBar += BAR * numberOfBars
    progressBar += ' ' * (barWidth - numberOfBars)
    progressBar += ']'

    percentComplete =round(progress / total * 100,1)
    progressBar += ' ' + str(percentComplete) + '%'
    progressBar += ' ' + str(progress) + '/' + str(total)
    return progressBar

if __name__ == '__main__':
    main()
