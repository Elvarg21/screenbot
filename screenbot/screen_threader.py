import threading
import time
try:
    import queue
except ImportError:
    import Queue as queue

DEFAULT_THREAD_NUMBER = 8
DEFAULT_DELAY = 0.5


class ScreenThread(threading.Thread):
    def __init__(self, input_queue, start_time):
        threading.Thread.__init__(self)
        self.input_queue = input_queue
        self.start_time = start_time

    def run(self):
        while True:
            input = self.input_queue.get()
            if input is None:
                self.input_queue.task_done()
                break
            move_start, move = input
            if move_start - time.time() + self.start_time.time < 0:
                self.start_time.fix_time(move_start - time.time() + self.start_time.time)
            '''while move_start - time.time() + self.start_time.time > 0:
                pass
            '''
            #print(move_start - time.time() + self.start_time)
            time.sleep(max(move_start - time.time() + self.start_time.time, 0))
            move.run()
            self.input_queue.task_done()


class UniversalTime:
    def __init__(self):
        self.time = time.time()

    def fix_time(self, diff_time):
        self.time = self.time - diff_time


def threaded_run(input_list, thread_number=DEFAULT_THREAD_NUMBER):
    move_queue = queue.Queue()
    key_queue = queue.Queue()
    for input in sorted(input_list):
        if input[1].__class__.__name__ == 'MouseMove':
            move_queue.put(input)
        else:
            key_queue.put(input)
    move_queue.put(None)
    for i in range(thread_number - 1):
        key_queue.put(None)

    start_time = UniversalTime()
    threads = [ScreenThread(move_queue, start_time)]
    for i in range(thread_number - 1):
        threads.append(ScreenThread(key_queue, start_time))
    print('treads created')
    #move_queue.join()
    #print('queue joining')
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
