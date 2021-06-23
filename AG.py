import random
from Funciones import Funciones
class AG:
    def __init__(self,tipo_funcion,criterio,num_cromosas,num_generaciones,rango_inferior,rango_superior):
        self.Funciones = Funciones()
        self.tipo_funcion = tipo_funcion
        self.criterio = criterio
        self.num_cromosomas = num_cromosas
        self.num_generaciones = num_generaciones
        self.rango_inferior = rango_inferior
        self.rango_superior = rango_superior
        self.longitud_binario = 0
        self.cromosomas = []
        
    def iniciar_algoritmo(self):
        bits = self.representacion()
        print("La representación será binaria con una longitud de",bits,"bits")
        print("-----")
        print("La función de evaluación es: ", self.funcion_evaluacion(self.tipo_funcion))
        print("-----")
        print("La función de cruzamiento será de un solo punto, tal que h(x1,x2,p). siendo 1 <= p <=",bits-1)
        print("-----")
        print("la función de mutación, m(X^k,i) elegirá una posicion i de un cromosoma x^k donde 1 <= i <=",bits,"para cambiar el bit por su complemento. Se ejecutará cada generación par")
        print("-----")
        print("Las restricciones serán:\n",self.tipo_restricciones(self.tipo_funcion,self.rango_inferior,self.rango_superior))
        print("-----")
        valor = int(input("¿Desea continuar? 1. Sí. 2. No. "))
        if valor == 1:
            self.ejecutar_algoritmo()
        elif valor == 2:
            print("Fin")
    def ejecutar_algoritmo(self):
        self.crear_poblacion()
        i = 0
        while i<self.num_generaciones:
            if self.num_cromosomas%4==0:
                cromosomas_seleccionados = self.seleccion()
                self.cromosomas.clear()
                while cromosomas_seleccionados:
                    cromosoma1 = cromosomas_seleccionados.pop()
                    self.cromosomas.append(cromosoma1)
                    cromosoma2 = cromosomas_seleccionados.pop()
                    self.cromosomas.append(cromosoma2)
                    nuevo_individuo1,nuevo_individuo2 = self.cruzamiento(cromosoma1[0],cromosoma2[0])
                    decimal = self.pasar_a_decimal(nuevo_individuo1)
                    valor = self.restricciones(decimal)
                    if valor:
                        if [nuevo_individuo1,decimal] not in self.cromosomas:
                            self.cromosomas.append([nuevo_individuo1,decimal])
                        else:
                            valor = False
                            while not valor:
                                [nuevo_individuo,numero] = self.crear_individuo()
                                valor = self.restricciones(numero)
                            self.cromosomas.append([nuevo_individuo,numero])        
                    else:
                        valor = False
                        while not valor:
                            [nuevo_individuo,numero] = self.crear_individuo()
                            valor = self.restricciones(numero)
                        self.cromosomas.append([nuevo_individuo,numero])


                    decimal = self.pasar_a_decimal(nuevo_individuo2)
                    valor = self.restricciones(decimal)
                    if valor:
                        if [nuevo_individuo2,decimal] not in self.cromosomas:
                            self.cromosomas.append([nuevo_individuo2,decimal])
                        else:
                            valor = False
                            while not valor:
                                [nuevo_individuo,numero] = self.crear_individuo()
                                valor = self.restricciones(numero)
                            self.cromosomas.append([nuevo_individuo,numero]) 
                    else: 
                        valor = False
                        while not valor:
                            [nuevo_individuo,numero] = self.crear_individuo()
                            valor = self.restricciones(numero)
                        self.cromosomas.append([nuevo_individuo,numero])
            if i%2==0 and i!=0:
                num = random.randint(0,self.num_cromosomas-1)
                cromosoma_k = self.cromosomas[num][0]
                posicion = random.randint(1,self.longitud_binario)
                cromosoma_k = self.mutacion(cromosoma_k,posicion)
                

            print("Generación",i+1)
            for cromosoma in self.cromosomas:
                evaluacion = self.evaluar(cromosoma[1])
                cromosoma.append(evaluacion)
                print(cromosoma[0],cromosoma[1],cromosoma[2])
            i+=1

    def crear_poblacion(self):
        j=0
        while j<self.num_cromosomas: 
            [individuo,numero] = self.crear_individuo()
            valor_restriccion = self.restricciones(numero)
            if valor_restriccion:
                if [individuo,numero] not in self.cromosomas:
                    self.cromosomas.append([individuo,numero])
                    j+=1
        for cromosoma in self.cromosomas:
            evaluacion = self.evaluar(cromosoma[1])
            cromosoma.append(evaluacion)
            print(cromosoma[0],cromosoma[1],cromosoma[2])
        
    def seleccion(self):
        aux = self.cromosomas
        if self.criterio == 1:     
            self.cromosomas = sorted(aux,key=lambda aux: aux[2])
        elif self.criterio == 2:
            self.cromosomas = sorted(aux,key=lambda aux: aux[2],reverse=True)
        mitad = self.num_cromosomas//2
        cont = 0
        cromosomas_seleccionados = []
        while cont<mitad:
            cromosoma = self.cromosomas.pop()
            cromosomas_seleccionados.append([cromosoma[0],cromosoma[1]])
            cont+=1
        cromosomas_seleccionados.reverse()
        return cromosomas_seleccionados

    def evaluar(self,x):
        return self.Funciones.menu_funcion(self.tipo_funcion,x)

    def funcion_evaluacion(self,tipo_funcion):
        if tipo_funcion==1:
            return "x^2"
        elif tipo_funcion == 2:
            return "40*sin(x)"
        elif tipo_funcion == 3:
            return "cos(x)+x"
        elif tipo_funcion == 4:
            return "(1000/abs(50-x))+x"
        elif tipo_funcion == 5:
            return "(1000/abs(30-x))+(1000/abs(50-x))+(1000/abs(80-x))"
    
    def tipo_restricciones(self,tipo_funcion,rango_inferior, rango_superior):
        if tipo_funcion==1 or tipo_funcion ==2 or tipo_funcion ==3:
            return "R1: "+str(rango_inferior)+" <= x <= "+str(rango_superior)+"\n R2: No individuos duplicados"
        elif tipo_funcion == 4:
            return "R1: "+str(rango_inferior)+" <= x <= "+str(rango_superior)+"\n R2: No individuos duplicados\n R3: x!=50"
        elif tipo_funcion == 5:
            return "R1: "+str(rango_inferior)+" <= x <= "+str(rango_superior)+"\n R2: No individuos duplicados\n R3: x!=50\n R4: x!=30\n R5: x!=80"
    
    def representacion(self):
        sup = abs(self.rango_superior)
        inf = abs(self.rango_inferior)
        mayor = 0
        if sup>inf:
            mayor = sup
        else: mayor = inf
        binario = self.pasar_a_binario(mayor)
        self.longitud_binario = len(binario)-1
        return self.longitud_binario

    def crear_individuo(self):
        numero = random.randint(self.rango_inferior,self.rango_superior)
        individuo = self.pasar_a_binario(numero)
        return [individuo,numero]
    
    def restricciones(self,x):
        if x>=self.rango_inferior and x<=self.rango_superior:
            if self.tipo_funcion == 1 or self.tipo_funcion == 2 or self.tipo_funcion ==3 :
                return True
            elif self.tipo_funcion == 4:
                if x == 50:
                    return False
                else: 
                    return True
            elif self.tipo_funcion == 5:
                if x == 30 or x == 50 or x == 80:
                    return False
                else: 
                    return True
        else:
            return False
               
    def cruzamiento(self, individuo1,individuo2):
        p = random.randint(2,self.longitud_binario-1)
        nuevo_individuo1 = individuo1[:p]+individuo2[p:]
        nuevo_individuo2 = individuo2[:p]+individuo1[p:]
        return nuevo_individuo1,nuevo_individuo2

    def mutacion(self,individuo, indice):
        if individuo[indice-1] == 0:
            individuo[indice-1] = 1
        elif individuo[indice-1] == 1:
            individuo[indice-1] = 0
        return individuo

    def pasar_a_binario(self,decimal):
        decimal_inicial = decimal
        binario=""
        while abs(decimal) // 2 != 0:
            binario = str(abs(decimal) % 2) + binario
            decimal = abs(decimal) // 2
        binario = str(decimal)+binario    
        while len(binario)<self.longitud_binario:
            binario = "0"+binario
        if decimal_inicial<0: binario = "-"+binario
        elif decimal_inicial>0: binario = "+"+binario
        return binario
    
    def pasar_a_decimal(self,numero_binario):
        numero_decimal = 0 
        signo = numero_binario[0]
        numero_binario = numero_binario[1:]
        for posicion, digito_string in enumerate(numero_binario[::-1]):
            numero_decimal += int(digito_string) * 2 ** posicion
        if signo == "-":
            numero_decimal = -numero_decimal 
        return numero_decimal


# algoritmo = AG(1,2,8,10,-1000,1000) #tipo_funcion,criterio,num_cromosas,num_generaciones,rango_inferior,rango_superior
# algoritmo.iniciar_algoritmo()

