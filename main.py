from functions.basic import *
from functions.regex import *
from functions.logging import *

from classes.KeyHandler import *
from classes.Lessons import *


lessons_handler = KeyHandler("Resourses/text/lessons")

smartPrint("Добро пожаловать в наш новый чат бот, созданный специально для изучения Английского Языка!")
while True:
	n()
	showArrayValues (lessons_handler.get_strings_by_header("key.lesson"), "Выберите тему для урока:")
	match inputHandler(input('> ')):
		case 0:
			LessonSimple("Resourses/text/present_simple", "Resourses/exersises/present_simple").initialise()
		case 1:
			LessonContinuous("Resourses/text/present_continuous", "Resourses/exersises/present_continuous").initialise()
		case 2:
			LessonSimple("Resourses/text/future_simple", "Resourses/exersises/future_simple").initialise()
		case 3:
			die()