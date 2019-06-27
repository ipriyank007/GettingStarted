import threading
from queue import Queue
import time

printlock = threading.Lock()
start = time.time()
q = Queue()

def exampleEmp(emp):
    time.sleep(0.5)
    with printlock:
        print(threading.current_thread().name, emp)
        

def Threader():
    while True:
        employee = q.get()
        exampleEmp(employee)
        q.task_done()

for i in range(10):
    t = threading.Thread(target=Threader)
    t.daemon = True
    t.start()
for emp in range(10):
    q.put(emp)

q.join()

print('Process took', time.time()-start)
