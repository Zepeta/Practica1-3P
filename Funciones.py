
import math
class Funciones:
    def __init__(self):
        self.x = 0
    def menu_funcion(self,tipo_funcion,x):
        if tipo_funcion ==1:
            return self.funcion1(x)
        elif tipo_funcion ==2:
            return self.funcion2(x)
        elif tipo_funcion ==3:
            return self.funcion3(x)
        elif tipo_funcion ==4:
            return self.funcion4(x)
        elif tipo_funcion ==5:
            return self.funcion5(x)
    def funcion1(self,x):
        return x**2
    def funcion2(self,x):
        return 40*math.sin(x)
    def funcion3(self,x):
        return x+math.cos(x)
    def funcion4(self,x):
        return (1000/(abs(50-x)))+x
    def funcion5(self,x):
        return (1000/(abs(30-x)))+(1000/(abs(50-x)))+(1000/(abs(80-x)))+x
