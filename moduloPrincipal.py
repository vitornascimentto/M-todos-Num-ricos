#IMPORTANDO O MODULO DELETAR
import moduloDeletar

#IMPORTANDO O MODULO EXECUTAR
import moduloExecutar

#MÉTODO COM UM MENU QUE DA AS OPÇÕES PRINCIPAIS
def principal():
	try:
		print('1 - Gerar Gráficos\n2 - Apagar Gráficos Existentes\n')

		opc = int(input('Digite a opção desejada: '))
		print('\n')

		if opc == 1:
			moduloExecutar.main()
		
		elif opc == 2:
			moduloDeletar.main()
		
		else:
			print('Opção não existe')

	except ValueError:
		print('\nERRO! Digite somente números inteiros')

	except TypeError:
		print('\nERRO! Digite somente números inteiros')

#CHAMADA DO MÉTODO DA CLASSE PRINCIPAL, QUE POR CONSEQUENTE IRÁ CHAMAR TODOS OS OUTROS CONFORME FOR O DESEJO DO USUÁRIO
principal()