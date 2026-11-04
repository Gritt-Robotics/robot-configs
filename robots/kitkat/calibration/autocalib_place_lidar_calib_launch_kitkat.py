#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

""" place_detector_cam_camera_link from livox_place_frame """
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
                "place_detector_cam_camera_link",
                "--child-frame-id",
                "livox_place_frame",
                "--x",
                "-0.0431567",
                "--y",
                "-0.00175683",
                "--z",
                "0.095411",
                "--qx",
                "-0.176863",
                "--qy",
                "0.167053",
                "--qz",
                "-0.6848",
                "--qw",
                "0.686921",
                # "--roll",
                # "3.1255",
                # "--pitch",
                # "2.65033",
                # "--yaw",
                # "1.57792",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00396885,
#     "translation_err_m": 0.00259109.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00681944,
#     "translation_err_m": 0.00344197.
