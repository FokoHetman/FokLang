


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



def isAlpha(src):
    return src.upper() != src.lower()

def charCode(fr, index):
    return ord(fr[index])

def isInt(src):
    try:
        _ = int(src)
        return True
    except:
        return False

def isSkippable(src):
    return src.isspace() or src==''





class Token:
    def __init__(self, Value, TokenType):
        self.val = Value
        self.type = TokenType
    def set(self, thing, value):
        a = self.toDict()
        a[thing]=value
        self.fromDict(a)


    def fromDict(self, dict):
        self.val = dict['val']
        self.type = dict['type']
    def toDict(self):
        return {"val": self.val, "type": self.type}
    def print(self):
        print(self.toDict())


keywords = {
"let": TokenTypes.let,
"const": TokenTypes.const,
"null": TokenTypes.null,

    }

        
class Tokenizer:
    def __init__(self):
        self.tokens = []
    def tokenize(self, source):
        self.tokens = []
        src = []
        lat="e"
        for i in source: src.append(i)
        while len(src)>0:
            if src[0]=="(":
                self.tokens.append(Token(src[0], TokenTypes.oparen))
            elif src[0]==")":
                self.tokens.append(Token(src[0], TokenTypes.cparen))
            elif src[0] in ["+", "-", "*", "/", "%", "^"]:
                self.tokens.append(Token(src[0], TokenTypes.binaryOperator))
            elif src[0]=="=":
                self.tokens.append(Token(src[0], TokenTypes.equals))
            elif src[0]==";":
                self.tokens.append(Token(src[0], TokenTypes.semiColon))
            else:
                if isInt(str(src[0])):
                    num = ""
                    
                    while len(src) > 0 and isInt(str(src[0])):
                        num = num + src[0]
                        lat = src[0]
                        del src[0]

                    self.tokens.append(Token(num, TokenTypes.number))
                elif isAlpha(src[0]):
                    ident = ""
                    while len(src)>0 and isAlpha(src[0]):
                        ident = ident + src[0]
                        del src[0]

                        
                    if ident in keywords:
                        self.tokens.append(Token(ident, keywords[ident]))
                    else:
                        self.tokens.append(Token(ident, TokenTypes.identifier))
            if len(src)>0 and isInt(lat)==False:
                del src[0]
            lat="e"
        self.tokens.append(Token("EOF", TokenTypes.EOF))
        return self.tokens
    def formatResult(self):
        l = []
        for i in self.tokens:
            l.append(i.toDict())
        return l

class Main:
    def __init__(self):
        self.tok = Tokenizer()
    def getTokenizer(self):
        return self.tok
