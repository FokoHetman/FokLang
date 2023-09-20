import copy #<3 2

class Node:
    def __init__(self, kind, constant=None, identifier=None, body=None, value=0, left=None, symbol=None,right=None,operator=None):
        self.kind=kind
        self.body=body
        self.value=value
        self.left=left
        self.right=right
        self.symbol=symbol
        self.operator=operator
        self.identifier=identifier
        self.constant=constant
    def visualize(self):
        x={}
        for i in vars(self):
            if not vars(self)[i]==None:
                if i=='left' or i=='right':
                    x[i]=vars(self)[i].visualize()
                else:
                    x[i]=vars(self)[i]
        return x
    def visualizeBody(self):
        x=[]
        for i in self.body:
            if isinstance(i, Node):
                x.append(i.visualize())
        return x
class Nodes:
    def __init__(self):
        self.Program = Node("Program", body=[])
        self.Identifier = Node("Identifier", symbol=None)
        self.NumericLiteral = Node("NumericLiteral", value=0)
        self.Expr = Node("Expr", value=0)
        self.BinaryExpr = Node("BinaryExpr", left=self.Expr, right=self.Expr, operator=None)
        
        self.Stmt = Node("Stmt")
        self.NullLiteral = Node("NullLiteral", symbol=None)

        self.VarDeclaration = Node("VarDeclaration", constant=None, identifier=None, value=None)
nodes = Nodes()





# vals

class Val:
    def __init__(self, kind, value):
        self.kind=kind
        self.value=value






def isInt(num):
    return isinstance(num, int)


class ErrorHandler:
    def __init__(self):
        pass
    def binaryOpErrors(self, l, r):
        return not (isInt(l) and isInt(r))
    def divisionErrors(self, l, r):
        return r==0



    
errorHandler = ErrorHandler()
class Interpreter:
    def __init__(self):
        self.eval = None

    def eval_program(self, program, env):
        lastEval = Node("null", nodes.NullLiteral)
        for stat in program:
            lastEval = self.evaluate(stat, env)

        return lastEval


    def evaluate_binaryExpr(self, node, env):
        result = 0
        left = self.evaluate(node['left'], env).value
        right = self.evaluate(node['right'], env).value
        if errorHandler.binaryOpErrors(left,right):
            raise Exception("errorHandler.binaryOpErrors [13: Not int values]: ", left, right)
        match node['operator']:
            case "+":
                result = left+right
            case "-":
                result = left-right
            case "*":
                print(node)
                result = left*right
            case "/":
                if errorHandler.divisionErrors(left, right):
                    raise Exception("Interpreting error [14: errorHandler.divisionErrors]: Can't divide by 0!")
                result = left/right
            case "^":
                result = left**right
            case "%":
                result = left % right #modulus

        return Val("number", result)



    def eval_identifier(self, node, env):
        return env.get(node['symbol'])

    def eval_var_declaration(self, node, env):
        print(node)
        return env.declare(node['identifier']['val'], self.evaluate(node['value'].visualize(), env))
    def evaluate(self, node, env):
        match node['kind']:
            case "Program":
                return eval_program(node, env)
            case "NullLiteral":
                return Val("null", "null")
            case "NumericLiteral":
                return Val("number", node['value'])

            case "BinaryExpr":
                return self.evaluate_binaryExpr(node, env)
            case "Identifier":
                return self.eval_identifier(node, env)
            case "VarDeclaration":
                return self.eval_var_declaration(node, env)
            case _:
                raise Exception("Interpreting error [12: Unknown Node]: ", node)




    


                
'''prog = [{'kind': 'NullLiteral', 'value': 15}]


inter = Interpreter()
a = inter.eval_program(prog)
print(a.kind, a.value)'''
