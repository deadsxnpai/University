a = 7
m = 4096
 
main_str = input()
 
Y = [0] * 8
Y[0] = 502
for i in range(1,8):
    Y[i] = (a * Y[i-1]) % m
print(Y)
 
gamma = ""
for i in range(len(Y)):
    print(Y[i]%26+97)
    gamma += chr(Y[i]%26+97)
print(gamma)
 
result_str = ""
cnt = 0
for i in range(len(main_str)):
    print((ord(main_str[i]) ^ ord(gamma[cnt]))+97)
    result_str += chr((ord(main_str[i]) ^ ord(gamma[cnt]))+97)
    if cnt == 7:
        cnt = 0
print(result_str)