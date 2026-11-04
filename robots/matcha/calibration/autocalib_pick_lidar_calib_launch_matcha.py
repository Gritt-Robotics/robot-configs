#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

# pick_detector_cam_camera_link from livox_pick_frame
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
                "-0.0442139",
                "--y",
                "0.00528452",
                "--z",
                "0.102189",
                "--qx",
                "-0.169394",
                "--qy",
                "0.173666",
                "--qz",
                "-0.681621",
                "--qw",
                "0.690318",
                # "--roll",
                # "0.00326101",
                # "--pitch",
                # "0.490078",
                # "--yaw",
                # "-1.55893",
            ],
        ),
    ]
    return LaunchDescription(nodes)


# Reprojection errors acquired via automated calibration
# lidar-camera training
#     "rotation_err_rad": 0.0058365,
#     "translation_err_m": 0.00287237.


# Reprojection errors acquired via automated calibration
# lidar-camera validation
#     "rotation_err_rad": 0.00736806,
#     "translation_err_m": 0.00349674.
