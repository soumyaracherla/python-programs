import threading

def worker():
    """thread worker function"""
    print("Worker starts running..")
    return

def hello(num):
    print("Hello ",num)
    return

threads = []
for i in range(5):
    #create a new thread
    t=threading.Thread(target=hello,args=(i,))
    #threads are added to list
    threads.append(t)
    # starting the thread execution
    t.start()