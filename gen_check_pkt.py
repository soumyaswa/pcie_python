
import random

class PktBase:
    def __init__(self):
        self.bdf = 5
        self.cfg_type = 0
        self.ep = 0
        self.td = 0
        self.block = 1

    def pkt_rand(self):
        self.bdf = random.randint(251, 259)
        self.cfg_type = random.randint(0, 1)
        self.ep = random.randint(0, 1)
        self.td = random.randint(0, 1)
        self.block = 1

    def pkt_rand_def(self):
        print('bdf value is {}, cfg_type is {}, ep is {}, block is {}'.format(self.bdf, self.cfg_type, self.ep, self.block))

def generate_packets(num_packets):
    packets = []
    for i in range(num_packets):
        p = PktBase()
        p.pkt_rand()
        packets.append(p)
    return packets

def check_packets(packets):
    valid_packets = []
    invalid_packets = []
    for i, p in enumerate(packets):
        if not (251 <= p.bdf <= 256 and 0 <= p.cfg_type <= 1 and 0 <= p.ep <= 1 and 0 <= p.td <= 1 and p.block == 1):
            invalid_packets.append(i)
        else:
            valid_packets.append(i)
    if invalid_packets:
        print("Invalid packets: {}".format(invalid_packets))
    if valid_packets:
        print("Valid packets: {}".format(valid_packets))
    if not invalid_packets:
        return True
    else:
        return False

num_packets = 10
packets = generate_packets(num_packets)
print("Generated {} packets:".format(num_packets))
for p in packets:
    p.pkt_rand_def()

if check_packets(packets):
    print("All packets are valid")
else:
    print("Error: invalid packet generated")


