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
                "-0.0412605",
                "--y",
                "-6.67121e-05",
                "--z",
                "0.0889234",
                "--qx",
                "-0.178608",
                "--qy",
                "0.165537",
                "--qz",
                "-0.687295",
                "--qw",
                "0.684341",
                # "--roll",
                # "3.12241",
                # "--pitch",
                # "2.64994",
                # "--yaw",
                # "1.5713",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00734494,
#     "translation_err_m": 0.00265782.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00434226,
#     "translation_err_m": 0.00247245.
