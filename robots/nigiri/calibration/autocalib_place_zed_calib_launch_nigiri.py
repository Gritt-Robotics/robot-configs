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
                "-0.0934508",
                "--y",
                "-2.04448",
                "--z",
                "1.36248",
                "--qx",
                "0.137059",
                "--qy",
                "0.317617",
                "--qz",
                "-0.358679",
                "--qw",
                "0.866997",
                # "--roll",
                # "0.549173",
                # "--pitch",
                # "0.469483",
                # "--yaw",
                # "-0.919061",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00360954,
#     "translation_err_m": 0.00486196.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot training
#     "valid": true,
#     "num_views": 20,
#     "rotation_scatter_rad": 0.00244585,
#     "translation_scatter_m": 0.00132805.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00206009,
#     "translation_err_m": 0.00232659.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot validation
#     "valid": true,
#     "num_views": 10,
#     "rotation_scatter_rad": 0.00185233,
#     "translation_scatter_m": 0.00115396.
