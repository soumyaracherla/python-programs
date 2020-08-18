import threading
import time
from threading import Thread

for i in range(3):
    print("hello",i)

def appeartest(name):
    print("appearing for the test....",name)
    print("current thread::", threading.current_thread())
    #print(threading.enumerate())

#create a instance
t1= Thread(target=appeartest,args=("swathi",))
t1.start()
t1.setName("swathi")
time.sleep(3)
#print("current thread::",threading.current_thread())

t2= Thread(target=appeartest,args=("mayuri",))
t2.start()
t2.setName("mayuri")
time.sleep(3)
#print("current thread::",threading.current_thread())

t3= Thread(target=appeartest,args=("sowmya",))
t3.start()
t3.setName("sowmya")
time.sleep(3)
print(threading.enumerate())

print(time.ctime())
#print("current thread::",threading.current_thread())
#print(threading.current_thread().getName())
#print(threading.active_count())
#print(threading.enumerate())
#print(threading.get_ident())

