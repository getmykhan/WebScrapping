from urllib.request import urlopen

try:
    html = urlopen("http://www.small-biga-data.com/savings-bank.txt")
    print(html.read())
except:
    print ("Sorry File does not exist!")
