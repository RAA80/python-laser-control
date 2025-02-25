#! /usr/bin/env python3

"""Модуль, описывающий протокол управления лазером."""

from __future__ import annotations

from re import Match, search
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .device import LASER_DEVICE


class LaserProtocolError(Exception):
    pass


class Protocol:
    """Класс протокола управления лазером."""

    def __init__(self, device: LASER_DEVICE) -> None:
        """Инициализация класса Protocol."""

        self.device = device

    def _bus_exchange(self, packet: str) -> str:
        """Обмен по интерфейсу."""

        raise NotImplementedError

    def _compare(self, cmd: str, pattern: str) -> Match[str]:
        """Сравнение результата обмена с заданным паттерном."""

        result = self._bus_exchange(cmd)
        if match := search(pattern, result):
            return match
        raise LaserProtocolError(result)

    def _set(self, cmd: str, value: float | str | None = None) -> bool:
        """Записать новое значение параметра."""

        cmd, pattern = (f"{cmd}\r", f"{cmd}\r") if value is None else \
                       (f"{cmd} {value}\r", f"{cmd}: {value}\r")
        return bool(self._compare(cmd, pattern))

    def _get(self, cmd: str, frmt: object) -> float | str:
        """Прочитать значение параметра."""

        cmd, pattern = (f"{cmd}\r", f"{cmd}: (\\S+)\r")
        return frmt(self._compare(cmd, pattern)[1])     # type: ignore

    def send(self, cmd: str, value: float | str | None = None) -> float | str | bool:
        """Послать команду в устройство."""

        cmd = cmd.upper()
        if not (device_info := self.device.get(cmd)):
            msg = f"Unknown command {cmd}"
            raise LaserProtocolError(msg)

        frmt = device_info["type"]
        func = device_info["func"]

        return {"set": lambda: self._set(cmd, frmt(value) if frmt else None),
                "get": lambda: self._get(cmd, frmt),
               }[func]()                                # type: ignore


__all__ = ["Protocol"]
