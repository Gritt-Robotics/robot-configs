#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

""" pick_detector_cam_camera_link from livox_pick_frame """
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
                "pick_detector_cam_camera_link",
                "--child-frame-id",
                "livox_pick_frame",
                "--x",
                "-0.0371726",
                "--y",
                "-0.00673232",
                "--z",
                "0.100293",
                "--qx",
                "-0.175221",
                "--qy",
                "0.167318",
                "--qz",
                "-0.685727",
                "--qw",
                "0.686354",
                # "--roll",
                # "3.12906",
                # "--pitch",
                # "2.65232",
                # "--yaw",
                # "1.57484",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00731579,
#     "translation_err_m": 0.00319137.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00582118,
#     "translation_err_m": 0.00401411.
