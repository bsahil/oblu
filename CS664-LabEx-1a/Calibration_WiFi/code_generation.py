# -*- coding: utf-8 -*-
'''
  Copyright (C) 2018 GT Silicon Pvt Ltd

  Licensed under the Creative Commons Attribution 4.0
  International Public License (the "CCBY4.0 License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
  https://creativecommons.org/licenses/by/4.0/legalcode
'''
# Function generates a .h file containing the calibration matrix
#     Date     |    Review    |      Author                      |  Comments
# -------------+--------------+-----------------------------------------------------
#   21-08-2016 |    0.0       |   Rahul Tiwari                   | Initial Release

import math


def code_generation(acc, gyro, C_int, b_acc_int, b_gyro_int, nr_imus, filename):
    file_data = open(filename, 'w')
    file_data.write('#define FLOG2_NR_IMU %d\n' % math.log(nr_imus, 2))
    file_data.write('#define ACC_BIAS { %d, %d, %d }\n' % (b_acc_int[0], b_acc_int[1], b_acc_int[2]))
    file_data.write('#define GYRO_BIAS { %d, %d, %d }\n' % (b_gyro_int[0], b_gyro_int[1], b_gyro_int[2]))
    file_data.write('#define CALIBRATION_MATRIX \\\n')
    file_data.write('{ \\\n''{'+str(list(C_int[0, :]))[1:len(str(list(C_int[0, :])))-1]+'},\\\n')

    for m in range(1, 31):
        file_data.write('{'+str(list(C_int[m, :]))[1:len(str(list(C_int[m, :])))-1]+'},\\\n')

    file_data.write('{'+str(list(C_int[31, :]))[1:len(str(list(C_int[31, :])))-1]+'},\\\n}\n')
    file_data.close()
