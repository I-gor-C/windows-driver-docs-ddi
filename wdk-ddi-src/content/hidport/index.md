---
UID: NA:hidport
---

# Hidport.h header

## -description

This header is used by Human Interface Devices (HID). For more information, see
- [Human Interface Devices (HID)](../_hid/index.md)

Hidport.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [HidRegisterMinidriver function](nf-hidport-hidregisterminidriver.md) | The HidRegisterMinidriver routine is called by HID minidrivers, during their initialization, to register with the HID class driver. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_HID_DESCRIPTOR structure](ns-hidport-_hid_descriptor.md) | The HID_DESCRIPTOR structure represents a HID descriptor for a HIDClass device. |
| [_HID_DEVICE_ATTRIBUTES structure](ns-hidport-_hid_device_attributes.md) | The HID_DEVICE_ATTRIBUTES structure contains information about a HIDClass device. |
| [_HID_DEVICE_EXTENSION structure](ns-hidport-_hid_device_extension.md) | The HID_DEVICE_EXTENSION structure is used by a HID minidriver as its layout for the device extension of a HIDClass device's functional device object. |
| [_HID_MINIDRIVER_REGISTRATION structure](ns-hidport-_hid_minidriver_registration.md) | The HID_MINIDRIVER_REGISTRATION structure contains registration information that a HID minidriver passes to the HID Client Drivers when the minidriver registers with the class driver. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_HID_ACTIVATE_DEVICE IOCTL](ni-hidport-ioctl_hid_activate_device.md) | The IOCTL_HID_ACTIVATE_DEVICE request activates a HIDClass device, which makes it ready for I/O operations. |
| [IOCTL_HID_DEACTIVATE_DEVICE IOCTL](ni-hidport-ioctl_hid_deactivate_device.md) | The IOCTL_HID_DEACTIVATE_DEVICE request deactivates a HIDClass device, which causes it to stop operations and terminate all outstanding I/O requests. |
| [IOCTL_HID_GET_DEVICE_ATTRIBUTES IOCTL](ni-hidport-ioctl_hid_get_device_attributes.md) | The IOCTL_HID_GET_DEVICE_ATTRIBUTES request obtains a HIDClass device's attributes in a HID_DEVICE_ATTRIBUTES structure. |
| [IOCTL_HID_GET_DEVICE_DESCRIPTOR IOCTL](ni-hidport-ioctl_hid_get_device_descriptor.md) | The IOCTL_HID_GET_DEVICE_DESCRIPTOR request obtains a HIDClass device's HID descriptor. |
| [IOCTL_HID_GET_REPORT_DESCRIPTOR IOCTL](ni-hidport-ioctl_hid_get_report_descriptor.md) | The IOCTL_HID_GET_REPORT_DESCRIPTOR request obtains the report descriptor for a HIDClass device. |
| [IOCTL_HID_GET_STRING IOCTL](ni-hidport-ioctl_hid_get_string.md) | The IOCTL_HID_GET_STRING request obtains a manufacturer ID, product ID, or serial number for a top-level collection. The retrieved string is a NULL-terminated wide character string in a human-readable format. |
| [IOCTL_HID_READ_REPORT IOCTL](ni-hidport-ioctl_hid_read_report.md) | The IOCTL_HID_READ_REPORT request transfers an input report from a HIDClass device into the HID class driver's buffer. |
| [IOCTL_HID_SEND_IDLE_NOTIFICATION_REQUEST IOCTL](ni-hidport-ioctl_hid_send_idle_notification_request.md) | The IOCTL_HID_SEND_IDLE_NOTIFICATION_REQUEST control code is the IOCTL of the idle notification request IRP that HIDClass sends to HID mini drivers, such as HIDUSB, to inform the bus driver that the device is now idle. |
| [IOCTL_HID_WRITE_REPORT IOCTL](ni-hidport-ioctl_hid_write_report.md) | The IOCTL_HID_WRITE_REPORT request sends a HID report to a HIDClass device. |
| [IOCTL_UMDF_GET_PHYSICAL_DESCRIPTOR IOCTL](ni-hidport-ioctl_umdf_get_physical_descriptor.md) | The IOCTL_UMDF_GET_PHYSICAL_DESCRIPTOR control code obtains the physical descriptor of a HIDClass device. |
| [IOCTL_UMDF_HID_GET_FEATURE IOCTL](ni-hidport-ioctl_umdf_hid_get_feature.md) | The IOCTL_UMDF_HID_GET_FEATURE control code obtains a feature report from a HIDClass device. |
| [IOCTL_UMDF_HID_GET_INPUT_REPORT IOCTL](ni-hidport-ioctl_umdf_hid_get_input_report.md) | The IOCTL_UMDF_HID_GET_INPUT_REPORT control code returns an input report from a HIDClass device. |
| [IOCTL_UMDF_HID_SET_FEATURE IOCTL](ni-hidport-ioctl_umdf_hid_set_feature.md) | The IOCTL_UMDF_HID_GET_FEATURE control code sends a feature report to a HIDClass device. |
| [IOCTL_UMDF_HID_SET_OUTPUT_REPORT IOCTL](ni-hidport-ioctl_umdf_hid_set_output_report.md) | The IOCTL_UMDF_HID_SET_OUTPUT_REPORT control code sends an output report to a top-level collection. |
