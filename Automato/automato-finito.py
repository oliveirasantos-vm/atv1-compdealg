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

def simulaAFD():
    word = input("Informe a palavra: ")  
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
                    print("----------------")
                    print("\nTrue :)")
                else:
                    print("----------------")
                    print("\nFalse :( - "+estadoAtual+" não é estado final")
    

def simulaAFND():
    word = input("Informe a palavra: ")
    word = word.replace(" ", "&")

    estadosAtuais = {estadoInicial}

    def findNodos(estados, letra):
        next_estados = []
        for estado in estados:
            for nodo in nodos:
                n = nodo.split(" ")
                if n[0] == estado and letra == n[2]:
                    next_estados.append(n[1])
        return next_estados

    print(estadosAtuais)

    for i, l in enumerate(word):
        next_estados = findNodos(estadosAtuais, l)
        if not next_estados:
            print("----------------")
            print("False :( - Transição inválida")
            break
        else:
            estadosAtuais = set(next_estados)
            print(estadosAtuais, ", "+l)
            if i == len(word) - 1:
                print("----------------")
                accepted = any(estado in estadosFinais for estado in estadosAtuais)
                if accepted:
                    print("True :)")
                else:
                    print("False :( - Nenhum estado final alcançado")

def Main():
    isLooping = True

    while isLooping:
        print("----------------")
        print("Escolha uma opção:")
        print("1 - Simular AFD")
        print("2 - Simular AFND")
        print("3 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            simulaAFD()
        elif opcao == "2":
            simulaAFND()
        elif opcao == "3":
            isLooping = False
            print("Encerrando")
        else:
            print("Opção inválida.")

Main()