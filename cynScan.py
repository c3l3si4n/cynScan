# imports
import socket, argparse

# definitions
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
parser = argparse.ArgumentParser("cynScan")
args = parser.parse_args()
parser.add_argument("address", help="ip address to be scanned")
parser.add_argument("port", type=int, help="port to be scanned")

# functions
def main():
    if not args.address:
        print("-a <address> argument missing | type -h for help")

    result = sock.connect_ex((args.address, args.port))

    if result == 0:
        print("Port %s at %s is open!" % (args.port, args.address))
    else:
        print("Port %s at %s is closed" % (args.port, args.address))


# call
main()
