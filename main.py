import time
import hashlib
from unittest import skip

class jujuba:
    print("\n"*20)
    print("✅on")
    time.sleep(2)
    print("\n"*20)

    def menu():
        time.sleep(1)
        print("     ☢️ Umbrella Corporation® ")
        print("")
        print("             (1) ➫  Register")
        print("             (2) ➫  Login")
        print("             (3) ➫  Exit")
        print("")
        escolha = input("")
        if escolha == "1":
            jujuba.registro()
        elif escolha == "2":
            jujuba.login()
        elif escolha == "3":
            jujuba.breakzin()

    def registro():
        rlogin = input("Digite seu Login: ")
        if len(rlogin) != 4:
            print("Error! (limite de 4 caracteres)")
        else:
            rsenha = input("Digite sua Senha: ")
            if len(rsenha) != 4:
                print("Error! (limite de 4 caracteres)")
            else:
                skip
                shash1 = (rsenha).encode("utf8")
                shash = hashlib.md5(shash1).hexdigest()
                with open("db.txt", "a") as database:
                    database.write(str(rlogin) + "," + (shash) + "\n")
                    print("Usuario criado com sucesso!")
                jujuba.menu()
        jujuba.registro()

    def login():
        time.sleep(1)
        slogin = input("Digite seu Login: ")
        time.sleep(1)
        with open("db.txt", "r") as database:
            texto = database.read()
            if slogin in texto:
                ssenha = input("Digite sua Senha: ")
                shash1 = (ssenha).encode("utf8")
                shash = hashlib.md5(shash1).hexdigest()
                if shash in texto:
                    print("\n"*30)
                    time.sleep(1)
                    print("⬛⬜⬜⬜")
                    time.sleep(0.4)
                    print("⬛⬛⬜⬜")
                    time.sleep(0.4)
                    print("⬛⬛⬛⬜")
                    time.sleep(0.5)
                    print("⬛⬛⬛⬛")
                    time.sleep(1)
                    print("\n"*30)
                    print("Logado com Sucesso!")
                    print("")
                    time.sleep(0.5) 
                    print("")
                    if slogin in 'db.txt':
                            print("Bem vindo")
                else:
                    print("Login ou senha invalida, tente novamente!")
                    jujuba.login()
            else:
                print("Login ou senha invalida, tente novamente!")
                jujuba.login()

    def breakzin():
        time.sleep(1)
        print("Saindo....")
        exit

if __name__ == '__main__':

    jujuba.menu()

