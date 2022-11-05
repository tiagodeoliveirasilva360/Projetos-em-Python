class Carro:
    total_carro = 0

    def __init__(self,velocidade):
        self.velocidade = velocidade
        Carro.total_carro += 1
        
    def aumentarvelocidade(self,aum_vel):
        self.velocidade += aum_vel
    
    def reduzirvelocidade(self,red_vel):
        self.velocidade -=red_vel

c1 = Carro(int(input("digite a velocidade do carro: ")))
v=1
while(v!=0):
    v = int(input("digite [1] para acelerar\ndigite [2] para reduzir\ndigite [0] para manter: "))
    if(v==1):
        print("velocidade atual é: ",c1.velocidade)
        c1.aumentarvelocidade(int(input("quantos km deseja aumentar? ")))
    elif(v==2):
        print("velocidade atual é: ",c1.velocidade)
        c1.reduzirvelocidade(int(input("quantos km deseja reduzir? ")))
    elif(v==0):
        break
    else:
        print("valor não encontrado")
print("quantidade de carros registrado é: ",c1.total_carro)
        
c2 = Carro(int(input("digite a velocidade do carro: ")))
v=1
while(v!=0):
    v = int(input("digite [1] para acelerar\ndigite [2] para reduzir\ndigite [0] para manter: "))
    if(v==1):
        print("velocidade atual é: ",c2.velocidade)
        c2.aumentarvelocidade(int(input("quantos km deseja aumentar? ")))
    elif(v==2):
        print("velocidade atual é: ",c2.velocidade)
        c2.reduzirvelocidade(int(input("quantos km deseja reduzir? ")))
    elif(v==0):
        break
    else:
        print("valor não encontrado")
print("quantidade de carros registrado é: ",c2.total_carro)

        
c3 = Carro(int(input("digite a velocidade do carro: ")))
v=1
while(v!=0):
    v = int(input("digite [1] para acelerar\ndigite [2] para reduzir\ndigite [0] para manter: "))
    if(v==1):
        print("velocidade atual é: ",c3.velocidade)
        c3.aumentarvelocidade(int(input("quantos km deseja aumentar? ")))
    elif(v==2):
        print("velocidade atual é: ",c3.velocidade)
        c3.reduzirvelocidade(int(input("quantos km deseja reduzir? ")))
    elif(v==0):
        break
    else:
        print("valor não encontrado")
print("quantidade de carros registrado é: ",c3.total_carro)
print("velocidade do carro 1 é:",c1.velocidade)
print("velocidade do carro 2 é:",c2.velocidade)
print("velocidade do carro 3 é:",c3.velocidade)