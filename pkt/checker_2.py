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
        print('Packet dictionary:', packet_check)

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
            f.write('Packet dictionary: {}\n'.format(packet))
            f.write(f'Packet {i} failed the checker!\n')
            
            #f.write('checker_fn BDF = {}, config type {} for {}, {}, pkt is {}, ECRC is {}'.format(c1.bdf, c1.conf_type, "Switch" if c1.conf_type else "end-point", "Blocking" if c1.block else "Non-blocking", "Poisoned" if c1.ep else "Not poisoned", "Enabled" if c1.td else "Disabled \n"))
            invalid_pkt.append(i)
        else:
            print(f'Packet {i} passed the checker!')
            f.write('Packet dictionary: {}\n'.format(packet))
            f.write(f'Packet {i} passed the checker!\n')
            
            #f.write('checker_fn BDF = {}, config type {} for {}, {}, pkt is {}, ECRC is {}'.format(c1.bdf, c1.conf_type, "Switch" if c1.conf_type else "end-point", "Blocking" if c1.block else "Non-blocking", "Poisoned" if c1.ep else "Not poisoned", "Enabled" if c1.td else "Disabled \n"))
            valid_pkt.append(i)


    f.write(f'Invalid packets: {invalid_pkt}\n')
    f.write(f'Valid packets: {valid_pkt}\n')


# Download output file
import shutil
import os

output_file1 = 'output.txt'
destination = 'Desktop/pcie/pkt'

shutil.move(output_file1, os.path.join(destination, output_file1))

print(f"File '{output_file1}' moved to directory: {destination}")
