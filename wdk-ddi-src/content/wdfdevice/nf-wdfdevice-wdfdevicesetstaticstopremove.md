---
UID : NF:wdfdevice.WdfDeviceSetStaticStopRemove
title : WdfDeviceSetStaticStopRemove function
author : windows-driver-content
description : The WdfDeviceSetStaticStopRemove method informs the framework whether a device can be stopped and removed.
old-location : wdf\wdfdevicesetstaticstopremove.htm
old-project : wdf
ms.assetid : b2776618-2585-4a7a-9f8f-536f1d28745b
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : kmdf.wdfdevicesetstaticstopremove, DFDeviceObjectGeneralRef_9874b784-6344-4336-9753-0b172563f981.xml, WdfDeviceSetStaticStopRemove method, wdfdevice/WdfDeviceSetStaticStopRemove, PFN_WDFDEVICESETSTATICSTOPREMOVE, WdfDeviceSetStaticStopRemove, wdf.wdfdevicesetstaticstopremove
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
req.irql : "<=DISPATCH_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WDF_STATE_NOTIFICATION_TYPE
req.product : Windows 10 or later.
---


# WdfDeviceSetStaticStopRemove function
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfDeviceSetStaticStopRemove</b> method informs the framework whether a device can be stopped and removed.

## Syntax

````
VOID WdfDeviceSetStaticStopRemove(
  _In_ WDFDEVICE Device,
  _In_ BOOLEAN   Stoppable
);
````

## Parameters

`Device`

A handle to a framework device object.

`Stoppable`

A Boolean value that indicates whether the specified device can be stopped and removed. If <b>TRUE</b>, the device can be stopped and removed. If <b>FALSE</b>, the device cannot be stopped and removed.


## Return Value

None.

A bug check occurs if the driver supplies an invalid object handle.

## Remarks

By default, a device can be stopped and removed. Therefore, a driver typically calls <b>WdfDeviceSetStaticStopRemove</b> only if it must temporarily set the <i>Stoppable</i> parameter to <b>FALSE</b>. For example, a driver that controls a DVD writer might call <b>WdfDeviceSetStaticStopRemove</b> with <i>Stoppable</i> set to <b>FALSE</b> before it begins burning a DVD. After the driver has finished burning the DVD, it would call <b>WdfDeviceSetStaticStopRemove</b> again with <i>Stoppable</i> set to <b>TRUE</b>.  

If your driver's device is supporting a special file (see <a href="..\wdfdevice\nf-wdfdevice-wdfdevicesetspecialfilesupport.md">WdfDeviceSetSpecialFileSupport</a>), the framework will not allow the device to be stopped or removed. In this case, your driver does not have to call <b>WdfDeviceSetStaticStopRemove</b> .

The driver must match every call to <b>WdfDeviceSetStaticStopRemove</b> with <i>Stoppable</i> set to <b>FALSE</b> with a call to <b>WdfDeviceSetStaticStopRemove</b> with <i>Stoppable</i> set to <b>TRUE</b>.

Calling <b>WdfDeviceSetStaticStopRemove</b> with <i>Stoppable</i> set to <b>FALSE</b> does not prevent the framework from notifying the driver if the device is unexpectedly removed (surprise-removed).

For more information about how to prevent the operating system from stopping a device, see <a href="https://msdn.microsoft.com/4c8f37b3-7961-4c78-a88b-3eec58155e66">Handling Requests to Stop a Device</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfdevice.h (include Wdf.h) |
| **Library** | Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF) |
| **IRQL** | "<=DISPATCH_LEVEL" |
| **DDI compliance rules** | DriverCreate, KmdfIrql, KmdfIrql2 |