---
UID: NF.wdfcontrol.WdfControlFinishInitializing
title: WdfControlFinishInitializing function
author: windows-driver-content
description: The WdfControlFinishInitializing method informs the framework that a driver has finished initializing a specified control device object.
old-location: wdf\wdfcontrolfinishinitializing.htm
old-project: wdf
ms.assetid: 13375ae1-6908-44d8-b775-4375f4fdde4d
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfControlFinishInitializing
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfcontrol.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfControlFinishInitializing
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: CtlDeviceFinishInitDeviceAdd, CtlDeviceFinishInitDrEntry, DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfControlFinishInitializing function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfControlFinishInitializing</b> method informs the framework that a driver has finished initializing a specified control device object.



## -syntax

````
VOID WdfControlFinishInitializing(
  _In_ WDFDEVICE Device
);
````


## -parameters

### -param Device [in]

A handle to a control device object.


## -returns
None.

A system bug check occurs if the driver supplies an invalid object handle.


## -remarks
The system will not send I/O requests or Windows Management Instrumentation (WMI) requests to a control device object unless the driver has called <b>WdfControlFinishInitializing</b>.

For more information about control device objects and calling <b>WdfControlFinishInitializing</b>, see <a href="wdf.using_control_device_objects">Using Control Device Objects</a>.

For a code example that uses <b>WdfControlFinishInitializing</b>, see <a href="wdf.wdfcontroldeviceinitallocate">WdfControlDeviceInitAllocate</a>.


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
<dt>Wdfcontrol.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
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
<a href="devtest.kmdf_ctldevicefinishinitdeviceadd">CtlDeviceFinishInitDeviceAdd</a>, <a href="devtest.kmdf_ctldevicefinishinitdrentry">CtlDeviceFinishInitDrEntry</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>