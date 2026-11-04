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
                "-0.0365487",
                "--y",
                "0.00542039",
                "--z",
                "0.090821",
                "--qx",
                "-0.175027",
                "--qy",
                "0.161102",
                "--qz",
                "-0.689596",
                "--qw",
                "0.68401",
                # "--roll",
                # "3.12214",
                # "--pitch",
                # "2.66159",
                # "--yaw",
                # "1.56742",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00607484,
#     "translation_err_m": 0.00280775.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00820067,
#     "translation_err_m": 0.00358286.
