import rospy
import time

from autolab_suction.srv import Suction

if __name__ == '__main__':
    rospy.init_node('suction_toggle_node')
    rospy.wait_for_service('toggle_suction')
    toggle_suction = rospy.ServiceProxy('toggle_suction', Suction)
    rospy.loginfo('Suction On')
    toggle_suction(True)
    time.sleep(5)
    rospy.loginfo('Suction Off')
    toggle_suction(False)
