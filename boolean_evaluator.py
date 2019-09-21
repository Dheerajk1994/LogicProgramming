class Binop:
    def __init__(self, left, right, op_string):
        self.left = left
        self.right = right
        self.op_string = op_string

    def __str__(self):
        return "({} {} {})".format(
            str(self.left),
            self.op_string,
            str(self.right))

class And(Binop):
    def __init__(self, left, right):
        super().__init__(left, right, "&&")

class Or(Binop):
    def __init__(self, left, right):
        super().__init__(left, right, "||")

def eval_expr(expression):
	#print(expression.Binop.left 
	if(expression == True or expression == False):
		return expression
	else:
		leftEval = eval_expr(expression.left)
		rightEval = eval_expr(expression.right)
		if(expression.op_string == "&&"):
			return leftEval and rightEval
		else:
			return leftEval or rightEval

# tests that evaluate to true
true_tests = [And(True, True),
              Or(True, True),
              Or(True, False),
              Or(False, True),
              Or(And(False, True),
                 And(True, True))]

# tests that evaluate to false
false_tests = [And(True, False),
               And(False, True),
               And(False, False),
               Or(False, False),
               And(Or(True, False),
                   Or(False, False))]

def run_tests():
    tests_failed = False
    for test in true_tests:
        if not eval_expr(test):
            print("Failed: {}".format(test))
            print("\tWas false, should have been true")
            tests_failed = True

    for test in false_tests:
        if eval_expr(test):
            print("Failed: {}".format(test))
            print("\tWas true, should have been false")
            tests_failed = True

    if not tests_failed:
        print("All tests passed")

if __name__ == "__main__":
    run_tests()
