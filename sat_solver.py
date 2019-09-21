class Literal:
    def __init__(self, variable, is_positive):
        self.variable = variable
        self.is_positive = is_positive

    def __str__(self):
        if self.is_positive:
            return self.variable
        else:
            return "!{}".format(self.variable)

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

# naive immutable map implementation
# just does a copy over an underlying dict
class ImmutableMap:
    def __init__(self, mapping = None):
        self.mapping = mapping if mapping is not None else dict()

    def add(self, key, value):
        new_mapping = self.mapping.copy()
        new_mapping[key] = value
        return ImmutableMap(new_mapping)

    def contains(self, key):
        return key in self.mapping

    def get(self, key):
        return self.mapping[key]

class List:
    def __init__(self):
        pass

class Nil(List):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "nil"

class Cons(List):
    def __init__(self, head, tail):
        super().__init__()
        self.head = head
        self.tail = tail
        
    def __str__(self):
        return "cons({}, {})".format(self.head, self.tail)

def add_literal(immutable_map, variable, boolean):
    if immutable_map.contains(variable):
        if immutable_map.get(variable) == boolean:
            return immutable_map
        else:
            return None
    else:
        return immutable_map.add(variable, boolean)

# solve
def solve(goals, literals):
    if(isinstance(goals, Literal)):
        result = add_literal(literals, goals.variable, goals.is_positive)
        if(result == None):
            return None
        else:
            return result
    elif (isinstance(goals, Cons)):
        if(isinstance(goals.head, And)):
            result = solve(Cons(goals.head.left, Nil()), literals)
            return result
        elif(isinstance(goals.head, Or)):
            newList1 = literals
            newList2 = literals
            #leftResult = solve(goals.head.left, ImmutableMap())
            #rightResult = solve(goals.head.right, ImmutableMap())
            leftResult = solve(goals.head.left, newList1)
            rightResult = solve(goals.head.right, newList2)
            if(leftResult != None or rightResult != None):
                return literals
            else:
                return None

#solve_one
def solve_one(formula):
    return solve(Cons(formula, Nil()), ImmutableMap())

# tests that should be satisfiable
sat_tests = [
             And(Or(Literal("a", True), Literal("b", False)), Literal("b", True)),
             # (a || !b) && b
            
             And(Or(Literal("a", True), Literal("a", False)), Literal("a", True)),
             #(a || !a) && a
            
             And(Or(Literal("x", True), Literal("y", False)), Or(Literal("y", False), Literal("z", True))),
             # (x || !y) && (!y || z)
             ] 

# tests that should be unsatisfiable
unsat_tests = [
               And(Literal("x", True), Literal("x", False)) 
               # x && !x
              ] 

def run_tests():
    tests_failed = False
    for test in sat_tests:
        if solve_one(test) is None:
            print("Failed: {}".format(test))
            print("\tWas UNSAT, should have been SAT")
            tests_failed = True

    for test in unsat_tests:
        if solve_one(test) is not None:
            print("Failed: {}".format(test))
            print("\tWas SAT, should have been UNSAT")
            tests_failed = True

    if not tests_failed:
        print("All tests passed")

if __name__ == "__main__":
    run_tests()
