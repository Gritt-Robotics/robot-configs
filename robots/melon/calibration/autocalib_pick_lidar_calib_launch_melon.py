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
                "-0.0437049",
                "--y",
                "0.000443164",
                "--z",
                "0.101161",
                "--qx",
                "-0.173026",
                "--qy",
                "0.17626",
                "--qz",
                "-0.687389",
                "--qw",
                "0.683001",
                # "--roll",
                # "0.00679214",
                # "--pitch",
                # "0.49911",
                # "--yaw",
                # "-1.57893",
            ],
        ),
    ]
    return LaunchDescription(nodes)


# Reprojection errors acquired via automated calibration
# lidar-camera training
#     "rotation_err_rad": 0.00732878,
#     "translation_err_m": 0.0032862.


# Reprojection errors acquired via automated calibration
# lidar-camera validation
#     "rotation_err_rad": 0.00284665,
#     "translation_err_m": 0.0026917.
