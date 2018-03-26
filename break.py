import webbrowser
import time

#print current time
print(time.ctime())

for i in range(3):
    #wait 10 seconds for opening of the browser
    time.sleep(10)
    webbrowser.open('https://dragosbusu.com')