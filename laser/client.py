#! /usr/bin/env python3

"""Реализация классов клиентов для управления лазером."""

import logging
from socket import AF_INET, SOCK_DGRAM, SOCK_STREAM, socket
from typing import Callable

from serial import Serial

from .device import LASER_DEVICE
from .protocol import Protocol

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


def log(func: Callable) -> Callable:
    """Вывод отладочной информации."""

    def wrapper(self: Callable[[str], bytes], packet: str) -> str:
        _logger.debug("Send frame: %r", packet)
        answer = func(self, packet.encode("ascii")).decode("ascii")
        _logger.debug("Recv frame: %r", answer)
        return answer

    return wrapper


class LaserSerialClient(Protocol):
    """Класс клиента для управления лазером через порт RS-232."""

    def __init__(self, device: LASER_DEVICE, address: str = "COM1",
                       baudrate: int = 9600, timeout: float = 1.0) -> None:
        """Инициализация класса клиента с указанным адресом и устройством."""

        super().__init__(device)
        self.socket = Serial(port=address, baudrate=baudrate, timeout=timeout)

    def __del__(self) -> None:
        """Закрытие соединения с устройством при удалении объекта."""

        if self.socket.is_open:
            self.socket.close()

    @log
    def _bus_exchange(self, packet: bytes) -> bytes:
        """Обмен по интерфейсу."""

        self.socket.reset_input_buffer()
        self.socket.reset_output_buffer()

        self.socket.write(packet)
        return self.socket.read_until(b"\r")


class LaserTcpClient(Protocol):
    """Класс клиента для управления лазером по протоколу TCP."""

    def __init__(self, device: LASER_DEVICE, address: str = "127.0.0.1:10001",
                       timeout: float = 1.0) -> None:
        """Инициализация класса клиента с указанным адресом и устройством."""

        super().__init__(device)

        ip, tcp_port = address.split(":")
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.settimeout(timeout)
        self.socket.connect((ip, int(tcp_port)))

    def __del__(self) -> None:
        """Закрытие соединения с устройством при удалении объекта."""

        if self.socket:
            self.socket.close()

    @log
    def _bus_exchange(self, packet: bytes) -> bytes:
        """Обмен по интерфейсу."""

        self.socket.sendall(packet)
        return self.socket.recv(64)


class LaserUdpClient(Protocol):
    """Класс клиента для управления лазером по протоколу UDP."""

    def __init__(self, device: LASER_DEVICE, address: str = "127.0.0.1:8099",
                       timeout: float = 1.0) -> None:
        """Инициализация класса клиента с указанным адресом и устройством."""

        super().__init__(device)

        self.ip, self.udp_port = address.split(":")
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.settimeout(timeout)

    def __del__(self) -> None:
        """Закрытие соединения с устройством при удалении объекта."""

        if self.socket:
            self.socket.close()

    @log
    def _bus_exchange(self, packet: bytes) -> bytes:
        """Обмен по интерфейсу."""

        self.socket.sendto(packet, (self.ip, int(self.udp_port)))
        return self.socket.recvfrom(64)[0]


__all__ = ["LaserSerialClient", "LaserTcpClient", "LaserUdpClient"]
