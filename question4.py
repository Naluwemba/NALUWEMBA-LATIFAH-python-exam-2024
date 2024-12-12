#4i)a)
#an OOP is used to define a certain class of different objects
#b)
# A class is a container that define attributes of objects or it defines and initiates
#  different objects while an object is a key which is assigned a value under a given class




#4ii)
sentence = "My name is latifah and My class is cohort 4"
word_counts = {}

for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts) 
# 
# 4iii)

# 
# 4(iv)
class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color

my_car = Car("2020 model", "Harrier", "Black")
print(my_car.brand) 
print(my_car.name)
print(my_car.color) 

#4(v)
class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color

    def start_engine(self):
        print(f"The engine of the {self.brand} {self.name} {self.color} car has started.")


my_car = Car("2020 model", "Harrier", "Black")
my_car.start_engine()