# Basic calculator implemented in Python

# Import standard Python libraries
import sys
from math import sqrt

# Import PyQt5 libraries
try:
	from PyQt5.QtCore import *
	from PyQt5.QtGui import *
	from PyQt5.QtWidgets import *
except ImportError:
	raise ImportError("PyQt5 libraries must be installed.")

# Global variables
num = 0.0
newNum = 0.0
sumIt = 0.0
sumAll = 0.0
operator = ""

opVar = False

# Main calculator class
class Calc(QMainWindow):

	def __init__(self):
		QMainWindow.__init__(self)
		self.initUI()

	# Calculator screen initialization
	def initUI(self):

		# "line" is the calculator "display" where input and results appear
		self.line = QLineEdit(self)
		self.line.move(5, 5)
		self.line.setReadOnly(True)
		self.line.setAlignment(Qt.AlignRight)
		font = self.line.font()
		font.setPointSize(40)
		self.line.setFont(font)
		self.line.resize(266, 70)

		# Following are the calculator buttons for numbers and functions
		zero = QPushButton("0", self)
		zero.move(5, 265)
		zero.resize(45, 40)

		one = QPushButton("1", self)
		one.move(5, 215)
		one.resize(45, 40)

		two = QPushButton("2", self)
		two.move(60, 215)
		two.resize(45, 40)

		three = QPushButton("3", self)
		three.move(115, 215)
		three.resize(45, 40)

		four = QPushButton("4", self)
		four.move(5, 165)
		four.resize(45, 40)

		five = QPushButton("5", self)
		five.move(60, 165)
		five.resize(45, 40)

		six = QPushButton("6", self)
		six.move(115, 165)
		six.resize(45, 40)

		seven = QPushButton("7", self)
		seven.move(5, 115)
		seven.resize(45, 40)

		eight = QPushButton("8", self)
		eight.move(60, 115)
		eight.resize(45, 40)

		nine = QPushButton("9", self)
		nine.move(115, 115)
		nine.resize(45, 40)

		switch = QPushButton("±", self)
		switch.move(60, 265)
		switch.resize(45, 40)
		switch.clicked.connect(self.Switch)

		point = QPushButton(".", self)
		point.move(115, 265)
		point.resize(45, 40)
		point.clicked.connect(self.Point)

		plus = QPushButton("+", self)
		plus.move(170, 265)
		plus.resize(45, 40)

		minus = QPushButton("-", self)
		minus.move(170, 215)
		minus.resize(45, 40)

		multiply = QPushButton("x", self)
		multiply.move(170, 165)
		multiply.resize(45, 40)

		divide = QPushButton("/", self)
		divide.move(170, 115)
		divide.resize(45, 40)

		percent = QPushButton("%", self)
		percent.move(225, 115)
		percent.resize(45, 40)
		percent.clicked.connect(self.Percent)

		equals = QPushButton("=", self)
		equals.move(225, 265)
		equals.resize(45, 40)
		equals.clicked.connect(self.Equal)

		squared = QPushButton("x²", self)
		squared.move(225, 215)
		squared.resize(45, 40)
		squared.clicked.connect(self.Squared)

		sqroot = QPushButton("√", self)
		sqroot.move(225, 165)
		sqroot.resize(45, 40)
		sqroot.clicked.connect(self.SqRoot)

		ce = QPushButton("CE", self)
		ce.move(54, 75)
		ce.resize(112, 40)
		ce.clicked.connect(self.CE)

		clear = QPushButton("C", self)
		clear.move(164, 75)
		clear.resize(112, 40)
		clear.clicked.connect(self.Clear)

		# Apply CSS styling to buttons
		nums = [zero, one, two, three, four, five, six, seven, eight, nine, ]
		operators = [ce, clear, plus, minus, multiply, divide, equals, ]
		others = [switch, squared, sqroot, point, percent, ]

		for i in nums:
			i.setStyleSheet("color: blue; font-weight: bold;")
			i.clicked.connect(self.Num)

		for i in (operators + others):
			i.setStyleSheet("color: red;")

		for i in operators[2:]:
			i.clicked.connect(self.operator)

		# Set window size and title and display it
		self.setGeometry(300, 300, 273, 320)
		self.setWindowTitle("PyQt5 Calculator")
		self.setFixedSize(273, 320)
		self.show()

	# Handle entry of numbers and display them on screen
	def Num(self):
		global num
		global newNum
		global opVar

		sender = self.sender()

		newNew = int(sender.text())
		setNum = str(newNew)

		if opVar == False:
			self.line.setText(self.line.text() + setNum)
		else:
			self.line.setText(setNum)
			opVar = False

	# Process operator action or complete operation on "="
	def operator(self):
		global sumIt
		global num
		global opVar
		global operator

		sumIt += 1

		# If this is intermediate calculation, complete it.
		if sumIt > 1:
			self.Equal()

		num = self.line.text()
		sender = self.sender()
		operator = sender.text()

		opVar = True

	# Check to see if decimal point exists in number and, if not, add it.
	def Point(self):
		print(self.line.text())
		if "." not in self.line.text():
			self.line.setText(self.line.text() + ".")

	# Complete calculation using the specified operator (+, -, x, /)
	def Equal(self):
		global num
		global newNum
		global sumAll
		global operator
		global opVar
		global sumIt

		sumIt = 0

		newNum = self.line.text()

		if operator == "+":
			sumAll = float(num) + float(newNum)

		elif operator == "-":
			sumAll = float(num) - float(newNum)

		elif operator == "/":
			sumAll = float(num) / float(newNum)

		elif operator == "x":
			sumAll = float(num) * float(newNum)

		self.line.setText(str(sumAll))
		opVar = True

	def Percent(self):
		global num

		num = float(self.line.text())
		num /= 100
		self.line.setText(str(num))

	def SqRoot(self):
		global num

		num = float(self.line.text())
		num = sqrt(num)
		self.line.setText(str(num))

	def Squared(self):
		global num

		num = float(self.line.text())
		num = num * num
		self.line.setText(str(num))

	def Switch(self):
		global num

		num = float(self.line.text())
		num = (-1.0) * num
		self.line.setText(str(num))

	def CE(self):
		self.line.backspace()

	def Clear(self):
		global num
		global newNum
		global sumAll
		global operator

		self.line.clear()

		num = 0.0
		newNum = 0.0
		sumAll = 0.0
		operator = ""


def main():
	app = QApplication(sys.argv)
	main = Calc()
	main.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()

