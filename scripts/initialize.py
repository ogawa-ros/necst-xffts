#! /usr/bin/env python

import xfftspy

# initialize XFFTS boards
cmd = xfftspy.udp_client(host='localhost')
cmd.stop()
cmd.set_synctime(100000)          # synctime : 100 ms
cmd.set_usedsections([1,1])       # use board : 1
cmd.set_board_bandwidth(1, 2000)  # bandwidth : 2000 MHz
cmd.set_board_bandwidth(2, 2000)
cmd.configure()                   # apply settings
cmd.caladc()                      # calibrate ADCs
cmd.start()                       # start measurement
