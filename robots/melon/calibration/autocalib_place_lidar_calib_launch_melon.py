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
                "-0.0457631",
                "--y",
                "0.00234302",
                "--z",
                "0.0888284",
                "--qx",
                "-0.168995",
                "--qy",
                "0.168805",
                "--qz",
                "-0.688136",
                "--qw",
                "0.685138",
                # "--roll",
                # "0.000849515",
                # "--pitch",
                # "0.482384",
                # "--yaw",
                # "-1.57537",
            ],
        ),
    ]
    return LaunchDescription(nodes)


# Reprojection errors acquired via automated calibration
# lidar-camera training
#     "rotation_err_rad": 0.00689599,
#     "translation_err_m": 0.00257006.


# Reprojection errors acquired via automated calibration
# lidar-camera validation
#     "rotation_err_rad": 0.00354333,
#     "translation_err_m": 0.00249265.
