#вроде работает но все равно выводит sys-usr

import zipfile
import json
import string

not_like = string.hexdigits
lovely_words = []

z = zipfile.ZipFile("test.json.zip", "r")
my_file = z.extract("test.json")
f_json = open(my_file, "r", encoding = "utf-8")
data = json.load(f_json)
	
def for_di(di):
	for key in di:
		if type(key) == dict:
			for_di(key)
		else:	
			key=str(key)
			hate = False #проверяем китайский ли ключ
			for symb in key:
				if symb in not_like:
					hate = True
					
			if hate == False:
				lovely_words.append(key)

			if type(di[key]) == dict:   #смотрим значение ключа
				for_di(di[key])
			
			elif type(di[key]) == list:
				for_li(di[key])
			else:
				di[key]=str(di[key])
				hate = False
				for symb in di[key]:
					if symb in not_like:
						hate = True
						
				if hate == False:
					lovely_words.append(di[key])
				
		 

			
def for_li(li):
	for elem in li:
		if type(elem) == list:
			for_li(elem)
		else:
			elem=str(elem)
			hate = False
			for symb in elem:
				if symb in not_like:
					hate = True
					
			if hate == False:
				lovely_words.append(elem)
				
for_di(data)


z.close()  #можно закрыть зип выше, после объявления data?

print(lovely_words)
