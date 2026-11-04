#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

""" link_6_1 from pick_detector_cam_camera_link """
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
                "link_6_1",
                "--child-frame-id",
                "pick_detector_cam_camera_link",
                "--x",
                "-0.572764",
                "--y",
                "-0.0347474",
                "--z",
                "-0.273658",
                "--qx",
                "0.684927",
                "--qy",
                "0.408959",
                "--qz",
                "-0.303768",
                "--qw",
                "0.520915",
                # "--roll",
                # "1.84706",
                # "--pitch",
                # "0.00994928",
                # "--yaw",
                # "-1.06903",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00240474,
#     "translation_err_m": 0.00353262.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00211221,
#     "translation_err_m": 0.00330422.
