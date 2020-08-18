from threading import *
import time

class Flight:

    def __init__(self,available):
        self.available=available
        self.l=Lock()
        print("constructor", self.l)


    def reserve(self,required):
        self.l.acquire(blocking=True, timeout=-1)
        print("reserve fun begins ", self.l)
        print('Available seats:',self.available)

        if(self.available >= required):
            time.sleep(4)           # beocz of sleep the output is not in correct order
            name=current_thread().name
            print(f'{required} seat is alloted to {name}')
            self.available-=required

        else:
            print(f'sorry{current_thread().name}!!! All seats has been Reserved')

        self.l.release()

f=Flight(2)
user1=Thread(target=f.reserve,args=(1,),name="Ram")
user2=Thread(target=f.reserve,args=(1,),name="Ramaa")
user3=Thread(target=f.reserve,args=(1,),name="Shyam")
user1.start()
user2.start()
user3.start()
