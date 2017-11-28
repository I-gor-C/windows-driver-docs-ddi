---
UID: NF.wdfcontrol.WdfControlFinishInitializing
title: WdfControlFinishInitializing
author: windows-driver-content
description: The WdfControlFinishInitializing method informs the framework that a driver has finished initializing a specified control device object.
old-location: wdf\wdfcontrolfinishinitializing.htm
old-project: wdf
ms.assetid: 13375ae1-6908-44d8-b775-4375f4fdde4d
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfControlFinishInitializing function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfControlFinishInitializing</b> method informs the framework that a driver has finished initializing a specified control device object.</p>


## -syntax

````
VOID WdfControlFinishInitializing(
  _In_ WDFDEVICE Device
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a control device object.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A system bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>The system will not send I/O requests or Windows Management Instrumentation (WMI) requests to a control device object unless the driver has called <b>WdfControlFinishInitializing</b>.</p>

<p>For more information about control device objects and calling <b>WdfControlFinishInitializing</b>, see <a href="wdf.using_control_device_objects">Using Control Device Objects</a>.</p>

<p>For a code example that uses <b>WdfControlFinishInitializing</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545841">WdfControlDeviceInitAllocate</a>.</p>

<p>The system will not send I/O requests or Windows Management Instrumentation (WMI) requests to a control device object unless the driver has called <b>WdfControlFinishInitializing</b>.</p>

<p>For more information about control device objects and calling <b>WdfControlFinishInitializing</b>, see <a href="wdf.using_control_device_objects">Using Control Device Objects</a>.</p>

<p>For a code example that uses <b>WdfControlFinishInitializing</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545841">WdfControlDeviceInitAllocate</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfcontrol.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543607">CtlDeviceFinishInitDeviceAdd</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543610">CtlDeviceFinishInitDrEntry</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>