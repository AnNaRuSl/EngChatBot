import re

def preg_match(regex, text):
	return bool(re.search(regex, text))


def preg_replase(regex, replacement, text):
	return re.sub(regex, replacement, text)

def preg_get(regex, text):
	match = re.search(regex, text)
	whatIWant = match.group(1) if match else None
	return whatIWant