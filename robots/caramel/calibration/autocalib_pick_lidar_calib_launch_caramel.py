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
                "-0.0429401",
                "--y",
                "-0.00261304",
                "--z",
                "0.099458",
                "--qx",
                "-0.170023",
                "--qy",
                "0.165979",
                "--qz",
                "-0.687532",
                "--qw",
                "0.68618",
                # "--roll",
                # "3.13584",
                # "--pitch",
                # "2.66182",
                # "--yaw",
                # "1.57023",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00542359,
#     "translation_err_m": 0.00302539.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00578837,
#     "translation_err_m": 0.00324572.
