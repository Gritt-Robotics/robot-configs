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
                "0.0961329",
                "--y",
                "0.309715",
                "--z",
                "0.190808",
                "--qx",
                "-0.651717",
                "--qy",
                "0.269193",
                "--qz",
                "-0.270227",
                "--qw",
                "0.655574",
                # "--roll",
                # "1.5787",
                # "--pitch",
                # "2.35892",
                # "--yaw",
                # "3.13675",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.0013354,
#     "translation_err_m": 0.00160459.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00172603,
#     "translation_err_m": 0.00235435.
