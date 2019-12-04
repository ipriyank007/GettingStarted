import threading
import time

def job_to_do(time_to_wait):
    time.sleep(time_to_wait)
    print(f'Job done, waited for {time_to_wait} seconds')

def works(t):
    for i in range(2):
        job_to_do(t)

start_time = time.time()

threads = []

for i in range(10):
    t = threading.Thread(target=works, args=(i/2,))
    t.start()
    threads.append(t)

# print(threads)

for thread in threads:
    print(thread._started)
    thread.join()

end_time = time.time()

print(f'process took {end_time - start_time} seconds')

