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
                "-0.0726452",
                "--y",
                "-1.94306",
                "--z",
                "1.39889",
                "--qx",
                "0.162079",
                "--qy",
                "0.358634",
                "--qz",
                "-0.34116",
                "--qw",
                "0.853652",
                # "--roll",
                # "0.646971",
                # "--pitch",
                # "0.525572",
                # "--yaw",
                # "-0.940293",
            ],
        ),
    ]
    return LaunchDescription(nodes)


# Reprojection errors acquired via automated calibration
# camera-robot training
#     "rotation_err_rad": 0.0023582,
#     "translation_err_m": 0.00297293.


# Reprojection errors acquired via automated calibration
# camera-robot validation
#     "rotation_err_rad": 0.00380507,
#     "translation_err_m": 0.00597211.
