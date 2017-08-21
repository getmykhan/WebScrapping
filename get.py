from urllib.request import urlopen
import time
import requests


def run():
    try:
        html = urlopen("http://pythonscraping.com/pages/page1.html")
        time.sleep(2)
        return (html.read())

    except:
        print ("Sorry File does not exist!")

    filetowrite = open('test.txt', 'w')
    writeToFile = filetowrite.write(html)
    print (writeToFile.read())

print(run())
