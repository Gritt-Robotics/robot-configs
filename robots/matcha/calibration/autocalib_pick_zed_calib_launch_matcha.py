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
                "0.081249",
                "--y",
                "0.00903952",
                "--z",
                "-0.311339",
                "--qx",
                "0.926787",
                "--qy",
                "-0.0130334",
                "--qz",
                "0.375232",
                "--qw",
                "0.00984433",
                # "--roll",
                # "3.10259",
                # "--pitch",
                # "0.768786",
                # "--yaw",
                # "0.0439042",
            ],
        ),
    ]
    return LaunchDescription(nodes)


# Reprojection errors acquired via automated calibration
# camera-robot training
#     "rotation_err_rad": 0.00516126,
#     "translation_err_m": 0.00623857.


# Reprojection errors acquired via automated calibration
# camera-robot validation
#     "rotation_err_rad": 0.00842569,
#     "translation_err_m": 0.00813548.
