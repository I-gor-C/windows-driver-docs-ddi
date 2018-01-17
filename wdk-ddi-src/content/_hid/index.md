---
UID: TP:hid
ms.assetid: 87c002be-da96-313a-bae1-c6a49c9ce065
ms.author: windowsdriverdev
ms.date: 01/16/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# Human Interface Devices (HID)


Overview of the Human Interface Devices (HID) technology.

To develop Human Interface Devices (HID), you need these headers:

 * [hidpddi.h](..\hidpddi\index.md)
 * [hidport.h](..\hidport\index.md)
 * [kbdmou.h](..\kbdmou\index.md)
 * [ntdd8042.h](..\ntdd8042\index.md)

For the programming guide, see [Human Interface Devices (HID)](https://docs.microsoft.com/en-us/windows-hardware/drivers/hid).

## Functions

| Title   | Description   |
| ---- |:---- |
| [HidP_GetCollectionDescription function](..\hidpddi\nf-hidpddi-hidp_getcollectiondescription.md) | Fills a device description block with collection description and the corresponding report ID information for the specified report descriptor. |
| [HidRegisterMinidriver function](..\hidport\nf-hidport-hidregisterminidriver.md) | The HidRegisterMinidriver routine is called by HID minidrivers, during their initialization, to register with the HID class driver. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PI8042_ISR_WRITE_PORT callback](..\ntdd8042\nc-ntdd8042-pi8042_isr_write_port.md) | The PI8042_ISR_WRITE_PORT-typed callback routine writes data to an i8042 port. I8042prt provides this callback. |
| [PI8042_KEYBOARD_INITIALIZATION_ROUTINE callback](..\ntdd8042\nc-ntdd8042-pi8042_keyboard_initialization_routine.md) | A PI8042_KEYBOARD_INITIALIZATION_ROUTINE-typed callback routine supplements the default initialization of a keyboard device by I8042prt. |
| [PI8042_KEYBOARD_ISR callback](..\ntdd8042\nc-ntdd8042-pi8042_keyboard_isr.md) | A PI8042_KEYBOARD_ISR-typed callback routine customizes the operation of the I8042prt keyboard ISR. |
| [PI8042_MOUSE_ISR callback](..\ntdd8042\nc-ntdd8042-pi8042_mouse_isr.md) | A PI8042_MOUSE_ISR-typed callback routine customizes the operation of the I8042prt mouse ISR. |
| [PI8042_QUEUE_PACKET callback](..\ntdd8042\nc-ntdd8042-pi8042_queue_packet.md) | The PI8042_QUEUE_PACKET-typed callback routine queues an input data packet for processing by the ISR DPC of a keyboard or mouse device. I8042prt provides this callback. |
| [PI8042_SYNCH_READ_PORT callback](..\ntdd8042\nc-ntdd8042-pi8042_synch_read_port.md) | The PI8042_SYNCH_READ_PORT-typed callback routine does a synchronized read from an i8042 port. I8042prt supplies this callback. |
| [PI8042_SYNCH_WRITE_PORT callback](..\ntdd8042\nc-ntdd8042-pi8042_synch_write_port.md) | The PI8042_SYNCH_READ_PORT-typed callback routine does a synchronized write to an i8042 port. I8042prt supplies this routine. |
| [PSERVICE_CALLBACK_ROUTINE callback](..\kbdmou\nc-kbdmou-pservice_callback_routine.md) | A function driver calls the class service callback in its ISR dispatch completion routine. The class service callback transfers input data from the input data buffer of a device to the class data queue. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_CONNECT_DATA structure](..\kbdmou\ns-kbdmou-_connect_data.md) | CONNECT_DATA specifies information that Kbdclass and Mouclass use to connect to a keyboard or mouse port. |
| [_HIDP_COLLECTION_DESC structure](..\hidpddi\ns-hidpddi-_hidp_collection_desc.md) | Contains the information of a top-level-collection. This structure is used in the HidP_GetCollectionDescription call. |
| [_HIDP_DEVICE_DESC structure](..\hidpddi\ns-hidpddi-_hidp_device_desc.md) | Contains the device description block filled in collection descriptions as linked lists. This structure is used by HidP_GetCollectionDescription. |
| [_HIDP_GETCOLDESC_DBG structure](..\hidpddi\ns-hidpddi-_hidp_getcoldesc_dbg.md) | Contains the error code indicating the failure in parsing the report descriptor. This structure is used in the HidP_GetCollectionDescription call. |
| [_HIDP_REPORT_IDS structure](..\hidpddi\ns-hidpddi-_hidp_report_ids.md) | Contains report ID information for a top-level collection. |
| [_HID_DESCRIPTOR structure](..\hidport\ns-hidport-_hid_descriptor.md) | The HID_DESCRIPTOR structure represents a HID descriptor for a HIDClass device. |
| [_HID_DEVICE_ATTRIBUTES structure](..\hidport\ns-hidport-_hid_device_attributes.md) | The HID_DEVICE_ATTRIBUTES structure contains information about a HIDClass device. |
| [_HID_DEVICE_EXTENSION structure](..\hidport\ns-hidport-_hid_device_extension.md) | The HID_DEVICE_EXTENSION structure is used by a HID minidriver as its layout for the device extension of a HIDClass device's functional device object. |
| [_HID_MINIDRIVER_REGISTRATION structure](..\hidport\ns-hidport-_hid_minidriver_registration.md) | The HID_MINIDRIVER_REGISTRATION structure contains registration information that a HID minidriver passes to the HID Client Drivers when the minidriver registers with the class driver. |
| [_INTERNAL_I8042_HOOK_KEYBOARD structure](..\ntdd8042\ns-ntdd8042-_internal_i8042_hook_keyboard.md) | INTERNAL_I8042_HOOK_KEYBOARD is used by I8042prt to connect optional callback routines that supplement keyboard initialization and the keyboard ISR. The callbacks can be supplied by an optional, vendor-supplied, upper-level filter driver. |
| [_INTERNAL_I8042_HOOK_MOUSE structure](..\ntdd8042\ns-ntdd8042-_internal_i8042_hook_mouse.md) | INTERNAL_I8042_HOOK_MOUSE is used by I8042prt to connect an optional callback routine that supplements the operation of the mouse ISR. The callback can be supplied by an optional, vendor-supplied, upper-level filter driver. |
| [_INTERNAL_I8042_START_INFORMATION structure](..\ntdd8042\ns-ntdd8042-_internal_i8042_start_information.md) | INTERNAL_I8042_START_INFORMATION specifies the interrupt object that an optional, vendor-supplied, upper-level filter device driver can use to synchronize its operation with an I8042prt ISR. |
| [_OUTPUT_PACKET structure](..\ntdd8042\ns-ntdd8042-_output_packet.md) | OUTPUT_PACKET contains information about the data that is being written to a keyboard or mouse device by I8042prt. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_KEYBOARD_SCAN_STATE enumeration](..\ntdd8042\ne-ntdd8042-_keyboard_scan_state.md) | The KEYBOARD_SCAN_STATE enumeration type indicates the scan state of an input byte from a keyboard. |
| [_MOUSE_STATE enumeration](..\ntdd8042\ne-ntdd8042-_mouse_state.md) | The MOUSE_STATE enumeration type identifies the current state of input from a mouse. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_HID_ACTIVATE_DEVICE IOCTL](..\hidport\ni-hidport-ioctl_hid_activate_device.md) | The IOCTL_HID_ACTIVATE_DEVICE request activates a HIDClass device, which makes it ready for I/O operations. |
| [IOCTL_HID_DEACTIVATE_DEVICE IOCTL](..\hidport\ni-hidport-ioctl_hid_deactivate_device.md) | The IOCTL_HID_DEACTIVATE_DEVICE request deactivates a HIDClass device, which causes it to stop operations and terminate all outstanding I/O requests. |
| [IOCTL_HID_GET_DEVICE_ATTRIBUTES IOCTL](..\hidport\ni-hidport-ioctl_hid_get_device_attributes.md) | The IOCTL_HID_GET_DEVICE_ATTRIBUTES request obtains a HIDClass device's attributes in a HID_DEVICE_ATTRIBUTES structure. |
| [IOCTL_HID_GET_DEVICE_DESCRIPTOR IOCTL](..\hidport\ni-hidport-ioctl_hid_get_device_descriptor.md) | The IOCTL_HID_GET_DEVICE_DESCRIPTOR request obtains a HIDClass device's HID descriptor. |
| [IOCTL_HID_GET_REPORT_DESCRIPTOR IOCTL](..\hidport\ni-hidport-ioctl_hid_get_report_descriptor.md) | The IOCTL_HID_GET_REPORT_DESCRIPTOR request obtains the report descriptor for a HIDClass device. |
| [IOCTL_HID_GET_STRING IOCTL](..\hidport\ni-hidport-ioctl_hid_get_string.md) | The IOCTL_HID_GET_STRING request obtains a manufacturer ID, product ID, or serial number for a top-level collection. The retrieved string is a NULL-terminated wide character string in a human-readable format. |
| [IOCTL_HID_READ_REPORT IOCTL](..\hidport\ni-hidport-ioctl_hid_read_report.md) | The IOCTL_HID_READ_REPORT request transfers an input report from a HIDClass device into the HID class driver's buffer. |
| [IOCTL_HID_SEND_IDLE_NOTIFICATION_REQUEST IOCTL](..\hidport\ni-hidport-ioctl_hid_send_idle_notification_request.md) | The IOCTL_HID_SEND_IDLE_NOTIFICATION_REQUEST control code is the IOCTL of the idle notification request IRP that HIDClass sends to HID mini drivers, such as HIDUSB, to inform the bus driver that the device is now idle. |
| [IOCTL_HID_WRITE_REPORT IOCTL](..\hidport\ni-hidport-ioctl_hid_write_report.md) | The IOCTL_HID_WRITE_REPORT request sends a HID report to a HIDClass device. |
| [IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER IOCTL](..\ntdd8042\ni-ntdd8042-ioctl_internal_i8042_controller_write_buffer.md) | The IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER request is not supported. |
| [IOCTL_INTERNAL_I8042_HOOK_KEYBOARD IOCTL](..\ntdd8042\ni-ntdd8042-ioctl_internal_i8042_hook_keyboard.md) | The IOCTL_INTERNAL_I8042_HOOK_KEYBOARD request does the following |
| [IOCTL_INTERNAL_I8042_HOOK_MOUSE IOCTL](..\ntdd8042\ni-ntdd8042-ioctl_internal_i8042_hook_mouse.md) | The IOCTL_INTERNAL_I8042_HOOK_MOUSE request adds an ISR callback routine to the I8042prt mouse ISR. |
| [IOCTL_INTERNAL_I8042_KEYBOARD_START_INFORMATION IOCTL](..\ntdd8042\ni-ntdd8042-ioctl_internal_i8042_keyboard_start_information.md) | The IOCTL_INTERNAL_I8042_KEYBOARD_START_INFORMATION request passes a pointer to a keyboard interrupt object. |
| [IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER IOCTL](..\ntdd8042\ni-ntdd8042-ioctl_internal_i8042_keyboard_write_buffer.md) | The IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a keyboard device. |
| [IOCTL_INTERNAL_I8042_MOUSE_START_INFORMATION IOCTL](..\ntdd8042\ni-ntdd8042-ioctl_internal_i8042_mouse_start_information.md) | The IOCTL_INTERNAL_I8042_MOUSE_START_INFORMATION request passes a pointer to a mouse interrupt object. |
| [IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER IOCTL](..\ntdd8042\ni-ntdd8042-ioctl_internal_i8042_mouse_write_buffer.md) | The IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a mouse device. |
| [IOCTL_INTERNAL_KEYBOARD_CONNECT IOCTL](..\kbdmou\ni-kbdmou-ioctl_internal_keyboard_connect.md) | The IOCTL_INTERNAL_KEYBOARD_CONNECT request connects the Kbdclass service to the keyboard device. |
| [IOCTL_INTERNAL_KEYBOARD_DISCONNECT IOCTL](..\kbdmou\ni-kbdmou-ioctl_internal_keyboard_disconnect.md) | The IOCTL_INTERNAL_KEYBOARD_DISCONNECT request is completed with a status of STATUS_NOT_IMPLEMENTED. Note that a Plug and Play keyboard can be added or removed by the Plug and Play manager. |
| [IOCTL_INTERNAL_MOUSE_CONNECT IOCTL](..\kbdmou\ni-kbdmou-ioctl_internal_mouse_connect.md) | The IOCTL_INTERNAL_MOUSE_CONNECT request connects Mouclass service to a mouse device. |
| [IOCTL_INTERNAL_MOUSE_DISCONNECT IOCTL](..\kbdmou\ni-kbdmou-ioctl_internal_mouse_disconnect.md) | The IOCTL_INTERNAL_MOUSE_DISCONNECT request is completed by Moufiltr with an error status of STATUS_NOT_IMPLEMENTED. |
| [IOCTL_UMDF_GET_PHYSICAL_DESCRIPTOR IOCTL](..\hidport\ni-hidport-ioctl_umdf_get_physical_descriptor.md) | The IOCTL_UMDF_GET_PHYSICAL_DESCRIPTOR control code obtains the physical descriptor of a HIDClass device. |
| [IOCTL_UMDF_HID_GET_FEATURE IOCTL](..\hidport\ni-hidport-ioctl_umdf_hid_get_feature.md) | The IOCTL_UMDF_HID_GET_FEATURE control code obtains a feature report from a HIDClass device. |
| [IOCTL_UMDF_HID_GET_INPUT_REPORT IOCTL](..\hidport\ni-hidport-ioctl_umdf_hid_get_input_report.md) | The IOCTL_UMDF_HID_GET_INPUT_REPORT control code returns an input report from a HIDClass device. |
| [IOCTL_UMDF_HID_SET_FEATURE IOCTL](..\hidport\ni-hidport-ioctl_umdf_hid_set_feature.md) | The IOCTL_UMDF_HID_GET_FEATURE control code sends a feature report to a HIDClass device. |
| [IOCTL_UMDF_HID_SET_OUTPUT_REPORT IOCTL](..\hidport\ni-hidport-ioctl_umdf_hid_set_output_report.md) | The IOCTL_UMDF_HID_SET_OUTPUT_REPORT control code sends an output report to a top-level collection. |
