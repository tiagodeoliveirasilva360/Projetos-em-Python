import string

pc = "false"
nome = input("digite o seu nome: ")

while(pc == "false"):
    print("digite a sua data de nascimento: ")
    try:
        datanasc = int(input())
        if(datanasc > 1922) and(datanasc < 2021):
            idade = 2022 - datanasc
            pc = "true"
        else:
            print("Ano de nascimento incorreto!")
    except:
        print("caracter invalido! ")

print("Seu nome é:",nome,"\nE sua idade é:",idade)