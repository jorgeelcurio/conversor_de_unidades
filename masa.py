def Kilogramos_a_Gramos(kg):
    g = kg * 1000
    return g

def Kilogramos_a_Toneladas(t):
    kg = t / 1000
    return kg

def gramos_a_kilogramos(g):
    kg = g / 1000
    return kg

def gramos_a_toneladas(g):
    t = g / 1000
    return t

def tonelada_a_kilogramos(t):
    kg = t * 1000
    return kg

def tonelada_a_gramos(t):
    g = t * 1000000
    return g

if __name__ == "__main__":

    print("Ejemplos de conversión de masa:")
    print("25kg a gr:", Kilogramos_a_Gramos(25))
    print("25kg a t:", Kilogramos_a_Toneladas(25))
    print("25g a kg:", gramos_a_kilogramos(25))
    print("25t a g:", gramos_a_toneladas(25))
    print("25kg a t:", tonelada_a_kilogramos(25))
    print("25g a t:", tonelada_a_gramos(25))
    




    
