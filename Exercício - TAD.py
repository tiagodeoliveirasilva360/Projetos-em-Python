class calculadora:
    n1 = complex
    n2 = complex
    n3 = complex

while(True):
    print("[1] para soma \n[2] para subtração \n[3] para mutiplicação \n[4] para divisão\n[0] para sair ")
    operacao = int(input("Digite a operação que irá fazer: "))
    def numeros():
        num = calculadora()
        num.n1 = complex (input("\ndigite o primeiro número "))
        num.n2 = complex (input("\ndigite o segundo número: "))
        num.n3 = complex (input("\ndigite o terceiro número: "))

        if(operacao > 4):
            print("Essa operação não existe?")
        elif(operacao == 1):
            soma = num.n1 + num.n2 + num.n3
            print(soma, " número real é: ",soma.real," número imaginarío é: ", soma.imag)
        elif(operacao == 2):
            sub = num.n1 -num.n2 - num.n3
            print( sub," número real é: ",sub.real," número imaginarío é: ",  sub.imag)
        elif(operacao == 3):
            mut = num.n1 * num.n2 * num.n3
            print(mut, " número real é: ",mut.real, " número imaginarío é: ", mut.imag)
        elif(operacao == 4):
            div = num.n1/num.n2/num.n3
            print(div, " número real é: ",div.real," número imaginarío é: ", div.imag )
    if(operacao == 0):
        print("Saindo")
        break
    numeros()