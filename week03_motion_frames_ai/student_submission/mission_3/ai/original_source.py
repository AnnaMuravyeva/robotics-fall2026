import math


def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name != "rounded_rectangle":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    straight_speed = 0.15
    arc_linear_speed = 0.12
    arc_angular_speed = 0.80

    long_duration = 0.40 / straight_speed
    short_duration = 0.25 / straight_speed
    arc_duration = (math.pi / 2) / arc_angular_speed

    return [
        Segment(straight_speed, 0.0, long_duration),
        Segment(arc_linear_speed, arc_angular_speed, arc_duration),
        Segment(straight_speed, 0.0, short_duration),
        Segment(arc_linear_speed, arc_angular_speed, arc_duration),
        Segment(straight_speed, 0.0, long_duration),
        Segment(arc_linear_speed, arc_angular_speed, arc_duration),
        Segment(straight_speed, 0.0, short_duration),
        Segment(arc_linear_speed, arc_angular_speed, arc_duration),
    ]