#path = input("Informe o path do seu arquivo: ")
class Transicao:
  def __init__(self, transicaoAnt, estadoAnterior, estadoAtual, letra):
    self.transicaoAnt = transicaoAnt
    self.estadoAnterior = estadoAnterior
    self.estadoAtual = estadoAtual
    self.letra = letra

transicoes = []
def printTransicao(transicao):
  if transicao.transicaoAnt != None:
    printTransicao(transicao.transicaoAnt)
  print(transicao.estadoAnterior+" -> "+transicao.estadoAtual+", "+transicao.letra)

def printTransicoes(transicoes):
  for transicao in transicoes:
    printTransicao(transicao)

def compareTransicoes(transicao1, transicao2):
  if transicao1 == None and transicao2 == None:
    return True
  elif (transicao1 == None and transicao2 != None) or (transicao1 != None and transicao2 == None):
    return False
  elif compareTransicoes(transicao1.transicaoAnt, transicao2.transicaoAnt) and transicao1.estadoAnterior == transicao2.estadoAnterior and transicao1.estadoAtual == transicao2.estadoAtual and transicao1.letra == transicao2.letra:
    return True
  else:
    return False

def findNextEstado(transicaoAnterior, ultimoEstado, letra):
  estado = ""

  for transicao in transicoes:
    if ultimoEstado == transicao.estadoAnterior and letra == transicao.letra:
      #if compareTransicoes(transicaoAnterior, transicao.transicaoAnt) == True: 
      return transicao.estadoAtual
  
  return estado

estadoInicial = ""
alfabeto = []
estados = []
estadosFinais = []
transicoes = []

with open("./alfabeto.txt","r") as file:
  texto = file.read()
  linhas = texto.split("\n")

estadoInicial = linhas[0]
alfabeto = linhas[1].split(" ")
estados = linhas[2].split(" ")
estadosFinais = linhas[3].split(" ")
del linhas[0:4]

transicaoAnt = None

for linha in linhas:
  posicao = linha.split(" ")
  transicoes.append(Transicao(transicaoAnt, posicao[0], posicao[1],posicao[2]))
  transicaoAnt = Transicao(transicaoAnt, posicao[0], posicao[1],posicao[2])



print("Estado Inicial:")
print(estadoInicial)
print("\n")
print("Alfabeto:")
print(alfabeto)
print("\n")
print("Estados:")
print(estados)
print("\n")
print("Estado Final:")
print(estadosFinais)
print("\n")
print("Transições:")
printTransicao(transicoes[len(transicoes) - 1])
print("\n")

palavra = input("Informe a entrada:")
first = True
transicaoAnt = None
for l in palavra:
  if first:
    first = False
    estAtual = findNextEstado(transicaoAnt, estadoInicial, l)
    if estAtual == "":
      print("Recusado!")
    else:
      transicaoLocal = Transicao(transicaoAnt, estadoInicial, estAtual, l)
      transicaoAnt = transicaoLocal
  else:
    estAtual = findNextEstado(transicaoAnt, transicaoAnt.estadoAtual, l)
    if estAtual == "":
      print("Recusado!")
    else:
      transicaoLocal = Transicao(transicaoAnt, transicaoAnt.estadoAtual, estAtual, l)
      transicaoAnt = transicaoLocal

printTransicao(transicaoAnt)
