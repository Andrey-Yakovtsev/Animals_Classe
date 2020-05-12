from pprint import pprint


class Domestic_animals:
    domestic_animals_list = []
    objectcounter = 0
    milk = 0  # liters
    eggs = 0  # units
    wool = 0  # kg
    foodstatus = "hungry"
    waterstatus = "thirsty"
    sound = "silent"

    def __init__(self, name="None", weight=0):
        self.name = name
        self.weight = weight
        Domestic_animals.objectcounter += 1
        new_object_dict = dict(
            classname=Domestic_animals.__name__,
            #subclassname=Birds,
            object=self,
            name=self.name,
            weight=self.weight
        )
        Domestic_animals.domestic_animals_list.append(new_object_dict)


    def hydrate(self):
        self.waterstatus = "hydrated"

    def feed(self):
        self.foodstatus = "got food"

    def rest(self):
        self.status = "resting"

    def be_active(self):
        self.status = "is active"


# def make_a_sound(self):
# self.sound = "sound"

class Birds(Domestic_animals):
    def geteggs(self):
        self.eggs = "eggs collected"
        print(f'Добыли у {self.name} яичек')


class Horny_animals(Domestic_animals):

    def getmilk(self, liters):
        self.milk = self.milk - liters
        print(f'Надоили {liters}. У {self.name} осталось {self.milk} литров молока')

    def getwool(self):
        self.wool = "shaved"
        print(f'Получили с {self.name} шерсти клочок')


class Goose(Birds):
    sound = "Shshshsh"


class Chicken(Birds):
    sound = "QuKareqoooo"


class Duck(Birds):
    sound = "Krya-krya"


class Cow(Horny_animals):
    sound = "Moooo"


class Goat(Horny_animals):
    sound = "Meeeee"


class Sheep(Horny_animals):
    wool = 3  # kg
    sound = "Beee-Beeee"


Grey_Goose = Goose("Серый", 1.5)
Grey_Goose.eggs = 3

White_Goose = Goose("Белый", 2.5)
White_Goose.eggs = 4

Manka_Cow = Cow("Манька", 500)
Manka_Cow.milk = 25

Barashek_sheep = Sheep("Барашек", 80)
Barashek_sheep.milk = 1
Barashek_sheep.wool = 5

Qurly_sheep = Sheep("Кудряшка", 50)
Qurly_sheep.milk = 0
Qurly_sheep.wool = 3

Ko_Ko_chicken = Chicken("Ко-Ко", 2.2)
Ko_Ko_chicken.eggs = 5

Kukareku_chicken = Chicken("Кукареку", 2.8)
Kukareku_chicken.eggs = 4

Roga_goat = Goat("Рога", 65)
Roga_goat.wool = 2.8

Kopyta_goat = Goat("Копыта", 65)
Kopyta_goat.wool = 2

Kryakva_duck = Duck("Кряква", 3.8)
Kryakva_duck.eggs = 1


# Задача 2
# активности с животными

print("Работаем:")
Kryakva_duck.hydrate()
Manka_Cow.getmilk(15)
Kryakva_duck.geteggs()
Roga_goat.getwool()
print()
print("Получаем итоги работы:")
print(Kryakva_duck.waterstatus)
print(Manka_Cow.milk)
print(Kryakva_duck.eggs)
print(Roga_goat.wool)
print()


print("Получаем звуки:")
print(Kryakva_duck.sound)
print(Manka_Cow.sound)
print(Kryakva_duck.sound)
print(Roga_goat.sound)
print()


# Задача 3
# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.)



def animals_weight_list():
    i = 0
    animals_weight_list = []
    for weight in Domestic_animals.domestic_animals_list:
        #print(weight)
        animals_weight_list.append(weight['weight'])
        i+=1
    total_weight = sum(animals_weight_list)
    print(f'Общий вес всех животных {total_weight} кг.')

    max_weight = max(animals_weight_list)
    for heavy_animal_name in Domestic_animals.domestic_animals_list:
        if heavy_animal_name['weight'] == max_weight:
            print(f'Самое тяжелое животное весит {max(animals_weight_list)} кг. и зовется')
            print(heavy_animal_name['name'])

animals_weight_list()


