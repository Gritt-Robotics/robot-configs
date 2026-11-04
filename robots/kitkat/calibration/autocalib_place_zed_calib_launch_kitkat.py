#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

""" base_link from place_detector_cam_camera_link """
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
                "base_link",
                "--child-frame-id",
                "place_detector_cam_camera_link",
                "--x",
                "-0.692363",
                "--y",
                "-0.171874",
                "--z",
                "1.97381",
                "--qx",
                "-0.198295",
                "--qy",
                "0.209313",
                "--qz",
                "0.68778",
                "--qw",
                "0.666203",
                # "--roll",
                # "2.55666",
                # "--pitch",
                # "3.13547",
                # "--yaw",
                # "-1.53708",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00328387,
#     "translation_err_m": 0.00413018.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00289067,
#     "translation_err_m": 0.00337216.
