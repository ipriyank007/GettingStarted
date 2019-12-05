import threading
import time

def job_to_do(sec):
    time.sleep(sec)
    print('done sleeping...')

t1 = time.time()

threads = []

for _ in range(10):
    t = threading.Thread(target=job_to_do, args=(1,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

t2 = time.time()

print(f'process took {t2-t1} sec(s)')