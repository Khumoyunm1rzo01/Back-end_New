class University:
    def __init__(self, nomi):
        self.nomi = nomi
    def get_name(self):
        return f'{self.nomi}'

class Student(University):
    def __init__(self, name, age, nomi):
        super().__init__(nomi)
        self.name = name
        self.age = age
    
    def fullname(self):
        return f"Mening ismim {self.name} yoshim {self.nomi} men o'qiyotgan universitet {self.age}"

p1 = Student("Humoyunmirzo", "Andijon Davlat Universiteti.", 21)

print(p1.fullname())