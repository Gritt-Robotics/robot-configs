#!/usr/bin/env -S ros2 launch
# Copyright 2026 Gritt Robotics Inc.

"""Static transform publisher acquired via automated calibration"""

""" base_link from place_detector_cam_camera_link """
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
                "base_link",
                "--child-frame-id",
                "place_detector_cam_camera_link",
                "--x",
                "-0.0790889",
                "--y",
                "-2.04976",
                "--z",
                "1.34881",
                "--qx",
                "0.175895",
                "--qy",
                "0.322886",
                "--qz",
                "-0.321771",
                "--qw",
                "0.872507",
                # "--roll",
                # "0.614399",
                # "--pitch",
                # "0.467041",
                # "--yaw",
                # "-0.85726",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00300932,
#     "translation_err_m": 0.00484297.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot training
#     "valid": true,
#     "num_views": 19,
#     "rotation_scatter_rad": 0.00218062,
#     "translation_scatter_m": 0.00199346.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00234014,
#     "translation_err_m": 0.00421542.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot validation
#     "valid": true,
#     "num_views": 10,
#     "rotation_scatter_rad": 0.00163145,
#     "translation_scatter_m": 0.00142865.
