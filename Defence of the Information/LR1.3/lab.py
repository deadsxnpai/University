A = 11001010
B = 11000001
M = 2
Y0 = 11001010
 
 
def Gamma(y):
    gamma_list = []
    for _ in range(5):
        y = (A * y + B) % M
        gamma_list.append(y)
    return gamma_list
 
 
def Crypt():
    gamma = Gamma(Y0)
    res = open("Defence of the Information/LR1.3/Result.txt", "w",encoding="utf-8")
    with open('Defence of the Information/LR1.3/Sourse.txt', 'r',encoding="utf-8") as f:
        r_int = ""
        r=""
        while True:
            temp = f.read(8)
            if temp:
                for i, item in enumerate(temp):
                    r_int = r_int + " "+str(ord(item) ^ gamma[i])
                    r = r +" "+chr(ord(item) ^ gamma[i])
                    res.write(chr(ord(item) ^ gamma[i]))
 
            else:
                break
    print(r_int)
    res.close()
 
Crypt()
 
def DeCrypt():
    gamma = Gamma(Y0)
    res = open("Defence of the Information/LR1.3/NewResult.txt", "w",encoding="utf-8")
    with open('Defence of the Information/LR1.3/Result.txt', 'r',encoding="utf-8") as f:
        r_int = ""
        r = ""
        while True:
            temp = f.read(8)
            if temp:
                for i, item in enumerate(temp):
                    r_int = r_int + " " + str(ord(item) ^ gamma[i])
                    r = r + chr(ord(item) ^ gamma[i])
                    res.write(chr(ord(item) ^ gamma[i]))
            else:
                break
    print(r_int)
    res.close()
 
DeCrypt()
