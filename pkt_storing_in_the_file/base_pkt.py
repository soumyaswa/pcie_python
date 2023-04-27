import random


print("_base_pkt")
class pkt_base:
    def __init__(self):
        self.bdf = 12
        self.conf_type = 0
        self.block = 1
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
        print('Base Class: BDF = {}, config type {} for {}, {}, pkt is {}, ECRC is {}'.format(self.bdf, self.conf_type, "Switch" if self.conf_type else "end-point", "Blocking" if self.block else "Non-blocking", "Poisoned" if self.ep else "Not poisoned", "Enabled" if self.td else "Disabled"))
        print(self.packet)

p1 = pkt_base()
p1.print_bdf()



