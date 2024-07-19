import threading
def print_series():
    for i in range(0,10,2):
        print(i)
t1=threading.Thread(target=print_series)
print('Active Count',threading.active_count)
t1.start()
t1.join()