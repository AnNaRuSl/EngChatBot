from libs.base_functions import *
from libs.file_management import *

class PresentSimple:
	def __init__(self, args):
		self.args = args

	def initialise(self):
		file_path = self.args['FilePath']
		folder_path = self.args['FolderPath']

		#Paths
		tables = readFilePath(file_path, 'tables')
		usage = readFilePath(file_path, 'usage')
		usageToBe = readFilePath(file_path, 'usageToBe')

		#TableArrays
		about = read_row_by_keyword(tables, 'about')
		sentences_types = read_row_by_keyword(tables, 'sentences_types')
		to_be = read_row_by_keyword(tables, 'to_be')

		#Folders
		make_sentence = readFilePath(folder_path, 'make_sentence')
		make_sentence_to_be = readFilePath(folder_path, 'make_sentence_to_be')
		while True:
			n()
			showArrayValues (about, "Выберите вариант:")
			match inputHandler(input('>> ')):
				case 0:
					n()
					smartPrint(readTxt(usage))
				case 1:
					while True:
						n()
						showArrayValues(sentences_types)
						match inputHandler(input('>>> ')):
							case 0:
								n()
								smartPrint(readSenteceTypes(make_sentence, 0))
							case 1:
								n()
								smartPrint(readSenteceTypes(make_sentence, 1))
							case 2:
								n()
								smartPrint(readSenteceTypes(make_sentence, 2))
							case 3:
								break
				case 2:
					while True:
						n()
						showArrayValues(to_be)
						match inputHandler(input('>>> ')):
							case 0:
								n()
								smartPrint(readTxt(usageToBe))
							case 1:
								while True:
									n()
									showArrayValues(sentences_types)
									match inputHandler(input('>>>> ')):
										case 0:
											n()
											smartPrint(readSenteceTypes(make_sentence_to_be, 0))
										case 1:
											n()
											smartPrint(readSenteceTypes(make_sentence_to_be, 1))
										case 2:
											n()
											smartPrint(readSenteceTypes(make_sentence_to_be, 2))
										case 3:
											break
							case 2:
								break
				case 3:
					smartPrint("В разработке!")
				case 4:
					break