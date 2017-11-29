# Gpioclx.h header


This header is used by GPIO. For more information, see
- [GPIO](../_GPIO/index.md)

Gpioclx.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [GPIO_CLX_AcquireInterruptLock function](nf-gpioclx-gpio-clx-acquireinterruptlock.md) | The GPIO_CLX_AcquireInterruptLock method acquires an interrupt lock on a bank of pins in the general-purpose I/O (GPIO) controller. |
| [GPIO_CLX_ProcessAddDevicePostDeviceCreate function](nf-gpioclx-gpio-clx-processadddevicepostdevicecreate.md) | The GPIO_CLX_ProcessAddDevicePostDeviceCreate method passes a framework device object to the GPIO framework extension (GpioClx). |
| [GPIO_CLX_ProcessAddDevicePreDeviceCreate function](nf-gpioclx-gpio-clx-processadddevicepredevicecreate.md) | The GPIO_CLX_ProcessAddDevicePreDeviceCreate method loads initialization information into two structures that are passed as input parameters to the WdfDeviceCreate method. |
| [GPIO_CLX_RegisterClient function](nf-gpioclx-gpio-clx-registerclient.md) | The GPIO_CLX_RegisterClient method registers a general-purpose I/O (GPIO) controller driver as a client of the GPIO framework extension (GpioClx). |
| [GPIO_CLX_ReleaseInterruptLock function](nf-gpioclx-gpio-clx-releaseinterruptlock.md) | The GPIO_CLX_ReleaseInterruptLock method releases an interrupt lock on the specified bank. |
| [GPIO_CLX_UnregisterClient function](nf-gpioclx-gpio-clx-unregisterclient.md) | The GPIO_CLX_UnregisterClient method removes a general-purpose I/O (GPIO) controller driver's registration with the GPIO framework extension (GpioClx). |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [GPIO_CLIENT_CLEAR_ACTIVE_INTERRUPTS callback](nc-gpioclx-gpio-client-clear-active-interrupts.md) | The CLIENT_ClearActiveInterrupts event callback function clears active interrupts on a set of general-purpose I/O (GPIO) pins that are configured as interrupt inputs. |
| [GPIO_CLIENT_CONNECT_IO_PINS callback](nc-gpioclx-gpio-client-connect-io-pins.md) | The CLIENT_ConnectIoPins event callback function opens a logical connection to a set of general-purpose I/O (GPIO) pins and configures these pins for data read or write operations. |
| [GPIO_CLIENT_CONTROLLER_SPECIFIC_FUNCTION callback](nc-gpioclx-gpio-client-controller-specific-function.md) | The CLIENT_ControllerSpecificFunction event callback function performs an operation that is specific to a particular general-purpose I/O (GPIO) controller. |
| [GPIO_CLIENT_DISABLE_INTERRUPT callback](nc-gpioclx-gpio-client-disable-interrupt.md) | The CLIENT_DisableInterrupt event callback function disables interrupts on a general-purpose I/O (GPIO) pin that is configured as an interrupt input. |
| [GPIO_CLIENT_DISCONNECT_IO_PINS callback](nc-gpioclx-gpio-client-disconnect-io-pins.md) | The CLIENT_DisconnectIoPins event callback function closes a logical connection to a set of general-purpose I/O (GPIO) pins that are configured for data read or write operations. |
| [GPIO_CLIENT_ENABLE_INTERRUPT callback](nc-gpioclx-gpio-client-enable-interrupt.md) | The CLIENT_EnableInterrupt event callback function enables interrupts on a general-purpose I/O (GPIO) pin that is configured as an interrupt input. |
| [GPIO_CLIENT_MASK_INTERRUPTS callback](nc-gpioclx-gpio-client-mask-interrupts.md) | The CLIENT_MaskInterrupts event callback function masks interrupts on a set of general-purpose I/O (GPIO) pins that are configured as interrupt inputs. |
| [GPIO_CLIENT_PREPARE_CONTROLLER callback](nc-gpioclx-gpio-client-prepare-controller.md) | The CLIENT_PrepareController event callback function performs any operations that are needed to make the general-purpose I/O (GPIO) controller ready to be accessed by the GPIO controller driver. |
| [GPIO_CLIENT_PRE_PROCESS_CONTROLLER_INTERRUPT callback](nc-gpioclx-gpio-client-pre-process-controller-interrupt.md) | The CLIENT_PreProcessControllerInterrupt event callback function performs any pre-processing of a general-purpose I/O (GPIO) interrupt that must be done immediately if the ISR is scheduled to run at a later time. |
| [GPIO_CLIENT_QUERY_ACTIVE_INTERRUPTS callback](nc-gpioclx-gpio-client-query-active-interrupts.md) | The CLIENT_QueryActiveInterrupts event callback function queries the state of a set of general-purpose I/O (GPIO) pins that are configured as interrupt inputs. |
| [GPIO_CLIENT_QUERY_CONTROLLER_BASIC_INFORMATION callback](nc-gpioclx-gpio-client-query-controller-basic-information.md) | The CLIENT_QueryControllerBasicInformation event callback function retrieves the hardware attributes of the general-purpose I/O (GPIO) controller. |
| [GPIO_CLIENT_QUERY_ENABLED_INTERRUPTS callback](nc-gpioclx-gpio-client-query-enabled-interrupts.md) | The CLIENT_QueryEnabledInterrupts event callback function queries the state of a set of general-purpose I/O (GPIO) pins to determine which pins are both configured as interrupt inputs and enabled for interrupts. |
| [GPIO_CLIENT_QUERY_SET_CONTROLLER_INFORMATION callback](nc-gpioclx-gpio-client-query-set-controller-information.md) | The CLIENT_QuerySetControllerInformation event callback function queries the general-purpose I/O (GPIO) controller driver for the specified set of attributes of the GPIO controller. |
| [GPIO_CLIENT_READ_PINS callback](nc-gpioclx-gpio-client-read-pins.md) | The CLIENT_ReadGpioPins event callback function reads a set of general-purpose I/O (GPIO) pins that are configured as data inputs. |
| [GPIO_CLIENT_READ_PINS_MASK callback](nc-gpioclx-gpio-client-read-pins-mask.md) | The CLIENT_ReadGpioPinsUsingMask event callback function reads a bank of general-purpose I/O (GPIO) pins. |
| [GPIO_CLIENT_RECONFIGURE_INTERRUPT callback](nc-gpioclx-gpio-client-reconfigure-interrupt.md) | The CLIENT_ReconfigureInterrupt event callback function reconfigures a general-purpose I/O (GPIO) pin that is used as an interrupt input. |
| [GPIO_CLIENT_RELEASE_CONTROLLER callback](nc-gpioclx-gpio-client-release-controller.md) | The CLIENT_ReleaseController event callback function performs operations that are needed when the general-purpose I/O (GPIO) controller device is no longer accessible. |
| [GPIO_CLIENT_RESTORE_BANK_HARDWARE_CONTEXT callback](nc-gpioclx-gpio-client-restore-bank-hardware-context.md) | The CLIENT_RestoreBankHardwareContext event callback function restores the hardware context of a bank of general-purpose I/O (GPIO) pins. |
| [GPIO_CLIENT_SAVE_BANK_HARDWARE_CONTEXT callback](nc-gpioclx-gpio-client-save-bank-hardware-context.md) | The CLIENT_SaveBankHardwareContext event callback function saves the hardware context of a bank of general-purpose I/O (GPIO) pins. |
| [GPIO_CLIENT_START_CONTROLLER callback](nc-gpioclx-gpio-client-start-controller.md) | The CLIENT_StartController event callback function performs operations that are needed when the general-purpose I/O (GPIO) controller device enters the D0 power state. |
| [GPIO_CLIENT_STOP_CONTROLLER callback](nc-gpioclx-gpio-client-stop-controller.md) | The CLIENT_StopController event callback function performs operations that are needed to prepare the general-purpose I/O (GPIO) controller device to exit the D0 power state. |
| [GPIO_CLIENT_UNMASK_INTERRUPT callback](nc-gpioclx-gpio-client-unmask-interrupt.md) | The CLIENT_UnmaskInterrupt event callback function unmasks the interrupt on a general-purpose I/O (GPIO) pin that is configured as an interrupt input. |
| [GPIO_CLIENT_WRITE_PINS callback](nc-gpioclx-gpio-client-write-pins.md) | The CLIENT_WriteGpioPins event callback function writes to a set of general-purpose I/O (GPIO) pins that are configured as data outputs. |
| [GPIO_CLIENT_WRITE_PINS_MASK callback](nc-gpioclx-gpio-client-write-pins-mask.md) | The CLIENT_WriteGpioPinsUsingMask event callback function writes to a set of general-purpose I/O (GPIO) pins that are configured as data outputs. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [CLIENT_CONTROLLER_BASIC_INFORMATION structure](ns-gpioclx--client-controller-basic-information.md) | The CLIENT_CONTROLLER_BASIC_INFORMATION structure contains general-purpose I/O (GPIO) controller hardware attributes and configuration information. |
| [CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT structure](ns-gpioclx--client-controller-query-set-information-input.md) | The CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT structure contains a request for the hardware attributes of the general-purpose I/O (GPIO) controller. |
| [CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT structure](ns-gpioclx--client-controller-query-set-information-output.md) | The CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT structure contains a set of general-purpose I/O (GPIO) controller attributes that were requested by the GPIO framework extension (GpioClx). |
| [CLIENT_QUERY_BANK_POWER_INFORMATION_OUTPUT structure](ns-gpioclx--client-query-bank-power-information-output.md) | The CLIENT_QUERY_BANK_POWER_INFORMATION_OUTPUT structure contains information about the power-management capabilities of a bank of general-purpose I/O (GPIO) pins. |
| [CONTROLLER_ATTRIBUTE_FLAGS structure](ns-gpioclx--controller-attribute-flags.md) | The CONTROLLER_ATTRIBUTE_FLAGS structure describes the hardware attributes of the general-purpose I/O (GPIO) controller device. |
| [GPIO_CLEAR_ACTIVE_INTERRUPTS_PARAMETERS structure](ns-gpioclx--gpio-clear-active-interrupts-parameters.md) | The GPIO_CLEAR_ACTIVE_INTERRUPTS_PARAMETERS structure describes a set of general-purpose I/O (GPIO) interrupt pins to clear. |
| [GPIO_CLIENT_CONTROLLER_SPECIFIC_FUNCTION_PARAMETERS structure](ns-gpioclx--gpio-client-controller-specific-function-parameters.md) | The GPIO_CLIENT_CONTROLLER_SPECIFIC_FUNCTION_PARAMETERS structure describes the input and output buffers for a controller-specific operation. |
| [GPIO_CLIENT_REGISTRATION_PACKET structure](ns-gpioclx--gpio-client-registration-packet.md) | The GPIO_CLIENT_REGISTRATION_PACKET structure contains registration information that the general-purpose I/O (GPIO) controller driver passes to the GPIO framework extension (GpioClx). |
| [GPIO_CONNECT_IO_PINS_PARAMETERS structure](ns-gpioclx--gpio-connect-io-pins-parameters.md) | The GPIO_CONNECT_IO_PINS_PARAMETERS structure describes a logical connection to a set of general-purpose I/O (GPIO) pins and specifies whether to configure these pins as data inputs or outputs. |
| [GPIO_DISABLE_INTERRUPT_PARAMETERS structure](ns-gpioclx--gpio-disable-interrupt-parameters.md) | The GPIO_DISABLE_INTERRUPT_PARAMETERS structure describes a general-purpose I/O (GPIO) interrupt pin to disable. |
| [GPIO_DISCONNECT_IO_PINS_PARAMETERS structure](ns-gpioclx--gpio-disconnect-io-pins-parameters.md) | The GPIO_DISCONNECT_IO_PINS_PARAMETERS structure describes a set of general-purpose I/O (GPIO) pins that are to be disconnected. |
| [GPIO_ENABLE_INTERRUPT_PARAMETERS structure](ns-gpioclx--gpio-enable-interrupt-parameters.md) | The GPIO_ENABLE_INTERRUPT_PARAMETERS structure specifies a general-purpose I/O (GPIO) pin and describes the interrupt attributes of this pin. |
| [GPIO_MASK_INTERRUPT_PARAMETERS structure](ns-gpioclx--gpio-mask-interrupt-parameters.md) | The GPIO_MASK_INTERRUPT_PARAMETERS structure describes a set of general-purpose I/O (GPIO) interrupt pins to mask. |
| [GPIO_QUERY_ACTIVE_INTERRUPTS_PARAMETERS structure](ns-gpioclx--gpio-query-active-interrupts-parameters.md) | The GPIO_QUERY_ACTIVE_INTERRUPTS_PARAMETERS structure describes a set of general-purpose I/O (GPIO) interrupt pins to query for their enabled and active states. |
| [GPIO_QUERY_ENABLED_INTERRUPTS_PARAMETERS structure](ns-gpioclx--gpio-query-enabled-interrupts-parameters.md) | The GPIO_QUERY_ENABLED_INTERRUPTS_PARAMETERS structure indicates which interrupt pins in a bank of general-purpose I/O (GPIO) pins are enabled. |
| [GPIO_READ_PINS_MASK_PARAMETERS structure](ns-gpioclx--gpio-read-pins-mask-parameters.md) | The GPIO_READ_PINS_MASK_PARAMETERS structure describes a read operation on a bank of general-purpose I/O (GPIO) pins. |
| [GPIO_READ_PINS_PARAMETERS structure](ns-gpioclx--gpio-read-pins-parameters.md) | The GPIO_READ_PINS_PARAMETERS structure describes a read operation on a group of general-purpose I/O (GPIO) pins. |
| [GPIO_RECONFIGURE_INTERRUPTS_PARAMETERS structure](ns-gpioclx--gpio-reconfigure-interrupts-parameters.md) | The GPIO_RECONFIGURE_INTERRUPTS_PARAMETERS structure describes the general-purpose I/O (GPIO) interrupt pin to reconfigure. |
| [GPIO_SAVE_RESTORE_BANK_HARDWARE_CONTEXT_PARAMETERS structure](ns-gpioclx--gpio-save-restore-bank-hardware-context-parameters.md) | The GPIO_SAVE_RESTORE_BANK_HARDWARE_CONTEXT_PARAMETERS structure describes a bank of general-purpose I/O (GPIO) pins whose hardware state is to be saved or restored. |
| [GPIO_WRITE_PINS_MASK_PARAMETERS structure](ns-gpioclx--gpio-write-pins-mask-parameters.md) | The GPIO_WRITE_PINS_MASK_PARAMETERS structure describes a write operation on a bank of general-purpose I/O (GPIO) pins. |
| [GPIO_WRITE_PINS_PARAMETERS structure](ns-gpioclx--gpio-write-pins-parameters.md) | The GPIO_WRITE_PINS_PARAMETERS structure describes a write operation on a group of general-purpose I/O (GPIO) pins. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE enumeration](ne-gpioclx--client-controller-query-set-request-type.md) | The CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE enumeration type indicates what type of attribute information the GPIO framework extension (GpioClx) is requesting from the GPIO controller driver. |
| [GPIO_CONNECT_IO_PINS_MODE enumeration](ne-gpioclx--gpio-connect-io-pins-mode.md) | The GPIO_CONNECT_IO_PINS_MODE enumeration indicates whether a set of general-purpose I/O (GPIO) pins is configured as inputs or outputs. |
