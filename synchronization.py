import threading
lock = threading.Lock() #create a lock instance
print("at Start::",lock)

def first_function():
    for i in range(5):
        lock.acquire()
        print('lock acquired',lock)
        print('Executing the first function')
        lock.release()
        print('lock released',lock)

def second_function():
    for i in range(5):
        lock.acquire()
        print('lock acquired',lock)
        print('Executing the second funcion')
        lock.release()


thread_one = threading.Thread(target=first_function)
thread_two = threading.Thread(target=second_function)

thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()
