#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

""" place_detector_cam_camera_link from livox_place_frame """
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
                "-0.0423574",
                "--y",
                "-0.00398939",
                "--z",
                "0.0868373",
                "--qx",
                "-0.166612",
                "--qy",
                "0.172516",
                "--qz",
                "-0.681233",
                "--qw",
                "0.691665",
                # "--roll",
                # "0.00516152",
                # "--pitch",
                # "0.484368",
                # "--yaw",
                # "-1.55688",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# lidar-camera training
#     "rotation_err_rad": 0.00474128,
#     "translation_err_m": 0.00255502.


""" Reprojection errors acquired via automated calibration """
# lidar-camera validation
#     "rotation_err_rad": 0.00703214,
#     "translation_err_m": 0.00323395.
