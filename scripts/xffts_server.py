#! /usr/bin/env python

import xfftspy

import rospy
import std_msgs.msg


def spectra_fowarding_loop(xffts):
    pub_dict = {}
    xffts.clear_buffer()
    while not rospy.is_shutdown():
        d = xffts.receive_once()

        for bnum in d['data']:
            if bnum not in pub_dict:
                pub_dict[bnum] = rospy.Publisher(
                                        '/xffts_board{0:02d}'.format(bnum),
                                        std_msgs.msg.Float32MultiArray,
                                        queue_size = 1)
                pass
            spec = std_msgs.msg.Float32MultiArray()
            spec.data = d['data'][bnum]
            pub_dict[bnum].publish(spec)
            continue
        continue
    return

if __name__ == '__main__':
    rospy.init_node('xffts')
    host = 'localhost'

    xffts = xfftspy.data_consumer(host)
    spectra_fowarding_loop(xffts)
