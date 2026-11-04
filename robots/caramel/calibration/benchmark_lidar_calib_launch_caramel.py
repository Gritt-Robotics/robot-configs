# Copyright 2025-2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated lidar-camera calibration"""

""" place_detector_cam_left_camera_optical_frame from livox_place_frame """
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
                "benchmark_detector_cam_camera_link",
                "--child-frame-id",
                "livox_benchmark_frame",
                "--x",
                "-0.04227",
                "--y",
                "0.000429339",
                "--z",
                "0.0884724",
                "--qx",
                "-0.161738",
                "--qy",
                "0.171923",
                "--qz",
                "-0.687511",
                "--qw",
                "0.68674",
                # "--roll",
                # "0.0160394",
                # "--pitch",
                # "0.476336",
                # "--yaw",
                # "-1.57581",
            ],
        ),
    ]
    return LaunchDescription(nodes)
