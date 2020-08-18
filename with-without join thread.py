import time
import threading

def sqrs(num):
    print("cal squares")
    for i in num:
        time.sleep(0.2)
        print("squares is::", i*i)


def cubes(num):
    print("cal cubes")
    for i in num:
        time.sleep(0.2)
        print("cubes is::",i*i*i)

arr=[2,3,4,5]

t1= threading.Thread(target=sqrs, args=(arr,))
t2=threading.Thread(target=cubes, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("i m done")


