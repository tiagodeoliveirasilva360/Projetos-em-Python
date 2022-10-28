import enum
from tokenize import String
voto = "não"
encerrarvotação = "não"
votosx = 0
votosy = 0
votosz = 0
votosb = 0
nulo = 0
class Candidatos(enum.Enum):
    candidato_x = 889
    canditato_y = 847
    candidato_z = 515
    branco = 0
votototal = 0
while(encerrarvotação =="não"):
    voto="não"
    while(voto=="não"):
        print("Digite o número do candidato que deseja votar: ")
        try:
            votos = int(input())
            voto = str(input("Digite sim para confirmar: "))
            if(votos==889):
                votosx = votosx + 1
            elif(votos==847):
                votosy = votosy + 1
            elif(votos == 515):
                votosz = votosz + 1
            elif(votos == 0):
                votosb = votosb + 1
            else:
                nulo = nulo + 1
        except:
            print("caracter incorreto!")
    print ("Votação confirmada!")
    encerrarvotação = (input("Deseja encerrar votação? "))
print("votação encerrada")
if(votosx > votosy) and (votosx > votosz):
    mvotos = votosx
    melhorcandidato = Candidatos.candidato_x
elif(votosy > votosx) and (votosy > votosz):
    mvotos = votosy
    melhorcandidato = Candidatos.canditato_y
elif(votosz > votosx) and (votosz > votosy):
    mvotos = votosx
    melhorcandidato = Candidatos.candidato_z

candidatox = Candidatos.candidato_x
candidatoy = Candidatos.canditato_y
candidatoz = Candidatos.candidato_z
branco = Candidatos.branco

print("vencedor é: ",melhorcandidato.name," com ",mvotos,"votos")
print(candidatox.name," recebeu ",votosx, " votos")
print(candidatoy.name," recebeu ",votosy, " votos")
print(candidatoz.name," recebeu ",votosz, " votos")
print(branco.name," recebeu ",votosb, " votos")
print("nulo recebeu ",nulo, " votos")