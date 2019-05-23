#!/usr/bin/env python

import rospy
from gazebo_msgs.srv import SpawnModel, DeleteModel, SpawnModelRequest
import tf
from geometry_msgs.msg import Quaternion, Pose, Point


if __name__ == "__main__":
    rospy.init_node("spawner")
    rospy.wait_for_service("/gazebo/spawn_urdf_model")
    print("Spawn service started")

    spawner = rospy.ServiceProxy("/gazebo/spawn_urdf_model", SpawnModel)

    urdf_file = ''

    with open("/home/user/car_ws/src/car_description/urdf/simple_car_description_gazebo.urdf", "r") as f:
        urdf_file = f.read()

    orientation = tf.transformations.quaternion_from_euler(0, 0, 0)
    pose = Pose()
    pose.position.x = 0.0
    pose.position.y = 0.0
    pose.position.z = 0.0
    pose.orientation.x = orientation[0]
    pose.orientation.y = orientation[1]
    pose.orientation.z = orientation[2]
    pose.orientation.w = orientation[3]

    request = SpawnModelRequest()
    request.model_name = "car"
    request.model_xml = urdf_file
    request.robot_namespace = ""
    request.initial_pose = pose
    request.reference_frame = "world"

    response = spawner(request)
    print(response.success)
    print(response.status_message)
