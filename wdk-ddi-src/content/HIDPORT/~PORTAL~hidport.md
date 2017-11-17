# Declarations in the hidport header
This header Hidport contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [HidNotifyPresence function](nf-hidport-hidnotifypresence.md) | TBD |
| [HidRegisterMinidriver function](nf-hidport-hidregisterminidriver.md) | The HidRegisterMinidriver routine is called by HID minidrivers, during their initialization, to register with the HID class driver. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_HID_ACTIVATE_DEVICE IOCTL](ni-hidport-ioctl-hid-activate-device.md) | The IOCTL_HID_ACTIVATE_DEVICE request activates a HIDClass device, which makes it ready for I/O operations. |
| [IOCTL_UMDF_GET_PHYSICAL_DESCRIPTOR IOCTL](ni-hidport-ioctl-umdf-get-physical-descriptor.md) | The IOCTL_UMDF_GET_PHYSICAL_DESCRIPTOR control code obtains the physical descriptor of a HIDClass device. |
| [IOCTL_UMDF_HID_SET_FEATURE IOCTL](ni-hidport-ioctl-umdf-hid-set-feature.md) | The IOCTL_UMDF_HID_GET_FEATURE control code sends a feature report to a HIDClass device. |
| [IOCTL_UMDF_HID_SET_OUTPUT_REPORT IOCTL](ni-hidport-ioctl-umdf-hid-set-output-report.md) | The IOCTL_UMDF_HID_SET_OUTPUT_REPORT control code sends an output report to a top-level collection. |
| [IOCTL_HID_GET_DEVICE_ATTRIBUTES IOCTL](ni-hidport-ioctl-hid-get-device-attributes.md) | The IOCTL_HID_GET_DEVICE_ATTRIBUTES request obtains a HIDClass device's attributes in a HID_DEVICE_ATTRIBUTES structure. |
| [IOCTL_HID_GET_STRING IOCTL](ni-hidport-ioctl-hid-get-string.md) | The IOCTL_HID_GET_STRING request obtains a manufacturer ID, product ID, or serial number for a top-level collection. The retrieved string is a NULL-terminated wide character string in a human-readable format. |
| [IOCTL_HID_GET_DEVICE_DESCRIPTOR IOCTL](ni-hidport-ioctl-hid-get-device-descriptor.md) | The IOCTL_HID_GET_DEVICE_DESCRIPTOR request obtains a HIDClass device's HID descriptor. |
| [IOCTL_HID_SEND_IDLE_NOTIFICATION_REQUEST IOCTL](ni-hidport-ioctl-hid-send-idle-notification-request.md) | The IOCTL_HID_SEND_IDLE_NOTIFICATION_REQUEST control code is the IOCTL of the idle notification request IRP that HIDClass sends to HID mini drivers, such as HIDUSB, to inform the bus driver that the device is now idle. |
| [IOCTL_HID_DEACTIVATE_DEVICE IOCTL](ni-hidport-ioctl-hid-deactivate-device.md) | The IOCTL_HID_DEACTIVATE_DEVICE request deactivates a HIDClass device, which causes it to stop operations and terminate all outstanding I/O requests. |
| [IOCTL_HID_GET_REPORT_DESCRIPTOR IOCTL](ni-hidport-ioctl-hid-get-report-descriptor.md) | The IOCTL_HID_GET_REPORT_DESCRIPTOR request obtains the report descriptor for a HIDClass device. |
| [IOCTL_HID_READ_REPORT IOCTL](ni-hidport-ioctl-hid-read-report.md) | The IOCTL_HID_READ_REPORT request transfers an input report from a HIDClass device into the HID class driver's buffer. |
| [IOCTL_HID_WRITE_REPORT IOCTL](ni-hidport-ioctl-hid-write-report.md) | The IOCTL_HID_WRITE_REPORT request sends a HID report to a HIDClass device. |
| [IOCTL_UMDF_HID_GET_INPUT_REPORT IOCTL](ni-hidport-ioctl-umdf-hid-get-input-report.md) | The IOCTL_UMDF_HID_GET_INPUT_REPORT control code returns an input report from a HIDClass device. |
| [IOCTL_UMDF_HID_GET_FEATURE IOCTL](ni-hidport-ioctl-umdf-hid-get-feature.md) | The IOCTL_UMDF_HID_GET_FEATURE control code obtains a feature report from a HIDClass device. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [HID_MINIDRIVER_REGISTRATION structure](ns-hidport--hid-minidriver-registration.md) | The HID_MINIDRIVER_REGISTRATION structure contains registration information that a HID minidriver passes to the HID Client Drivers when the minidriver registers with the class driver. |
| [HID_SUBMIT_IDLE_NOTIFICATION_CALLBACK_INFO structure](ns-hidport--hid-submit-idle-notification-callback-info.md) | TBD |
| [HID_DEVICE_EXTENSION structure](ns-hidport--hid-device-extension.md) | The HID_DEVICE_EXTENSION structure is used by a HID minidriver as its layout for the device extension of a HIDClass device's functional device object. |
| [HID_DEVICE_ATTRIBUTES structure](ns-hidport--hid-device-attributes.md) | The HID_DEVICE_ATTRIBUTES structure contains information about a HIDClass device. |
| [HID_DESCRIPTOR structure](ns-hidport--hid-descriptor.md) | The HID_DESCRIPTOR structure represents a HID descriptor for a HIDClass device. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [HID_SEND_IDLE_CALLBACK callback function](nc-hidport-hid-send-idle-callback.md) | TBD |

This header is used in these topics:

- [hid](..content/_hid)
- [wdf](..content/_wdf)
