from thread_handler.thread_handler import ThreadHandler

def run_centre(l):
    import centre

def run_check_net(l):
    import check_net

handle = ThreadHandler()

handle.spawn_thread(run_centre, [None])
handle.spawn_thread(run_check_net, [None])