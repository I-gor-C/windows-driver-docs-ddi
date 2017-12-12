---
UID: NA:
---

# Ntddser.h header

## -description

This header is used by serports. For more information, see
- [serports](../_serports/index.md)

Ntddser.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_SERIALPERF_STATS structure](ns-ntddser-_serialperf_stats.md) | The SERIALPERF_STATS structure contains performance statistics for a serial port. |
| [_SERIAL_BAUD_RATE structure](ns-ntddser-_serial_baud_rate.md) | The SERIAL_BAUD_RATE structure specifies the baud rate at which a serial port is currently configured to transmit and receive data. |
| [_SERIAL_CHARS structure](ns-ntddser-_serial_chars.md) | The SERIAL_CHARS structure specifies the special characters that the serial controller driver uses for handshake flow control. |
| [_SERIAL_COMMPROP structure](ns-ntddser-_serial_commprop.md) | The SERIAL_COMMPROP structure specifies the properties of a serial port. |
| [_SERIAL_HANDFLOW structure](ns-ntddser-_serial_handflow.md) | The SERIAL_HANDFLOW structure specifies the handshake and flow control settings for a serial port. |
| [_SERIAL_LINE_CONTROL structure](ns-ntddser-_serial_line_control.md) | The SERIAL_LINE_CONTROL structure describes the control settings for the serial line. |
| [_SERIAL_QUEUE_SIZE structure](ns-ntddser-_serial_queue_size.md) | The SERIAL_QUEUE_SIZE structure is used to resize the input buffer that the serial controller driver uses for serial receive operations. |
| [_SERIAL_STATUS structure](ns-ntddser-_serial_status.md) | The SERIAL_STATUS structure contains status information about the serial port. |
| [_SERIAL_TIMEOUTS structure](ns-ntddser-_serial_timeouts.md) | The SERIAL_TIMEOUTS structure specifies the time-out parameters for read and write operations by the serial port. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_SERENUM_PORT_DESC IOCTL](ni-ntddser-ioctl_serenum_port_desc.md) | The IOCTL_SERENUM_PORT_DESC request returns a description of the RS-232 port associated with a filter DO. |
