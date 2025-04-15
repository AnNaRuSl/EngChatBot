from datetime import datetime

def log (text):
	with open("./Logs/logs.txt", 'a', encoding='utf-8') as file:
		now = datetime.now()
		date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
		file.write(date_time + " - " + text + '\n')