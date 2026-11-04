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
                "0.0618462",
                "--y",
                "-0.0128935",
                "--z",
                "0.315817",
                "--qx",
                "0.00447726",
                "--qy",
                "0.379483",
                "--qz",
                "0.00132284",
                "--qw",
                "0.925187",
                # "--roll",
                # "0.010226",
                # "--pitch",
                # "0.77848",
                # "--yaw",
                # "-0.0013348",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00149066,
#     "translation_err_m": 0.00132837.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot training
#     "valid": true,
#     "num_views": 16,
#     "rotation_scatter_rad": 0.00131016,
#     "translation_scatter_m": 0.000541946.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00117461,
#     "translation_err_m": 0.0011835.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot validation
#     "valid": true,
#     "num_views": 9,
#     "rotation_scatter_rad": 0.000803352,
#     "translation_scatter_m": 0.000463214.
