from cfg0_pkt import *
from checker import *

c1 = checker_pkt()
inval_pkt = 0
val_pkt = 0
inval_pkt_num = []
val_pkt_num = []

# Open a file to store the output
filename = 'output.txt'
with open(filename, 'w') as f:
    for i in range(default_base_pkt.num_packets):
        p2 = cfg0_pkt()
        p2.bdf_fn_cfg0()
        p2.print_new_bdf()
        if not c1.checker_fn():
            print('Packet failed the checker!')
            inval_pkt += 1
            inval_pkt_num.append(i)
            f.write('Packet failed the checker!\n')
        else:
            print('Packet passed the checker!')
            val_pkt += 1
            val_pkt_num.append(i)
            f.write('Packet passed the checker!\n')
        f.write('Generated packet {} dictionary: {}\n'.format(i, pkt_dict))
        f.write('Checked packet {} dictionary: {}\n'.format(i, pkt_dict))

    f.write("Number of invalid packets: {}\n".format(inval_pkt))
    f.write("Number of valid packets: {}\n".format(val_pkt))
    f.write("Invalid packet numbers: {}\n".format(inval_pkt_num))
    f.write("Valid packet numbers: {}\n".format(val_pkt_num))

# Move output file to directory

import shutil
import os

output_file = 'output.txt'
destination = 'Desktop/pcie/pkt_28_4'

shutil.move(output_file, os.path.join(destination, output_file))

print(f"File '{output_file}' moved to directory: {destination}")

