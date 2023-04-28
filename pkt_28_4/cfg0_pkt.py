import random
from default_base_class import *
from pkt_dict import *

class cfg0_pkt(default_base_pkt):
    def __init__(self):
        super().__init__()   
        
    def bdf_fn_cfg0(self):
        self.bdf = random.randint(0, (2**9)-1)        
        self.conf_type = random.randint(0,1)
        self.ep = random.randint(0, 1)
        self.td = random.randint(0, 1)
        pkt_dict["bdf"] =  self.bdf
        pkt_dict["conf_type"] =  self.conf_type
        pkt_dict["block"] =  self.block 
        pkt_dict["ep"] =  self.ep 
        pkt_dict["td"] =  self.td
        print(pkt_dict)
        with open('output.txt', 'a') as f:
            f.write('Packet {}: {}\n'.format(self.num_packets, pkt_dict))
       
    def print_new_bdf(self):
        print('cfg0_pkt BDF = {}, config type {} for {}, {}, pkt is {}, ECRC is {}'.format(self.bdf, self.conf_type, "Switch" if self.conf_type else "end-point", "Blocking" if self.block else "Non-blocking", "Poisoned" if self.ep else "Not poisoned", "Enabled" if self.td else "Disabled"))

      
