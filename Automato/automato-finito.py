# Cria variáveis para ler do arquivo

# Exemplo

# q0
# a b
# q0 q1 q2 q3
# q1 q3
# q0 q1 a
# q1 q1 a
# q1 q2 b
# q2 q1 b
# q2 q3 a

# estadoInicial = "q0"
# alfabeto = [a, b]
# estados = [q0, q1, q2, q3]
# estadosFinais = [q1, q3]
# nodos = [q0 q1 a, q1 q1 a, q1 q2 b, q2 q1 b, q2 q3 a]

estadoInicial = ""
alfabeto = []
estados = []
estadosFinais = []
nodos = []

with open("./alfabeto.txt","r") as file:
    content = file.read()
    lines = content.split("\n")

estadoInicial = lines[0]
alfabeto = lines[1].split(" ")
estados = lines[2].split(" ")
estadosFinais = lines[3].split(" ")
nodos = lines[4:]

#Atividade 4----------------------------------
for i, nodo in enumerate(nodos):
    n = nodo.split(" ")
    if n[2] == "":
        nodos[i] = n[0]+" "+n[1]+" &"
#Atividade 4----------------------------------

print("Estado Inicial:", estadoInicial)
print("Alfabeto:", alfabeto)
print("Estados:", estados)
print("Estados Finais:", estadosFinais)
print("Nodos:", nodos)

isLooping = True

while isLooping == True:

    word = input("Informe a palavra: ")  
    #Atividade 4----------------------------------
    word = word.replace(" ", "&")
    #Atividade 4----------------------------------
    estadoAtual = estadoInicial

    def findNodo(estado, letra):
        for nodo in nodos:
            n = nodo.split(" ")
            if n[0] == estado and letra == n[2]:
                return n[1]
        return None
    print("----------------")   
    print(estadoAtual+"\n|\nv")

    i = -1
    for l in word:
        i += 1
        estadoAtual = findNodo(estadoAtual, l)
        if estadoAtual is None:
            print("\nFalse :( - Transição inválida")
            break
        else:
            print(estadoAtual+", "+l)
            if i != len(word) - 1:
                print("|\nv")
            else:
                if estadoAtual in estadosFinais:
                    print("\nTrue :)")
                else:
                    print("\nFalse :( - "+estadoAtual+" não é estado final")
    print("----------------")

   
    finalizar = input("Deseja finalizar? S - Sim; Qualquer outro - Não\n")
    
    if finalizar == "S":
        isLooping = False
    
print("Encerrando")

