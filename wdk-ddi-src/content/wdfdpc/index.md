---
UID : NA:wdfdpc
ms.assetid : e2e9ce8e-b03b-3a8f-8754-1634cc244cf0
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# wdfdpc.h header



wdfdpc.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [WDF_DPC_CONFIG_INIT](nf-wdfdpc-wdf_dpc_config_init.md) | The WDF_DPC_CONFIG_INIT function initializes a driver's WDF_DPC_CONFIG structure. |
| [WdfDpcCancel](nf-wdfdpc-wdfdpccancel.md) | The WdfDpcCancel method attempts to cancel the execution of a DPC object's scheduled EvtDpcFunc callback function. |
| [WdfDpcCreate](nf-wdfdpc-wdfdpccreate.md) | The WdfDpcCreate method creates a framework DPC object and registers an EvtDpcFunc callback function. |
| [WdfDpcEnqueue](nf-wdfdpc-wdfdpcenqueue.md) | The WdfDpcEnqueue method schedules the execution of a DPC object's EvtDpcFunc callback function. |
| [WdfDpcGetParentObject](nf-wdfdpc-wdfdpcgetparentobject.md) | The WdfDpcGetParentObject method returns the parent object of a specified DPC object. |
| [WdfDpcWdmGetDpc](nf-wdfdpc-wdfdpcwdmgetdpc.md) | The WdfDpcWdmGetDpc method returns a pointer to the KDPC structure that is associated with a specified framework DPC object. |



## Structures
| Title | Description |
| ---- |:---- |
| [_WDF_DPC_CONFIG](ns-wdfdpc-_wdf_dpc_config.md) | The WDF_DPC_CONFIG structure contains configuration information for a DPC object. |