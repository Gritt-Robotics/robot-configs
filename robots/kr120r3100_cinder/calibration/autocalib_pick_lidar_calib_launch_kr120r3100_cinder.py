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
                "-0.0401776",
                "--y",
                "0.00153632",
                "--z",
                "0.100203",
                "--qx",
                "-0.175675",
                "--qy",
                "0.172829",
                "--qz",
                "-0.684973",
                "--qw",
                "0.685624",
                # "--roll",
                # "3.13689",
                # "--pitch",
                # "2.64361",
                # "--yaw",
                # "1.57294",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00743015,
#     "translation_err_m": 0.00274871.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.0109364,
#     "translation_err_m": 0.00325842.
