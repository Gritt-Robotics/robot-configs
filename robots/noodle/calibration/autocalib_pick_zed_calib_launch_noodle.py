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
                "0.0654145",
                "--y",
                "-0.00273417",
                "--z",
                "0.308365",
                "--qx",
                "-0.00279256",
                "--qy",
                "0.38192",
                "--qz",
                "-0.0067689",
                "--qw",
                "0.924166",
                # "--roll",
                # "1.2381e-05",
                # "--pitch",
                # "0.783767",
                # "--yaw",
                # "-0.0146535",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00264581,
#     "translation_err_m": 0.00219521.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot training
#     "valid": true,
#     "num_views": 19,
#     "rotation_scatter_rad": 0.0023794,
#     "translation_scatter_m": 0.0015282.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00158872,
#     "translation_err_m": 0.00201572.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot validation
#     "valid": true,
#     "num_views": 6,
#     "rotation_scatter_rad": 0.00134662,
#     "translation_scatter_m": 0.00131101.
