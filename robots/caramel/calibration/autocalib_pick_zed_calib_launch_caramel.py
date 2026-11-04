#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

""" gripper_frame_1 from pick_detector_cam_camera_link """
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    nodes = [
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output="log",
            arguments=[
                "--frame-id",
                "gripper_frame_1",
                "--child-frame-id",
                "pick_detector_cam_camera_link",
                "--x",
                "0.154246",
                "--y",
                "0.240718",
                "--z",
                "0.271067",
                "--qx",
                "-0.53029",
                "--qy",
                "0.382075",
                "--qz",
                "-0.280678",
                "--qw",
                "0.702873",
                # "--roll",
                # "1.83847",
                # "--pitch",
                # "2.15386",
                # "--yaw",
                # "-3.12223",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00448687,
#     "translation_err_m": 0.00538752.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00403685,
#     "translation_err_m": 0.00675289.
