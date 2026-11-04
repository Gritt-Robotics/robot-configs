#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

""" pick_detector_cam_camera_link from livox_pick_frame """
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
                "pick_detector_cam_camera_link",
                "--child-frame-id",
                "livox_pick_frame",
                "--x",
                "-0.036148",
                "--y",
                "0.00569598",
                "--z",
                "0.10329",
                "--qx",
                "-0.164676",
                "--qy",
                "0.162728",
                "--qz",
                "-0.687059",
                "--qw",
                "0.688732",
                # "--roll",
                # "3.13798",
                # "--pitch",
                # "2.67434",
                # "--yaw",
                # "1.57409",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00650026,
#     "translation_err_m": 0.00260383.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00840854,
#     "translation_err_m": 0.00300545.
