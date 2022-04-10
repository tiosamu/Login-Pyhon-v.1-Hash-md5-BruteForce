import hashlib
import time



def brute():
    eae = input ("Digite o MD5 hash da senha: ")
    for password in open("wordlist.txt", "r").readlines():
        hashed = hashlib.md5(password.strip().encode()).hexdigest()
        respostas(hashed,eae,password)

def respostas(hashed,eae,password):
    if hashed == eae:
        print(f"\nGotcha!\n         (づ￣ ³￣)づ \n\n          ↬Senha: {password}")
        time.sleep(1) 
    else:
        print("não achei :c")  

brute()