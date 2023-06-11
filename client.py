import sys
import socket
import logging
import time
#set basic logging
logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('172.18.0.5', 32444)
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    # Read File Content
    with open("test_file.txt", 'r') as f:
        content = f.readlines()
    # Send data
    message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ dari Mesin : {}'.format(int(sys.argv[1]))
    # message = 'INI ADALAH ISI FILE TXT : {}'.format(content)
    time.sleep(5)
    logging.info(f"sending {message}")
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        logging.info(f"{data}")
        
except Exception as ee:
    logging.info(f"ERROR: {str(ee)}")
    exit(0)
finally:
    logging.info("closing")
    sock.close()