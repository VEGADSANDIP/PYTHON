class person:
    surname = "vegad"
    def __init__(self, name):
        self.name = name #local variable

    def greet(self):
        print(f"Hello, I am {self.name}!")
        print(person.surname.capitalize())

person1 = person("sandip")
person1.greet() 
