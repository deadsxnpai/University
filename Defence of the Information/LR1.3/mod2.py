import re
import sys 

def regular(mode, text):
	if mode == 'word': template = r"[А-ЯЁa-яё\s]"
	else: template = r"[0-9]" 
	return re.findall(template, text)

def cryptWord(keyWord, gamma):
    arrayKeyWord = regular('word', keyWord)
    arrayGamma = regular('word', gamma)
    if len(gamma) < len(keyWord):
        df = len(keyWord)-len(gamma)
        arrayGamma*= df+1
    res = ''
    for i in range(len(arrayKeyWord)):
        res += str(ord(arrayKeyWord[i].encode('cp1251')) ^ ord(arrayGamma[i].encode('cp1251')))+' '
    return res

if __name__ == '__main__':
    keyWord = input("Enter a keyword: ")

    gamma = input("Enter a gamma: ")
    r = cryptWord(keyWord, gamma)
    print('Result is '+ r)