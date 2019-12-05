import time
import concurrent.futures

def job_to_do(sec):
    time.sleep(sec)
    return f'done sleeping...{sec} sec(s)'

t1 = time.time()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(job_to_do, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

    # results = executor.map(job_to_do, secs)
    
    # for result in results:
    #     print(result)

t2 = time.time()

print(f'Process took {t2-t1} sec(s)')

