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

        def bark(self):
            print("dog is barking....")
class cat(animal):
    pass

class puppies(dog):
    def weep(self):
        print("they do weep a lot")

animal1=animal()
animal1.eat()
animal1.walk()
animal1.sleep()


dog1=dog()
dog1.eat()
dog1.walk()     # inheriting the property of animal(walk)
dog1.bark()

cat1=cat()
cat1.sleep()

babydog=puppies()
babydog.weep()
babydog.eat()
babydog.walk()
babydog.sleep()