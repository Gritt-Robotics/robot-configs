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
                "-0.0839743",
                "--y",
                "-2.04187",
                "--z",
                "1.36683",
                "--qx",
                "0.13497",
                "--qy",
                "0.321983",
                "--qz",
                "-0.371215",
                "--qw",
                "0.860412",
                # "--roll",
                # "0.557335",
                # "--pitch",
                # "0.471104",
                # "--yaw",
                # "-0.951747",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00317047,
#     "translation_err_m": 0.00431088.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot training
#     "valid": true,
#     "num_views": 20,
#     "rotation_scatter_rad": 0.00233332,
#     "translation_scatter_m": 0.00110896.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.0021149,
#     "translation_err_m": 0.00279648.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot validation
#     "valid": true,
#     "num_views": 10,
#     "rotation_scatter_rad": 0.00151591,
#     "translation_scatter_m": 0.00112909.
