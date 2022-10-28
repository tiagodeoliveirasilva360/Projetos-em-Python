rodas = int (input("Quantas rodas tem no veiculo? "))
pesobruto = float (input("Qual o peso bruto do veiculo? "))
pessoas = int (input("Quantas pessoas acomodam nesse veiculo? "))

if(rodas <= 3):
    print("A melhor categoria seria a A para o veiculo informado.")

elif(rodas == 4 and pessoas <= 8 and pesobruto <= 3500.0):
    print("A melhor categoria seria a B para o veiculo informado.")

elif(rodas>= 4 and pessoas <= 8 and pesobruto>= 3500 and pesobruto <= 6000):
    print("A melhor categoria seria a C para o veiculo informado.")

elif(rodas>= 4 and pessoas > 8):
    print("A melhor categoria seria a D para o veiculo informado.")

else:
    print("A melhor categoria seria a E para o veiculo informado.")