import time

def countDown(seconds):
    while seconds > 0:
        min = int(seconds/60)
        sec = int(seconds % 60)

        timer = f'{min}:{sec}'
        print(timer)
        seconds -= 1
    print('time up')
seconds = input("Enter the time in no. of seconds > ")
countDown(int(seconds))