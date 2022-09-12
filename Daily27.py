class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


animal = Pet()
animal.set_animal("Dog")
animal.set_age("7")
animal.set_name("Clifford")

print(f"animal type: {animal.get_animal()}\nage: {animal.get_age()}\nname: {animal.get_name()}")