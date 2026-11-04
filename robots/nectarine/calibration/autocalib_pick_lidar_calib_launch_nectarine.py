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
                "-0.043842",
                "--y",
                "-0.0020362",
                "--z",
                "0.0905212",
                "--qx",
                "-0.169908",
                "--qy",
                "0.168119",
                "--qz",
                "-0.684232",
                "--qw",
                "0.688981",
                # "--roll",
                # "3.13701",
                # "--pitch",
                # "2.65889",
                # "--yaw",
                # "1.57884",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00651514,
#     "translation_err_m": 0.00277889.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00445127,
#     "translation_err_m": 0.00262406.
