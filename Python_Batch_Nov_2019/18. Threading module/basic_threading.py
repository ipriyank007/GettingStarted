import threading
import time

class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            time.sleep(0.5)
            print(self.getName())

start_time = time.time()
x1 = Messenger(name='Send Message')
x2 = Messenger(name='Recieve Message')


x1.start()
x2.start()

x1.join()
x2.join()

end_time = time.time()

print(f'process took {end_time - start_time}')