import Tokenizer.main as main
import Parser.main as parser
import Interpreter.main as interpreter
from Interpreter.environment import Environment
typ = 'command'

env = Environment()
env.declare("true", interpreter.Val("bool", True))
env.declare("false", interpreter.Val("bool", False))

env.declare("x", interpreter.Val("number", 100))
parser = parser.Main().getParser()
tokenizer = main.Main().getTokenizer()
interpreter = interpreter.Interpreter()
if typ=='file':
    with open("file.fok", 'r+') as f:
        var = f.read()
    print(var)

    # TOKENIZING

    
    tokenized_file = tokenizer.tokenize(var)
    tokenized_dict=tokenizer.formatResult()
    #print(tokenized_dict)
    #print('-'*80)

    # PARSING


    program = parser.parse(tokenized_dict)
    #print(program.visualizeBody())
    # INTERPRETTING
    

    
    result=interpreter.eval_program(program.visualizeBody(), env)
    print(result)
else:
    x=input("> ")
    while not x=='exit':
        # TOKENIZING
        tokenized_file = tokenizer.tokenize(x)
        tokenized_dict=tokenizer.formatResult()
        #print(tokenized_dict)



        # PARSING

        
        program = parser.parse(tokenized_dict)
        #print(program.visualizeBody())


        result=interpreter.eval_program(program.visualizeBody(), env)

        print(result.value)
        # REDO
        x=input("> ")
