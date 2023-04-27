from cfg0_pkt import *
from checker import *

c1 = checker_pkt()
inval_pkt = 0
val_pkt = 0
inval_pkt_num = [];
val_pkt_num = [];

# Open a file to store the output
filename = 'output.txt'
with open(filename, 'w') as f:
    for i in range(default_base_pkt.num_packets):
        p2 = cfg0_pkt()
        p2.bdf_fn_cfg0()
        p2.print_new_bdf()
        if not c1.checker_fn():
            print('Packet failed the checker!')
           # print('checker_fn BDF = {}, config type {} for {}, {}, pkt is {}, ECRC is {}'.format(bdf, conf_type, "Switch" if conf_type else "end-point", "Blocking" if block else "Non-blocking", "Poisoned" if ep else "Not poisoned", "Enabled" if td else "Disabled"))
            #inval_pkt += 1
            inval_pkt_num.append(i)
            f.write('Packet failed the checker!\n')
        else:
            print('Packet passed the checker!')
            #print('checker_fn BDF = {}, config type {} for {}, {}, pkt is {}, ECRC is {}'.format(bdf, conf_type, "Switch" if conf_type else "end-point", "Blocking" if block else "Non-blocking", "Poisoned" if ep else "Not poisoned", "Enabled" if td else "Disabled"))
            #val_pkt += 1
            val_pkt_num.append(i)
            f.write('Packet passed the checker!\n')

    f.write("number of invalid packets are {}\n".format(inval_pkt))
    f.write("number of valid packets are {}\n".format(val_pkt))
    f.write("invalid packet numbers are {}\n".format(inval_pkt_num))
    f.write("valid packet numbers are {}\n".format(val_pkt_num))
# Move output file to directory
import shutil
import os

output_file = 'output.txt'
destination = 'Desktop/pcie/pkt_storing_in_the_file'

shutil.move(output_file, os.path.join(destination, output_file))

print(f"File '{output_file}' moved to directory: {destination}")