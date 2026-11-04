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
                "-0.0378349",
                "--y",
                "-0.00220926",
                "--z",
                "0.0881453",
                "--qx",
                "-0.171357",
                "--qy",
                "0.165001",
                "--qz",
                "-0.687748",
                "--qw",
                "0.685867",
                # "--roll",
                # "3.13246",
                # "--pitch",
                # "2.6613",
                # "--yaw",
                # "1.57029",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00684997,
#     "translation_err_m": 0.00287734.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00673485,
#     "translation_err_m": 0.00285735.
