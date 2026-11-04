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
                "0.0985723",
                "--y",
                "0.30367",
                "--z",
                "0.193726",
                "--qx",
                "-0.652352",
                "--qy",
                "0.272711",
                "--qz",
                "-0.28354",
                "--qw",
                "0.64782",
                # "--roll",
                # "1.57099",
                # "--pitch",
                # "2.33307",
                # "--yaw",
                # "3.12485",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00332766,
#     "translation_err_m": 0.0030356.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00282267,
#     "translation_err_m": 0.00380216.
