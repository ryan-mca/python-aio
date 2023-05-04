from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms

def read():
    print("(i) Setting up RFID")
    rfid = PiicoDev_RFID()

    print("(i) Place RFID device near RFID reader")

    while True:
        if rfid.tagPresent():
            id = rfid.readID()

            print(id)
    
        sleep_ms(100)