
import random
from generator import *
import json

class checker_pkt(cfg0_pkt):

    def checker_fn(self, packet_check):
        block = packet_check["block"]
        bdf = packet_check["bdf"]
        conf_type = packet_check["conf_type"]
        ep = packet_check["ep"]
        td = packet_check["td"]

        print('checker_fn BDF = {}, config type {} for {}, {}, pkt is {}, ECRC is {}'.format(bdf, conf_type, "Switch" if conf_type else "end-point", "Blocking" if block else "Non-blocking", "Poisoned" if ep else "Not poisoned", "Enabled" if td else "Disabled"))

        if not (0 <= bdf < 2**8 and 0 <= conf_type <= 1 and 0 <= ep <= 1 and 0 <= td <= 1 and block == 1):
            print("Packet is invalid")
            return False
        else:
            print("Packet is valid")
            return True

# Read packets from file
filename = 'packets.txt'
packets = []

with open(filename, 'r') as f:
    for line in f:
        packet_dict = json.loads(line.strip())
        packets.append(packet_dict)

# Check packets and save results to file
with open('output.txt', 'w') as f:
    invalid_pkt = []
    valid_pkt = []

    for i, packet in enumerate(packets):
        c1 = checker_pkt()
        if not c1.checker_fn(packet):
            print(f'Packet {i} failed the checker!')
            invalid_pkt.append(i)
        else:
            print(f'Packet {i} passed the checker!')
            valid_pkt.append(i)

    f.write("Packet results:\n")
    for i, packet in enumerate(packets):
        f.write(f"Packet {i}: {'Failed' if i in invalid_pkt else 'Passed'}\n")

    f.write(f'Invalid packets: {invalid_pkt}\n')
    f.write(f'Valid packets: {valid_pkt}\n')

# Move output file to directory
import shutil
import os

output_file = 'output.txt'
destination = 'Desktop/pcie/pkt'

shutil.move(output_file, os.path.join(destination, output_file))

print(f"File '{output_file}' moved to directory: {destination}")
