import random
import json
from default_base_class import *

class cfg0_pkt(default_base_pkt):
    def __init__(self):
        super().__init__()   

    def bdf_fn_cfg0(self):
        self.bdf = random.randint(0, (2**9)-1)        
        self.conf_type = random.randint(0,1)
        self.ep = random.randint(0, 1)
        self.td = random.randint(0, 1)
        self.packet = {"bdf" : self.bdf, 
                       "conf_type" : self.conf_type, 
                       "block" : self.block, 
                       "ep" : self.ep, 
                       "td" : self.td
                       }

        # Print packet dictionary to console
        print(self.packet)

        return self.packet

    def save_packet(self, filename):
        with open(filename, 'a') as f:
            packet_str = json.dumps(self.packet)
            f.write(packet_str + '\n')

# Generate 10 packets and store them in a file
filename = 'out_dict.txt'
num_packets = 10

packets = []

for i in range(num_packets):
    packet = cfg0_pkt()
    packet_dict = packet.bdf_fn_cfg0()
    packets.append(packet_dict)

# Save packets to file
with open(filename, 'w') as f:
    for packet_dict in packets:
        packet_str = json.dumps(packet_dict)
        f.write(packet_str + '\n')
