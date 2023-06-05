from threading import Timer


def hello():
    print('こんにちは')


time = Timer(1, hello)

time.start()
