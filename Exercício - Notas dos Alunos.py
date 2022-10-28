from statistics import median
import string

nome = "Tiago de Oliveira Silva"
nota1 = 8.5 
nota2 = 6.5
media = (nota1 + nota2)/2
falta = 2

if (media < 7 or falta > 3):
    if(media < 7):
        print("Aluno ",nome," reprovado por nota com a note de: ",media)
    else:
        print("Aluno ",nome," reprovado por falta com ",falta," faltas.")
else:
    print("aluno está aprovado com a media de: ",media)