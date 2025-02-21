#! /usr/bin/env python3

"""Проверка работы всех функций."""

import logging

from laser.client import LaserSerialClient, LaserTcpClient, LaserUdpClient
from laser.device import RFL_C3000S

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    client = LaserSerialClient(device=RFL_C3000S, address="COM1", baudrate=9600)
    # client = LaserUdpClient(device=RFL_C3000S, address="127.0.0.1:8099")
    # client = LaserTcpClient(device=RFL_C3000S, address="127.0.0.1:10001")

    print(f'aiming_beam_off = {client.send("ABF")}')
    print(f'aiming_beam_on = {client.send("ABN")}')
    print(f'disable_external_aiming_beam_control = {client.send("DEABC")}')
    print(f'enable_external_aiming_beam_control = {client.send("EEABC")}')
    print(f'disable_external_control = {client.send("DEC")}')
    print(f'enable_external_control = {client.send("EEC")}')
    print(f'disable_hardware_emission_control = {client.send("DLE")}')
    print(f'enable_hardware_emission_control = {client.send("ELE")}')
    print(f'disable_gate_mode = {client.send("DGM")}')
    print(f'enable_gate_mode = {client.send("EGM")}')
    print(f'stop_emission = {client.send("EMOFF")}')
    print(f'start_emission = {client.send("EMON")}')
    print(f'main_power_off = {client.send("MPWROFF")}')
    print(f'main_power_on = {client.send("MPWRON")}')
    print(f'reset_errors = {client.send("PERR")}')
    print(f'program_stop = {client.send("PSTP")}')

    print(f'program_start = {client.send("PSRT", value=1)}')
    print(f'set_pulse_width = {client.send("SPW", value=100)}')
    print(f'set_pulse_repetition_rate = {client.send("SPRR", value=1000)}')
    print(f'set_diode_current = {client.send("SDC", value=100)}')
    print(f'set_ip = {client.send("SIP", value="192.168.0.10")}')
    print(f'set_subnet_mask = {client.send("SMASK", value="255.255.255.0")}')
    print(f'set_up_time = {client.send("SUT", value=50)}')
    print(f'set_down_time = {client.send("SDT", value=50)}')

    print(f'read_current_set_point = {client.send("RCS")}')
    print(f'read_pulse_repetition_rate = {client.send("RPRR")}')
    print(f'read_board_temperature = {client.send("RBT")}')
    print(f'read_pulse_width = {client.send("RPW")}')
    print(f'read_laser_temperature = {client.send("RCT")}')
    print(f'read_output_power = {client.send("ROP")}')
    print(f'read_serial_number = {client.send("RSN")}')
    print(f'read_ip = {client.send("RIP")}')
    print(f'read_subnet_mask = {client.send("RMASK")}')
    print(f'read_up_time = {client.send("RUT")}')
    print(f'read_down_time = {client.send("RDT")}')
    print(f'read_device_status = {client.send("STA")}')
