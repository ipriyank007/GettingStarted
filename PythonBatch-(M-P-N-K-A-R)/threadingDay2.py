import threading
from queue import Queue
import time

print_lock = threading.Lock()

q = Queue()


def job_to_do(worker):
    time.sleep(0.5)

    with print_lock:
        print(threading.current_thread().name, worker)


def threader():
    while True:
        employees = q.get()
        job_to_do(employees)
        q.task_done()


for i in range(10):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
start = time.time()

for workers in range(20):
    q.put(workers)

q.join()

print("Process Completed and took: ", time.time()-start)
