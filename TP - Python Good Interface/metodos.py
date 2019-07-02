from math import *

def calculoTrapezio(equacao,subIntervalos, a, b):

  h = (b-(a))/subIntervalos
  TAM = subIntervalos+1
  soma = 0

  vetorX = [TAM]
  vetorCI = [TAM]
  vetorY = [TAM]

#VETOR DOS VALORES DE X E CI
  vetorX[0] = a
  vetorCI[0] = 1
  i = 1
  while i<TAM:
      vetorX.append(vetorX[len(vetorX)-1]+h)
      vetorCI.append(2)
      i+=1 
  vetorX[subIntervalos] = b 
  vetorCI[subIntervalos] = 1

#VETOR DOS VALORES DE Y
  j = 1
  x = vetorX[0]
  vetorY[0] = eval(equacao)
  while j<TAM:
      x = vetorX[j]
      vetorY.append(eval(equacao))
      j+=1

  # CALCULO DA SOMA
  k = 0
  while k<TAM:
      soma+=(vetorCI[k]*vetorY[k])
      k+=1


#CALCULO DA INTEGRAL
  integral = (h*soma)/2
  return integral

def calculoPrimeiraSimpson(equacao, subIntervalos, a, b):
  #VARIAVEIS
  TAM = subIntervalos+1
  soma = 0

  #DISTANCIA ENTRE OS VALORES DE X
  h = (b-(a))/subIntervalos

  vetorX = [TAM]
  vetorCI = [TAM]
  vetorY = [TAM]

  #VETOR DOS VALORES DE X
  vetorX[0] = a
  i = 1
  while i<TAM:
      vetorX.append(vetorX[len(vetorX)-1]+h)
      i+=1 
  vetorX[subIntervalos] = b

  #VETOR DE VALORES DE CI
  vetorCI[0] = 1
  l = 1
  while l < TAM:
      if (l%2 == 1): 
          vetorCI.append(4)
      else:
          vetorCI.append(2)
      l+= 1
  vetorCI[subIntervalos] = 1

  #VETOR DE VALORES DE Y
  j = 1
  x = vetorX[0]
  vetorY[0] = eval(equacao)
  while j<TAM:
      x = vetorX[j]
      vetorY.append(eval(equacao))
      j+=1

  # CALCULO DA SOMA
  k = 0
  while k<TAM:
      soma+=(vetorCI[k]*vetorY[k])
      k+=1

  #CALCULO DA INTEGRAL
  integral = (h*soma)/3;
  return integral

def calculoSegundaSimpson(equacao, subIntervalos, a, b):
  #VARIAVEIS
  TAM = subIntervalos+1
  soma = 0

  #DISTANCIA ENTRE OS VALORES DE X
  h = (b-(a))/subIntervalos
  vetorX = [TAM]
  vetorCI = [TAM]
  vetorY = [TAM]

  #VETOR DOS VALORES DE X
  vetorX[0] = a
  i = 1
  while i<TAM:
      vetorX.append(vetorX[len(vetorX)-1]+h)
      i+=1 
  vetorX[subIntervalos] = b

  #VETOR DE VALORES DE CI
  vetorCI[0] = 1
  l = 1
  while l < TAM:
      if (l%3 == 0): 
          vetorCI.append(2)
      else:
          vetorCI.append(3)
      l+= 1
  vetorCI[subIntervalos] = 1

  #VETOR DE VALORES DE Y
  j = 1
  x = vetorX[0]
  vetorY[0] = eval(equacao)
  while j<TAM:
      x = vetorX[j]
      vetorY.append(eval(equacao))
      j+=1

  # CALCULO DA SOMA
  k = 0
  while k<TAM:
      soma+=(vetorCI[k]*vetorY[k])
      k+=1

  #CALCULO DA INTEGRAL
  integral = (3*h*soma)/8;
  return integral
