#IMPORTANDO A LIB DE GRÁFICOS
import matplotlib.pyplot as plt

#IMPORTANDO O MODULO DOS MÉTODOS
import moduloMetodos

#CALCULAR MAIS DE UM GRÁFICO POR MÉTODO
def calcularVariasVezes(auxObject, salto, limite, auxSalto, contador, finalSalto):

	#CADA VEZ QUE ESSE WHILE RODA, ELE MUDA O SALTO, ASSIM MUDANDO A CURVA
	while True:
		nome = ''

		#ESSE IF E OS DOIS ELIF'S SERVEM PARA OLHAR QUAL O OBJETO QUE CHAMOU O MÉTODO PARA CHAMAR SEUS RESPECTIVO CÁLCULO
		if isinstance(auxObject, moduloMetodos.EulerClass):
			objeto = moduloMetodos.EulerClass(0, 0.01, 1e-14, [], [])
			caminho = "/home/nascimento/Documents/Graficos/Euler/" + str(contador)
			nome = 'Euler '

		elif isinstance(auxObject, moduloMetodos.EulerMelhoradoClass):
			objeto = moduloMetodos.EulerMelhoradoClass(0, 0.01, 1e-14, [], [])
			caminho = "/home/nascimento/Documents/Graficos/EulerMelhorado/" + str(contador)
			nome = 'Euler Melhorado '

		elif isinstance(auxObject, moduloMetodos.RungeKuttaClass):
			objeto = moduloMetodos.RungeKuttaClass(0, 0.01, 1e-14, [], [])
			caminho = "/home/nascimento/Documents/Graficos/RungeKutta/" + str(contador)
			nome = 'Runge Kutta '

		if auxSalto > finalSalto:
			break

		#ESSE WHILE CHAMA O MÉTODO DA CLASSE, CALCULANDO TUDO E JOGANDO NAS LISTAS, PARA GERAR O GRÁFICO
		while True:

			if objeto.bi > limite:		
				break

			#print(objeto.dt, objeto.bi)

			objeto.x.append(objeto.dt)
			objeto.y.append(objeto.bi)

			objeto.bi = objeto.funcao(auxSalto)

			objeto.dt += salto

		#CONFIGURAÇÕES PARA GERAR O GRÁFICO
		plt.clf()
		plt.title(nome + str(auxSalto))
		plt.xlabel('Passo')
		plt.ylabel('Porcentagem')
		plt.grid(True) 
		plt.plot(objeto.x, objeto.y)
		#plt.show()
		plt.savefig(caminho)

		auxSalto += salto
		contador += 1

#CALCULA UMA VEZ OS TRÊS MÉTODOS E FAZ UM ÚNICO GRÁFICO
def calcularUmaVezMesmoGrafico(auxObject, salto, limite):

	#ESSE IF E OS DOIS ELIF'S SERVEM PARA OLHAR QUAL O OBJETO QUE CHAMOU O MÉTODO PARA CHAMAR SEUS RESPECTIVO CÁLCULO
	if isinstance(auxObject, moduloMetodos.EulerClass):
		objeto = moduloMetodos.EulerClass(0, 0.01, 1e-14, [], [])
		caminho = "/home/nascimento/Documents/Graficos/Comparacao/Todos"

	elif isinstance(auxObject, moduloMetodos.EulerMelhoradoClass):
		objeto = moduloMetodos.EulerMelhoradoClass(0, 0.01, 1e-14, [], [])
		caminho = "/home/nascimento/Documents/Graficos/Comparacao/Todos"

	elif isinstance(auxObject, moduloMetodos.RungeKuttaClass):
		objeto = moduloMetodos.RungeKuttaClass(0, 0.01, 1e-14, [], [])
		caminho = "/home/nascimento/Documents/Graficos/Comparacao/Todos"

	#ESSE WHILE CHAMA O MÉTODO DA CLASSE, CALCULANDO TUDO E JOGANDO NAS LISTAS, PARA GERAR O GRÁFICO
	while True:

		if objeto.bi > limite:		
			break

		#print(objeto.dt, objeto.bi)

		objeto.x.append(objeto.dt)
		objeto.y.append(objeto.bi)

		objeto.bi = objeto.funcao(salto)

		objeto.dt += salto

	#CONFIGURAÇÕES PARA GERAR O GRÁFICO
	plt.title(str(salto))
	plt.xlabel('Passo')
	plt.ylabel('Porcentagem')
	plt.grid(True) 
	plt.plot(objeto.x, objeto.y)
	#plt.show()
	plt.savefig(caminho)

#CALCULA TODOS OS MÉTODOS UMA VEZ, E FAZ GRÁFICOS DIFERENTES PARA CADA UM DELES
def calcularUmaVez(auxObject, salto, limite):
	nome = ''

	#ESSE IF E OS DOIS ELIF'S SERVEM PARA OLHAR QUAL O OBJETO QUE CHAMOU O MÉTODO PARA CHAMAR SEUS RESPECTIVO CÁLCULO
	if isinstance(auxObject, moduloMetodos.EulerClass):
		objeto = moduloMetodos.EulerClass(0, 0.01, 1e-14, [], [])
		caminho = "/home/nascimento/Documents/Graficos/Euler/1"
		nome = 'Euler'

	elif isinstance(auxObject, moduloMetodos.EulerMelhoradoClass):
		objeto = moduloMetodos.EulerMelhoradoClass(0, 0.01, 1e-14, [], [])
		caminho = "/home/nascimento/Documents/Graficos/EulerMelhorado/1"
		nome = 'Euler Melhorado'

	elif isinstance(auxObject, moduloMetodos.RungeKuttaClass):
		objeto = moduloMetodos.RungeKuttaClass(0, 0.01, 1e-14, [], [])
		caminho = "/home/nascimento/Documents/Graficos/RungeKutta/1"
		nome = 'Runge Kutta'

	#ESSE WHILE CHAMA O MÉTODO DA CLASSE, CALCULANDO TUDO E JOGANDO NAS LISTAS, PARA GERAR O GRÁFICO
	while True:

		if objeto.bi > limite:		
			break

		#print(objeto.dt, objeto.bi)

		objeto.x.append(objeto.dt)
		objeto.y.append(objeto.bi)

		objeto.bi = objeto.funcao(salto)

		objeto.dt += salto

	#CONFIGURAÇÕES PARA GERAR O GRÁFICO
	plt.clf()
	plt.title(nome)
	plt.xlabel('Passo')
	plt.ylabel('Porcentagem')
	plt.grid(True) 
	plt.plot(objeto.x, objeto.y)
	#plt.show()
	plt.savefig(caminho)