import rfid
   
def main():
    rfid.read()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit("CTRL+C")