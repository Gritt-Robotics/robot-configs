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
                "-0.0737174",
                "--y",
                "-2.07393",
                "--z",
                "1.32558",
                "--qx",
                "0.202936",
                "--qy",
                "0.401068",
                "--qz",
                "-0.337928",
                "--qw",
                "0.826901",
                # "--roll",
                # "0.794343",
                # "--pitch",
                # "0.554047",
                # "--yaw",
                # "-1.01333",
            ],
        ),
    ]
    return LaunchDescription(nodes)


""" Reprojection errors acquired via automated calibration """
# camera-robot training
#     "rotation_err_rad": 0.00295999,
#     "translation_err_m": 0.00411225.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot training
#     "valid": true,
#     "num_views": 20,
#     "rotation_scatter_rad": 0.00210227,
#     "translation_scatter_m": 0.00112466.


""" Reprojection errors acquired via automated calibration """
# camera-robot validation
#     "rotation_err_rad": 0.00157211,
#     "translation_err_m": 0.00248871.

""" Target pose scatter (order-independent) acquired via automated calibration """
# camera-robot validation
#     "valid": true,
#     "num_views": 10,
#     "rotation_scatter_rad": 0.00140314,
#     "translation_scatter_m": 0.000678735.
