#IMPORTANDO O SISTEMA
import os

#MÉTODO QUE PEGA O DIRETÓRIO, VASCULHA OS ARQUIVOS E OS DELETA
def apagar(path):  
    dir = os.listdir(path)
    for file in dir:
    	newFile = path + str(file)
    	os.remove(newFile)

#MÉTODO COM UM MENU QUE DÁ AS OPÇÕES DE DELETE
def main():
	print('----- DELETANDO -----')
	print('1 - Apagar gráficos de uma pasta específica\n2 - Apagar todos os gráficos\n')
	
	try:
		opc = int(input('Digite a opção desejada: '))
		print('\n')

		if opc == 1:
			print('1 - Euler\n2 - EulerMelhorado\n3 - RungeKutta\n4 - Comparacao\n')

			opc2 = int(input("Digite a opção desejada: "))
			print('\n')

			if opc2 == 1:
				path = "/home/nascimento/Documents/Graficos/Euler/"
				apagar(path)
			
			elif opc2 == 2:
				path = "/home/nascimento/Documents/Graficos/EulerMelhorado/"
				apagar(path)

			elif opc2 == 3:
				path = "/home/nascimento/Documents/Graficos/RungeKutta/"
				apagar(path)

			elif opc2 == 4:
				path = "/home/nascimento/Documents/Graficos/Comparacao/"
				apagar(path)

			else:
				print('Opção não existe!')

		elif opc == 2:
			path = "/home/nascimento/Documents/Graficos/Euler/"
			apagar(path)

			path = "/home/nascimento/Documents/Graficos/EulerMelhorado/"
			apagar(path)

			path = "/home/nascimento/Documents/Graficos/RungeKutta/"
			apagar(path)

			path = "/home/nascimento/Documents/Graficos/Comparacao/"
			apagar(path)

		else:
			print('Opção não existe!')

	except ValueError:
		print('\nERRO! Digite somente números inteiros')

	except TypeError:
		print('\nERRO! Digite somente números inteiros')