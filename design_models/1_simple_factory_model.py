# # -*- coding:utf-8 -*-
class Operation:

	def GetResult(self):
		pass


class OperationAdd(Operation):

	def GetResult(self):
		print("我是加法")
		return self.op1 + self.op2

class OperationSub(Operation):

	def GetResult(self):
		print("我是减法")
		return self.op1 - self.op2

class OperationMul(Operation):

	def GetResult(self):
		print("我是乘法")
		return self.op1 * self.op2

class OperationDiv(Operation):

	def GetResult(self):
		print("我是除法")

		try:
			result = self.op1 / self.op2
			return result
		except:
			print"error:divided by zero."
		return 0

class OperationUndef(Operation):

	def GetResult(self):

		print"Undefine operation."
		return 0

class OperationFactory:

	operation = {}
	operation["+"] = OperationAdd()
	operation["-"] = OperationSub()
	operation["*"] = OperationMul()
	operation["/"] = OperationDiv()
	print(operation)

	def createOperation(self, ch):

		if ch in self.operation:
			op = self.operation[ch]
		else:
			op = OperationUndef()
		return op

if __name__ == "__main__":
	op = raw_input("operator: ")
	opa = input("a: ")
	opb = input("b: ")
	factory = OperationFactory()
	cal = factory.createOperation(op)
	print("the operation is:".encode(encoding='utf-8'), cal)
	cal.op1 = opa
	cal.op2 = opb
	print cal.GetResult()
