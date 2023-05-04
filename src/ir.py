from appdirs import user_config_dir
from piir.decode import decode
from piir.io import receive

def read(pin):
    keys = {}

    while True:
        data = decode(receive(pin))
        if data:
            name = input("Name for received data: ")
            break
    keys[name] = data
    print(keys)
