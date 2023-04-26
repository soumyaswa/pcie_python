import random
from base_pkt import pkt_base

print("hello base_pkt")

class default_base_pkt(pkt_base):
    def __init__(self):
        super().__init__()
        self.bdf = 10
        self.conf_type = 0
        self.ep = 0
        self.td = 0
        #self.packet = [self.bdf, self.conf_type, self.block, self.ep, self.td]
        self.packet = {"bdf" : self.bdf, 
                       "conf_type" : self.conf_type, 
                       "block" : self.block, 
                       "ep" : self.ep, 
                       "td" : self.td
                       }


    def print_bdf(self):
        print('Default Base Class: BDF = {}, config type {} for {}, {}, pkt is {}, ECRC is {}'.format(self.bdf, self.conf_type, "Switch" if self.conf_type else "end-point", "Blocking" if self.block else "Non-blocking", "Poisoned" if self.ep else "Not poisoned", "Enabled" if self.td else "Disabled"))
        print(self.packet)

    num_packets = 10


p1 = default_base_pkt()
p1.print_bdf()
