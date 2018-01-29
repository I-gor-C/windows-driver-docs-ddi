---
UID : NF:wdfdevice.WdfDeviceClearRemovalRelationsDevices
title : WdfDeviceClearRemovalRelationsDevices function
author : windows-driver-content
description : The WdfDeviceClearRemovalRelationsDevices method removes all devices from the list of devices that must be removed when a specified device is removed.
old-location : wdf\wdfdeviceclearremovalrelationsdevices.htm
old-project : wdf
ms.assetid : c3ff7c9d-380e-4d66-88a4-aef7abe20c9d
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.wdfdeviceclearremovalrelationsdevices, WdfDeviceClearRemovalRelationsDevices method, wdfdevice/WdfDeviceClearRemovalRelationsDevices, WdfDeviceClearRemovalRelationsDevices, DFDeviceObjectGeneralRef_e2dc5cb6-4f45-441c-b242-5b67ea8fa381.xml, kmdf.wdfdeviceclearremovalrelationsdevices, PFN_WDFDEVICECLEARREMOVALRELATIONSDEVICES
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdfdevice.h
req.include-header : Wdf.h
req.target-type : Universal
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 1.0
req.umdf-ver : 
req.ddi-compliance : DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Wdf01000.sys (see Framework Library Versioning.)
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


# WdfDeviceClearRemovalRelationsDevices function
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceClearRemovalRelationsDevices</b> method removes all devices from the list of devices that must be removed when a specified device is removed.

## Syntax

````
VOID WdfDeviceClearRemovalRelationsDevices(
  _In_ WDFDEVICE Device
);
````

## Parameters

`Device`

A handle to a framework device object.


## Return Value

None.

A bug check occurs if the driver supplies an invalid object handle.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** |  |
| **Header** | wdfdevice.h (include Wdf.h) |
| **Library** |  |
| **IRQL** | <= DISPATCH_LEVEL |
| **DDI compliance rules** | DriverCreate, KmdfIrql, KmdfIrql2 |

## See Also

<a href="..\wdfdevice\nf-wdfdevice-wdfdeviceaddremovalrelationsphysicaldevice.md">WdfDeviceAddRemovalRelationsPhysicalDevice</a>

<a href="..\wdfdevice\nf-wdfdevice-wdfdeviceremoveremovalrelationsphysicaldevice.md">WdfDeviceRemoveRemovalRelationsPhysicalDevice</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceClearRemovalRelationsDevices method%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>