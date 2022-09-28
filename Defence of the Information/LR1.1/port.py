from re import findall
ONE = 1

stageOne = ['000'+str(x) for x in range(ONE,10)]
stageTwo = ['00'+str(x) for x in range(10,100)] 
stageThree = ['0'+str(x) for x in range(100,1000)] # 100 - 676
stageFour = [str(x) for x in range(1000,1156+ONE)]
keys = tuple(stageOne + stageTwo + stageThree+ stageFour)

alphabet = ["А","Б","В","Г","Д","Е","Ё","Ж","З","И",'Й',"К","Л","М","Н","О",
"П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я"," "]

del stageOne, stageTwo, stageThree,stageFour, ONE

coordinateX = tuple([alpha for alpha in alphabet]) # 65-91
coordinateY = tuple([alpha for alpha in alphabet])

cryptKeys = {x:None for x in keys}

counter = 0
for x in coordinateX:
	for y in coordinateY:
		cryptKeys[keys[counter]] = x + y
		counter += 1

del coordinateX, coordinateY, counter, keys

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode not in (E/D)")
	raise SystemExit
startMessage = input("Write the message: ").upper()

def regular(mode, text):
	if mode == 'E': template = r"[А-ЯЁ\s]{2}"
	else: template = r"[0-9]{3}" 
	return findall(template, text)

def encryptDecrypt(mode, message, final = ""):
	if mode == 'E':
		for symbol in message:
			if symbol not in [x for x in alphabet]: 
				message = message.replace(symbol,'')
		if len(message)%2 != 0: message += 'Х'
		for symbols in regular(mode, message):
			for key in cryptKeys:
				if symbols == cryptKeys[key]:
					final += key
	else:
		for number in regular(mode, message):
			if number in cryptKeys:
				final += cryptKeys[number]
	return final
print("Final message:",encryptDecrypt(cryptMode, startMessage))