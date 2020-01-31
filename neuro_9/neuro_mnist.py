import numpy
import scipy.special


class neuralNetwork:
	def __init__(self, 
		inputnodes, hiddennodes, outputnodes, learningrate):
	# задать количество узлов во входном, скрытом и выходном слое
		self.inodes = inputnodes
		self.hnodes = hiddennodes
		self.onodes = outputnodes

		#Матрицы весовых коэфицентов связей wih и who
		#Весовые коэфиценты связей между узлом i и узлом j
		#следующего слоя обозначены как w_i_j:
		#w11 w21
		#w12 w22
		self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5),(self.hnodes, self.inodes)
		self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
		#коэфицент обучения
		self.lr = learningrate

		#использование сигмоиды в качестве функции активации
		self.activation_function = lambda x: scipy.special.explit(x)

		pass
		#тренировка нейронной сети
	def train():
		pass















