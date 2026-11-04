# Copyright 2025-2026 Gritt Robotics Inc.

"""Static transform publisher acquired via MoveIt 2 hand-eye calibration"""

""" EYE-IN-HAND: gripper_frame_1 -> benchmark_detector_cam_camera_link """
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
                "benchmark_detector_cam_camera_link",
                "--x",
                "0.150654",
                "--y",
                "0.245679",
                "--z",
                "0.280305",
                "--qx",
                "-0.55466",
                "--qy",
                "0.325692",
                "--qz",
                "-0.244992",
                "--qw",
                "0.725435",
                # "--roll",
                # "1.83214",
                # "--pitch",
                # "2.30209",
                # "--yaw",
                # "-3.13284",
            ],
        ),
    ]
    return LaunchDescription(nodes)
