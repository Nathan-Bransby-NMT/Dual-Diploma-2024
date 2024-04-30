import threading

from source import *


def main(*args, **kwargs) -> None:
    ...


MAIN_THREAD = threading.Thread(main())

if __name__ == '__main__':
    MAIN_THREAD.run()
