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
                "-0.0451441",
                "--y",
                "-0.0126126",
                "--z",
                "0.0916465",
                "--qx",
                "-0.167584",
                "--qy",
                "0.168075",
                "--qz",
                "-0.687239",
                "--qw",
                "0.686563",
                # "--roll",
                # "0.00101618",
                # "--pitch",
                # "0.479266",
                # "--yaw",
                # "-1.57203",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00952369,
#     "translation_err_m": 0.00306081.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.0139487,
#     "translation_err_m": 0.00444825.
