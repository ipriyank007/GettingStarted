import threading

class MessengerApp(threading.Thread):
    def run(self):
        for i in range(20):
            print(threading.current_thread().getName())

send = MessengerApp(name='Sending Messages')
recv = MessengerApp(name='Reciving Messages')
send.start()
recv.start()