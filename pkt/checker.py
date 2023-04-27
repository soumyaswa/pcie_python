
import random
import json
from generator import *
print("checker block")

class checker_pkt(cfg0_pkt):

    def checker_fn(self, packet_dict):
        block = packet_dict["block"]
        bdf = packet_dict["bdf"]
        conf_type = packet_dict["conf_type"]
        ep = packet_dict["ep"]
        td = packet_dict["td"]

        print('checker_fn BDF = {}, config type {} for {}, {}, pkt is {}, ECRC is {}'.format(bdf, conf_type, "Switch" if conf_type else "end-point", "Blocking" if block else "Non-blocking", "Poisoned" if ep else "Not poisoned", "Enabled" if td else "Disabled"))
        
        if not (0 <= bdf < 2**8 and 0 <= conf_type <= 1 and 0 <= ep <= 1 and 0 <= td <= 1 and block == 1):
            print("Packet is invalid")
            return False
        else:
            print("Packet is valid")
            return True

c1 = checker_pkt()

invalid_pkt = []
valid_pkt = []

filename = 'packets.txt'
with open(filename, 'r') as f:
    packets = f.readlines()

for i, packet_str in enumerate(packets):
    packet_dict = json.loads(packet_str.strip())
    if not c1.checker_fn(packet_dict):
        print('Packet {} failed the checker!'.format(i))
        invalid_pkt.append(i)
    else:
        print('Packet {} passed the checker!'.format(i))
        valid_pkt.append(i)

print("Invalid packets: {}".format(invalid_pkt))
print("Valid packets: {}".format(valid_pkt))
