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
                "-0.0412624",
                "--y",
                "0.00186297",
                "--z",
                "0.0908389",
                "--qx",
                "-0.176095",
                "--qy",
                "0.167462",
                "--qz",
                "-0.685271",
                "--qw",
                "0.68655",
                # "--roll",
                # "3.12767",
                # "--pitch",
                # "2.65084",
                # "--yaw",
                # "1.57615",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00754527,
#     "translation_err_m": 0.00273269.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00409831,
#     "translation_err_m": 0.0025278.
