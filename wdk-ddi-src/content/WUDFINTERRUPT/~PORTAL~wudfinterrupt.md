# Declarations in the wudfinterrupt header
This header Wudfinterrupt contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [WUDF_INTERRUPT_ENABLE callback](nc-wudfinterrupt-wudf-interrupt-enable.md) | A driver's OnInterruptEnable event callback function enables a specified hardware interrupt. |
| [WUDF_INTERRUPT_DISABLE callback](nc-wudfinterrupt-wudf-interrupt-disable.md) | A driver's OnInterruptDisable event callback function disables a specified hardware interrupt. |
| [WUDF_INTERRUPT_WORKITEM callback](nc-wudfinterrupt-wudf-interrupt-workitem.md) | A driver's OnInterruptWorkItem event callback function processes interrupt information that the driver's OnInterruptIsr callback function has stored. |
| [WUDF_INTERRUPT_ISR callback](nc-wudfinterrupt-wudf-interrupt-isr.md) | A driver's OnInterruptIsr event callback function services a hardware interrupt. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_INTERRUPT_POLICY enumeration](ne-wudfinterrupt--wdf-interrupt-policy.md) | The WDF_INTERRUPT_POLICY enumeration type identifies the affinity policies that the Plug and Play (PnP) manager can use when it assigns a device's interrupts to the processors of a multiprocessor system. |
| [WDF_INTERRUPT_PRIORITY enumeration](ne-wudfinterrupt--wdf-interrupt-priority.md) | The WDF_INTERRUPT_PRIORITY enumeration type identifies relative priorities for device interrupts. |
| [WDF_INTERRUPT_POLARITY enumeration](ne-wudfinterrupt--wdf-interrupt-polarity.md) | The WDF_INTERRUPT_POLARITY enumeration type is used to specify an interrupt signal's polarity. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WUDF_INTERRUPT_CONFIG structure](ns-wudfinterrupt--wudf-interrupt-config.md) | The WUDF_INTERRUPT_CONFIG structure contains configuration information for a device interrupt. |
| [WDF_INTERRUPT_EXTENDED_POLICY structure](ns-wudfinterrupt--wdf-interrupt-extended-policy.md) | The WDF_INTERRUPT_EXTENDED_POLICY structure contains information about an interrupt's policy, priority, affinity, and group. |
| [WDF_INTERRUPT_INFO structure](ns-wudfinterrupt--wdf-interrupt-info.md) | The WDF_INTERRUPT_INFO structure contains information about a device's interrupt resource. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_INTERRUPT_EXTENDED_POLICY_INIT function](nf-wudfinterrupt-wdf-interrupt-extended-policy-init.md) | The WDF_INTERRUPT_EXTENDED_POLICY_INIT function initializes a WDF_INTERRUPT_EXTENDED_POLICY structure. |
| [WDF_INTERRUPT_INFO_INIT function](nf-wudfinterrupt-wdf-interrupt-info-init.md) | The WDF_INTERRUPT_INFO_INIT function initializes a WDF_INTERRUPT_INFO structure. |
| [WUDF_INTERRUPT_CONFIG_INIT function](nf-wudfinterrupt-wudf-interrupt-config-init.md) | The WUDF_INTERRUPT_CONFIG_INIT function initializes a WUDF_INTERRUPT_CONFIG structure. |

This header is used in these topics:

- [wdf](..content/_wdf)
