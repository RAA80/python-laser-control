#! /usr/bin/env python3

"""Файл, содержащий настройки приборов."""


# Назначение полей таблиц настроек:
#   1. Название команды (в верхнем регистре)
#       * Назначение команды "func":
#           - для записи: 'set'
#           - для чтения: 'get'
#       * Тип аргумента команды "type":
#           - для записи: None - если аргумента нет,
#                         float, int, str - тип аргумента
#           - для чтения: float, int, str - тип возвращаемого значения


# таблица настроек Raycus RFL-C3000S
RFL_C3000S = {
    "ABF":     {"func": "set", "type": None},   # Aiming Beam OFF
    "ABN":     {"func": "set", "type": None},   # Aiming Beam ON
    "DEABC":   {"func": "set", "type": None},   # Disable External Aiming Beam Control
    "EEABC":   {"func": "set", "type": None},   # Enable External Aiming Beam Control
    "DEC":     {"func": "set", "type": None},   # Disable External Control
    "EEC":     {"func": "set", "type": None},   # Enable External Control
    "DLE":     {"func": "set", "type": None},   # Disable Hardware Emission Control
    "ELE":     {"func": "set", "type": None},   # Enable Hardware Emission Control
    "DGM":     {"func": "set", "type": None},   # Disable Gate Mode
    "EGM":     {"func": "set", "type": None},   # Enable Gate Mode
    "EMOFF":   {"func": "set", "type": None},   # Stop Emission
    "EMON":    {"func": "set", "type": None},   # Start Emission
    "MPWROFF": {"func": "set", "type": None},   # Main Power OFF
    "MPWRON":  {"func": "set", "type": None},   # Main Power ON
    "PERR":    {"func": "set", "type": None},   # Reset Errors
    "PSTP":    {"func": "set", "type": None},   # Program Stop
    "PSRT":    {"func": "set", "type": int},    # Program Start
    "SPW":     {"func": "set", "type": int},    # Set Pulse Width
    "RPW":     {"func": "get", "type": float},  # Read Pulse Width
    "SPRR":    {"func": "set", "type": int},    # Set Pulse Repetition Rate
    "RPRR":    {"func": "get", "type": int},    # Read Pulse Repetition Rate
    "SDC":     {"func": "set", "type": int},    # Set Diode Current
    "RCS":     {"func": "get", "type": float},  # Read Current Setpoint
    "SIP":     {"func": "set", "type": str},    # Set IP
    "RIP":     {"func": "get", "type": str},    # Read IP
    "SMASK":   {"func": "set", "type": str},    # Set Sub-net Mask
    "RMASK":   {"func": "get", "type": str},    # Read Sub-net Mask
    "SUT":     {"func": "set", "type": int},    # Set Up Time
    "RUT":     {"func": "get", "type": int},    # Read Up Time
    "SDT":     {"func": "set", "type": int},    # Set Down Time
    "RDT":     {"func": "get", "type": int},    # Read Down Time
    "RBT":     {"func": "get", "type": float},  # Read Board Temperature
    "RCT":     {"func": "get", "type": float},  # Read Laser Temperature
    "ROP":     {"func": "get", "type": float},  # Read Output Power
    "RSN":     {"func": "get", "type": int},    # Read Serial Number
    "STA":     {"func": "get", "type": int},    # Read device status
}

# таблица настроек Raycus RFL-C3000XZ, RFL-C4000XZ и т.д.
RFL_XZ_SERIES = {
    "ABF":     {"func": "set", "type": None},   # Aiming Beam OFF
    "ABN":     {"func": "set", "type": None},   # Aiming Beam ON
    "DEABC":   {"func": "set", "type": None},   # Disable External Aiming Beam Control
    "EEABC":   {"func": "set", "type": None},   # Enable External Aiming Beam Control
    "DEC":     {"func": "set", "type": None},   # Disable External Control
    "EEC":     {"func": "set", "type": None},   # Enable External Control
    "DLE":     {"func": "set", "type": None},   # Disable Hardware Emission Control
    "ELE":     {"func": "set", "type": None},   # Enable Hardware Emission Control
    "EMOFF":   {"func": "set", "type": None},   # Stop Emission
    "EMON":    {"func": "set", "type": None},   # Start Emission
    "MPWROFF": {"func": "set", "type": None},   # Main Power OFF
    "MPWRON":  {"func": "set", "type": None},   # Main Power ON
    "PERR":    {"func": "set", "type": None},   # Reset Errors
    "ECM":     {"func": "set", "type": None},   # Enable Calibration Mode
    "DCM":     {"func": "set", "type": None},   # Disable Calibration Mode
    "PSTP":    {"func": "set", "type": None},   # Program Stop
    "PSRT":    {"func": "set", "type": int},    # Program Start
    "SPW":     {"func": "set", "type": int},    # Set Pulse Width
    "RPW":     {"func": "get", "type": float},  # Read Pulse Width
    "SPRR":    {"func": "set", "type": int},    # Set Pulse Repetition Rate
    "RPRR":    {"func": "get", "type": int},    # Read Pulse Repetition Rate
    "SDC":     {"func": "set", "type": int},    # Set Diode Current
    "RCS":     {"func": "get", "type": float},  # Read Current Setpoint
    "SUT":     {"func": "set", "type": int},    # Set Up Time
    "RUT":     {"func": "get", "type": int},    # Read Up Time
    "SDT":     {"func": "set", "type": int},    # Set Down Time
    "RDT":     {"func": "get", "type": int},    # Read Down Time
    "RBT":     {"func": "get", "type": float},  # Read Board Temperature
    "RCT":     {"func": "get", "type": float},  # Read Laser Temperature
    "STA":     {"func": "get", "type": int},    # Read device status
}

# таблица настроек Raycus RFL-1500/1500-ABP, RFL-2000/2000-ABP и т.д.
RFL_ABP_SERIES = {
    "ABF":     {"func": "set", "type": None},   # Aiming Beam OFF
    "ABN":     {"func": "set", "type": None},   # Aiming Beam ON
    "DEABC":   {"func": "set", "type": None},   # Disable External Aiming Beam Control
    "EEABC":   {"func": "set", "type": None},   # Enable External Aiming Beam Control
    "DEC":     {"func": "set", "type": None},   # Disable External Control
    "EEC":     {"func": "set", "type": None},   # Enable External Control
    "DLE":     {"func": "set", "type": None},   # Disable Hardware Emission Control
    "ELE":     {"func": "set", "type": None},   # Enable Hardware Emission Control
    "EMOFF":   {"func": "set", "type": None},   # Stop Emission
    "EMON":    {"func": "set", "type": None},   # Start Emission
    "MPWROFF": {"func": "set", "type": None},   # Main Power OFF
    "MPWRON":  {"func": "set", "type": None},   # Main Power ON
    "PERR":    {"func": "set", "type": None},   # Reset Errors
    "ECM":     {"func": "set", "type": None},   # Enable Calibration Mode
    "DCM":     {"func": "set", "type": None},   # Disable Calibration Mode
    "PSTP":    {"func": "set", "type": None},   # Program Stop
    "PSRT":    {"func": "set", "type": int},    # Program Start
    "SPW":     {"func": "set", "type": int},    # Set Pulse Width
    "SPRR":    {"func": "set", "type": int},    # Set Pulse Repetition Rate
    "RCS":     {"func": "get", "type": float},  # Read Current Setpoint
    "RPRR":    {"func": "get", "type": int},    # Read Pulse Repetition Rate
    "SDC":     {"func": "set", "type": int},    # Set Diode Current
    "RBT":     {"func": "get", "type": float},  # Read Board Temperature
    "RPW":     {"func": "get", "type": float},  # Read Pulse Width
    "RCT":     {"func": "get", "type": float},  # Read Laser Temperature
    "SUT":     {"func": "set", "type": int},    # Set Up Time
    "RUT":     {"func": "get", "type": int},    # Read Up Time
    "SDT":     {"func": "set", "type": int},    # Set Down Time
    "RDT":     {"func": "get", "type": int},    # Read Down Time
    "STA":     {"func": "get", "type": int},    # Read device status
}

# таблица настроек Raycus RFL-QCW150/1500
RFL_QCW150_1500 = {
    "ABF":   {"func": "set", "type": None},     # Aiming Beam OFF
    "ABN":   {"func": "set", "type": None},     # Aiming Beam ON
    "DEABC": {"func": "set", "type": None},     # Disable External Aiming Beam Control
    "DEC":   {"func": "set", "type": None},     # Disable External Control
    "DGM":   {"func": "set", "type": None},     # Disable Gate Mode
    "DLE":   {"func": "set", "type": None},     # Disable Hardware Emission Control
    "DMOD":  {"func": "set", "type": None},     # Disable Modulation
    "DPM":   {"func": "set", "type": None},     # Disable PULSE Mode
    "EEABC": {"func": "set", "type": None},     # Enable External Aiming Beam Control
    "EEC":   {"func": "set", "type": None},     # Enable External Control
    "EGM":   {"func": "set", "type": None},     # Enable Gate Mode
    "ELE":   {"func": "set", "type": None},     # Enable Hardware Emission Control
    "EMOD":  {"func": "set", "type": None},     # Enable Modulation
    "EMOFF": {"func": "set", "type": None},     # Stop Emission
    "EMON":  {"func": "set", "type": None},     # Start Emission
    "EPM":   {"func": "set", "type": None},     # Enable PULSE Mode
    "RERR":  {"func": "set", "type": None},     # Reset Errors
    "RBT":   {"func": "get", "type": float},    # Read Board Temperature
    "RCS":   {"func": "get", "type": float},    # Read Current Setpoint
    "RCT":   {"func": "get", "type": float},    # Read Laser Temperature
    "RDGW":  {"func": "get", "type": str},      # Read Default Gateway
    "RIP":   {"func": "get", "type": str},      # Read IP
    "RMASK": {"func": "get", "type": str},      # Read Sub-net Mask
    "RPRR":  {"func": "get", "type": int},      # Read Pulse Repetition Rate
    "RPW":   {"func": "get", "type": float},    # Read Pulse Width
    "SDC":   {"func": "set", "type": float},    # Set Diode Current
    "SDGW":  {"func": "set", "type": str},      # Set Default Gateway
    "SIP":   {"func": "set", "type": str},      # Set IP
    "SMASK": {"func": "set", "type": str},      # Set Sub-net Mask
    "SPRR":  {"func": "set", "type": int},      # Set Pulse Repetition Rate
    "SPW":   {"func": "set", "type": float},    # Set Pulse Width
    "STA":   {"func": "get", "type": int},      # Read device status
    "STR":   {"func": "get", "type": int},      # Read Raycus Errs
}

# таблица настроек IPG YLR_SERIES
YLR_SERIES = {
    "ABF":   {"func": "set", "type": None},     # Aiming Beam OFF
    "ABN":   {"func": "set", "type": None},     # Aiming Beam ON
    "DEABC": {"func": "set", "type": None},     # Disable External Aiming Beam Control
    "EEABC": {"func": "set", "type": None},     # Enable External Aiming Beam Control
    "DEC":   {"func": "set", "type": None},     # Disable External Control
    "EEC":   {"func": "set", "type": None},     # Enable External Control
    "DGM":   {"func": "set", "type": None},     # Disable Gate Mode
    "EGM":   {"func": "set", "type": None},     # Enable Gate Mode
    "DLE":   {"func": "set", "type": None},     # Disable Hardware Emission Control
    "ELE":   {"func": "set", "type": None},     # Enable Hardware Emission Control
    "DMOD":  {"func": "set", "type": None},     # Disable Modulation
    "EMOD":  {"func": "set", "type": None},     # Enable Modulation
    "DPM":   {"func": "set", "type": None},     # Disable PULSE Mode
    "EPM":   {"func": "set", "type": None},     # Enable PULSE Mode
    "EMOFF": {"func": "set", "type": None},     # Stop Emission
    "EMON":  {"func": "set", "type": None},     # Start Emission
    "LFP":   {"func": "set", "type": None},     # Lock Front Panel
    "UFP":   {"func": "set", "type": None},     # Unlock Front Panel
    "RERR":  {"func": "set", "type": None},     # Reset Errors
    "RCS":   {"func": "get", "type": float},    # Read Current Setpoint
    "SDC":   {"func": "set", "type": float},    # Set Diode Current
    "SPRR":  {"func": "set", "type": int},      # Set Pulse Repetition Rate
    "RPRR":  {"func": "get", "type": int},      # Read Pulse Repetition Rate
    "SPW":   {"func": "set", "type": float},    # Set Pulse Width
    "RPW":   {"func": "get", "type": float},    # Read Pulse Width
    "RCT":   {"func": "get", "type": float},    # Read Laser Temperature
    "RET":   {"func": "get", "type": int},      # Read Elapsed Time
    "RFV":   {"func": "get", "type": str},      # Read current software revision
    "RMEC":  {"func": "get", "type": int},      # Read Module Error Code
    "RNC":   {"func": "get", "type": float},    # Read Minimum Current Setpoint
    "ROP":   {"func": "get", "type": int},      # Read Output Power
    "RPP":   {"func": "get", "type": int},      # Read Peak Power
    "RSN":   {"func": "get", "type": int},      # Read Serial Number
    "STA":   {"func": "get", "type": int},      # Read device status
}
