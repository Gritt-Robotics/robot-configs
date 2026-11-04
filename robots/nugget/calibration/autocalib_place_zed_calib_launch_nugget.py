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
                "-0.0869213",
                "--y",
                "-2.03257",
                "--z",
                "1.37114",
                "--qx",
                "0.120884",
                "--qy",
                "0.316097",
                "--qz",
                "-0.359524",
                "--qw",
                "0.869605",
                # "--roll",
                # "0.516203",
                # "--pitch",
                # "0.481193",
                # "--yaw",
                # "-0.913424",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00436016,
#     "translation_err_m": 0.00694227.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot training
#     "valid": true,
#     "num_views": 19,
#     "rotation_scatter_rad": 0.00387142,
#     "translation_scatter_m": 0.00288024.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00381464,
#     "translation_err_m": 0.0066855.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot validation
#     "valid": true,
#     "num_views": 10,
#     "rotation_scatter_rad": 0.00318973,
#     "translation_scatter_m": 0.00265482.
