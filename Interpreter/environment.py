class Val:
    def __init__(self, kind, value):
        self.kind=kind
        self.value=value


class Environment:
    def __init__(self, parent=None):
        self.parent=parent
        self.variables={}

    def declare(self, varname, value):
        if varname in self.variables:
            raise Exception("Environment [0: variable exists]")
        self.variables[varname]=value
        return value

    def assignVar(self, varname, value):
        env=self.resolve(varname)
        env.variables[varname]=value
    
    def resolve(self, varname):
        if varname in self.variables:
            return self
        if self.parent==None: #might change that to return null instead
            raise Exception("Environment [1: non-existent variable] couldn't resolve: ", varname)
        return self.parent.resolve(varname)

    def get(self, varname):
        env = self.resolve(varname)
        return env.variables[varname]

'''Testing part:
env = Environment()
env2 = Environment(env)

env.declare("h", Val("null", "12"))
print(env2.get("h").value)

print(env.get("h").value)'''
