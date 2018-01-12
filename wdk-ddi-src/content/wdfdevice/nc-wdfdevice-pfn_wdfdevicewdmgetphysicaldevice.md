---
UID: NC:wdfdevice.PFN_WDFDEVICEWDMGETPHYSICALDEVICE
title: PFN_WDFDEVICEWDMGETPHYSICALDEVICE function
author: windows-driver-content
description: The WdfDeviceWdmGetPhysicalDevice method retrieves the physical device's WDM PDO from the device stack.
old-location: wdf\wdfdevicewdmgetphysicaldevice.htm
old-project: wdf
ms.assetid: 88bd9cc7-6769-4fdf-b149-2193d765fc6c
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: PFN_WDFDEVICEWDMGETPHYSICALDEVICE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDeviceWdmGetPhysicalDevice
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.typenames: WDF_DEVICE_SHUTDOWN_FLAGS
req.product: Windows 10 or later.
---

# PFN_WDFDEVICEWDMGETPHYSICALDEVICE function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceWdmGetPhysicalDevice</b> method retrieves the physical device's WDM PDO from the device stack.



## -syntax

````
PDEVICE_OBJECT WdfDeviceWdmGetPhysicalDevice(
  _In_ WDFDEVICE Device
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.


## -returns
<b>WdfDeviceWdmGetPhysicalDevice</b> returns a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure.

A bug check occurs if the driver supplies an invalid object handle.


## -remarks
The pointer that the <b>WdfDeviceWdmGetPhysicalDevice</b> method returns is valid until the framework device object is deleted. If the driver provides an <a href="..\wdfobject\nc-wdfobject-evt_wdf_object_context_cleanup.md">EvtCleanupCallback</a> function for the framework device object, the pointer is valid until the callback function returns.

For a code example that uses <b>WdfDeviceWdmGetPhysicalDevice</b>, see <a href="..\wdfdevice\nf-wdfdevice-wdfdevicewdmgetattacheddevice.md">WdfDeviceWdmGetAttachedDevice</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="https://msdn.microsoft.com/51db6f3c-45cb-46a7-9dd4-2bab67893fea">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;=DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>