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
                "0.0660761",
                "--y",
                "0.00700745",
                "--z",
                "0.310033",
                "--qx",
                "-0.00498772",
                "--qy",
                "0.378855",
                "--qz",
                "-0.00416603",
                "--qw",
                "0.925433",
                # "--roll",
                # "3.13307",
                # "--pitch",
                # "2.36444",
                # "--yaw",
                # "3.13608",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.0023207,
#     "translation_err_m": 0.00193205.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot training
#     "valid": true,
#     "num_views": 19,
#     "rotation_scatter_rad": 0.00201799,
#     "translation_scatter_m": 0.000763826.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.0030654,
#     "translation_err_m": 0.00279236.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot validation
#     "valid": true,
#     "num_views": 6,
#     "rotation_scatter_rad": 0.00182614,
#     "translation_scatter_m": 0.000412338.
