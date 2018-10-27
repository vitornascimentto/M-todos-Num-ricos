#IMPORTANDO O MODULO DOS MÉTODOS
import moduloMetodos

#IMPORTANDO O MODULO DOS CÁLCULOS
import moduloCalculos

#MÉTODO COM UM MENU QUE DÁ AS OPÇÕES DE EXECUÇÃO
def main():
	print('----- EXECUTANDO -----')
	print('1 - Fazer mais de uma execução\n2 - Fazer uma execução com todos no mesmo gráfico\n3 - Fazer somente uma execução\n')

	try:
		opc = int(input('Digite a opção desejada: '))
		print('\n')

		if opc == 1:	
			try:
				inicioSalto = float(input('Digite o inicio do salto: '))
				finalSalto = float(input('Digite o final do salto: '))
				salto = float(input('Digite o valor do salto: '))
				limite = float(input('Digite o valor do limite: '))

				auxSalto = inicioSalto
				contador = 1

				objectEuler = moduloMetodos.EulerClass(0, 0, 0, 0, 0)
				objectEulerMelhorado = moduloMetodos.EulerMelhoradoClass(0, 0, 0, 0, 0)
				objectRungeKutta = moduloMetodos.RungeKuttaClass(0, 0, 0, 0, 0)

				moduloCalculos.calcularVariasVezes(objectEuler, salto, limite, auxSalto, contador, finalSalto)
				moduloCalculos.calcularVariasVezes(objectEulerMelhorado, salto, limite, auxSalto, contador, finalSalto)
				moduloCalculos.calcularVariasVezes(objectRungeKutta, salto, limite, auxSalto, contador, finalSalto)

			except ValueError:
				print('\nERRO! Digite somente números')
			except TypeError:
				print('\nERRO! Digite somente números')

		elif opc == 2:
			try:
				salto = float(input('Digite o valor do salto: '))
				limite = float(input('Digite o valor do limite: '))

				objectEuler = moduloMetodos.EulerClass(0, 0, 0, 0, 0)
				objectEulerMelhorado = moduloMetodos.EulerMelhoradoClass(0, 0, 0, 0, 0)
				objectRungeKutta = moduloMetodos.RungeKuttaClass(0, 0, 0, 0, 0)

				moduloCalculos.calcularUmaVezMesmoGrafico(objectEuler, salto, limite)
				moduloCalculos.calcularUmaVezMesmoGrafico(objectEulerMelhorado, salto, limite)
				moduloCalculos.calcularUmaVezMesmoGrafico(objectRungeKutta, salto, limite)

			except ValueError:
				print('\nERRO! Digite somente números')
			except TypeError:
				print('\nERRO! Digite somente números')

		elif opc == 3:
			try:
				salto = float(input('Digite o valor do salto: '))
				limite = float(input('Digite o valor do limite: '))

				objectEuler = moduloMetodos.EulerClass(0, 0, 0, 0, 0)
				objectEulerMelhorado = moduloMetodos.EulerMelhoradoClass(0, 0, 0, 0, 0)
				objectRungeKutta = moduloMetodos.RungeKuttaClass(0, 0, 0, 0, 0)

				moduloCalculos.calcularUmaVez(objectEuler, salto, limite)
				moduloCalculos.calcularUmaVez(objectEulerMelhorado, salto, limite)
				moduloCalculos.calcularUmaVez(objectRungeKutta, salto, limite)

			except ValueError:
				print('\nERRO! Digite somente números')
			except TypeError:
				print('\nERRO! Digite somente números')

		else:
			print('Opção não existe!')

	except ValueError:
		print('\nERRO! Digite somente números inteiros')

	except TypeError:
		print('\nERRO! Digite somente números inteiros')