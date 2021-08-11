def var_name(variable):
    for name in globals():
        if eval(name) == variable:
            return(name)

class var:
    def __init__(self, var):
        self.var=var
    @property
    def float(self):
        return float(self.int)
    @property
    def int(self):
        if isinstance(self.var, str):
            return len(self.var)
        return int(self.var) 
    @property
    def str(self):
        s=str(self.var)
        assert isinstance(s, str)
        return s
    @property
    def bool(self):
        if isinstance(self.var, str):
            if self.var.lower()=="true":
                return True
            else:
                return False 
        return bool(self.var) # If self.var==0, returns 0. Else, returns 1
    def normalize(self): # Retrieved from https://micro.recursospython.com/recursos/como-quitar-tildes-de-una-cadena.html
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = self.str.replace(a, b).replace(a.upper(), b.upper())
        return s

if __name__=="__main__":
    If = "you are reading this,"
    you = var("are not importing this file")
    print(var_name(If), If, var_name(you), you.str)
