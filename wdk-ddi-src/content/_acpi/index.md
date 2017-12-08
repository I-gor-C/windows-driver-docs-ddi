# ACPI

Overview of the ACPI technology.

To develop ACPI, you need these headers:

 * [acpiioct.h](..\acpiioct\index.md)
 * [acpitabl.h](..\acpitabl\index.md)
 * [oprghdlr.h](..\oprghdlr\index.md)

For the programming guide, see [ACPI](https://docs.microsoft.com/en-us/windows-hardware/drivers/acpi).

## Functions

| Title   | Description   |
| ---- |:---- |
| [DeRegisterOpRegionHandler function](..\oprghdlr\nf-oprghdlr-deregisteropregionhandler.md) | The DeRegisterOpRegionHandler routine deregisters an operation region handler with the ACPI driver. |
| [RegisterOpRegionHandler function](..\oprghdlr\nf-oprghdlr-registeropregionhandler.md) | The RegisterOpRegionHandler routine registers an operation region handler with the ACPI driver. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [ACPI_OP_REGION_HANDLER callback](..\oprghdlr\nc-oprghdlr-acpi-op-region-handler.md) | An ACPI_OP_REGION_HANDLER-typed routine is supplied by an ACPI device function driver to provide access by the ACPI driver to the device's operation region. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER structure](..\acpiioct\ns-acpiioct--acpi-device-information-output-buffer.md) | The ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER structure contains output arguments from the IOCTL_ACPI_GET_DEVICE_INFORMATION control method. |
| [ACPI_ENUM_CHILD structure](..\acpiioct\ns-acpiioct--acpi-enum-child.md) | The ACPI_ENUM_CHILD structure is a member of the ACPI_ENUM_CHILDREN_OUTPUT_BUFFER structure and contains the full path and name of an object in an ACPI namespace. |
| [ACPI_ENUM_CHILDREN_INPUT_BUFFER structure](..\acpiioct\ns-acpiioct--acpi-enum-children-input-buffer.md) | The ACPI_ENUM_CHILDREN_INPUT_BUFFER structure is used as input to an IOCTL_ACPI_ENUM_CHILDREN request. The structure specifies which child objects to enumerate in the namespace of the device to which the request is sent. |
| [ACPI_ENUM_CHILDREN_OUTPUT_BUFFER structure](..\acpiioct\ns-acpiioct--acpi-enum-children-output-buffer.md) | The ACPI_ENUM_CHILDREN_OUTPUT_BUFFER structure contains an array of object names in an ACPI namespace. |
| [ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1 structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-complex-v1.md) | The ACPI_EVAL_INPUT_BUFFER_COMPLEX structure is used as input to an IOCTL_ACPI_EVAL_METHOD request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD request. The structure supplies the name of a control method and an input array of ACPI_METHOD_ARGUMENT structures. |
| [ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1 structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-complex-v1~r1.md) | The ACPI_EVAL_INPUT_BUFFER_COMPLEX structure is used as input to an IOCTL_ACPI_EVAL_METHOD request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD request. The structure supplies the name of a control method and an input array of ACPI_METHOD_ARGUMENT structures. |
| [ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-complex-v1-ex.md) | The ACPI_EVAL_INPUT_BUFFER_COMPLEX_EX structure is used as input to an IOCTL_ACPI_EVAL_METHOD_EX request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD_EX request. |
| [ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-complex-v1-ex~r1.md) | The ACPI_EVAL_INPUT_BUFFER_COMPLEX_EX structure is used as input to an IOCTL_ACPI_EVAL_METHOD_EX request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD_EX request. |
| [ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2 structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-complex-v2.md) | This topic describes the ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2 structure. |
| [ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-complex-v2-ex.md) | This topic describes the ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX structure. |
| [ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1 structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-simple-integer-v1.md) | The ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER structure is used as input to an IOCTL_ACPI_EVAL_METHOD request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD request. The structure supplies the name of a control method and an input argument of type ULONG. |
| [ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1 structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-simple-integer-v1~r1.md) | The ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER structure is used as input to an IOCTL_ACPI_EVAL_METHOD request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD request. The structure supplies the name of a control method and an input argument of type ULONG. |
| [ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-simple-integer-v1-ex.md) | The ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_EX structure is used as input to an IOCTL_ACPI_EVAL_METHOD_EX request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD_EX request. |
| [ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-simple-integer-v1-ex~r1.md) | The ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_EX structure is used as input to an IOCTL_ACPI_EVAL_METHOD_EX request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD_EX request. |
| [ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2 structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-simple-integer-v2.md) | This topic describes the ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2 structure. |
| [ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2_EX structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-simple-integer-v2-ex.md) | This topic describes the ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V2_EX structure. |
| [ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1 structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-simple-string-v1.md) | The ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING structure is used as input to an IOCTL_ACPI_EVAL_METHOD request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD request. The structure supplies the name of a control method and an input argument that is an ASCII string. |
| [ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1 structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-simple-string-v1~r1.md) | The ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING structure is used as input to an IOCTL_ACPI_EVAL_METHOD request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD request. The structure supplies the name of a control method and an input argument that is an ASCII string. |
| [ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1_EX structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-simple-string-v1-ex.md) | The ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_EX structure is used as input to an IOCTL_ACPI_EVAL_METHOD_EX request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD_EX request. |
| [ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1_EX structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-simple-string-v1-ex~r1.md) | The ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_EX structure is used as input to an IOCTL_ACPI_EVAL_METHOD_EX request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD_EX request. |
| [ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2 structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-simple-string-v2.md) | This topic describes the ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2 structure. |
| [ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2_EX structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-simple-string-v2-ex.md) | This topic describes the ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V2_EX structure. |
| [ACPI_EVAL_INPUT_BUFFER_V1 structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-v1.md) | The ACPI_EVAL_INPUT_BUFFER structure is used as input to an IOCTL_ACPI_EVAL_METHOD request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD request. The structure supplies the name of a control method that does not take an input argument. |
| [ACPI_EVAL_INPUT_BUFFER_V1 structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-v1~r1.md) | The ACPI_EVAL_INPUT_BUFFER structure is used as input to an IOCTL_ACPI_EVAL_METHOD request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD request. The structure supplies the name of a control method that does not take an input argument. |
| [ACPI_EVAL_INPUT_BUFFER_V1_EX structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-v1-ex.md) | The ACPI_EVAL_INPUT_BUFFER_EX structure is used as input to an IOCTL_ACPI_EVAL_METHOD_EX request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD_EX request. |
| [ACPI_EVAL_INPUT_BUFFER_V1_EX structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-v1-ex~r1.md) | The ACPI_EVAL_INPUT_BUFFER_EX structure is used as input to an IOCTL_ACPI_EVAL_METHOD_EX request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD_EX request. |
| [ACPI_EVAL_INPUT_BUFFER_V2 structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-v2.md) | This topic describes the ACPI_EVAL_INPUT_BUFFER_V2 structure. |
| [ACPI_EVAL_INPUT_BUFFER_V2_EX structure](..\acpiioct\ns-acpiioct--acpi-eval-input-buffer-v2-ex.md) | This topic describes the ACPI_EVAL_INPUT_BUFFER_V2_EX structure. |
| [ACPI_EVAL_OUTPUT_BUFFER_V1 structure](..\acpiioct\ns-acpiioct--acpi-eval-output-buffer-v1.md) | The ACPI_EVAL_OUTPUT_BUFFER structure contains output arguments from an ACPI control method. |
| [ACPI_EVAL_OUTPUT_BUFFER_V1 structure](..\acpiioct\ns-acpiioct--acpi-eval-output-buffer-v1~r1.md) | The ACPI_EVAL_OUTPUT_BUFFER structure contains output arguments from an ACPI control method. |
| [ACPI_EVAL_OUTPUT_BUFFER_V1 structure](..\acpiioct\ns-acpiioct--acpi-eval-output-buffer-v1~r2.md) | The ACPI_EVAL_OUTPUT_BUFFER structure contains output arguments from an ACPI control method. |
| [ACPI_EVAL_OUTPUT_BUFFER_V2 structure](..\acpiioct\ns-acpiioct--acpi-eval-output-buffer-v2.md) | This topic describes the ACPI_EVAL_OUTPUT_BUFFER_V2 structure. |
| [ACPI_GET_DEVICE_SPECIFIC_DATA structure](..\acpiioct\ns-acpiioct--acpi-get-device-specific-data.md) | The ACPI_GET_DEVICE_SPECIFIC_DATA structure contains input arguments for the IOCTL_ACPI_GET_DEVICE_SPECIFIC_DATA control method. |
| [ACPI_MANIPULATE_GLOBAL_LOCK_BUFFER structure](..\acpiioct\ns-acpiioct--acpi-manipulate-global-lock-buffer.md) | This topic describes the ACPI_MANIPULATE_GLOBAL_LOCK_BUFFER structure. |
| [ACPI_METHOD_ARGUMENT_V1 structure](..\acpiioct\ns-acpiioct--acpi-method-argument-v1.md) | The ACPI_METHOD_ARGUMENT structure contains the value of an input or output argument of an ACPI control method. |
| [ACPI_METHOD_ARGUMENT_V1 structure](..\acpiioct\ns-acpiioct--acpi-method-argument-v1~r1.md) | The ACPI_METHOD_ARGUMENT structure contains the value of an input or output argument of an ACPI control method. |
| [ACPI_METHOD_ARGUMENT_V2 structure](..\acpiioct\ns-acpiioct--acpi-method-argument-v2.md) | This topic describes the ACPI_METHOD_ARGUMENT_V2 structure. |
| [BBRT_TABLE structure](..\acpitabl\ns-acpitabl--bbrt-table.md) | Defines a Boot Background Resource Table. |
| [GIC_ITS structure](..\acpitabl\ns-acpitabl--gic-its.md) | This topic describes the GIC_ITS structure. |
| [LPIT structure](..\acpitabl\ns-acpitabl--lpit.md) | Defines an LPI ACPI table. |
| [LPI_STATE_DESCRIPTOR structure](..\acpitabl\ns-acpitabl--lpi-state-descriptor.md) | Defines an LPI state descriptor. |
| [LPI_STATE_FLAGS structure](..\acpitabl\ns-acpitabl--lpi-state-flags.md) | Defines LPI state flags, either as a structure or as an integer. |
| [SDEV_SECURE_ACPI_INFO_ENTRY structure](..\acpitabl\ns-acpitabl--sdev-secure-acpi-info-entry.md) | Defines an information entry for a secure ACPI device for use in a secure device table. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_ACPI_ACQUIRE_GLOBAL_LOCK IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-acquire-global-lock.md) | The IOCTL_ACPI_ACQUIRE_GLOBAL_LOCK device control request is reserved for internal use only. |
| [IOCTL_ACPI_ASYNC_EVAL_METHOD IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-async-eval-method.md) | A driver for a device can use the IOCTL_ACPI_ASYNC_EVAL_METHOD device control request to asynchronously evaluate an ACPI control method that is supported by the device. |
| [IOCTL_ACPI_ASYNC_EVAL_METHOD_EX IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-async-eval-method-ex.md) | A driver for a device can use the IOCTL_ACPI_ASYNC_EVAL_METHOD_EX device control request to asynchronously evaluate an ACPI control method that is supported by a child device of the device. |
| [IOCTL_ACPI_ASYNC_EVAL_METHOD_V1 IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-async-eval-method-v1.md) | The IOCTL_ACPI_ASYNC_EVAL_METHOD_V1 control code asynchronously evaluates an ACPI control method that is supported by the device. |
| [IOCTL_ACPI_ASYNC_EVAL_METHOD_V1_EX IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-async-eval-method-v1-ex.md) | The IOCTL_ACPI_ASYNC_EVAL_METHOD_V1_EX control code asynchronously evaluates an ACPI control method that is supported by the device. |
| [IOCTL_ACPI_ASYNC_EVAL_METHOD_V2 IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-async-eval-method-v2.md) | The IOCTL_ACPI_ASYNC_EVAL_METHOD_V2 control code asynchronously evaluates an ACPI control method that is supported by the device. |
| [IOCTL_ACPI_ASYNC_EVAL_METHOD_V2_EX IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-async-eval-method-v2-ex.md) | The IOCTL_ACPI_ASYNC_EVAL_METHOD_V2_EX control code asynchronously evaluates an ACPI control method that is supported by the device. |
| [IOCTL_ACPI_ENUM_CHILDREN IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-enum-children.md) | The IOCTL_ACPI_ENUM_CHILDREN device control request can be used to enumerate the path and name of devices or named child objects in the ACPI namespace of the device to which this request is sent. |
| [IOCTL_ACPI_EVAL_METHOD IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-eval-method.md) | A driver for a device can use the IOCTL_ACPI_EVAL_METHOD device control request to synchronously evaluate an ACPI control method that is supported by the device. |
| [IOCTL_ACPI_EVAL_METHOD_EX IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-eval-method-ex.md) | A driver for a device can use the IOCTL_ACPI_EVAL_METHOD_EX device control request to synchronously evaluate an ACPI control method that is supported by a child device in the namespace of the device. |
| [IOCTL_ACPI_EVAL_METHOD_V1 IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-eval-method-v1.md) | The IOCTL_ACPI_EVAL_METHOD_V1 control code synchronously evaluates an ACPI control method that is supported by the device. |
| [IOCTL_ACPI_EVAL_METHOD_V1_EX IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-eval-method-v1-ex.md) | The IOCTL_ACPI_EVAL_METHOD_V1_EX control code synchronously evaluates an ACPI control method that is supported by the device. |
| [IOCTL_ACPI_EVAL_METHOD_V2 IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-eval-method-v2.md) | The IOCTL_ACPI_EVAL_METHOD_V2 control code synchronously evaluates an ACPI control method that is supported by the device. |
| [IOCTL_ACPI_EVAL_METHOD_V2_EX IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-eval-method-v2-ex.md) | The IOCTL_ACPI_EVAL_METHOD_V2_EX control code synchronously evaluates an ACPI control method that is supported by the device. |
| [IOCTL_ACPI_GET_DEVICE_INFORMATION IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-get-device-information.md) | A driver for a device can use the IOCTL_ACPI_GET_DEVICE_INFORMATION device control request to obtain fine-grained identification information about its device. |
| [IOCTL_ACPI_GET_DEVICE_SPECIFIC_DATA IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-get-device-specific-data.md) | The IOCTL_ACPI_GET_DEVICE_SPECIFIC_DATA control code is used to get device specific data. |
| [IOCTL_ACPI_RELEASE_GLOBAL_LOCK IOCTL](..\acpiioct\ni-acpiioct-ioctl-acpi-release-global-lock.md) | The IOCTL_ACPI_RELEASE_GLOBAL_LOCK device control request is reserved for internal use only. |
