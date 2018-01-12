---
UID: NC:wdfdevice.PFN_WDFDEVICEINITSETDEVICETYPE
title: PFN_WDFDEVICEINITSETDEVICETYPE function
author: windows-driver-content
description: The WdfDeviceInitSetDeviceType method sets the device type for a specified device.
old-location: wdf\wdfdeviceinitsetdevicetype.htm
old-project: wdf
ms.assetid: 26c5c998-fb10-45c3-b28c-91a759fa941e
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: PFN_WDFDEVICEINITSETDEVICETYPE
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
req.alt-api: WdfDeviceInitSetDeviceType
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: ChildDeviceInitAPI, DeviceInitAPI, DriverCreate, KmdfIrql, KmdfIrql2, PdoDeviceInitAPI
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.typenames: WDF_DEVICE_SHUTDOWN_FLAGS
req.product: Windows 10 or later.
---

# PFN_WDFDEVICEINITSETDEVICETYPE function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceInitSetDeviceType</b> method sets the device type for a specified device.



## -syntax

````
VOID WdfDeviceInitSetDeviceType(
  _In_ PWDFDEVICE_INIT DeviceInit,
  _In_ DEVICE_TYPE     DeviceType
);
````


## -parameters

### -param DeviceInit [in]

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a> structure.


### -param DeviceType [in]

A FILE_DEVICE_XXXX value that identifies the device type. For more information about FILE_DEVICE_XXXX values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563821">Specifying Device Types</a>.


## -returns
None


## -remarks
If a driver calls <b>WdfDeviceInitSetDeviceType</b>, it must do so before it calls <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>.

For more information about calling <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>, see <a href="https://msdn.microsoft.com/25023c19-a153-4bd4-9fb6-3a1bf85860aa">Creating a Framework Device Object</a>.

The device type that a driver specifies determines the default priority boost value that the framework uses when the driver completes an I/O request. For more information about priority boost values, see <a href="https://msdn.microsoft.com/9a501ca1-58c9-4458-b202-9581f8ce5e5f">Specifying Priority Boosts When Completing I/O Requests</a>.


      If you are writing a UMDF driver, you  must modify your driver's INF file or make registry changes to specify a device type. For more information about using the registry, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563759">Setting Device Object Registry Properties During Installation</a>.

The following code example indicates that a device is a serial device.


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
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975068">ChildDeviceInitAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544843">DeviceInitAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550354">PdoDeviceInitAPI</a>
</td>
</tr>
</table>