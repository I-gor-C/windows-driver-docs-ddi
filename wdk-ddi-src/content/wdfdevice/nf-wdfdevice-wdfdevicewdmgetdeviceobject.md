---
UID : NF:wdfdevice.WdfDeviceWdmGetDeviceObject
title : WdfDeviceWdmGetDeviceObject function
author : windows-driver-content
description : The WdfDeviceWdmGetDeviceObject method returns the Windows Driver Model (WDM) device object that is associated with a specified framework device object.
old-location : wdf\wdfdevicewdmgetdeviceobject.htm
old-project : wdf
ms.assetid : 87a427ae-5c1e-4975-a48f-80c3549a3564
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.wdfdevicewdmgetdeviceobject, WdfDeviceWdmGetDeviceObject, WdfDeviceWdmGetDeviceObject method, wdfdevice/WdfDeviceWdmGetDeviceObject, kmdf.wdfdevicewdmgetdeviceobject, PFN_WDFDEVICEWDMGETDEVICEOBJECT, DFDeviceObjectGeneralRef_b145d3cd-578a-4be9-80d1-b260f5693b3d.xml
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


# WdfDeviceWdmGetDeviceObject function
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceWdmGetDeviceObject</b> method returns the Windows Driver Model (WDM) device object that is associated with a specified framework device object.

## Syntax

````
PDEVICE_OBJECT WdfDeviceWdmGetDeviceObject(
  _In_ WDFDEVICE hDevice
);
````

## Parameters

`Device`

TBD


## Return Value

<b>WdfDeviceWdmGetDeviceObject</b> returns a pointer to a <a href="..\wdm\ns-wdm-_device_object.md">DEVICE_OBJECT</a> structure.

A bug check occurs if the driver supplies an invalid object handle.

## Remarks

The pointer that the <b>WdfDeviceWdmGetDeviceObject</b> method returns is valid until the framework device object is deleted. If the driver provides an <a href="..\wdfobject\nc-wdfobject-evt_wdf_object_context_cleanup.md">EvtCleanupCallback</a> function for the framework device object, the pointer is valid until the callback function returns.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** |  |
| **Header** | wdfdevice.h (include Wdf.h) |
| **Library** |  |
| **IRQL** | <=DISPATCH_LEVEL |
| **DDI compliance rules** | DriverCreate, KmdfIrql, KmdfIrql2 |

## See Also

<a href="..\wdfdevice\nf-wdfdevice-wdfdevicewdmgetphysicaldevice.md">WdfDeviceWdmGetPhysicalDevice</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceWdmGetDeviceObject method%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>