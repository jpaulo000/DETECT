import streaming.track as track
import streaming.stream as stream 
import sendEmail.sendEmail as sendEmail
import os
import datetime, time
import urllib.request


currentHour = (int(time.strftime("%H")) * 100) + int(time.strftime("%M"))

mtime = datetime.datetime.fromtimestamp(os.path.getmtime(track.getPath()))
modHour = (int(str(mtime)[11:13]) * 100) + int(str(mtime)[14:16])

totalHour = abs(currentHour - modHour)

if  totalHour >= 10:
    
	csv = open(track.getPath(), 'r', encoding="utf-8" )
    
	try:
		urllib.request.urlopen('http://www.google.com', timeout=1)
		stream.manage_csv(csv, 1)
		sendEmail.sendEmail(2, str(totalHour))
	except urllib.request.URLError:
        	print("Erro")      
       
	csv.close()
