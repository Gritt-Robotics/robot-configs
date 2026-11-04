#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

# gripper_frame_1 from pick_detector_cam_camera_link
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
                "0.0633985",
                "--y",
                "0.00188482",
                "--z",
                "0.310661",
                "--qx",
                "-0.00321484",
                "--qy",
                "0.381513",
                "--qz",
                "0.00060472",
                "--qw",
                "0.924358",
                # "--roll",
                # "3.13256",
                # "--pitch",
                # "2.35874",
                # "--yaw",
                # "-3.13656",
            ],
        ),
    ]
    return LaunchDescription(nodes)


# Reprojection errors acquired via automated calibration
# camera-robot training
#     "rotation_err_rad": 0.00232024,
#     "translation_err_m": 0.00199304.


# Reprojection errors acquired via automated calibration
# camera-robot validation
#     "rotation_err_rad": 0.0017648,
#     "translation_err_m": 0.00151524.
