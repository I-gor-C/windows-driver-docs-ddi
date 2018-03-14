---
UID: NA:ntddser
ms.assetid: 1ef9acf8-d5d8-39b0-a68c-2a25e1e7e669
ms.author: windowsdriverdev
ms.date: 03/13/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# ntddser.h header



ntddser.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_INTERNAL_SERENUM_REMOVE_SELF](ni-ntddser-ioctl_internal_serenum_remove_self.md) | The IOCTL_INTERNAL_SERENUM_REMOVE_SELF request invalidates the bus relations of the filter DO that are associated with a target PDO. (Physically, this request invalidates the bus relations of the RS-232 port to which the target device is attached.). |
| [IOCTL_SERENUM_GET_PORT_NAME](ni-ntddser-ioctl_serenum_get_port_name.md) | The IOCTL_SERENUM_GET_PORT_NAME request returns the value of the PortName (or Identifier) entry value for the RS-232 port -- see Registry Settings for a Plug and Play Serial Device. |
| [IOCTL_SERENUM_PORT_DESC](ni-ntddser-ioctl_serenum_port_desc.md) | The IOCTL_SERENUM_PORT_DESC request returns a description of the RS-232 port associated with a filter DO. |
| [IOCTL_SERIAL_APPLY_DEFAULT_CONFIGURATION](ni-ntddser-ioctl_serial_apply_default_configuration.md) | The IOCTL_SERIAL_APPLY_DEFAULT_CONFIGURATION control code configures the serial port to use the default hardware settings for the serial controller device. |
| [IOCTL_SERIAL_CLEAR_STATS](ni-ntddser-ioctl_serial_clear_stats.md) | The IOCTL_SERIAL_CLEAR_STATS request clears the performance statistics for a serial device. |
| [IOCTL_SERIAL_CLR_DTR](ni-ntddser-ioctl_serial_clr_dtr.md) | The IOCTL_SERIAL_CLR_DTR request clears the data terminal ready (DTR) control signal. |
| [IOCTL_SERIAL_CLR_RTS](ni-ntddser-ioctl_serial_clr_rts.md) | The IOCTL_SERIAL_CLR_RTS request clears the request to send (RTS) control signal. |
| [IOCTL_SERIAL_CONFIG_SIZE](ni-ntddser-ioctl_serial_config_size.md) | The IOCTL_SERIAL_CONFIG_SIZE request returns information about configuration size. |
| [IOCTL_SERIAL_GET_BAUD_RATE](ni-ntddser-ioctl_serial_get_baud_rate.md) | The IOCTL_SERIAL_GET_BAUD_RATE request returns the baud rate at which the serial port is currently configured to transmit and receive data. |
| [IOCTL_SERIAL_GET_CHARS](ni-ntddser-ioctl_serial_get_chars.md) | The IOCTL_SERIAL_GET_CHARS request retrieves the special characters that the serial controller driver uses with handshake flow control. The special characters are described by a SERIAL_CHARS structure. |
| [IOCTL_SERIAL_GET_COMMSTATUS](ni-ntddser-ioctl_serial_get_commstatus.md) | The IOCTL_SERIAL_GET_COMMSTATUS request returns information about the communication status of a serial device. For more information about the status information that is retrieved by this request, see SERIAL_STATUS. |
| [IOCTL_SERIAL_GET_DTRRTS](ni-ntddser-ioctl_serial_get_dtrrts.md) | The IOCTL_SERIAL_GET_DTRRTS request returns information about the data terminal ready (DTR) control signal and the request to send (RTS) control signal. |
| [IOCTL_SERIAL_GET_HANDFLOW](ni-ntddser-ioctl_serial_get_handflow.md) | The IOCTL_SERIAL_GET_HANDFLOW request returns information about the configuration of the handshake flow control set for a serial device. |
| [IOCTL_SERIAL_GET_LINE_CONTROL](ni-ntddser-ioctl_serial_get_line_control.md) | The IOCTL_SERIAL_GET_LINE_CONTROL request returns information about the line control set for a serial device. The line control parameters include the number of stop bits, the number of data bits, and the parity. |
| [IOCTL_SERIAL_GET_MODEM_CONTROL](ni-ntddser-ioctl_serial_get_modem_control.md) | The IOCTL_SERIAL_GET_MODEM_CONTROL request returns the value of the modem control register in the serial controller. |
| [IOCTL_SERIAL_GET_MODEMSTATUS](ni-ntddser-ioctl_serial_get_modemstatus.md) | The IOCTL_SERIAL_GET_MODEMSTATUS request updates the modem status, and returns the value of the modem status register before the update. |
| [IOCTL_SERIAL_GET_PROPERTIES](ni-ntddser-ioctl_serial_get_properties.md) | The IOCTL_SERIAL_GET_PROPERTIES request returns information about the capabilities of a serial controller. The capabilities information is returned in a SERIAL_COMMPROP structure. |
| [IOCTL_SERIAL_GET_STATS](ni-ntddser-ioctl_serial_get_stats.md) | The IOCTL_SERIAL_GET_STATS request returns information about the performance of a serial controller. |
| [IOCTL_SERIAL_GET_TIMEOUTS](ni-ntddser-ioctl_serial_get_timeouts.md) | The IOCTL_SERIAL_GET_TIMEOUTS request returns the current setting of the time-out value that the system-supplied bus driver for parallel ports uses with write requests. |
| [IOCTL_SERIAL_GET_WAIT_MASK](ni-ntddser-ioctl_serial_get_wait_mask.md) | The IOCTL_SERIAL_GET_WAIT_MASK request returns the event wait mask that is currently set for the serial controller. |
| [IOCTL_SERIAL_IMMEDIATE_CHAR](ni-ntddser-ioctl_serial_immediate_char.md) | The IOCTL_SERIAL_IMMEDIATE_CHAR request causes a specified character to be transmitted as soon as possible. |
| [IOCTL_SERIAL_INTERNAL_BASIC_SETTINGS](ni-ntddser-ioctl_serial_internal_basic_settings.md) | The IOCTL_SERIAL_INTERNAL_BASIC_SETTINGS request sets a serial device to a basic operating mode. |
| [IOCTL_SERIAL_INTERNAL_CANCEL_WAIT_WAKE](ni-ntddser-ioctl_serial_internal_cancel_wait_wake.md) | The IOCTL_SERIAL_INTERNAL_CANCEL_WAIT_WAKE request disables the wait/wake operation of a serial device. |
| [IOCTL_SERIAL_INTERNAL_DO_WAIT_WAKE](ni-ntddser-ioctl_serial_internal_do_wait_wake.md) | The IOCTL_SERIAL_INTERNAL_DO_WAIT_WAKE request enables the wait/wake operation of a serial device. |
| [IOCTL_SERIAL_INTERNAL_RESTORE_SETTINGS](ni-ntddser-ioctl_serial_internal_restore_settings.md) | The IOCTL_SERIAL_INTERNAL_RESTORE_SETTINGS request restores the specified operating mode of a serial device. |
| [IOCTL_SERIAL_LSRMST_INSERT](ni-ntddser-ioctl_serial_lsrmst_insert.md) | The IOCTL_SERIAL_LSRMST_INSERT request enables or disables the insertion of information about line status and modem status in the receive data stream. |
| [IOCTL_SERIAL_PURGE](ni-ntddser-ioctl_serial_purge.md) | The IOCTL_SERIAL_PURGE request cancels the specified requests and deletes data from the specified buffers. |
| [IOCTL_SERIAL_RESET_DEVICE](ni-ntddser-ioctl_serial_reset_device.md) | The IOCTL_SERIAL_RESET_DEVICE request resets a serial device. |
| [IOCTL_SERIAL_SET_BAUD_RATE](ni-ntddser-ioctl_serial_set_baud_rate.md) | The IOCTL_SERIAL_SET_BAUD_RATE request sets the baud rate on a serial controller device. The serial controller driver verifies the specified baud rate. |
| [IOCTL_SERIAL_SET_BREAK_OFF](ni-ntddser-ioctl_serial_set_break_off.md) | The IOCTL_SERIAL_SET_BREAK_OFF request sets the line control break signal inactive. |
| [IOCTL_SERIAL_SET_BREAK_ON](ni-ntddser-ioctl_serial_set_break_on.md) | The IOCTL_SERIAL_SET_BREAK_ON request sets the line control break signal active. |
| [IOCTL_SERIAL_SET_CHARS](ni-ntddser-ioctl_serial_set_chars.md) | The IOCTL_SERIAL_SET_CHARS request sets the special characters that the serial controller driver uses for handshake flow control. This driver verifies the specified special characters. |
| [IOCTL_SERIAL_SET_DTR](ni-ntddser-ioctl_serial_set_dtr.md) | The IOCTL_SERIAL_SET_DTR request sets DTR (data terminal ready). |
| [IOCTL_SERIAL_SET_FIFO_CONTROL](ni-ntddser-ioctl_serial_set_fifo_control.md) | The IOCTL_SERIAL_SET_FIFO_CONTROL request sets the FIFO control register (FCR). Serial does not verify the specified FIFO control information. |
| [IOCTL_SERIAL_SET_HANDFLOW](ni-ntddser-ioctl_serial_set_handflow.md) | The IOCTL_SERIAL_SET_HANDFLOW request sets the configuration of handshake flow control. The serial controller driver verifies the specified handshake flow control information. |
| [IOCTL_SERIAL_SET_LINE_CONTROL](ni-ntddser-ioctl_serial_set_line_control.md) | The IOCTL_SERIAL_SET_LINE_CONTROL request sets the line control register (LCR). The line control register controls the data size, the number of stop bits, and the parity. |
| [IOCTL_SERIAL_SET_MODEM_CONTROL](ni-ntddser-ioctl_serial_set_modem_control.md) | The IOCTL_SERIAL_SET_MODEM_CONTROL request sets the modem control register (MCR) in the UART. No parameter checking is done on the client-supplied register settings. |
| [IOCTL_SERIAL_SET_QUEUE_SIZE](ni-ntddser-ioctl_serial_set_queue_size.md) | The IOCTL_SERIAL_SET_QUEUE_SIZE request sets the size of the internal receive buffer. If the requested size is greater than the current receive buffer size, a new receive buffer is created. Otherwise, the receive buffer is not changed. |
| [IOCTL_SERIAL_SET_RTS](ni-ntddser-ioctl_serial_set_rts.md) | The IOCTL_SERIAL_SET_RTS request sets RTS (request to send). |
| [IOCTL_SERIAL_SET_TIMEOUTS](ni-ntddser-ioctl_serial_set_timeouts.md) | An IOCTL_SERIAL_SET_TIMEOUTS request resets the time-out value that the system-supplied bus driver for parallel ports uses with write requests. |
| [IOCTL_SERIAL_SET_WAIT_MASK](ni-ntddser-ioctl_serial_set_wait_mask.md) | The IOCTL_SERIAL_SET_WAIT_MASK request configures the serial controller driver to notify a client after the occurrence of any one of a specified set of wait events. |
| [IOCTL_SERIAL_SET_XOFF](ni-ntddser-ioctl_serial_set_xoff.md) | The IOCTL_SERIAL_SET_XOFF request emulates the reception of an XOFF (transmit off) character. |
| [IOCTL_SERIAL_SET_XON](ni-ntddser-ioctl_serial_set_xon.md) | The IOCTL_SERIAL_SET_XON request emulates the reception of a XON (transmit on) character, which restarts reception of data. |
| [IOCTL_SERIAL_WAIT_ON_MASK](ni-ntddser-ioctl_serial_wait_on_mask.md) | The IOCTL_SERIAL_WAIT_ON_MASK request is used to wait for the occurrence of any wait event specified by using an IOCTL_SERIAL_SET_WAIT_MASK request. |
| [IOCTL_SERIAL_XOFF_COUNTER](ni-ntddser-ioctl_serial_xoff_counter.md) | The IOCTL_SERIAL_XOFF_COUNTER request sets an XOFF counter. An XOFF counter request supports clients that use software to emulate hardware handshake flow control. |




## Structures
| Title | Description |
| ---- |:---- |
| [_SERIAL_BAUD_RATE](ns-ntddser-_serial_baud_rate.md) | The SERIAL_BAUD_RATE structure specifies the baud rate at which a serial port is currently configured to transmit and receive data. |
| [_SERIAL_CHARS](ns-ntddser-_serial_chars.md) | The SERIAL_CHARS structure specifies the special characters that the serial controller driver uses for handshake flow control. |
| [_SERIAL_COMMPROP](ns-ntddser-_serial_commprop.md) | The SERIAL_COMMPROP structure specifies the properties of a serial port. |
| [_SERIAL_HANDFLOW](ns-ntddser-_serial_handflow.md) | The SERIAL_HANDFLOW structure specifies the handshake and flow control settings for a serial port. |
| [_SERIAL_LINE_CONTROL](ns-ntddser-_serial_line_control.md) | The SERIAL_LINE_CONTROL structure describes the control settings for the serial line. |
| [_SERIAL_QUEUE_SIZE](ns-ntddser-_serial_queue_size.md) | The SERIAL_QUEUE_SIZE structure is used to resize the input buffer that the serial controller driver uses for serial receive operations. |
| [_SERIAL_STATUS](ns-ntddser-_serial_status.md) | The SERIAL_STATUS structure contains status information about the serial port. |
| [_SERIAL_TIMEOUTS](ns-ntddser-_serial_timeouts.md) | The SERIAL_TIMEOUTS structure specifies the time-out parameters for read and write operations by the serial port. |
| [_SERIALPERF_STATS](ns-ntddser-_serialperf_stats.md) | The SERIALPERF_STATS structure contains performance statistics for a serial port. |