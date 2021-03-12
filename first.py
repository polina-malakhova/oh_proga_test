import re 

in_reference = False
ref_li=[]
f = open ("proceedings.txt", "r", encoding = "utf-8")
for line in f:
	if line == '':                             #пустая строка
		in_reference = False
	if in_reference == True:
		ref_li.append(line)
	if "References" in line:
		in_reference = True
f.close


find='.*[A-Z]?\.?\s?.*\.'


for refer in ref_li:
	match = re.findall(find, refer)
	print(match) 
	