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
                "-0.036396",
                "--y",
                "-0.00119769",
                "--z",
                "0.0999703",
                "--qx",
                "-0.172346",
                "--qy",
                "0.170625",
                "--qz",
                "-0.685183",
                "--qw",
                "0.68681",
                # "--roll",
                # "3.13828",
                # "--pitch",
                # "2.65168",
                # "--yaw",
                # "1.57399",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00675945,
#     "translation_err_m": 0.0027239.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00414981,
#     "translation_err_m": 0.00288619.
