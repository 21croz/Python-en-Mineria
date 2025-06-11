class Person:
    def __init__(self, name, age, job, area):
        self.name = name
        self.age = age
        self.job = job
        self.area = area

    def greet(self):
        print(f"Hola, soy {self.name}, tengo {self.age} años, soy {self.job}, y trabajo en el área de {self.area}.")
        return
    
    def greet_income(self):
        print(f"Soy {} y gano {}")



class Machine:
    def __init__(self, type, model, performance):
        self.type = type
        self.model = model
        self.performance = performance
        return
    
    def presentation(self):
        print(f" Tipo: {self.type}\n Modelo: {self.model}\n Rendimiento: {self.performance}")
        return
    
    def fuel(self, distance):
        needed_fuel = distance/self.performance
        print(f"Para avanzar {distance} km, necesitamos {needed_fuel} litros de combustible.")
        return        


class Rock:
    def __init__(self, rocktype, density, grade):
        self.rocktype = rocktype
        self.density = density
        self.grade = grade
    
    def value(self, volume, price, recovery, costs):
        block_tonnage = volume * self.density
        earnings = block_tonnage * price * (recovery / 100) * (self.grade / 100) * 2204.6
        losses = costs * block_tonnage
        block_value = earnings - losses
        print(f"El valor del bloque es: ${block_value}")
        return



# persona1 = Person("Hugo", 23, "Ingeniero", "Tronadura")
# persona1.greet()

# camion1 = Machine(type = "Camion", model = "CAT", performance = 0.2)
# camion1.presentation()
# camion1.fuel(100)

# rock1 = Rock(
#     rocktype = 'Calcopirita',
#     density = 2.78,
#     grade = 0.9)
# rock1.value(
#     volume = 1000,
#     price = 4,
#     recovery = 87,
#     costs = 5
# )

# AGREGAR ATRIBUTO SUELDO A LA CLASE PERSON.
# AGREGAR UN METODO QUE DIGA, 'Soy <nombre> y gano $<sueldo>'.
# AGREGAR UN METODO QUE, SI LA PERSONA ES MAYOR A 30, DUPLICAR EL SUELDO.
# CREAR PERSONA (mayor a 30).
# SALUDAR.
# DECIR SALARIO.
# USAR METODO DE AUMENTO DE SUELDO.
# DECIR SALARIO.