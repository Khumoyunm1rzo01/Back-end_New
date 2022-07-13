class Universitet:
    def __init__(self, name=("ANDIJON DAVLAT UNIVERSITETI"), ism =("Humoyunmirzo") yo) -> None:
        self.name = name
        self.ism = ism
        self.yosh = yosh
        print("Person __init__function__called")
        def get_info(self):
            return f"{self.name}-{self.name}"

class Student(Universitet):
    def __init__(self, ismi, yosh) -> None:
        #    Person.__init__(self, first_name, last_name)
        self.ismi = ismi
        self.yosh = yosh
        super().__init__(name)
        self.course = course

s1 = Student("Humoyunmirzo", "Abduhalimov")
print(s1.get_info())