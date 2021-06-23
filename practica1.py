from AG import AG

class Practica_1:
    def __init__(self):
        self.salir = False
        #self.AG = AG()
    def menu(self):
        while not self.salir:
            lista = []
            print("Elige la expresión a evaluar")
            print("1. x^2")
            print("2. 40*sin(x)")
            print("3. cos(x)+x")
            print("4. (1000/abs(50-x))+x")
            print("5. (1000/abs(30-x))+(1000/abs(50-x))+(1000/abs(80-x))")
            opcion = int(input())
            lista.append(opcion)
            print("¿Qué deseas?")
            print("1. Maximizar")
            print("2. Minimizar")
            opcion = int(input())
            lista.append(opcion)
            opcion = int(input("Número de cromosomas: "))
            lista.append(opcion)
            opcion = int(input("Número de generaciones: "))
            lista.append(opcion)
            print("Intervalo de x")
            opcion = int(input("De:"))
            lista.append(opcion)
            opcion = int(input("Hasta:"))
            lista.append(opcion)


            obj = AG(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5])
            obj.iniciar_algoritmo()
            #obj.iniciar_algoritmo(lista)
            opcion = int(input("¿Volver a ejecutar programa? 1. Sí 2.No y salir. "))
            if opcion == 1:
                lista.clear()
                opcion = 0
            elif opcion ==2:
                self.salir = True
                
obj = Practica_1()
obj.menu()