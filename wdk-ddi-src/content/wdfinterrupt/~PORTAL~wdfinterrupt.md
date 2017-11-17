# Declarations in the wdfinterrupt header
This header Wdfinterrupt contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [*PFN_WDFINTERRUPTQUEUEDPCFORISR callback function](nc-wdfinterrupt-pfn-wdfinterruptqueuedpcforisr.md) | TBD |
| [EVT_WDF_INTERRUPT_DPC callback](nc-wdfinterrupt-evt-wdf-interrupt-dpc.md) | A driver's EvtInterruptDpc event callback function processes interrupt information that the driver's EvtInterruptIsr callback function has stored. |
| [EVT_WDF_INTERRUPT_SYNCHRONIZE callback](nc-wdfinterrupt-evt-wdf-interrupt-synchronize.md) | A driver's EvtInterruptSynchronize event callback function performs operations that must be synchronized with an EvtInterruptIsr callback function. |
| [PFN_WDFINTERRUPTGETINFO callback function](nc-wdfinterrupt-pfn-wdfinterruptgetinfo.md) | TBD |
| [PFN_WDFINTERRUPTREPORTINACTIVE callback function](nc-wdfinterrupt-pfn-wdfinterruptreportinactive.md) | TBD |
| [PFN_WDFINTERRUPTRELEASELOCK callback function](nc-wdfinterrupt-pfn-wdfinterruptreleaselock.md) | TBD |
| [PFN_WDFINTERRUPTDISABLE callback function](nc-wdfinterrupt-pfn-wdfinterruptdisable.md) | TBD |
| [EVT_WDF_INTERRUPT_ISR callback](nc-wdfinterrupt-evt-wdf-interrupt-isr.md) | A driver's EvtInterruptIsr event callback function services a hardware interrupt. |
| [PFN_WDFINTERRUPTSYNCHRONIZE callback function](nc-wdfinterrupt-pfn-wdfinterruptsynchronize.md) | TBD |
| [EVT_WDF_INTERRUPT_ENABLE callback](nc-wdfinterrupt-evt-wdf-interrupt-enable.md) | A driver's EvtInterruptEnable event callback function enables a specified hardware interrupt. |
| [PFN_WDFINTERRUPTTRYTOACQUIRELOCK callback function](nc-wdfinterrupt-pfn-wdfinterrupttrytoacquirelock.md) | TBD |
| [*PFN_WDFINTERRUPTGETDEVICE callback function](nc-wdfinterrupt-pfn-wdfinterruptgetdevice.md) | TBD |
| [PFN_WDFINTERRUPTENABLE callback function](nc-wdfinterrupt-pfn-wdfinterruptenable.md) | TBD |
| [PFN_WDFINTERRUPTCREATE callback function](nc-wdfinterrupt-pfn-wdfinterruptcreate.md) | TBD |
| [EVT_WDF_INTERRUPT_WORKITEM callback](nc-wdfinterrupt-evt-wdf-interrupt-workitem.md) | A driver's EvtInterruptWorkItem event callback function processes interrupt information that the driver's EvtInterruptIsr callback function has stored. |
| [EVT_WDF_INTERRUPT_DISABLE callback](nc-wdfinterrupt-evt-wdf-interrupt-disable.md) | A driver's EvtInterruptDisable event callback function disables a specified hardware interrupt. |
| [PFN_WDFINTERRUPTSETEXTENDEDPOLICY callback function](nc-wdfinterrupt-pfn-wdfinterruptsetextendedpolicy.md) | TBD |
| [PFN_WDFINTERRUPTACQUIRELOCK callback function](nc-wdfinterrupt-pfn-wdfinterruptacquirelock.md) | TBD |
| [PFN_WDFINTERRUPTREPORTACTIVE callback function](nc-wdfinterrupt-pfn-wdfinterruptreportactive.md) | TBD |
| [PFN_WDFINTERRUPTSETPOLICY callback function](nc-wdfinterrupt-pfn-wdfinterruptsetpolicy.md) | TBD |
| [*PFN_WDFINTERRUPTWDMGETINTERRUPT callback function](nc-wdfinterrupt-pfn-wdfinterruptwdmgetinterrupt.md) | TBD |
| [*PFN_WDFINTERRUPTQUEUEWORKITEMFORISR callback function](nc-wdfinterrupt-pfn-wdfinterruptqueueworkitemforisr.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfInterruptSetExtendedPolicy function](nf-wdfinterrupt-wdfinterruptsetextendedpolicy.md) | The WdfInterruptSetExtendedPolicy method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt. |
| [WDF_INTERRUPT_CONFIG_INIT function](nf-wdfinterrupt-wdf-interrupt-config-init.md) | The WDF_INTERRUPT_CONFIG_INIT function initializes a WDF_INTERRUPT_CONFIG structure. |
| [WdfInterruptWdmGetInterrupt function](nf-wdfinterrupt-wdfinterruptwdmgetinterrupt.md) | The WdfInterruptWdmGetInterrupt method returns a pointer to the WDM interrupt object that is associated with a specified framework interrupt object. |
| [WdfInterruptReportActive function](nf-wdfinterrupt-wdfinterruptreportactive.md) | The WdfInterruptReportActive informs the system that the interrupt is active and the driver is ready to process interrupt requests on the associated lines. |
| [WdfInterruptQueueDpcForIsr function](nf-wdfinterrupt-wdfinterruptqueuedpcforisr.md) | The WdfInterruptQueueDpcForIsr method queues a framework interrupt object's EvtInterruptDpc callback function for execution. |
| [WdfInterruptTryToAcquireLock function](nf-wdfinterrupt-wdfinterrupttrytoacquirelock.md) | The WdfInterruptTryToAcquireLock method attempts to acquire an interrupt object's passive lock. |
| [WdfInterruptQueueWorkItemForIsr function](nf-wdfinterrupt-wdfinterruptqueueworkitemforisr.md) | The WdfInterruptQueueWorkItemForIsr method queues a framework interrupt object's EvtInterruptWorkItem callback function for execution. |
| [WdfInterruptDisable function](nf-wdfinterrupt-wdfinterruptdisable.md) | The WdfInterruptDisable method disables a specified device interrupt by calling the driver's EvtInterruptDisable callback function. |
| [WdfInterruptEnable function](nf-wdfinterrupt-wdfinterruptenable.md) | The WdfInterruptEnable method enables a specified device interrupt by calling the driver's EvtInterruptEnable callback function. |
| [WdfInterruptGetInfo function](nf-wdfinterrupt-wdfinterruptgetinfo.md) | The WdfInterruptGetInfo method retrieves information about a specified interrupt. |
| [WDF_INTERRUPT_EXTENDED_POLICY_INIT function](nf-wdfinterrupt-wdf-interrupt-extended-policy-init.md) | The WDF_INTERRUPT_EXTENDED_POLICY_INIT function initializes a WDF_INTERRUPT_EXTENDED_POLICY structure. |
| [WdfInterruptReportInactive function](nf-wdfinterrupt-wdfinterruptreportinactive.md) | The WdfInterruptReportInactive method informs the system that the interrupt is no longer active and the driver is not expecting interrupt requests on the associated lines. |
| [WdfInterruptCreate function](nf-wdfinterrupt-wdfinterruptcreate.md) | The WdfInterruptCreate method creates a framework interrupt object. |
| [WdfInterruptSynchronize function](nf-wdfinterrupt-wdfinterruptsynchronize.md) | The WdfInterruptSynchronize method executes a specified callback function at the device's DIRQL while holding an interrupt object's spin lock. |
| [WDF_INTERRUPT_INFO_INIT function](nf-wdfinterrupt-wdf-interrupt-info-init.md) | The WDF_INTERRUPT_INFO_INIT function initializes a WDF_INTERRUPT_INFO structure. |
| [WdfInterruptSetPolicy function](nf-wdfinterrupt-wdfinterruptsetpolicy.md) | The WdfInterruptSetPolicy method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt. |
| [WdfInterruptGetDevice function](nf-wdfinterrupt-wdfinterruptgetdevice.md) | The WdfInterruptGetDevice method returns a handle to the framework device object that is associated with a specified framework interrupt object. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_INTERRUPT_INFO structure](ns-wdfinterrupt--wdf-interrupt-info.md) | The WDF_INTERRUPT_INFO structure contains information about a device's interrupt resource. |
| [WDF_INTERRUPT_EXTENDED_POLICY structure](ns-wdfinterrupt--wdf-interrupt-extended-policy.md) | The WDF_INTERRUPT_EXTENDED_POLICY structure contains information about an interrupt's policy, priority, affinity, and group. |
| [WDF_INTERRUPT_CONFIG structure](ns-wdfinterrupt--wdf-interrupt-config.md) | The WDF_INTERRUPT_CONFIG structure contains configuration information for a device interrupt. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_INTERRUPT_PRIORITY enumeration](ne-wdfinterrupt--wdf-interrupt-priority.md) | The WDF_INTERRUPT_PRIORITY enumeration type identifies relative priorities for device interrupts. |
| [WDF_INTERRUPT_POLICY enumeration](ne-wdfinterrupt--wdf-interrupt-policy.md) | The WDF_INTERRUPT_POLICY enumeration type identifies the affinity policies that the PnP manager can use when it assigns a device's interrupts to the processors of a multiprocessor system. |
| [WDF_INTERRUPT_POLARITY enumeration](ne-wdfinterrupt--wdf-interrupt-polarity.md) | The WDF_INTERRUPT_POLARITY enumeration type is used to specify an interrupt signal's polarity. |

This header is used in these topics:

- [wdf](..content/_wdf)
