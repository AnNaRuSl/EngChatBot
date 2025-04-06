import csv

def readTxt(path):
	with open(path + ".txt", 'r', encoding='utf-8') as file:
		return file.read()

def csv_to_list(path, delimiter_char = '|'):
	with open(path + ".csv", 'r', encoding='utf-8') as csvfile:
		newList = []
		reader = csv.reader(csvfile, delimiter = delimiter_char)
		for row in reader:
			newList.append(row)
		return newList

def read_row_by_keyword(path, keyword, delimiter_char = '|'):
	with open(path + ".csv", 'r', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile, delimiter = delimiter_char)
		newList = []
		for row in reader:
			if row[0] == keyword:
				for i in range(1, len(row)):
					newList.append(row[i])
		return newList;



def readFilePath(path, keyword, delimiter_char = '|'):
	with open(path + ".csv", 'r', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile, delimiter = delimiter_char)
		for row in reader:
			if row[0] == keyword:
				return row[1]
		return None


def readSenteceTypes(path, type):
	args = ['plus', 'minus', 'question']
	return readTxt(path + '/' + args[type])