# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.


# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.

nomealunos=[]
numerodealunos=[]
while True:
    alunos=(input(f"digite o nome do aluno,quando terminar coloque 0:"))
    nomealunos.append(alunos)
    numerodealunos.append(alunos) 
    if alunos =="0":
        nomealunos.remove("0")
        break
    
print ("alunos presentes: {} ".format(len(nomealunos)))
print (nomealunos)
if len(alunos)<5:
    print("revise a lista de chamada")
else:
    print("tudo certo") 
    

