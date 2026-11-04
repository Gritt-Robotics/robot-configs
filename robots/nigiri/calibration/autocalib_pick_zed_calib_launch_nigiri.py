#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

""" gripper_frame_1 from pick_detector_cam_camera_link """
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
                "gripper_frame_1",
                "--child-frame-id",
                "pick_detector_cam_camera_link",
                "--x",
                "0.0594519",
                "--y",
                "0.000862285",
                "--z",
                "0.317746",
                "--qx",
                "0.00276148",
                "--qy",
                "0.378599",
                "--qz",
                "0.000242377",
                "--qw",
                "0.925557",
                # "--roll",
                # "0.00690891",
                # "--pitch",
                # "0.776561",
                # "--yaw",
                # "-0.00230233",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00240125,
#     "translation_err_m": 0.00192561.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot training
#     "valid": true,
#     "num_views": 17,
#     "rotation_scatter_rad": 0.00195059,
#     "translation_scatter_m": 0.00081557.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00192038,
#     "translation_err_m": 0.00173187.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot validation
#     "valid": true,
#     "num_views": 8,
#     "rotation_scatter_rad": 0.00157598,
#     "translation_scatter_m": 0.00116582.
