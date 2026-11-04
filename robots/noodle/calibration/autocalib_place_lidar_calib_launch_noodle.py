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
                "-0.0386842",
                "--y",
                "-0.000340944",
                "--z",
                "0.0915874",
                "--qx",
                "-0.174129",
                "--qy",
                "0.170561",
                "--qz",
                "-0.685607",
                "--qw",
                "0.685953",
                # "--roll",
                # "3.1359",
                # "--pitch",
                # "2.64917",
                # "--yaw",
                # "1.57273",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00935648,
#     "translation_err_m": 0.00279017.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00705488,
#     "translation_err_m": 0.00269131.
