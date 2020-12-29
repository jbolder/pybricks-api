# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Pybricks Authors

from typing import Callable, Optional, Tuple

from ._common import ColorLight
from .iodevices import AnalogSensor
from .parameters import Color, Port

class TouchSensor:
    def __init__(self, port: Port): ...
    def pressed(self) -> bool: ...

class LightSensor:
    def __init__(self, port: Port): ...
    def ambient(self) -> int: ...
    def reflection(self) -> int: ...

class ColorSensor:
    light: ColorLight
    def __init__(self, port: Port): ...
    def color(self) -> Optional[Color]: ...
    def ambient(self) -> int: ...
    def reflection(self) -> int: ...
    def rgb(self) -> Tuple[int, int, int]: ...

class UltrasonicSensor:
    def __init__(self, port: Port): ...
    def distance(self) -> int: ...

class SoundSensor:
    def __init__(self, port: Port): ...
    def intensity(self, audible_only: bool = True) -> int: ...

class TemperatureSensor:
    def __init__(self, port: Port): ...
    def temperature(self) -> int: ...

class EnergyMeter:
    def __init__(self, port: Port): ...
    def storage(self) -> int: ...
    def input(self) -> Tuple[int, int, int]: ...
    def output(self) -> Tuple[int, int, int]: ...

class VernierAdapter(AnalogSensor):
    def __init__(
        self, port: Port, conversion: Optional[Callable[[int], float]] = None
    ): ...
    def voltage(self) -> int: ...
    def conversion(self, voltage: int) -> float: ...
    def value(self) -> float: ...