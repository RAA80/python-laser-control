#! /usr/bin/env python3

"""Реализация классов клиентов для управления лазером."""

import logging
from socket import AF_INET, SOCK_DGRAM, SOCK_STREAM, socket

from serial import Serial

from .protocol import Protocol

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


def log(func):
    """Вывод отладочной информации."""

    def wrapper(self, packet):
        _logger.debug("Send frame: %r", packet)
        answer = func(self, packet.encode("ascii")).decode("ascii")
        _logger.debug("Recv frame: %r", answer)
        return answer

    return wrapper


class BaseClient(Protocol):
    """Базовый класс клиента."""

    def __init__(self, address, device, **kwargs):
        """Инициализация класса клиента с указанным адресом и устройством."""

        super().__init__(device)

        self.socket = None
        self.address = address

        self.port = kwargs.get("port", 10001)
        self.baudrate = kwargs.get("baudrate", 9600)
        self.timeout = kwargs.get("timeout", 1.0)

        self.connect()

    def __repr__(self):
        """Строковое представление объекта."""

        return f"{type(self).__name__}(socket={self.socket})"

    def __del__(self):
        """Закрытие соединения с устройством при удалении объекта."""

        if self.socket:
            self.socket.close()

    def connect(self):
        """Подключение к устройству."""

        raise NotImplementedError

    def _bus_exchange(self, packet):
        """Обмен по интерфейсу."""

        raise NotImplementedError


class LaserSerialClient(BaseClient):
    """Класс клиента для управления лазером через порт RS-232."""

    def connect(self):
        """Подключение к устройству."""

        self.socket = Serial(port=self.address, baudrate=self.baudrate,
                             timeout=self.timeout)

    @log
    def _bus_exchange(self, packet):
        """Обмен по интерфейсу."""

        self.socket.reset_input_buffer()
        self.socket.reset_output_buffer()

        self.socket.write(packet)
        return self.socket.read_until(b"\r")


class LaserTcpClient(BaseClient):
    """Класс клиента для управления лазером по протоколу TCP."""

    def connect(self):
        """Подключение к устройству."""

        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.settimeout(self.timeout)
        self.socket.connect((self.address, self.port))

    @log
    def _bus_exchange(self, packet):
        """Обмен по интерфейсу."""

        self.socket.sendall(packet)
        return self.socket.recv(64)


class LaserUdpClient(BaseClient):
    """Класс клиента для управления лазером по протоколу UDP."""

    def connect(self):
        """Подключение к устройству."""

        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.settimeout(self.timeout)

    @log
    def _bus_exchange(self, packet):
        """Обмен по интерфейсу."""

        self.socket.sendto(packet, (self.address, self.port))
        return self.socket.recvfrom(64)[0]


__all__ = ["LaserSerialClient", "LaserTcpClient", "LaserUdpClient"]
