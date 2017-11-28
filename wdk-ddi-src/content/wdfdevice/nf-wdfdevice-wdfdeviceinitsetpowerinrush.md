---
UID: NF.wdfdevice.WdfDeviceInitSetPowerInrush
title: WdfDeviceInitSetPowerInrush
author: windows-driver-content
description: The WdfDeviceInitSetPowerInrush method informs the power manager that the specified device requires an inrush of current when it starts.
old-location: wdf\wdfdeviceinitsetpowerinrush.htm
old-project: wdf
ms.assetid: 91b29a5b-8bc0-44c0-8c48-2d023da12dcb
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfDeviceInitSetPowerInrush
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
req.alt-api: WdfDeviceInitSetPowerInrush
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceInitSetPowerInrush function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDeviceInitSetPowerInrush</b> method informs the power manager that the specified device requires an inrush of current when it starts.</p>


## -syntax

````
VOID WdfDeviceInitSetPowerInrush(
  _In_ PWDFDEVICE_INIT DeviceInit
);
````


## -parameters
<dl>

### -param <i>DeviceInit</i> [in]

<dd>
<p>A caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a> structure.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>To avoid overloading the system's power supply, the system starts devices that require an inrush of current one at a time.</p>

<p>If your driver calls <b>WdfDeviceInitSetPowerInrush</b>, the framework makes it <a href="wdf.creating_pageable_code_in_a_kmdf_driver">nonpageable</a> during power state transitions and the driver must not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546766">WdfDeviceInitSetPowerPageable</a>. </p>

<p>Your driver must call <b>WdfDeviceInitSetPowerInrush</b> before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>. For more information about calling <b>WdfDeviceCreate</b>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>Calling <b>WdfDeviceInitSetPowerInrush</b> from a filter driver has no effect. For filter drivers, the framework uses the setting that the next-lower driver in the driver stack specifies.</p>

<p>The following code example informs the power manager that a device requires an inrush of current when it starts.</p>

<p>To avoid overloading the system's power supply, the system starts devices that require an inrush of current one at a time.</p>

<p>If your driver calls <b>WdfDeviceInitSetPowerInrush</b>, the framework makes it <a href="wdf.creating_pageable_code_in_a_kmdf_driver">nonpageable</a> during power state transitions and the driver must not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546766">WdfDeviceInitSetPowerPageable</a>. </p>

<p>Your driver must call <b>WdfDeviceInitSetPowerInrush</b> before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>. For more information about calling <b>WdfDeviceCreate</b>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>Calling <b>WdfDeviceInitSetPowerInrush</b> from a filter driver has no effect. For filter drivers, the framework uses the setting that the next-lower driver in the driver stack specifies.</p>

<p>The following code example informs the power manager that a device requires an inrush of current when it starts.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975068">ChildDeviceInitAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544843">DeviceInitAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550354">PdoDeviceInitAPI</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitSetPowerInrush method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
