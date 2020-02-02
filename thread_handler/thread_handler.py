import threading

class ThreadHandler():
    def __init__(self):
        self.thread_list = list()

    def spawn_thread(self, target_func_name, args):
        t = threading.Thread(target=target_func_name, args=args)
        self.thread_list.append(t)

        t.start()

