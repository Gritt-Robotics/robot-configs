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
                "-0.0408682",
                "--y",
                "0.000113074",
                "--z",
                "0.0912839",
                "--qx",
                "-0.170662",
                "--qy",
                "0.168936",
                "--qz",
                "-0.687693",
                "--qw",
                "0.685137",
                # "--roll",
                # "3.1399",
                # "--pitch",
                # "2.65658",
                # "--yaw",
                # "1.56749",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00825545,
#     "translation_err_m": 0.00297457.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00531466,
#     "translation_err_m": 0.00300211.
