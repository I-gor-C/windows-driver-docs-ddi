# Declarations in the usbscan header
This header Usbscan contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [DEVICE_DESCRIPTOR structure](ns-usbscan--device-descriptor.md) | The DEVICE_DESCRIPTOR structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_DEVICE_DESCRIPTOR. |
| [USBSCAN_PIPE_CONFIGURATION structure](ns-usbscan--usbscan-pipe-configuration.md) | The USBSCAN_PIPE_CONFIGURATION structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_PIPE_CONFIGURATION. |
| [IO_BLOCK structure](ns-usbscan--io-block.md) | The IO_BLOCK structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_READ_REGISTERS or IOCTL_WRITE_REGISTERS. |
| [DRV_VERSION structure](ns-usbscan--drv-version.md) | The DRV_VERSION structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_VERSION. |
| [IO_BLOCK_EX structure](ns-usbscan--io-block-ex.md) | The IO_BLOCK_EX structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_SEND_USB_REQUEST. |
| [USBSCAN_PIPE_INFORMATION structure](ns-usbscan--usbscan-pipe-information.md) | The USBSCAN_PIPE_INFORMATION structure is used to describe a USB transfer pipe for a still image device. An array of USBSCAN_PIPE_INFORMATION structures is supplied within a USBSCAN_PIPE_CONFIGURATION structure. |
| [USBSCAN_GET_DESCRIPTOR structure](ns-usbscan--usbscan-get-descriptor.md) | The USBSCAN_GET_DESCRIPTOR structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_USB_DESCRIPTOR. |
| [USBSCAN_TIMEOUT structure](ns-usbscan--usbscan-timeout.md) | The USBSCAN_TIMEOUT structure stores time-out values for USB bulk IN and bulk OUT operations, and interrupts. |
| [CHANNEL_INFO structure](ns-usbscan--channel-info.md) | The CHANNEL_INFO structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_CHANNEL_ALIGN_RQST. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_GET_DEVICE_DESCRIPTOR IOCTL](ni-usbscan-ioctl-get-device-descriptor.md) | TBD |
| [IOCTL_WAIT_ON_DEVICE_EVENT IOCTL](ni-usbscan-ioctl-wait-on-device-event.md) | TBD |
| [IOCTL_WRITE_REGISTERS IOCTL](ni-usbscan-ioctl-write-registers.md) | TBD |
| [IOCTL_GET_PIPE_CONFIGURATION IOCTL](ni-usbscan-ioctl-get-pipe-configuration.md) | TBD |
| [IOCTL_GET_VERSION IOCTL](ni-usbscan-ioctl-get-version.md) | TBD |
| [IOCTL_READ_REGISTERS IOCTL](ni-usbscan-ioctl-read-registers.md) | TBD |
| [IOCTL_CANCEL_IO IOCTL](ni-usbscan-ioctl-cancel-io.md) | TBD |
| [IOCTL_GET_CHANNEL_ALIGN_RQST IOCTL](ni-usbscan-ioctl-get-channel-align-rqst.md) | TBD |
| [IOCTL_SET_TIMEOUT IOCTL](ni-usbscan-ioctl-set-timeout.md) | TBD |
| [IOCTL_ABORT_PIPE IOCTL](ni-usbscan-ioctl-abort-pipe.md) | TBD |
| [IOCTL_SEND_USB_REQUEST IOCTL](ni-usbscan-ioctl-send-usb-request.md) | TBD |
| [IOCTL_GET_USB_DESCRIPTOR IOCTL](ni-usbscan-ioctl-get-usb-descriptor.md) | TBD |
| [IOCTL_RESET_PIPE IOCTL](ni-usbscan-ioctl-reset-pipe.md) | TBD |
| [IOCTL_INDEX IOCTL](ni-usbscan-ioctl-index.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [RAW_PIPE_TYPE enumeration](ne-usbscan--raw-pipe-type.md) | The RAW_PIPE_TYPE data type is used to specify the type of a USB pipe. |
| [PIPE_TYPE enumeration](ne-usbscan-pipe-type.md) | The PIPE_TYPE data type is used as input to the DeviceIoControl function, if the I/O control code is IOCTL_CANCEL_IO or IOCTL_RESET_PIPE. |

This header is used in these topics:

- [image](..content/_image)
