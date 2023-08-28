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

print("Estado Inicial:", estadoInicial)
print("Alfabeto:", alfabeto)
print("Estados:", estados)
print("Estados Finais:", estadosFinais)
print("Nodos:", nodos)

#####################################

#função para simular Automato Finito Determinístico
def simulaAFD():
    word = input("Informe a palavra: ")
    estadoAtual = estadoInicial
    

    def buscaNodo(estado, letra):
        for nodo in nodos:
            n = nodo.split(" ")
            if n[0] == estado and n[2] == letra:
                return n[1]
        return None
    print("----------------")   
    print(estadoAtual+"\n|\nv")
    i = -1
    for letter in word:
        i += 1
        estadoAtual = buscaNodo(estadoAtual, letter)
        if estadoAtual is None:
            print("Estado ou Alfabeto inválido")
            print("False :(")
            break
        if i != len(word) - 1:
            print(estadoAtual+", "+letter)
            print("|")
            print("v")
        else:
            print(estadoAtual+", "+letter)
            if estadoAtual in estadosFinais:
                print("True :)")
            else:
                ("Estado "+estadoAtual+" não é um estado Final.")
                print("False :(")

simulaAFD()
