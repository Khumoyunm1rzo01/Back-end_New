# class Person:
#     ism = ""
#     familiya = ""
#     yosh = 0
#     tugilgan_kun = ""

# person1 = Person()
# person1.ism = ("Kamol")
# person1.familiya = ("Olimov")
# person1.tugilgan_kun = "12-12-2005"
# person1.yosh = 27

# person2 = Person()

# person2.ism = ("Anvar")
# person2.familiya = ("Kozimov")
# person2.yosh = 30
# person2.tugilgan_kun = "25-04-2004"

# print(person1.tugilgan_kun)
# from datetime import datetime
# class Person:
#     def __init__(self, ism, familiya, yosh, tugilgan_sana):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
#         self.tugilgan_sana = tugilgan_sana

#     def get_info(self):
#         return f"{self.ism}-{self.familiya}"
    
#     def check_age(self):
#         today = datetime.now()
#         self.yosh = today.year - self.tugilgan_sana.year
#         return self.yosh


# person1 = Person("Kamol", "Olimov", 15, datetime(1994,6, 15))
# person2 = Person("Anvar", "Kozimov", 16, datetime(1991, 6, 25))
# print(person1.check_age())
# print(person1.yosh)
# print(person2.check_age())
# print(person2.yosh)
# # print(person1.get_info())

class TogriTortburchak:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def get_perimetr(self):
        return (self.a * self.b)

    def get_yuza(self):
        return self.a * self.b

    def get_max_size(self):
        return self.a if self.b > self.b else self.b
    
    def is_square(self):
        return 

t1 = TogriTortburchak(4, 7)
t2 = TogriTortburchak(10, 5)

print(t2.get_perimetr())
print(t2.get_yuza())
print(t2.get_max_size())
