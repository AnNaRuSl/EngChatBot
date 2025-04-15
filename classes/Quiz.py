import random
import copy
from functions.basic import *
from functions.regex import *
from functions.logging import *


class Question:
	def __init__(self):
		self.question = ""
		self.answers = []
		self.right_answer = 0

#Getters
	def get_question(self):
		return self.question

	def get_answers(self):
		return self.answers

	def get_right_answer(self):
		return self.right_answer

#Setters
	def set_question(self, question):
		self.question = question

	def add_answer(self, answer):
		self.answers.append(answer)

	def set_right_answer(self, right_answer):
		self.right_answer = right_answer

	def reset(self):
		self.question = ""
		self.answers = []
		self.right_answer = 0


class Quiz:
	def __init__(self, questions, length):
		self.questions = questions
		self.length = length

	def initialise(self):
		questions = self.questions
		length = self.length
		completed = []


		for i in range(1, length):
			rand = random.randint(0, len(questions) - 1)
			if rand in completed:
				for i in range(0, len(questions) - 1):
					if i in completed:
						i = i + 1
					else:
						rand = i
					break

			question = questions[rand]
			answers = question.get_answers()
			right_answer = question.get_right_answer()
			count = len(answers)
			n()
			smartPrint(question.get_question())
			log("Предложение: " + question.get_question())
			for i in range(0, count):
				smartPrint(str(i + 1) + ") " + answers[i], end="    ")
				log("Вариант " + str(i + 1) + ": " + answers[i])
			smartPrint(str(count + 1) + ") " + "<---Прервать")
			input_answer = inputHandler(input('Ваш ответ >>>> '))
			input_answer = input_answer + 1
			if input_answer == right_answer:
				n()
				log("Ответ ученика: " + str(input_answer) + " Правильный ответ: " + str(right_answer) + "++++++++++++++++++++++++++++++++++++++++")
				smartPrint("Правильно!")
				n()
			elif input_answer == count + 1:
				log("Выполнение упражнений прервано!")
				break
			else:
				n()
				log("Ответ ученика: " + str(input_answer) + " Правильный ответ: " + str(right_answer) + "---------------------------------------")
				smartPrint("Неправильно! Правильный ответ: " + str(right_answer) + ") " + answers[right_answer - 1])
				n()
				







class QuizFactory():
	def __init__(self, file_path, length):
		self.file_path = file_path
		self.length = length

	def getQuiz(self):
		file_path = self.file_path
		length = self.length
		with open(file_path + ".txt", 'r', encoding='utf-8') as file:
			raw_lines = file.readlines()
			question = Question()
			reset = True

			lines = []
			questions = []
			for line in raw_lines:
				line = preg_replase(r"\n", "", line)
				lines.append(line)
			for line in lines:
				if reset:
					question.set_question(line)
					reset = False
				else:
					try:
						int(line)
						question.set_right_answer(int(line))
						questions.append(copy.deepcopy(question))
						question.reset()
						reset = True
					except ValueError:
						question.add_answer(line)
			return Quiz(questions, length)

        				
