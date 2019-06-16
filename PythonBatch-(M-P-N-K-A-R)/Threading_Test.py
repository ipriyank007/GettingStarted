import threading


class NewMessenger(threading.Thread):
    def run(self):
        for _ in range(50):
            print(threading.currentThread().getName())


x = NewMessenger(name= 'Send out messages')
y = NewMessenger(name= 'receive messages')
x.start()
y.start()
