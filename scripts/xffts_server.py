#! /usr/bin/env python

import time
import threading
import xfftspy

import rospy
import std_msgs.msg


def spectra_fowarding_loop(xffts):
    pub_dict = {}
    pub_dict_tp = {}
    xffts.clear_buffer()
    while not rospy.is_shutdown():
        d = xffts.receive_once()
        datatime= (time.time(),)
        for bnum in d['data']:
            if bnum not in pub_dict:
                pub_dict[bnum] = rospy.Publisher(
                                        '/xffts_board{0:02d}'.format(bnum),
                                        std_msgs.msg.Float64MultiArray,
                                        queue_size = 1)
                pass
            spec = std_msgs.msg.Float64MultiArray()
            spec.data = d['data'][bnum]+datatime
            pub_dict[bnum].publish(spec)
            #print(bnum)
           
            if bnum not in pub_dict_tp:
                pub_dict_tp[bnum] = rospy.Publisher(
                                        '/xffts_board{0:02d}_tp'.format(bnum),
                                        std_msgs.msg.Float64MultiArray,
                                        queue_size = 1)
                pass
            _tp = sum(q.data[:-1])
            t = q.data[-1]
            tp = Float64MultiArray()
            tp.data = [_tp,t]
            self.pub[arg].publish(tp)
                        
            continue
                    
        continue
   
    return

if __name__ == '__main__':
    rospy.init_node('xffts')
    host = 'localhost'

    xffts = xfftspy.data_consumer(host)
    th = threading.Thread(target=spectra_fowarding_loop, args=(xffts,))
    th.start()

    rospy.spin()
