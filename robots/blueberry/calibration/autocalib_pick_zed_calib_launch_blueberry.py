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
                "0.107033",
                "--y",
                "-0.341183",
                "--z",
                "-0.107932",
                "--qx",
                "0.566991",
                "--qy",
                "0.302232",
                "--qz",
                "0.236026",
                "--qw",
                "0.729019",
                # "--roll",
                # "1.32122",
                # "--pitch",
                # "0.787108",
                # "--yaw",
                # "0.00199561",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00224378,
#     "translation_err_m": 0.00469141.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.0047218,
#     "translation_err_m": 0.00729086.
