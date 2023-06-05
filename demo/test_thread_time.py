import time
from threading import Thread, Event

# custom task function
def task():
    # execute a task in a loop
    for i in range(5):
        # block for a moment
        time.sleep(1)
        # report a message
        print('Worker thread running...')
    print('Worker closing down')


thread = Thread(target=task)
thread.start()