---
UID : NF:wdfdevice.WdfDeviceGetDefaultQueue
title : WdfDeviceGetDefaultQueue function
author : windows-driver-content
description : The WdfDeviceGetDefaultQueue method returns a handle to a device's default I/O queue.
old-location : wdf\wdfdevicegetdefaultqueue.htm
old-project : wdf
ms.assetid : 914c4ef8-2210-468c-8720-11f8adf9dce7
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : DFDeviceObjectGeneralRef_17d2efb6-80ae-4045-baa4-68d610b9e0c3.xml, kmdf.wdfdevicegetdefaultqueue, PFN_WDFDEVICEGETDEFAULTQUEUE, wdf.wdfdevicegetdefaultqueue, WdfDeviceGetDefaultQueue method, wdfdevice/WdfDeviceGetDefaultQueue, WdfDeviceGetDefaultQueue
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdfdevice.h
req.include-header : Wdf.h
req.target-type : Universal
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 1.0
req.umdf-ver : 2.0
req.ddi-compliance : DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll : 
req.irql : "<= DISPATCH_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WDF_STATE_NOTIFICATION_TYPE
req.product : Windows 10 or later.
---


# WdfDeviceGetDefaultQueue function
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfDeviceGetDefaultQueue</b> method returns a handle to a device's default I/O queue.

## Syntax

````
WDFQUEUE WdfDeviceGetDefaultQueue(
  _In_ WDFDEVICE Device
);
````

## Parameters

`Device`

A handle to a framework device object.


## Return Value

If the operation succeeds, the method returns a handle to a framework queue object. If the driver did not create a default I/O queue for the device, the method returns <b>NULL</b>.

A bug check occurs if the driver supplies an invalid object handle.

## Remarks

For more information about default I/O queues, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/creating-i-o-queues">Creating I/O Queues</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfdevice.h (include Wdf.h) |
| **Library** | Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF) |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** | DriverCreate, KmdfIrql, KmdfIrql2 |