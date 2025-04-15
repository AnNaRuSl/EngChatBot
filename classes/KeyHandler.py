from functions.basic import *
from functions.regex import *

class KeyHandler:
	def __init__(self, key_path):
		self.key_path = key_path

	def get_full_array(self):
		with open(self.key_path + ".txt", 'r', encoding='utf-8') as file:
			raw_lines = file.readlines()
			lines = []
			for line in raw_lines:
				line = preg_replase(r"\n", "", line)
				if preg_match(r"key\.", line):
					lines.append(line)
			return lines

	def get_string(self, key):
		raw_lines = self.get_full_array()
		for line in raw_lines:
			if preg_match(r"" + key + "=", line):
				line = preg_replase(r"" + key + "=", "", line)
				return line

	def get_strings_by_header(self, header):
		raw_lines = self.get_full_array()
		lines = []
		for line in raw_lines:
			if preg_match(r"" + "(" + header + ".+)=", line):
					line = preg_replase(r"" + "(" + header + ".+)=", "", line)
					lines.append(line)
			elif preg_match(r"" + "(" + header + "+)=", line):
				line = preg_replase(r"" + "(" + header + "+)=", "", line)
				lines.append(line)
		return lines