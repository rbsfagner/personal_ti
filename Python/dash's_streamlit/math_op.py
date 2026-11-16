# Modulo de operaçõs matemáticas

def sum(x,y):
    return x+y 

def subtract(x,y):
    return x-y

def multply(x,y):
    return x*y

def divide(x,y):
    if y != 0:
        return x / y
    else:
      raise ValueError("Não é possivel dividir por ZERO")  

