import argparse
import rfid
   
def main():
    # Setting up argparser
    parser = argparse.ArgumentParser(
        prog="python-aio",
        description="Little script to control a few devices",
        epilog="License: GPLv3"
    )
    
    parser.add_argument(
        "-d", "--detailed",
        help="More detailed output on RFID",
        action="store_true")
    args = parser.parse_args()

    if args.detailed:
        rfid.read(True)
    else:
        rfid.read()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit("CTRL+C")