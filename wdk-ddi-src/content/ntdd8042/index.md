---
UID: NA:ntdd8042
ms.assetid: 20253ca3-2ef9-33f0-991d-bd37be11cc04
ms.author: windowsdriverdev
ms.date: 03/13/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# ntdd8042.h header



ntdd8042.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER](ni-ntdd8042-ioctl_internal_i8042_controller_write_buffer.md) | The IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER request is not supported. |
| [IOCTL_INTERNAL_I8042_HOOK_KEYBOARD](ni-ntdd8042-ioctl_internal_i8042_hook_keyboard.md) | The IOCTL_INTERNAL_I8042_HOOK_KEYBOARD request does the following:Adds an initialization callback routine to the I8042prt keyboard initialization routineAdds an ISR callback routine to the I8042prt keyboard ISRThe initialization and ISR callbacks are optional and are provided by an upper-level filter driver for a PS/2-style keyboard device.After I8042prt receives an IOCTL_INTERNAL_KEYBOARD_CONNECT request, it sends a synchronous IOCTL_INTERNAL_I8042_HOOK_KEYBOARD request to the top of the keyboard device stack.After Kbfiltr receives the hook keyboard request, Kbfiltr filters the request in the following way:Saves the upper-level information passed to Kbfiltr, which includes the context of an upper-level device object, a pointer to an initialization callback, and a pointer to an ISR callbackReplaces the upper-level information with its ownSaves the context of I8042prt and pointers to callbacks that the Kbfiltr ISR callback can useFor more information about this request and the callbacks, see the following topics:I8042prt Callback RoutinesKbfiltr Callback Routines. |
| [IOCTL_INTERNAL_I8042_HOOK_MOUSE](ni-ntdd8042-ioctl_internal_i8042_hook_mouse.md) | The IOCTL_INTERNAL_I8042_HOOK_MOUSE request adds an ISR callback routine to the I8042prt mouse ISR. |
| [IOCTL_INTERNAL_I8042_KEYBOARD_START_INFORMATION](ni-ntdd8042-ioctl_internal_i8042_keyboard_start_information.md) | The IOCTL_INTERNAL_I8042_KEYBOARD_START_INFORMATION request passes a pointer to a keyboard interrupt object. |
| [IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER](ni-ntdd8042-ioctl_internal_i8042_keyboard_write_buffer.md) | The IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a keyboard device. |
| [IOCTL_INTERNAL_I8042_MOUSE_START_INFORMATION](ni-ntdd8042-ioctl_internal_i8042_mouse_start_information.md) | The IOCTL_INTERNAL_I8042_MOUSE_START_INFORMATION request passes a pointer to a mouse interrupt object. |
| [IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER](ni-ntdd8042-ioctl_internal_i8042_mouse_write_buffer.md) | The IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a mouse device. |



## Callback functions
| Title | Description |
| ---- |:---- |
| [PI8042_ISR_WRITE_PORT](nc-ntdd8042-pi8042_isr_write_port.md) | The PI8042_ISR_WRITE_PORT-typed callback routine writes data to an i8042 port. I8042prt provides this callback. |
| [PI8042_KEYBOARD_INITIALIZATION_ROUTINE](nc-ntdd8042-pi8042_keyboard_initialization_routine.md) | A PI8042_KEYBOARD_INITIALIZATION_ROUTINE-typed callback routine supplements the default initialization of a keyboard device by I8042prt. |
| [PI8042_KEYBOARD_ISR](nc-ntdd8042-pi8042_keyboard_isr.md) | A PI8042_KEYBOARD_ISR-typed callback routine customizes the operation of the I8042prt keyboard ISR. |
| [PI8042_MOUSE_ISR](nc-ntdd8042-pi8042_mouse_isr.md) | A PI8042_MOUSE_ISR-typed callback routine customizes the operation of the I8042prt mouse ISR. |
| [PI8042_QUEUE_PACKET](nc-ntdd8042-pi8042_queue_packet.md) | The PI8042_QUEUE_PACKET-typed callback routine queues an input data packet for processing by the ISR DPC of a keyboard or mouse device. I8042prt provides this callback. |
| [PI8042_SYNCH_READ_PORT](nc-ntdd8042-pi8042_synch_read_port.md) | The PI8042_SYNCH_READ_PORT-typed callback routine does a synchronized read from an i8042 port. I8042prt supplies this callback. |
| [PI8042_SYNCH_WRITE_PORT](nc-ntdd8042-pi8042_synch_write_port.md) | The PI8042_SYNCH_READ_PORT-typed callback routine does a synchronized write to an i8042 port. I8042prt supplies this routine. |


## Structures
| Title | Description |
| ---- |:---- |
| [_INTERNAL_I8042_HOOK_KEYBOARD](ns-ntdd8042-_internal_i8042_hook_keyboard.md) | INTERNAL_I8042_HOOK_KEYBOARD is used by I8042prt to connect optional callback routines that supplement keyboard initialization and the keyboard ISR. The callbacks can be supplied by an optional, vendor-supplied, upper-level filter driver. |
| [_INTERNAL_I8042_HOOK_MOUSE](ns-ntdd8042-_internal_i8042_hook_mouse.md) | INTERNAL_I8042_HOOK_MOUSE is used by I8042prt to connect an optional callback routine that supplements the operation of the mouse ISR. The callback can be supplied by an optional, vendor-supplied, upper-level filter driver. |
| [_INTERNAL_I8042_START_INFORMATION](ns-ntdd8042-_internal_i8042_start_information.md) | INTERNAL_I8042_START_INFORMATION specifies the interrupt object that an optional, vendor-supplied, upper-level filter device driver can use to synchronize its operation with an I8042prt ISR. |
| [_OUTPUT_PACKET](ns-ntdd8042-_output_packet.md) | OUTPUT_PACKET contains information about the data that is being written to a keyboard or mouse device by I8042prt. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_KEYBOARD_SCAN_STATE](ne-ntdd8042-_keyboard_scan_state.md) | The KEYBOARD_SCAN_STATE enumeration type indicates the scan state of an input byte from a keyboard. |
| [_MOUSE_STATE](ne-ntdd8042-_mouse_state.md) | The MOUSE_STATE enumeration type identifies the current state of input from a mouse. |