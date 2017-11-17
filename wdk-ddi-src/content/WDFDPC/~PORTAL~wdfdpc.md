# Declarations in the wdfdpc header
This header Wdfdpc contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [*PFN_WDFDPCCANCEL callback function](nc-wdfdpc-pfn-wdfdpccancel.md) | TBD |
| [PFN_WDFDPCENQUEUE callback function](nc-wdfdpc-pfn-wdfdpcenqueue.md) | TBD |
| [PFN_WDFDPCGETPARENTOBJECT callback function](nc-wdfdpc-pfn-wdfdpcgetparentobject.md) | TBD |
| [PFN_WDFDPCWDMGETDPC callback function](nc-wdfdpc-pfn-wdfdpcwdmgetdpc.md) | TBD |
| [PFN_WDFDPCCREATE callback function](nc-wdfdpc-pfn-wdfdpccreate.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DPC_CONFIG_INIT function](nf-wdfdpc-wdf-dpc-config-init.md) | The WDF_DPC_CONFIG_INIT function initializes a driver's WDF_DPC_CONFIG structure. |
| [WdfDpcEnqueue function](nf-wdfdpc-wdfdpcenqueue.md) | The WdfDpcEnqueue method schedules the execution of a DPC object's EvtDpcFunc callback function. |
| [WdfDpcGetParentObject function](nf-wdfdpc-wdfdpcgetparentobject.md) | The WdfDpcGetParentObject method returns the parent object of a specified DPC object. |
| [WdfDpcCancel function](nf-wdfdpc-wdfdpccancel.md) | The WdfDpcCancel method attempts to cancel the execution of a DPC object's scheduled EvtDpcFunc callback function. |
| [WdfDpcWdmGetDpc function](nf-wdfdpc-wdfdpcwdmgetdpc.md) | The WdfDpcWdmGetDpc method returns a pointer to the KDPC structure that is associated with a specified framework DPC object. |
| [WdfDpcCreate function](nf-wdfdpc-wdfdpccreate.md) | The WdfDpcCreate method creates a framework DPC object and registers an EvtDpcFunc callback function. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DPC_CONFIG structure](ns-wdfdpc--wdf-dpc-config.md) | The WDF_DPC_CONFIG structure contains configuration information for a DPC object. |

This header is used in these topics:

- [wdf](..content/_wdf)
