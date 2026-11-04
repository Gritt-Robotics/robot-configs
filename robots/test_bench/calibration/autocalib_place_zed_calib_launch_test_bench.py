#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

""" base_link from place_detector_cam_camera_link """
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
                "base_link",
                "--child-frame-id",
                "place_detector_cam_camera_link",
                "--x",
                "-0.679461",
                "--y",
                "-0.172367",
                "--z",
                "1.97333",
                "--qx",
                "-0.19127",
                "--qy",
                "0.216234",
                "--qz",
                "0.677038",
                "--qw",
                "0.676963",
                # "--roll",
                # "2.55674",
                # "--pitch",
                # "3.10782",
                # "--yaw",
                # "-1.56052",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.0024236,
#     "translation_err_m": 0.0031468.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00441459,
#     "translation_err_m": 0.00588398.
