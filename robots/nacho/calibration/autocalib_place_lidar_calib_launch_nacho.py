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
                "-0.0437511",
                "--y",
                "0.0022962",
                "--z",
                "0.0899976",
                "--qx",
                "-0.168458",
                "--qy",
                "0.1707",
                "--qz",
                "-0.690164",
                "--qw",
                "0.682757",
                # "--roll",
                # "0.00631798",
                # "--pitch",
                # "0.484335",
                # "--yaw",
                # "-1.58315",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00483524,
#     "translation_err_m": 0.0025997.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00376985,
#     "translation_err_m": 0.003007.
