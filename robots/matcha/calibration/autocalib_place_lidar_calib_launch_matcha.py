#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

# place_detector_cam_camera_link from livox_place_frame
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
                "-0.0464444",
                "--y",
                "0.000400865",
                "--z",
                "0.0889201",
                "--qx",
                "-0.170022",
                "--qy",
                "0.172185",
                "--qz",
                "-0.680602",
                "--qw",
                "0.691539",
                # "--roll",
                # "3.14071",
                # "--pitch",
                # "2.65278",
                # "--yaw",
                # "1.58696",
            ],
        ),
    ]
    return LaunchDescription(nodes)


# Reprojection errors acquired via automated calibration
# lidar-camera training
#     "rotation_err_rad": 0.00654716,
#     "translation_err_m": 0.00289901.


# Reprojection errors acquired via automated calibration
# lidar-camera validation
#     "rotation_err_rad": 0.00374344,
#     "translation_err_m": 0.00493834.
