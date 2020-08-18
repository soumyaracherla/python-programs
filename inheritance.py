# SINGLE INHERITANCE

class animal:
    def eat(self):
        print("animal is eating....")

    def walk(self):
        print("animal is walking....")

    def sleep(self):
        print("animal is sleeping...")

class dog(animal):
        def eat(self):
            print("dog is eating the bones...")

class cat(animal):
    pass

animal1=animal()
animal1.eat()
animal1.walk()
animal1.sleep()


dog1=dog()
dog1.eat()
dog1.walk()         # inheriting the property of animal(walk)

cat1=cat()
cat1.sleep()