---
UID: NF.wdfdevice.WdfDeviceSetStaticStopRemove
title: WdfDeviceSetStaticStopRemove
author: windows-driver-content
description: The WdfDeviceSetStaticStopRemove method informs the framework whether a device can be stopped and removed.
old-location: wdf\wdfdevicesetstaticstopremove.htm
ms.assetid: b2776618-2585-4a7a-9f8f-536f1d28745b
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfDeviceSetStaticStopRemove
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WdfDeviceSetStaticStopRemove
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceSetStaticStopRemove function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfDeviceSetStaticStopRemove</b> method informs the framework whether a device can be stopped and removed.</p>


## -syntax

````
VOID WdfDeviceSetStaticStopRemove(
  _In_ WDFDEVICE Device,
  _In_ BOOLEAN   Stoppable
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>Stoppable</i> [in]

<dd>
<p>A Boolean value that indicates whether the specified device can be stopped and removed. If <b>TRUE</b>, the device can be stopped and removed. If <b>FALSE</b>, the device cannot be stopped and removed.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>By default, a device can be stopped and removed. Therefore, a driver typically calls <b>WdfDeviceSetStaticStopRemove</b> only if it must temporarily set the <i>Stoppable</i> parameter to <b>FALSE</b>. For example, a driver that controls a DVD writer might call <b>WdfDeviceSetStaticStopRemove</b> with <i>Stoppable</i> set to <b>FALSE</b> before it begins burning a DVD. After the driver has finished burning the DVD, it would call <b>WdfDeviceSetStaticStopRemove</b> again with <i>Stoppable</i> set to <b>TRUE</b>.  </p>

<p>If your driver's device is supporting a special file (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546903">WdfDeviceSetSpecialFileSupport</a>), the framework will not allow the device to be stopped or removed. In this case, your driver does not have to call <b>WdfDeviceSetStaticStopRemove</b> .</p>

<p>The driver must match every call to <b>WdfDeviceSetStaticStopRemove</b> with <i>Stoppable</i> set to <b>FALSE</b> with a call to <b>WdfDeviceSetStaticStopRemove</b> with <i>Stoppable</i> set to <b>TRUE</b>.</p>

<p>Calling <b>WdfDeviceSetStaticStopRemove</b> with <i>Stoppable</i> set to <b>FALSE</b> does not prevent the framework from notifying the driver if the device is unexpectedly removed (surprise-removed).</p>

<p>For more information about how to prevent the operating system from stopping a device, see <a href="wdf.handling_requests_to_stop_a_device">Handling Requests to Stop a Device</a>.</p>

<p>The following code example informs the framework that the specified device cannot be stopped and removed.</p>

<p>By default, a device can be stopped and removed. Therefore, a driver typically calls <b>WdfDeviceSetStaticStopRemove</b> only if it must temporarily set the <i>Stoppable</i> parameter to <b>FALSE</b>. For example, a driver that controls a DVD writer might call <b>WdfDeviceSetStaticStopRemove</b> with <i>Stoppable</i> set to <b>FALSE</b> before it begins burning a DVD. After the driver has finished burning the DVD, it would call <b>WdfDeviceSetStaticStopRemove</b> again with <i>Stoppable</i> set to <b>TRUE</b>.  </p>

<p>If your driver's device is supporting a special file (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546903">WdfDeviceSetSpecialFileSupport</a>), the framework will not allow the device to be stopped or removed. In this case, your driver does not have to call <b>WdfDeviceSetStaticStopRemove</b> .</p>

<p>The driver must match every call to <b>WdfDeviceSetStaticStopRemove</b> with <i>Stoppable</i> set to <b>FALSE</b> with a call to <b>WdfDeviceSetStaticStopRemove</b> with <i>Stoppable</i> set to <b>TRUE</b>.</p>

<p>Calling <b>WdfDeviceSetStaticStopRemove</b> with <i>Stoppable</i> set to <b>FALSE</b> does not prevent the framework from notifying the driver if the device is unexpectedly removed (surprise-removed).</p>

<p>For more information about how to prevent the operating system from stopping a device, see <a href="wdf.handling_requests_to_stop_a_device">Handling Requests to Stop a Device</a>.</p>

<p>The following code example informs the framework that the specified device cannot be stopped and removed.</p>

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
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>