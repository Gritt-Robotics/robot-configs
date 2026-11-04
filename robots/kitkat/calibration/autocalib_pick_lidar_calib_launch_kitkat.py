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
                "-0.0424484",
                "--y",
                "0.00511166",
                "--z",
                "0.102675",
                "--qx",
                "-0.170202",
                "--qy",
                "0.171274",
                "--qz",
                "-0.6877",
                "--qw",
                "0.684665",
                # "--roll",
                # "0.00283933",
                # "--pitch",
                # "0.487734",
                # "--yaw",
                # "-1.57593",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00665246,
#     "translation_err_m": 0.00268283.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00652099,
#     "translation_err_m": 0.00296139.
