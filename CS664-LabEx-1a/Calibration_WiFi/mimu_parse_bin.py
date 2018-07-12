# -*- coding: utf-8 -*-
'''
  Copyright (C) 2018 GT Silicon Pvt Ltd

  Licensed under the Creative Commons Attribution 4.0
  International Public License (the "CCBY4.0 License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
  https://creativecommons.org/licenses/by/4.0/legalcode
'''

# Function to parse the data from the sensor and checks if the pkt is valid or not. Discards if invalid
#
#     Date     |    Review    |      Author                      |  Comments
# -------------+--------------+-----------------------------------------------------
#   21-08-2016 |    0.0       |   Rahul Tiwari, Jaya sandhya M   | Initial Release
#
#

import struct
import os
import sys

import binascii
import numpy as np
import re
import tkMessageBox
MAX_FILENAME_SIZE = 1024

# get checksum
def get_checksum(pkt, start):  # to get checksum from the packet
    # return struct.unpack("!H", pkt[start:start+2])[0]
    val = int(pkt [start:],16)
    return val
# calculate checksum
def cal_checksum(pkt, end):  # to calculate checksum of a packet
    checksum = 0
    # a = pkt[0:end].encode('hex')
    a = pkt[0:end]
    x=0
    y=2
    for i in range(0,len(a)/2):
        checksum += int(a[x:y], 16)
        x +=2
        y +=2
    return checksum
def get_inertialdata(pkt):  # to calculate checksum of a packet
    pkt = binascii.unhexlify(pkt)
    return struct.unpack("!hhhhhhhhhhhhhhhhhhhhhhhh", pkt)


# parse the data from the sensor
def mimu_parse_bin(filename, nr_imus):
    #print "In file mimu_parse_bin.py"
    nof_imus = nr_imus
    PAYLOAD_SIZE = 4 + 12 * nof_imus
    PACKET_SIZE = (4 + PAYLOAD_SIZE + 2)*2
    nof_data_values = 6 * nof_imus
    data_values_size = 2 * nof_data_values
    filesize = os.stat(filename).st_size
    max_elts = filesize / PACKET_SIZE
    inertial_data = []
    time_data = []
    raw_data = []
    count = 0
    error_count = 0
    data = file(filename, "r")
    pkt = data.read(PACKET_SIZE)
    counte = 0
    while len(pkt)==PACKET_SIZE:

        # s1= pkt.encode("hex")
        s1 = pkt
        # binstr = binascii.unhexlify(pkt[0:8])
        # (start_code, pkt_num, payload_length) = struct.unpack("!BHB", binstr)
        (start_code, pkt_num, payload_length) = (hex(int(s1[0:2],16)),int(s1[2:6],16),int(s1[6:8],16))
        # Save the pkt if valid
        if start_code == '0xaa' and get_checksum(pkt, PACKET_SIZE-4) == cal_checksum(pkt, PACKET_SIZE-4):
            inertial_data.append(get_inertialdata(pkt[16:data_values_size*2+16]))
            binstr = binascii.unhexlify(pkt[8:16])
            time_data.append(struct.unpack("!L", binstr)[0])
            raw_data.append(pkt[8:data_values_size+16])
            pkt = data.read(PACKET_SIZE)
            counte = 0
            count += 1
        #   search for a new header AA and get a new packet
        elif re.search('[\d|\w]+aa.*', s1):
                lst = re.findall('[\d|\w]+(aa.*)', s1)
                strrem = lst[0]  # t=np.asarray(lst)
                lenght = len(strrem)
                pktrem=pkt[-lenght:]
                newlen = PACKET_SIZE - lenght
                pkt = data.read(newlen)
                pkt=pktrem+pkt
        # get a new packet if not valid
        else:
            pkt = data.read(PACKET_SIZE)
            # exit the code if the packet is detecting wrong continuously for more than 5 times
            counte += 1
            if counte > 10:
                counte = 0
                tkMessageBox.showinfo("Oops",
                                      "Something went wrong please restart the device and run the process again !")
                stop = file("error", 'w')
                stop.close()
                sys.exit(1)
    #print "total packets : ",count
    #print "Leaving file mimu_parse_bin.py"
    inertial_data = np.reshape(inertial_data,(len(inertial_data),len(inertial_data[0])))
    return inertial_data, time_data, raw_data

#
# filename = 'imu_data_test1.bin'
# nr_imus = 4
# mimu_parse_bin(filename, nr_imus)