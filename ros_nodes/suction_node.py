#!/usr/bin/env python
""" 
ROS Server for turing the suction on or off
Author: Vishal Satish
"""
import rospy
import time

from std_msgs.msg import Header

from autolab_suction import Vacuum
from autolab_suction.srv import Suction

class SuctionToggler(object):
    """ Toggles suction on or off.
    """
    def __init__(self):
        self._vacuum = Vacuum()

    def toggle_suction(self, request):
        rospy.loginfo('Suction {}'.format(request.on))
        if request.on:
            self._vacuum.on()
        else:
            self._vacuum.off()
        return True
            
if __name__ == '__main__':
    
    # initialize the ROS node
    rospy.init_node('Suction_Server')

    # create a policy 
    rospy.loginfo('Creating Suction Server')
    suction_server = SuctionToggler()

    # initialize the service        
    service = rospy.Service('toggle_suction', Suction, suction_server.toggle_suction)
    rospy.loginfo('Suction Initialized!')

    # spin
    rospy.spin()
