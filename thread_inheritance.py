from threading import Thread
import time

# student is a child thread and Thread is parent or base class
class Student(Thread):
    def run(self):      # run is automaticall called no need to writes1.run()
        self.appeartest()

    def appeartest(self):
        print("appearing for the test")

        for i in range(5):
            print("question",i)

        #time.sleep(5)
        print(self.name,"finished test")


student1=Student()
student1.start()
student1.join()

student2=Student()
student2.start()
student2.join()

student3=Student()
student3.start()
