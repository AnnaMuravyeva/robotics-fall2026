"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""
from __future__ import annotations
import math
from dataclasses import dataclass

@dataclass(frozen=True)
class Segment:
    linear_x: float
    angular_z: float
    duration: float

def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper always
    publishes it and the evaluator verifies it.
    """
    if pattern_name != "rounded_rectangle":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    straight_speed = 0.15
    arc_linear_speed = 0.12
    arc_angular_speed = 0.80

    long_distance = 0.40 
    short_distance = 0.25 
    turn_angle = math.pi / 2

    long_duration = long_distance / straight_speed
    short_duration = short_distance / straight_speed
    arc_duration = turn_angle / arc_angular_speed
        
    segments = []

    for _ in range(2):
        segments.append(Segment(straight_speed, 0.0, long_duration))
        segments.append(Segment(arc_linear_speed, arc_angular_speed, arc_duration))
        segments.append(Segment(straight_speed, 0.0, short_duration))
        segments.append(Segment(arc_linear_speed, arc_angular_speed, arc_duration))
    
    return segments

