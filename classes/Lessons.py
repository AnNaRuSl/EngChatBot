from functions.basic import *
from functions.regex import *
from functions.logging import *

from classes.KeyHandler import *
from classes.Quiz import *

class LessonSimple:

	def __init__(self, file_path, quiz_path):
		self.handler = KeyHandler(file_path)
		self.quiz_path = quiz_path


	def initialise(self):
		handler = self.handler
		while True:
			n()
			showArrayValues (handler.get_strings_by_header("key.choose.about"), "Выберите вариант:")
			match inputHandler(input('>> ')):
				case 0:
					n()
					smartPrint(handler.get_string("key.usage.general"))
				case 1:
					while True:
						n()
						showArrayValues(handler.get_strings_by_header("key.choose.sentences_types"))
						match inputHandler(input('>>> ')):
							case 0:
								n()
								smartPrint(handler.get_string("key.make_sentence.common.positive"))
							case 1:
								n()
								smartPrint(handler.get_string("key.make_sentence.common.negative"))
							case 2:
								n()
								smartPrint(handler.get_string("key.make_sentence.common.question"))
							case 3:
								break
				case 2:
					while True:
						n()
						showArrayValues (handler.get_strings_by_header("key.choose.to_be"), "Выберите вариант:")
						match inputHandler(input('>>> ')):
							case 0:
								n()
								smartPrint(handler.get_string("key.usage.to_be"))
							case 1:
								while True:
									n()
									showArrayValues(handler.get_strings_by_header("key.choose.sentences_types"))
									match inputHandler(input('>>>> ')):
										case 0:
											n()
											smartPrint(handler.get_string("key.make_sentence.to_be.positive"))
										case 1:
											n()
											smartPrint(handler.get_string("key.make_sentence.to_be.negative"))
										case 2:
											n()
											smartPrint(handler.get_string("key.make_sentence.to_be.question"))
										case 3:
											break
							case 2:
								break
				case 3:
					n()
					smartPrint("Укажите желаемое кол-во упражнений от 1 до 15:")
					while True:
						input_exersise_count = inputHandler(input('>>> '))
						input_exersise_count = input_exersise_count + 2
						if input_exersise_count >= 1 and input_exersise_count <= 16:
							n()
							log("Открыты упражнения: " + str(input_exersise_count - 1) + " штук")
							quiz = QuizFactory(self.quiz_path, input_exersise_count).getQuiz()
							quiz.initialise()
							break
						else:
							n()
							smartPrint("Введено некорректное число!")
							smartPrint("Пожалуйста укажите желаемое кол-во упражнений от 1 до 15:")

				case 4:
					break



class LessonContinuous:

	def __init__(self, file_path, quiz_path):
		self.handler = KeyHandler(file_path)
		self.quiz_path = quiz_path


	def initialise(self):
		handler = self.handler
		while True:
			n()
			showArrayValues (handler.get_strings_by_header("key.choose.about"), "Выберите вариант:")
			match inputHandler(input('>> ')):
				case 0:
					n()
					smartPrint(handler.get_string("key.usage.general"))
				case 1:
					while True:
						n()
						showArrayValues(handler.get_strings_by_header("key.choose.sentences_types"))
						match inputHandler(input('>>> ')):
							case 0:
								n()
								smartPrint(handler.get_string("key.make_sentence.common.positive"))
							case 1:
								n()
								smartPrint(handler.get_string("key.make_sentence.common.negative"))
							case 2:
								n()
								smartPrint(handler.get_string("key.make_sentence.common.question"))
							case 3:
								break
				case 2:
					n()
					smartPrint("Укажите желаемое кол-во упражнений от 1 до 15:")
					while True:
						input_exersise_count = inputHandler(input('>>> '))
						input_exersise_count = input_exersise_count + 2
						if input_exersise_count >= 1 and input_exersise_count <= 16:
							n()
							log("Открыты упражнения: " + str(input_exersise_count - 1) + " штук")
							quiz = QuizFactory(self.quiz_path, input_exersise_count).getQuiz()
							quiz.initialise()
							break
						else:
							n()
							smartPrint("Введено некорректное число!")
							smartPrint("Пожалуйста укажите желаемое кол-во упражнений от 1 до 15:")
				case 3:
					break