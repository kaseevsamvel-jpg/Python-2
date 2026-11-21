import time

def get_system_time():
    seconds = time.time()
    now = time.ctime(seconds)
    return now

print(get_system_time())

