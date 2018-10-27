#CLASSE DO MÉTODO DE EULER
class EulerClass:

	#CONSTRUTOR DA CLASSE, COM OS PARÂMETROS DA EQUAÇÃO
	def __init__(self, dt, ki, bi, x, y):
		self.dt = dt # 0 
		self.ki = ki # 0.01
		self.bi = bi # 1e-14
		self.x = x # Lista que vai armazenar os valores do eixo x
		self.y = y # Lista que vai armazenar os valores do eixo y

	#MÉTODO PARA CALCULAR O MÉTODO DE EULER
	def funcao(self, salto):	
		return self.bi + salto * (self.ki * (1 - self.bi) * self.bi)

	#NOME DO OBJETO, NÃO MAIS O ENDEREÇO DE MEMÓRIA
	def __str__(self):
		return 'Euler'

#CLASSE DO MÉTODO DE EULER MELHORADO
class EulerMelhoradoClass:

	#CONSTRUTOR DA CLASSE, COM OS PARÂMETROS DA EQUAÇÃO
	def __init__(self, dt, ki, bi, x, y):
		self.dt = dt # 0 
		self.ki = ki # 0.01
		self.bi = bi # 1e-14
		self.x = x # Lista que vai armazenar os valores do eixo x
		self.y = y # Lista que vai armazenar os valores do eixo y

	#MÉTODO PARA CALCULAR O MÉTODO DE EULER MELHORADO
	def funcao(self, salto):
		f1 = (self.ki * (1 - self.bi) * self.bi )
		f2 = (self.ki * (1 - (self.bi + salto * f1)) * (self.bi + salto * f1))
		fn = self.bi + (f1 + f2) / 2 * salto

		return fn

	#NOME DO OBJETO, NÃO MAIS O ENDEREÇO DE MEMÓRIA
	def __str__(self):
		return 'EulerMelhorado'

#CLASSE DO MÉTODO DE RUNGE KUTTA
class RungeKuttaClass:

	#CONSTRUTOR DA CLASSE, COM OS PARÂMETROS DA EQUAÇÃO
	def __init__(self, dt, ki, bi, x, y):
		self.dt = dt # 0 
		self.ki = ki # 0.01
		self.bi = bi # 1e-14
		self.x = x # Lista que vai armazenar os valores do eixo x
		self.y = y # Lista que vai armazenar os valores do eixo y

	#MÉTODO PARA CALCULAR O MÉTODO DE RUNGE KUTTA
	def funcao(self, salto):
		k1 = (self.ki * (1 - self.bi) * self.bi)
		k2 = (self.ki * (1 - (self.bi + salto * k1 * 0.5)) * (self.bi + salto * k1 * 0.5))
		k3 = (self.ki * (1 - (self.bi + salto * k2 * 0.5)) * (self.bi + salto * k2 * 0.5))
		k4 = (self.ki * (1 - (self.bi + salto * k3)) * (self.bi + salto * k3))
		kn = self.bi + salto * ((k1 + 2 * k2 + 2 * k3 + k4) / 6)

		return kn

	#NOME DO OBJETO, NÃO MAIS O ENDEREÇO DE MEMÓRIA
	def __str__(self):
		return 'RungeKutta'