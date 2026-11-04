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
                "0.0596402",
                "--y",
                "-0.00301417",
                "--z",
                "0.310404",
                "--qx",
                "-0.00701976",
                "--qy",
                "0.383039",
                "--qz",
                "-0.00346366",
                "--qw",
                "0.923699",
                # "--roll",
                # "3.12699",
                # "--pitch",
                # "2.35539",
                # "--yaw",
                # "3.14015",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00254896,
#     "translation_err_m": 0.00210124.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot training
#     "valid": true,
#     "num_views": 18,
#     "rotation_scatter_rad": 0.00195851,
#     "translation_scatter_m": 0.000986918.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00156384,
#     "translation_err_m": 0.00141158.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot validation
#     "valid": true,
#     "num_views": 7,
#     "rotation_scatter_rad": 0.00171398,
#     "translation_scatter_m": 0.000562189.
