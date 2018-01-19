---
UID : NF:wdfdevice.WdfDeviceWdmGetPhysicalDevice
title : WdfDeviceWdmGetPhysicalDevice function
author : windows-driver-content
description : The WdfDeviceWdmGetPhysicalDevice method retrieves the physical device's WDM PDO from the device stack.
old-location : wdf\wdfdevicewdmgetphysicaldevice.htm
old-project : wdf
ms.assetid : 88bd9cc7-6769-4fdf-b149-2193d765fc6c
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : WdfDeviceWdmGetPhysicalDevice
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
req.alt-api : WdfDeviceWdmGetPhysicalDevice
req.alt-loc : Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance : DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Wdf01000.sys (see Framework Library Versioning.)
req.dll : 
req.irql : <=DISPATCH_LEVEL
req.typenames : WDF_STATE_NOTIFICATION_TYPE
req.product : Windows 10 or later.
---


# WdfDeviceWdmGetPhysicalDevice function
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceWdmGetPhysicalDevice</b> method retrieves the physical device's WDM PDO from the device stack.

## Syntax

````
PDEVICE_OBJECT WdfDeviceWdmGetPhysicalDevice(
  _In_ WDFDEVICE Device
);
````

## Parameters

`Device`

A handle to a framework device object.


## Return Value

<b>WdfDeviceWdmGetPhysicalDevice</b> returns a pointer to a <a href="..\wdm\ns-wdm-_device_object.md">DEVICE_OBJECT</a> structure.

A bug check occurs if the driver supplies an invalid object handle.

## Remarks

The pointer that the <b>WdfDeviceWdmGetPhysicalDevice</b> method returns is valid until the framework device object is deleted. If the driver provides an <a href="..\wdfobject\nc-wdfobject-evt_wdf_object_context_cleanup.md">EvtCleanupCallback</a> function for the framework device object, the pointer is valid until the callback function returns.

For a code example that uses <b>WdfDeviceWdmGetPhysicalDevice</b>, see <a href="..\wdfdevice\nf-wdfdevice-wdfdevicewdmgetattacheddevice.md">WdfDeviceWdmGetAttachedDevice</a>.</p>

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