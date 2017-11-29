# Ntdd8042.h header


This header is used by Human Interface Devices (HID). For more information, see
- [Human Interface Devices (HID)](../_hid/index.md)

Ntdd8042.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PI8042_ISR_WRITE_PORT callback](nc-ntdd8042-pi8042-isr-write-port.md) | The PI8042_ISR_WRITE_PORT-typed callback routine writes data to an i8042 port. I8042prt provides this callback. |
| [PI8042_KEYBOARD_INITIALIZATION_ROUTINE callback](nc-ntdd8042-pi8042-keyboard-initialization-routine.md) | A PI8042_KEYBOARD_INITIALIZATION_ROUTINE-typed callback routine supplements the default initialization of a keyboard device by I8042prt. |
| [PI8042_KEYBOARD_ISR callback](nc-ntdd8042-pi8042-keyboard-isr.md) | A PI8042_KEYBOARD_ISR-typed callback routine customizes the operation of the I8042prt keyboard ISR. |
| [PI8042_MOUSE_ISR callback](nc-ntdd8042-pi8042-mouse-isr.md) | A PI8042_MOUSE_ISR-typed callback routine customizes the operation of the I8042prt mouse ISR. |
| [PI8042_QUEUE_PACKET callback](nc-ntdd8042-pi8042-queue-packet.md) | The PI8042_QUEUE_PACKET-typed callback routine queues an input data packet for processing by the ISR DPC of a keyboard or mouse device. I8042prt provides this callback. |
| [PI8042_SYNCH_READ_PORT callback](nc-ntdd8042-pi8042-synch-read-port.md) | The PI8042_SYNCH_READ_PORT-typed callback routine does a synchronized read from an i8042 port. I8042prt supplies this callback. |
| [PI8042_SYNCH_WRITE_PORT callback](nc-ntdd8042-pi8042-synch-write-port.md) | The PI8042_SYNCH_READ_PORT-typed callback routine does a synchronized write to an i8042 port. I8042prt supplies this routine. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [INTERNAL_I8042_HOOK_KEYBOARD structure](ns-ntdd8042--internal-i8042-hook-keyboard.md) | INTERNAL_I8042_HOOK_KEYBOARD is used by I8042prt to connect optional callback routines that supplement keyboard initialization and the keyboard ISR. The callbacks can be supplied by an optional, vendor-supplied, upper-level filter driver. |
| [INTERNAL_I8042_HOOK_MOUSE structure](ns-ntdd8042--internal-i8042-hook-mouse.md) | INTERNAL_I8042_HOOK_MOUSE is used by I8042prt to connect an optional callback routine that supplements the operation of the mouse ISR. The callback can be supplied by an optional, vendor-supplied, upper-level filter driver. |
| [INTERNAL_I8042_START_INFORMATION structure](ns-ntdd8042--internal-i8042-start-information.md) | INTERNAL_I8042_START_INFORMATION specifies the interrupt object that an optional, vendor-supplied, upper-level filter device driver can use to synchronize its operation with an I8042prt ISR. |
| [OUTPUT_PACKET structure](ns-ntdd8042--output-packet.md) | OUTPUT_PACKET contains information about the data that is being written to a keyboard or mouse device by I8042prt. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER IOCTL](ni-ntdd8042-ioctl-internal-i8042-controller-write-buffer.md) | The IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER request is not supported. |
| [IOCTL_INTERNAL_I8042_HOOK_KEYBOARD IOCTL](ni-ntdd8042-ioctl-internal-i8042-hook-keyboard.md) | The IOCTL_INTERNAL_I8042_HOOK_KEYBOARD request does the following |
| [IOCTL_INTERNAL_I8042_HOOK_MOUSE IOCTL](ni-ntdd8042-ioctl-internal-i8042-hook-mouse.md) | The IOCTL_INTERNAL_I8042_HOOK_MOUSE request adds an ISR callback routine to the I8042prt mouse ISR. |
| [IOCTL_INTERNAL_I8042_KEYBOARD_START_INFORMATION IOCTL](ni-ntdd8042-ioctl-internal-i8042-keyboard-start-information.md) | The IOCTL_INTERNAL_I8042_KEYBOARD_START_INFORMATION request passes a pointer to a keyboard interrupt object. |
| [IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER IOCTL](ni-ntdd8042-ioctl-internal-i8042-keyboard-write-buffer.md) | The IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a keyboard device. |
| [IOCTL_INTERNAL_I8042_MOUSE_START_INFORMATION IOCTL](ni-ntdd8042-ioctl-internal-i8042-mouse-start-information.md) | The IOCTL_INTERNAL_I8042_MOUSE_START_INFORMATION request passes a pointer to a mouse interrupt object. |
| [IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER IOCTL](ni-ntdd8042-ioctl-internal-i8042-mouse-write-buffer.md) | The IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a mouse device. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [KEYBOARD_SCAN_STATE enumeration](ne-ntdd8042--keyboard-scan-state.md) | The KEYBOARD_SCAN_STATE enumeration type indicates the scan state of an input byte from a keyboard. |
| [MOUSE_STATE enumeration](ne-ntdd8042--mouse-state.md) | The MOUSE_STATE enumeration type identifies the current state of input from a mouse. |
