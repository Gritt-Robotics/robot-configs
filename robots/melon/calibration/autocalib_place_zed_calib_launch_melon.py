#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

# base_link from place_detector_cam_camera_link
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
                "-0.0994984",
                "--y",
                "-2.00907",
                "--z",
                "1.36094",
                "--qx",
                "0.17428",
                "--qy",
                "0.326713",
                "--qz",
                "-0.360767",
                "--qw",
                "0.855998",
                # "--roll",
                # "0.634423",
                # "--pitch",
                # "0.448465",
                # "--yaw",
                # "-0.947202",
            ],
        ),
    ]
    return LaunchDescription(nodes)


# Reprojection errors acquired via automated calibration
# camera-robot training
#     "rotation_err_rad": 0.00366015,
#     "translation_err_m": 0.00510892.


# Reprojection errors acquired via automated calibration
# camera-robot validation
#     "rotation_err_rad": 0.00229301,
#     "translation_err_m": 0.003203.
