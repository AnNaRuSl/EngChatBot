#Libraries
from libs.base_functions import *
from libs.file_management import *
#Classes
#from libs.regex import *
from objects.PresentSimple import *
from objects.PresentContinuous import *
from objects.FutureSimple import *


### Objects ang variables ###
lessons_list = csv_to_list("files/lessons")

present_simple = PresentSimple({'FilePath': 'files/ps/file_path', 'FolderPath' : 'files/ps/folder_path'})
present_continuous = PresentContinuous({'FilePath': 'files/pc/file_path', 'FolderPath' : 'files/pc/folder_path'})
future_simple = FutureSimple({'FilePath': 'files/fs/file_path', 'FolderPath' : 'files/fs/folder_path'})

##################### Welcoming #####################
smartPrint("Добро пожаловать в наш новый чат бот, созданный специально для изучения Английского Языка!")
while True:
	n()
	showArrayValues (lessons_list[0], "Выберите тему для урока:")
	match inputHandler(input('> ')):
		case 0:
			present_simple.initialise()
		case 1:
			present_continuous.initialise()
		case 2:
			future_simple.initialise()
		case 3:
			die()