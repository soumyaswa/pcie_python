import random
from cfg0_pkt import *

print("checker block")

class checker_pkt(cfg0_pkt):


	def checker_fn(self, packet_check):
		#bdf, conf_type, block, ep, td = packet_check
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


c1 = checker_pkt()
inval_pkt = []
val_pkt = []
for i in range(default_base_pkt.num_packets):
	p2 = cfg0_pkt()
	p2.bdf_fn_cfg0()
	p2.print_new_bdf()
	if not c1.checker_fn(p2.packet):
		print('Packet failed the checker!')
		#inval_pkt += 1
		inval_pkt.append(i)
	else:
		print('Packet passed the checker!')
		#val_pkt += 1
		val_pkt.append(i)

	if i == default_base_pkt.num_packets-1:
		print("Invalid packets: {}".format(inval_pkt))
		print("Valid packets: {}".format(val_pkt))
			
