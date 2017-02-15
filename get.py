from urllib.request import urlopen
import time



def run():
    try:
        html = urlopen("http://www.small-big-data.com/savings-bank.txt")
        time.sleep(2)
        return (html.read())
    except:
        print ("Sorry File does not exist!")

print(run())
