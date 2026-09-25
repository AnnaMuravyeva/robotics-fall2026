# Mission 2

## Snapshot

{'schema_version': 2, 'captured_at': '2026-09-25T11:41:38.673628+00:00', 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'frame_chain': ['hall_camera', 'odom', 'base_link', 'base_scan', 'rear_camera_link'], 'transforms': {'base_scan_to_base_link': {'translation': {'x': -0.032, 'y': 0.0, 'z': 0.172}, 'yaw': 0.0}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': -3.1415926535795866}, 'hall_camera_to_base_link': {'translation': {'x': -5.552191242463898, 'y': 2.466314098080506, 'z': 1.19}, 'yaw': -0.6878246727901672}}, 'point_prompts': {'hall_camera_point': 'Transform point (0.5, 0.0, 0.0) from hall_camera to base_link.'}, 'transformed_points': {'scan_point_in_base': {'x': 0.968, 'y': 0.0}, 'rear_camera_point_in_base': {'x': -1.18, 'y': -1.0206624774663903e-11}, 'hall_camera_point_in_base': {'x': -5.165876809578117, 'y': 2.1488851155597897}}, 'source': 'live'}

## Frame Context

The rear-camera transform stays fixed because the camera is attached to the robot. In other words, it moves with the robot and keeps the same position relative to base_link. On the other hand, the hallway camera stays in one place, so as the robot moves around, its position and orientation relative to base_link changes. 

## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.

## Initial Output

Here is a ROS 2 Python node that takes a point detected in the hallway camera frame and transforms it into the robot’s `base_link` frame using TF2.

```python
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PointStamped
from tf2_ros import Buffer, TransformListener
from tf2_geometry_msgs import do_transform_point


class PointTransformer(Node):
    def __init__(self):
        super().__init__('point_transformer')

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.subscription = self.create_subscription(
            PointStamped,
            '/hallway_camera/point',
            self.point_callback,
            10
        )

        self.publisher = self.create_publisher(
            PointStamped,
            '/point_in_base_link',
            10
        )

    def point_callback(self, point_msg):
        try:
            transform = self.tf_buffer.lookup_transform(
                'base_link',
                point_msg.header.frame_id,
                rclpy.time.Time()
            )

            transformed_point = do_transform_point(
                point_msg,
                transform
            )

            self.publisher.publish(transformed_point)

            self.get_logger().info(
                f'Point in base_link: '
                f'x={transformed_point.point.x:.2f}, '
                f'y={transformed_point.point.y:.2f}, '
                f'z={transformed_point.point.z:.2f}'
            )

        except Exception as e:
            self.get_logger().warning(
                f'Could not transform point: {e}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = PointTransformer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

This assumes that:

* The detected point is published as a `PointStamped` message on `/hallway_camera/point`.
* Its `header.frame_id` identifies the hallway camera's TF frame.
* A valid TF2 transform chain exists between the hallway camera frame and `base_link`.
* The transform available when the callback runs corresponds closely enough to the point's measurement time.

The node listens for detected points, asks TF2 for the transform from the point's camera frame into `base_link`, applies that transform, and publishes the resulting point on `/point_in_base_link`.


## Initial Source

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PointStamped
from tf2_ros import Buffer, TransformListener
from tf2_geometry_msgs import do_transform_point


class PointTransformer(Node):
    def __init__(self):
        super().__init__('point_transformer')

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.subscription = self.create_subscription(
            PointStamped,
            '/hallway_camera/point',
            self.point_callback,
            10
        )

        self.publisher = self.create_publisher(
            PointStamped,
            '/point_in_base_link',
            10
        )

    def point_callback(self, point_msg):
        try:
            transform = self.tf_buffer.lookup_transform(
                'base_link',
                point_msg.header.frame_id,
                rclpy.time.Time()
            )

            transformed_point = do_transform_point(
                point_msg,
                transform
            )

            self.publisher.publish(transformed_point)

            self.get_logger().info(
                f'Point in base_link: '
                f'x={transformed_point.point.x:.2f}, '
                f'y={transformed_point.point.y:.2f}, '
                f'z={transformed_point.point.z:.2f}'
            )

        except Exception as e:
            self.get_logger().warning(
                f'Could not transform point: {e}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = PointTransformer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

## Initial Analysis

The AI made several assumptions. It assumed that the detected point was a PointStamped message and that its frame_id correctly identified the hallway camera. It also made up topic names as I didn't provide them in my prompt. Another issue is that it used the latest available transform instead of using the transform from the time the point was detected. This could be an issue if the robot moved after the camera detected the point. Lastly, it also assumed that a TF transform between the hallway camera and base_link was available.

## Improved Changes

The improved prompt clearly says that the point must come from the hall_camera frame and be transformed into base_link. It also says to use the point's original timestamp so that the transformation matches the time when the point was detected. It specifies that instead of using hard-coded offsets, the code should just use the provided TF buffer. Lastly, if the transform is unavailable, it should return None without trying to move the robot.

## Live Pending

True

## Synthesis

The initial AI response made assumptions about the source frame, timestamp, and available TF transform because the original prompt didn't include any of this information. The improved prompt provides the missing information as it clearly specifics that the point comes from hall_camera and should be transformed into base_link using the TF buffer and the point's original timestamp. If the wrong transform were used then the robot could think that a detected person or object is in a different location and move way too close to them. The test that checks the buffer result and rotation helps to make sure that the right transform is being used. If no transform is available then the robot should return None and stay where it is.

## Live Issue

The live check failed because the TF lookup said it would require extrapolation into the future. I tried running the live verification multiple times and checked that the simulation clock and TF were running. But unfortunately, despite all 5 tests passing, I couldn't verify the live hall_camera to base_link transform.
