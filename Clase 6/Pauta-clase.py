# CLASES
# Una clase corresponde a una estructura de la programación orientada a objetos (OOP) que permite definir y agrupar
# datos (atributos) y comportamientos (metodos) relacionados bajo una misma entidad lógica. Es una forma de modelar
# entidades del mundo real (como personas, rocas, maquinas de trabajo, etc.) en el código.
# Al crear una clase, se está creando una planilla a partir del cual se puede instanciar objetos. Cada objeto creado
# a partir de esa clase tiene su propia copia de los atributos definidos

# Para definir una clase, se debe hacer de la siguiente manera:

# class <NOMBRE_DE_LA_CLASE>:
#     def __init__(self, <ATRIBUTOS>):
#         <DEFINIR_ATRIBUTOS_DENTRO_DE_LA_CLASE>
#
#     def <NOMBRE_DEL_METODO>(self, <PARAMETROS_DE_ENTRADA_DEL_METODO>):
#         <LISTADO_DE_ACCIONES_DEL_METODO>
#         return



class Person:
    """
    Esta clase crea un objeto Persona, el cual recibe los atributos nombre, edad, trabajo y área
    """
    def __init__(self, name, age, job, area):
        self.name = name
        self.age = age
        self.job = job
        self.area = area
        return
    

    def greet(self):
        print(f"Hola, soy {self.name}, tengo {self.age} años, soy {self.job} y trabajo en el area de {self.area}.")
        return



class Maquina:
    def __init__(self, tipo, modelo, rendimiento):
        self.tipo = tipo
        self.modelo = modelo
        self.rendimiento = rendimiento
        return
    

    def presentación(self):
        print(f"{self.tipo} modelo {self.modelo}. Con un rendimiento de {self.rendimiento}.")
        return
    

    def consumo(self, distancia):
        fuel_lts = distancia/self.rendimiento
        print(f"La maquina avanzó {distancia} y consumió {fuel_lts} litros de combustible.")
        return



class Roca:
    def __init__(self, rock_type, density, cu_grade):
        self.rock_type = rock_type
        self.density = density
        self.cu_grade = cu_grade
        return
    

    def value(self, tonnage, price, recovery, costs):
        block_value = tonnage*price*(self.cu_grade/100)*(recovery/100)*2204.62 - costs*tonnage
        rounded_block_value = round(block_value, 2)
        print(f"El valor de esa roca es de ${rounded_block_value:,}")
        return



per1 = Person("Cristobal", 23, "ingeniero", "planificacion")
per1.greet()

maq1 = Maquina('Camion', 'CAT', 0.2)
maq1.presentación()
maq1.consumo(100)

rock1 = Roca(
    rock_type = "Calcopirita",
    density = 2.7,
    cu_grade = 0.7)
rock1.value(
    tonnage = 100,
    price = 4,
    recovery = 80,
    costs = 15)