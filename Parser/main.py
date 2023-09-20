import copy # <3
class Types:
    def __init__(self):
        self.null = 'null'
        self.equals = 'equals'
        self.number = 'number'
        self.identifier = 'identifier'
        self.oparen = 'oparen'
        self.cparen = 'cparen'
        self.EOF = 'EOF'
        self.binaryOperator = 'binaryOperator'

        
        self.let = 'let'
        self.const = 'const'
        self.semiColon = 'semiColon'

TokenTypes = Types()
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

'''node = copy.copy(nodes.BinaryExpr)

print(node.visualize())'''

class Parser:
    def __init__(self):
        self.program=None



    def at(self):
        return copy.copy(self.tokens[0])
    def eat(self):
        prev = self.tokens[0]
        del self.tokens[0]
        return prev
    def eatExpect(self, expectedType, err):
        prev = self.tokens[0]
        del self.tokens[0]

        if prev['type']==expectedType:
            pass
        else:
            raise Exception(err, prev)
        return prev
    def parse(self, tokens):
        self.tokens=tokens
        self.program=Node("Program", body=[])
        while not self.tokens[0]['type']=="EOF":
            x = self.parse_stmt()
            self.program.body.append(x)
        return self.program

    
    def parse_stmt(self):
        
        match self.at()['type']:
            case TokenTypes.let:
                return self.parse_var_declaration()
            case TokenTypes.const:
                return self.parse_var_declaration()
            case _:
                return self.parse_expr()
        #pass

    def parse_var_declaration(self):
        isConstant = self.eat()['type']=="const"
        print(isConstant)
        identifier = self.eatExpect("identifier", "expected identifier")
        if self.at()['type'] == "semiColon":
            self.eat()
            if isConstant:
                raise Exception("Parser error [X: no value]: No Value assigned to constant expression!")
            x = copy.copy(nodes.VarDeclaration)
            x.identifier=identifier
            x.constant=False

            return x
        self.eatExpect(TokenTypes.equals, "Expected equals token")

        x = copy.copy(nodes.VarDeclaration)
        x.value = self.parse_expr()
        x.identifier=identifier
        x.contant = isConstant
        declaration = x

        return declaration
        
        
    def parse_expr(self):
        return self.parse_additive_expr()
        #pass


    def parse_additive_expr(self):
        lft = self.parse_multiplicitave_expr()

        while self.at()['val']=="+" or self.at()['val']=='-':

            operator=self.eat()['val']
            right = self.parse_multiplicitave_expr()
            left = copy.copy(nodes.BinaryExpr)
            left.left=lft
            left.right=right
            left.operator=operator
        try:
            left
        except:
            left=lft
        return left

    def parse_multiplicitave_expr(self):
        lft = self.parse_idunno_expr()

        while self.at()['val']=="*" or self.at()['val']=='/' or self.at()['val']=='%':

            operator=self.eat()['val']
            right = self.parse_idunno_expr()
            left = copy.copy(nodes.BinaryExpr)
            left.left=lft
            left.right=right
            left.operator=operator
        try:
            left
        except:
            left = lft
        return left

    def parse_idunno_expr(self):
        lft = self.parse_primary_expr()

        while self.at()['val']=="^":

            operator=self.eat()['val']
            right = self.parse_primary_expr()
            left = copy.copy(nodes.BinaryExpr)
            left.left=lft
            left.right=right
            left.operator=operator
        try:
            left
        except:
            left=lft
        return left

    
    def parse_primary_expr(self):
        tk = self.at()['type']
        eat=self.eat()
        match tk:
            case "identifier":
                x=copy.copy(nodes.Identifier)
                x.symbol=eat['val']
                return x
            case "null":
                x = copy.copy(nodes.NullLiteral)
                return x
            case "number":
                x=copy.copy(nodes.NumericLiteral)
                x.value=int(eat['val'])
                return x
            case "binaryOperator":
                x=copy.copy(nodes.BinaryExpr)
                x.operator=eat['val']
                return x
            case "oparen":
                value = self.parse_expr()
                self.eatExpect("cparen", "Invalid Token found, expected `)`: ")
                return value
            case _:
                raise Exception("Invalid Token found: ", eat)
            
        return "error"
                


'''pars = Parser()

var = [{'val': 'nul', 'type': 'null'}, {'val': 'EOF', 'type': 'EOF'}]

pars.parse(var)'''



class Main:
    def __init__(self):
        self.parser = Parser()
        self.parsed = []

    def getParser(self):
        return self.parser
