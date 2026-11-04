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
                "-0.0412389",
                "--y",
                "-0.000553814",
                "--z",
                "0.0934983",
                "--qx",
                "-0.172656",
                "--qy",
                "0.167563",
                "--qz",
                "-0.686359",
                "--qw",
                "0.686311",
                # "--roll",
                # "3.1337",
                # "--pitch",
                # "2.65569",
                # "--yaw",
                # "1.57268",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.0057806,
#     "translation_err_m": 0.00287872.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00449128,
#     "translation_err_m": 0.00247661.
