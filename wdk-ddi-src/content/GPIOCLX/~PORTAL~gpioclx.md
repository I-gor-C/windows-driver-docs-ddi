# Declarations in the gpioclx header
This header Gpioclx contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [GPIO_CLX_RegisterClient function](nf-gpioclx-gpio-clx-registerclient.md) | The GPIO_CLX_RegisterClient method registers a general-purpose I/O (GPIO) controller driver as a client of the GPIO framework extension (GpioClx). |
| [GPIO_CLX_ProcessAddDevicePostDeviceCreate function](nf-gpioclx-gpio-clx-processadddevicepostdevicecreate.md) | The GPIO_CLX_ProcessAddDevicePostDeviceCreate method passes a framework device object to the GPIO framework extension (GpioClx). |
| [GPIO_CLX_AcquireInterruptLock function](nf-gpioclx-gpio-clx-acquireinterruptlock.md) | The GPIO_CLX_AcquireInterruptLock method acquires an interrupt lock on a bank of pins in the general-purpose I/O (GPIO) controller. |
| [GPIO_CLX_ReleaseInterruptLock function](nf-gpioclx-gpio-clx-releaseinterruptlock.md) | The GPIO_CLX_ReleaseInterruptLock method releases an interrupt lock on the specified bank. |
| [GPIO_CLX_UnregisterClient function](nf-gpioclx-gpio-clx-unregisterclient.md) | The GPIO_CLX_UnregisterClient method removes a general-purpose I/O (GPIO) controller driver's registration with the GPIO framework extension (GpioClx). |
| [GPIO_CLX_ProcessAddDevicePreDeviceCreate function](nf-gpioclx-gpio-clx-processadddevicepredevicecreate.md) | The GPIO_CLX_ProcessAddDevicePreDeviceCreate method loads initialization information into two structures that are passed as input parameters to the WdfDeviceCreate method. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [GPIO_CLX_PROCESS_ADD_DEVICE_POST_DEVICE_CREATE callback function](nc-gpioclx-gpio-clx-process-add-device-post-device-create.md) | TBD |
| [GPIO_CLIENT_RECONFIGURE_INTERRUPT callback function](nc-gpioclx-gpio-client-reconfigure-interrupt.md) | TBD |
| [GPIO_CLIENT_CONNECT_IO_PINS callback function](nc-gpioclx-gpio-client-connect-io-pins.md) | TBD |
| [GPIO_CLX_ACQUIRE_INTERRUPT_LOCK callback function](nc-gpioclx-gpio-clx-acquire-interrupt-lock.md) | TBD |
| [GPIO_CLIENT_QUERY_CONTROLLER_BASIC_INFORMATION callback function](nc-gpioclx-gpio-client-query-controller-basic-information.md) | TBD |
| [GPIO_CLX_PROCESS_ADD_DEVICE_PRE_DEVICE_CREATE callback function](nc-gpioclx-gpio-clx-process-add-device-pre-device-create.md) | TBD |
| [GPIO_CLIENT_WRITE_PINS callback function](nc-gpioclx-gpio-client-write-pins.md) | TBD |
| [GPIO_CLIENT_READ_PINS_MASK callback function](nc-gpioclx-gpio-client-read-pins-mask.md) | TBD |
| [GPIO_CLX_UNREGISTER_CLIENT callback function](nc-gpioclx-gpio-clx-unregister-client.md) | TBD |
| [PGPIO_CLX_EXPORTED_INTERFACES callback function](nc-gpioclx-pgpio-clx-exported-interfaces.md) | TBD |
| [GPIO_CLIENT_START_CONTROLLER callback function](nc-gpioclx-gpio-client-start-controller.md) | TBD |
| [GPIO_CLIENT_RESTORE_BANK_HARDWARE_CONTEXT callback function](nc-gpioclx-gpio-client-restore-bank-hardware-context.md) | TBD |
| [GPIO_CLIENT_STOP_CONTROLLER callback function](nc-gpioclx-gpio-client-stop-controller.md) | TBD |
| [GPIO_CLIENT_SAVE_BANK_HARDWARE_CONTEXT callback function](nc-gpioclx-gpio-client-save-bank-hardware-context.md) | TBD |
| [GPIO_CLIENT_RELEASE_CONTROLLER callback function](nc-gpioclx-gpio-client-release-controller.md) | TBD |
| [GPIO_CLX_RELEASE_INTERRUPT_LOCK callback function](nc-gpioclx-gpio-clx-release-interrupt-lock.md) | TBD |
| [GPIO_CLIENT_PRE_PROCESS_CONTROLLER_INTERRUPT callback function](nc-gpioclx-gpio-client-pre-process-controller-interrupt.md) | TBD |
| [GPIO_CLIENT_DISCONNECT_FUNCTION_CONFIG_PINS callback function](nc-gpioclx-gpio-client-disconnect-function-config-pins.md) | TBD |
| [GPIO_CLIENT_QUERY_ACTIVE_INTERRUPTS callback function](nc-gpioclx-gpio-client-query-active-interrupts.md) | TBD |
| [GPIO_CLX_REGISTER_CLIENT callback function](nc-gpioclx-gpio-clx-register-client.md) | TBD |
| [GPIO_CLIENT_QUERY_ENABLED_INTERRUPTS callback function](nc-gpioclx-gpio-client-query-enabled-interrupts.md) | TBD |
| [GPIO_CLIENT_MASK_INTERRUPTS callback function](nc-gpioclx-gpio-client-mask-interrupts.md) | TBD |
| [GPIO_CLIENT_PREPARE_CONTROLLER callback function](nc-gpioclx-gpio-client-prepare-controller.md) | TBD |
| [GPIO_CLIENT_CLEAR_ACTIVE_INTERRUPTS callback function](nc-gpioclx-gpio-client-clear-active-interrupts.md) | TBD |
| [GPIO_CLIENT_CONNECT_FUNCTION_CONFIG_PINS callback function](nc-gpioclx-gpio-client-connect-function-config-pins.md) | TBD |
| [GPIO_CLIENT_QUERY_SET_CONTROLLER_INFORMATION callback function](nc-gpioclx-gpio-client-query-set-controller-information.md) | TBD |
| [GPIO_CLIENT_UNMASK_INTERRUPT callback function](nc-gpioclx-gpio-client-unmask-interrupt.md) | TBD |
| [GPIO_CLIENT_CONTROLLER_SPECIFIC_FUNCTION callback function](nc-gpioclx-gpio-client-controller-specific-function.md) | TBD |
| [GPIO_CLIENT_DISCONNECT_IO_PINS callback function](nc-gpioclx-gpio-client-disconnect-io-pins.md) | TBD |
| [GPIO_CLIENT_WRITE_PINS_MASK callback function](nc-gpioclx-gpio-client-write-pins-mask.md) | TBD |
| [GPIO_CLIENT_READ_PINS callback function](nc-gpioclx-gpio-client-read-pins.md) | TBD |
| [GPIO_CLIENT_DISABLE_INTERRUPT callback function](nc-gpioclx-gpio-client-disable-interrupt.md) | TBD |
| [GPIO_CLIENT_ENABLE_INTERRUPT callback function](nc-gpioclx-gpio-client-enable-interrupt.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [GPIO_RECONFIGURE_INTERRUPTS_PARAMETERS structure](ns-gpioclx--gpio-reconfigure-interrupts-parameters.md) | TBD |
| [GPIO_CLEAR_ACTIVE_INTERRUPTS_PARAMETERS structure](ns-gpioclx--gpio-clear-active-interrupts-parameters.md) | TBD |
| [GPIO_CONNECT_IO_PINS_PARAMETERS structure](ns-gpioclx--gpio-connect-io-pins-parameters.md) | The GPIO_CONNECT_IO_PINS_PARAMETERS structure describes a logical connection to a set of general-purpose I/O (GPIO) pins and specifies whether to configure these pins as data inputs or outputs. |
| [GPIO_DISABLE_INTERRUPT_PARAMETERS structure](ns-gpioclx--gpio-disable-interrupt-parameters.md) | The GPIO_DISABLE_INTERRUPT_PARAMETERS structure describes a general-purpose I/O (GPIO) interrupt pin to disable. |
| [GPIO_CLIENT_REGISTRATION_PACKET structure](ns-gpioclx--gpio-client-registration-packet.md) | The GPIO_CLIENT_REGISTRATION_PACKET structure contains registration information that the general-purpose I/O (GPIO) controller driver passes to the GPIO framework extension (GpioClx). |
| [GPIO_QUERY_ENABLED_INTERRUPTS_PARAMETERS structure](ns-gpioclx--gpio-query-enabled-interrupts-parameters.md) | TBD |
| [GPIO_READ_PINS_MASK_PARAMETERS structure](ns-gpioclx--gpio-read-pins-mask-parameters.md) | The GPIO_READ_PINS_MASK_PARAMETERS structure describes a read operation on a bank of general-purpose I/O (GPIO) pins. |
| [GPIO_SAVE_RESTORE_BANK_HARDWARE_CONTEXT_PARAMETERS structure](ns-gpioclx--gpio-save-restore-bank-hardware-context-parameters.md) | TBD |
| [GPIO_QUERY_ACTIVE_INTERRUPTS_PARAMETERS structure](ns-gpioclx--gpio-query-active-interrupts-parameters.md) | TBD |
| [GPIO_WRITE_PINS_FLAGS structure](ns-gpioclx--gpio-write-pins-flags.md) | TBD |
| [GPIO_ENABLE_INTERRUPT_FLAGS structure](ns-gpioclx--gpio-enable-interrupt-flags.md) | TBD |
| [CLIENT_CONTROLLER_BASIC_INFORMATION structure](ns-gpioclx--client-controller-basic-information.md) | The CLIENT_CONTROLLER_BASIC_INFORMATION structure contains general-purpose I/O (GPIO) controller hardware attributes and configuration information. |
| [GPIO_DISABLE_INTERRUPT_FLAGS structure](ns-gpioclx--gpio-disable-interrupt-flags.md) | TBD |
| [CONTROLLER_ATTRIBUTE_FLAGS structure](ns-gpioclx--controller-attribute-flags.md) | The CONTROLLER_ATTRIBUTE_FLAGS structure describes the hardware attributes of the general-purpose I/O (GPIO) controller device. |
| [GPIO_DISCONNECT_FUNCTION_CONFIG_PINS_PARAMETERS structure](ns-gpioclx--gpio-disconnect-function-config-pins-parameters.md) | TBD |
| [GPIO_CONNECT_FUNCTION_CONFIG_PINS_PARAMETERS structure](ns-gpioclx--gpio-connect-function-config-pins-parameters.md) | TBD |
| [GPIO_ENABLE_INTERRUPT_PARAMETERS structure](ns-gpioclx--gpio-enable-interrupt-parameters.md) | The GPIO_ENABLE_INTERRUPT_PARAMETERS structure specifies a general-purpose I/O (GPIO) pin and describes the interrupt attributes of this pin. |
| [GPIO_MASK_INTERRUPT_PARAMETERS structure](ns-gpioclx--gpio-mask-interrupt-parameters.md) | The GPIO_MASK_INTERRUPT_PARAMETERS structure describes a set of general-purpose I/O (GPIO) interrupt pins to mask. |
| [GPIO_CONNECT_FUNCTION_CONFIG_PINS_FLAGS structure](ns-gpioclx--gpio-connect-function-config-pins-flags.md) | TBD |
| [GPIO_READ_PINS_PARAMETERS structure](ns-gpioclx--gpio-read-pins-parameters.md) | The GPIO_READ_PINS_PARAMETERS structure describes a read operation on a group of general-purpose I/O (GPIO) pins. |
| [GPIO_CLIENT_CONTROLLER_SPECIFIC_FUNCTION_PARAMETERS structure](ns-gpioclx--gpio-client-controller-specific-function-parameters.md) | TBD |
| [GPIO_DISCONNECT_FUNCTION_CONFIG_PINS_FLAGS structure](ns-gpioclx--gpio-disconnect-function-config-pins-flags.md) | TBD |
| [GPIO_DISCONNECT_IO_PINS_FLAGS structure](ns-gpioclx--gpio-disconnect-io-pins-flags.md) | TBD |
| [GPIO_SAVE_RESTORE_BANK_HARDWARE_CONTEXT_FLAGS structure](ns-gpioclx--gpio-save-restore-bank-hardware-context-flags.md) | TBD |
| [GPIO_READ_PINS_FLAGS structure](ns-gpioclx--gpio-read-pins-flags.md) | TBD |
| [GPIO_RECONFIGURE_INTERRUPT_FLAGS structure](ns-gpioclx--gpio-reconfigure-interrupt-flags.md) | TBD |
| [GPIO_CONNECT_IO_PINS_FLAGS structure](ns-gpioclx--gpio-connect-io-pins-flags.md) | TBD |
| [CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT structure](ns-gpioclx--client-controller-query-set-information-input.md) | TBD |
| [GPIO_WRITE_PINS_PARAMETERS structure](ns-gpioclx--gpio-write-pins-parameters.md) | The GPIO_WRITE_PINS_PARAMETERS structure describes a write operation on a group of general-purpose I/O (GPIO) pins. |
| [GPIO_WRITE_PINS_MASK_PARAMETERS structure](ns-gpioclx--gpio-write-pins-mask-parameters.md) | The GPIO_WRITE_PINS_MASK_PARAMETERS structure describes a write operation on a bank of general-purpose I/O (GPIO) pins. |
| [CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT structure](ns-gpioclx--client-controller-query-set-information-output.md) | TBD |
| [CLIENT_QUERY_BANK_POWER_INFORMATION_OUTPUT structure](ns-gpioclx--client-query-bank-power-information-output.md) | TBD |
| [GPIO_DISCONNECT_IO_PINS_PARAMETERS structure](ns-gpioclx--gpio-disconnect-io-pins-parameters.md) | The GPIO_DISCONNECT_IO_PINS_PARAMETERS structure describes a set of general-purpose I/O (GPIO) pins that are to be disconnected. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [GPIO_CONNECT_IO_PINS_MODE enumeration](ne-gpioclx--gpio-connect-io-pins-mode.md) | The GPIO_CONNECT_IO_PINS_MODE enumeration indicates whether a set of general-purpose I/O (GPIO) pins is configured as inputs or outputs. |
| [CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE enumeration](ne-gpioclx--client-controller-query-set-request-type.md) | The CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE enumeration type indicates what type of attribute information the GPIO framework extension (GpioClx) is requesting from the GPIO controller driver. |
| [GPIO_CLX_EXPORT_INDEX enumeration](ne-gpioclx--gpio-clx-export-index.md) | TBD |

This header is used in these topics:

- [GPIO](..content/_GPIO)
