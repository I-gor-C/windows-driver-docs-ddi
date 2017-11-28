# Usbscan.h header


This header is used by unknown technology.

Usbscan.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [CHANNEL_INFO structure](ns-usbscan--channel-info.md) | The CHANNEL_INFO structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_CHANNEL_ALIGN_RQST. |
| [DEVICE_DESCRIPTOR structure](ns-usbscan--device-descriptor.md) | The DEVICE_DESCRIPTOR structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_DEVICE_DESCRIPTOR. |
| [DRV_VERSION structure](ns-usbscan--drv-version.md) | The DRV_VERSION structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_VERSION. |
| [IO_BLOCK structure](ns-usbscan--io-block.md) | The IO_BLOCK structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_READ_REGISTERS or IOCTL_WRITE_REGISTERS. |
| [IO_BLOCK_EX structure](ns-usbscan--io-block-ex.md) | The IO_BLOCK_EX structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_SEND_USB_REQUEST. |
| [USBSCAN_GET_DESCRIPTOR structure](ns-usbscan--usbscan-get-descriptor.md) | The USBSCAN_GET_DESCRIPTOR structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_USB_DESCRIPTOR. |
| [USBSCAN_PIPE_CONFIGURATION structure](ns-usbscan--usbscan-pipe-configuration.md) | The USBSCAN_PIPE_CONFIGURATION structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_PIPE_CONFIGURATION. |
| [USBSCAN_PIPE_INFORMATION structure](ns-usbscan--usbscan-pipe-information.md) | The USBSCAN_PIPE_INFORMATION structure is used to describe a USB transfer pipe for a still image device. An array of USBSCAN_PIPE_INFORMATION structures is supplied within a USBSCAN_PIPE_CONFIGURATION structure. |
| [USBSCAN_TIMEOUT structure](ns-usbscan--usbscan-timeout.md) | The USBSCAN_TIMEOUT structure stores time-out values for USB bulk IN and bulk OUT operations, and interrupts. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [PIPE_TYPE enumeration](ne-usbscan-pipe-type.md) | The PIPE_TYPE data type is used as input to the DeviceIoControl function, if the I/O control code is IOCTL_CANCEL_IO or IOCTL_RESET_PIPE. |
| [RAW_PIPE_TYPE enumeration](ne-usbscan--raw-pipe-type.md) | The RAW_PIPE_TYPE data type is used to specify the type of a USB pipe. |
