# Hidclass.h header


This header is used by Human Interface Devices (HID). For more information, see
- [Human Interface Devices (HID)](../_hid/index.md)

Hidclass.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [HID_COLLECTION_INFORMATION structure](ns-hidclass--hid-collection-information.md) | The HID_COLLECTION_INFORMATION structure contains general information about a top-level collection. |
| [HID_XFER_PACKET structure](ns-hidclass--hid-xfer-packet.md) | The HID_XFER_PACKET structure contains information about a HID report that the HID class driver uses with I/O requests to get or set a report. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_GET_NUM_DEVICE_INPUT_BUFFERS IOCTL](ni-hidclass-ioctl-get-num-device-input-buffers.md) | The IOCTL_GET_NUM_DEVICE_INPUT_BUFFERS request obtains the size of the input report queue for a top-level collection. |
| [IOCTL_GET_PHYSICAL_DESCRIPTOR IOCTL](ni-hidclass-ioctl-get-physical-descriptor.md) | The IOCTL_GET_PHYSICAL_DESCRIPTOR request obtains the physical descriptor of a top-level collection. |
| [IOCTL_HID_DEVICERESET_NOTIFICATION IOCTL](ni-hidclass-ioctl-hid-devicereset-notification.md) | The IOCTL_HID_DEVICERESET_NOTIFICATION request is sent by the HID client driver to HID class driver to wait for a device-initiated reset event. |
| [IOCTL_HID_DISABLE_SECURE_READ IOCTL](ni-hidclass-ioctl-hid-disable-secure-read.md) | The IOCTL_HID_DISABLE_SECURE_READ request cancels an IOCTL_HID_ENABLE_SECURE_READ request for a HID collection. |
| [IOCTL_HID_ENABLE_SECURE_READ IOCTL](ni-hidclass-ioctl-hid-enable-secure-read.md) | The IOCTL_HID_ENABLE_SECURE_READ request enables a secure read for open files of a HID collection. |
| [IOCTL_HID_ENABLE_WAKE_ON_SX IOCTL](ni-hidclass-ioctl-hid-enable-wake-on-sx.md) | The IOCTL_HID_ENABLE_WAKE_ON_SX request is used to indicate the requirement for a device to be able to wake from system sleep. |
| [IOCTL_HID_FLUSH_QUEUE IOCTL](ni-hidclass-ioctl-hid-flush-queue.md) | The IOCTL_HID_FLUSH_QUEUE request dequeues all of the unparsed input reports from a top-level collection's input report queue. |
| [IOCTL_HID_GET_COLLECTION_DESCRIPTOR IOCTL](ni-hidclass-ioctl-hid-get-collection-descriptor.md) | The IOCTL_HID_GET_COLLECTION_DESCRIPTOR request obtains a top-level collection's preparsed data, which the HID class driver extracted from the physical device's report descriptor during device initialization. |
| [IOCTL_HID_GET_COLLECTION_INFORMATION IOCTL](ni-hidclass-ioctl-hid-get-collection-information.md) | The IOCTL_HID_GET_COLLECTION_INFORMATION request obtains a top-level collection's HID_COLLECTION_INFORMATION structure. |
| [IOCTL_HID_GET_DRIVER_CONFIG IOCTL](ni-hidclass-ioctl-hid-get-driver-config.md) | The IOCTL_HID_GET_DRIVER_CONFIG request retrieves the driver configuration. |
| [IOCTL_HID_GET_FEATURE IOCTL](ni-hidclass-ioctl-hid-get-feature.md) | The IOCTL_HID_GET_FEATURE request obtains a feature report from a HIDClass device. |
| [IOCTL_HID_GET_HARDWARE_ID IOCTL](ni-hidclass-ioctl-hid-get-hardware-id.md) | The IOCTL_HID_GET_HARDWARE_ID request obtains the Plug and Play hardware ID of a top-level collection. |
| [IOCTL_HID_GET_INDEXED_STRING IOCTL](ni-hidclass-ioctl-hid-get-indexed-string.md) | The IOCTL_HID_GET_INDEXED_STRING request obtains a specified embedded string for a top-level collection. |
| [IOCTL_HID_GET_INPUT_REPORT IOCTL](ni-hidclass-ioctl-hid-get-input-report.md) | IOCTL_HID_GET_INPUT_REPORT returns an input report from a HID Class device. |
| [IOCTL_HID_GET_MANUFACTURER_STRING IOCTL](ni-hidclass-ioctl-hid-get-manufacturer-string.md) | The IOCTL_HID_GET_MANUFACTURER_STRING request obtains a top-level collection's embedded string that identifies the manufacturer of the device. |
| [IOCTL_HID_GET_MS_GENRE_DESCRIPTOR IOCTL](ni-hidclass-ioctl-hid-get-ms-genre-descriptor.md) | The IOCTL_HID_GET_MS_GENRE_DESCRIPTOR request is used for retrieving the genre descriptor for the device. |
| [IOCTL_HID_GET_POLL_FREQUENCY_MSEC IOCTL](ni-hidclass-ioctl-hid-get-poll-frequency-msec.md) | The IOCTL_HID_GET_POLL_FREQUENCY_MSEC request obtains the current polling frequency, in milliseconds, of a top-level collection. |
| [IOCTL_HID_GET_PRODUCT_STRING IOCTL](ni-hidclass-ioctl-hid-get-product-string.md) | The IOCTL_HID_GET_PRODUCT_STRING request obtains a top-level collection's embedded string that identifies the manufacturer's product. The retrieved string is a NULL-terminated wide character string in a human-readable format. |
| [IOCTL_HID_GET_SERIALNUMBER_STRING IOCTL](ni-hidclass-ioctl-hid-get-serialnumber-string.md) | The IOCTL_HID_GET_SERIALNUMBER_STRING request obtains a top-level collection's embedded string that identifies the device's serial number. |
| [IOCTL_HID_SET_DRIVER_CONFIG IOCTL](ni-hidclass-ioctl-hid-set-driver-config.md) | The IOCTL_HID_SET_DRIVER_CONFIG request sets the driver configuration. |
| [IOCTL_HID_SET_FEATURE IOCTL](ni-hidclass-ioctl-hid-set-feature.md) | IOCTL_HID_SET_FEATURE sends a feature report to a HIDClass device. |
| [IOCTL_HID_SET_OUTPUT_REPORT IOCTL](ni-hidclass-ioctl-hid-set-output-report.md) | The IOCTL_HID_SET_OUTPUT_REPORT request sends an output report to a top-level collection. |
| [IOCTL_HID_SET_POLL_FREQUENCY_MSEC IOCTL](ni-hidclass-ioctl-hid-set-poll-frequency-msec.md) | The IOCTL_HID_SET_POLL_FREQUENCY_MSEC request sets the polling frequency, in milliseconds, for a top-level collection. |
| [IOCTL_HID_SET_S0_IDLE_TIMEOUT IOCTL](ni-hidclass-ioctl-hid-set-s0-idle-timeout.md) | The IOCTL_HID_SET_S0_IDLE_TIMEOUT request is used by a client to inform the HID class driver about the client's preferred idle timeout value. |
| [IOCTL_SET_NUM_DEVICE_INPUT_BUFFERS IOCTL](ni-hidclass-ioctl-set-num-device-input-buffers.md) | The IOCTL_SET_NUM_DEVICE_INPUT_BUFFERS request sets the number of buffers for the input report queue of a top-level collection. |
