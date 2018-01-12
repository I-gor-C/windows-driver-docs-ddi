---
UID: NA:wdfinterrupt
---

# Wdfinterrupt.h header

## -description

This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdfinterrupt.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [PFN_WDFINTERRUPTDISABLE function](nc-wdfinterrupt-pfn_wdfinterruptdisable.md) | The WdfInterruptDisable method disables a specified device interrupt by calling the driver's EvtInterruptDisable callback function. |
| [PFN_WDFINTERRUPTENABLE function](nc-wdfinterrupt-pfn_wdfinterruptenable.md) | The WdfInterruptEnable method enables a specified device interrupt by calling the driver's EvtInterruptEnable callback function. |
| [PFN_WDFINTERRUPTGETINFO function](nc-wdfinterrupt-pfn_wdfinterruptgetinfo.md) | The WdfInterruptGetInfo method retrieves information about a specified interrupt. |
| [PFN_WDFINTERRUPTREPORTACTIVE function](nc-wdfinterrupt-pfn_wdfinterruptreportactive.md) | The WdfInterruptReportActive informs the system that the interrupt is active and the driver is ready to process interrupt requests on the associated lines. |
| [PFN_WDFINTERRUPTREPORTINACTIVE function](nc-wdfinterrupt-pfn_wdfinterruptreportinactive.md) | The WdfInterruptReportInactive method informs the system that the interrupt is no longer active and the driver is not expecting interrupt requests on the associated lines. |
| [PFN_WDFINTERRUPTSETEXTENDEDPOLICY function](nc-wdfinterrupt-pfn_wdfinterruptsetextendedpolicy.md) | The WdfInterruptSetExtendedPolicy method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt. |
| [PFN_WDFINTERRUPTSETPOLICY function](nc-wdfinterrupt-pfn_wdfinterruptsetpolicy.md) | The WdfInterruptSetPolicy method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt. |
| [PFN_WDFINTERRUPTSYNCHRONIZE function](nc-wdfinterrupt-pfn_wdfinterruptsynchronize.md) | The WdfInterruptSynchronize method executes a specified callback function at the device's DIRQL while holding an interrupt object's spin lock. |
| [PFN_WDFINTERRUPTTRYTOACQUIRELOCK function](nc-wdfinterrupt-pfn_wdfinterrupttrytoacquirelock.md) | The WdfInterruptTryToAcquireLock method attempts to acquire an interrupt object's passive lock. |
| [WDF_INTERRUPT_CONFIG_INIT function](nf-wdfinterrupt-wdf_interrupt_config_init.md) | The WDF_INTERRUPT_CONFIG_INIT function initializes a WDF_INTERRUPT_CONFIG structure. |
| [WDF_INTERRUPT_EXTENDED_POLICY_INIT function](nf-wdfinterrupt-wdf_interrupt_extended_policy_init.md) | The WDF_INTERRUPT_EXTENDED_POLICY_INIT function initializes a WDF_INTERRUPT_EXTENDED_POLICY structure. |
| [WDF_INTERRUPT_INFO_INIT function](nf-wdfinterrupt-wdf_interrupt_info_init.md) | The WDF_INTERRUPT_INFO_INIT function initializes a WDF_INTERRUPT_INFO structure. |
| [WdfInterruptCreate function](nf-wdfinterrupt-wdfinterruptcreate.md) | The WdfInterruptCreate method creates a framework interrupt object. |
| [WdfInterruptDisable function](nf-wdfinterrupt-wdfinterruptdisable.md) | The WdfInterruptDisable method disables a specified device interrupt by calling the driver's EvtInterruptDisable callback function. |
| [WdfInterruptEnable function](nf-wdfinterrupt-wdfinterruptenable.md) | The WdfInterruptEnable method enables a specified device interrupt by calling the driver's EvtInterruptEnable callback function. |
| [WdfInterruptGetDevice function](nf-wdfinterrupt-wdfinterruptgetdevice.md) | The WdfInterruptGetDevice method returns a handle to the framework device object that is associated with a specified framework interrupt object. |
| [WdfInterruptGetInfo function](nf-wdfinterrupt-wdfinterruptgetinfo.md) | The WdfInterruptGetInfo method retrieves information about a specified interrupt. |
| [WdfInterruptQueueDpcForIsr function](nf-wdfinterrupt-wdfinterruptqueuedpcforisr.md) | The WdfInterruptQueueDpcForIsr method queues a framework interrupt object's EvtInterruptDpc callback function for execution. |
| [WdfInterruptQueueWorkItemForIsr function](nf-wdfinterrupt-wdfinterruptqueueworkitemforisr.md) | The WdfInterruptQueueWorkItemForIsr method queues a framework interrupt object's EvtInterruptWorkItem callback function for execution. |
| [WdfInterruptReportActive function](nf-wdfinterrupt-wdfinterruptreportactive.md) | The WdfInterruptReportActive informs the system that the interrupt is active and the driver is ready to process interrupt requests on the associated lines. |
| [WdfInterruptReportInactive function](nf-wdfinterrupt-wdfinterruptreportinactive.md) | The WdfInterruptReportInactive method informs the system that the interrupt is no longer active and the driver is not expecting interrupt requests on the associated lines. |
| [WdfInterruptSetExtendedPolicy function](nf-wdfinterrupt-wdfinterruptsetextendedpolicy.md) | The WdfInterruptSetExtendedPolicy method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt. |
| [WdfInterruptSetPolicy function](nf-wdfinterrupt-wdfinterruptsetpolicy.md) | The WdfInterruptSetPolicy method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt. |
| [WdfInterruptSynchronize function](nf-wdfinterrupt-wdfinterruptsynchronize.md) | The WdfInterruptSynchronize method executes a specified callback function at the device's DIRQL while holding an interrupt object's spin lock. |
| [WdfInterruptTryToAcquireLock function](nf-wdfinterrupt-wdfinterrupttrytoacquirelock.md) | The WdfInterruptTryToAcquireLock method attempts to acquire an interrupt object's passive lock. |
| [WdfInterruptWdmGetInterrupt function](nf-wdfinterrupt-wdfinterruptwdmgetinterrupt.md) | The WdfInterruptWdmGetInterrupt method returns a pointer to the WDM interrupt object that is associated with a specified framework interrupt object. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_WDF_INTERRUPT_CONFIG structure](ns-wdfinterrupt-_wdf_interrupt_config.md) | The WDF_INTERRUPT_CONFIG structure contains configuration information for a device interrupt. |
| [_WDF_INTERRUPT_EXTENDED_POLICY structure](ns-wdfinterrupt-_wdf_interrupt_extended_policy.md) | The WDF_INTERRUPT_EXTENDED_POLICY structure contains information about an interrupt's policy, priority, affinity, and group. |
| [_WDF_INTERRUPT_INFO structure](ns-wdfinterrupt-_wdf_interrupt_info.md) | The WDF_INTERRUPT_INFO structure contains information about a device's interrupt resource. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_WDF_INTERRUPT_POLARITY enumeration](ne-wdfinterrupt-_wdf_interrupt_polarity.md) | The WDF_INTERRUPT_POLARITY enumeration type is used to specify an interrupt signal's polarity. |
| [_WDF_INTERRUPT_POLICY enumeration](ne-wdfinterrupt-_wdf_interrupt_policy.md) | The WDF_INTERRUPT_POLICY enumeration type identifies the affinity policies that the PnP manager can use when it assigns a device's interrupts to the processors of a multiprocessor system. |
| [_WDF_INTERRUPT_PRIORITY enumeration](ne-wdfinterrupt-_wdf_interrupt_priority.md) | The WDF_INTERRUPT_PRIORITY enumeration type identifies relative priorities for device interrupts. |
