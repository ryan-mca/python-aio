from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms

def read(detailed=False):
    print("(i) Setting up RFID")
    while True:
        try:
            rfid = PiicoDev_RFID()

            print("(i) Place RFID device near RFID reader")

            while True:
                if rfid.tagPresent():
                    id = rfid.readID(detail=detailed)

                    print(id)
            
                sleep_ms(100)
        except OSError:
            print("(-) Make sure your RFID device is connected properly")
            sleep_ms(1000)

def write():
    return 1