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
                "-0.948055",
                "--y",
                "-0.216509",
                "--z",
                "1.94677",
                "--qx",
                "-0.202739",
                "--qy",
                "0.210921",
                "--qz",
                "0.678473",
                "--qw",
                "0.673857",
                # "--roll",
                # "2.54785",
                # "--pitch",
                # "3.13244",
                # "--yaw",
                # "-1.56117",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00310676,
#     "translation_err_m": 0.00467203.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00592081,
#     "translation_err_m": 0.00883662.
