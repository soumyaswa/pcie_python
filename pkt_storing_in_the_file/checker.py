import random
from pkt_dict import *

print("checker block")

class checker_pkt():


	def checker_fn(self):
		#bdf, conf_type, block, ep, td = packet_check
		block = pkt_dict["block"]
		bdf = pkt_dict["bdf"]
		conf_type = pkt_dict["conf_type"]
		ep = pkt_dict["ep"]
		td = pkt_dict["td"]

		print('checker_fn BDF = {}, config type {} for {}, {}, pkt is {}, ECRC is {}'.format(bdf, conf_type, "Switch" if conf_type else "end-point", "Blocking" if block else "Non-blocking", "Poisoned" if ep else "Not poisoned", "Enabled" if td else "Disabled"))
		write_to_file('cfg0_pkt BDF = {}, config type {} for {}, {}, pkt is {}, ECRC is {}'.format(bdf, conf_type, "Switch" if conf_type else "end-point", "Blocking" if block else "Non-blocking", "Poisoned" if ep else "Not poisoned", "Enabled" if td else "Disabled"))
       
		if not (0 <= bdf < 2**8 and 0 <= conf_type <= 1 and 0 <= ep <= 1 and 0 <= td <= 1 and block == 1):
			print("Packet is invalid")
			if(bdf >= 2**8):
				print('INVALID BDF, value: {}'.format(bdf))
			if(conf_type != 0):
				print('Received config_type is for SWITCH, value: {} but required END-POINT instead,'.format(conf_type))
			if(ep != 0):
				print('Packet is poisoned, value: {} : Discarding the packet'.format(ep))
			if(block != 1):
				print('Non-blocking packet, value: {}'.format(block))
			return False
		else:
			print("Packet is valid")
			return True



