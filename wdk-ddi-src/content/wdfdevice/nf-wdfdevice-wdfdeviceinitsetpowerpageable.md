---
UID: NF.wdfdevice.WdfDeviceInitSetPowerPageable
title: WdfDeviceInitSetPowerPageable
author: windows-driver-content
description: The WdfDeviceInitSetPowerPageable method informs the power manager that the driver must be able to access pageable data while the system is transitioning between a sleeping state and the working (S0) state.
old-location: wdf\wdfdeviceinitsetpowerpageable.htm
ms.assetid: 3a216c35-f6b7-483f-a330-d0a66edb9205
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
req.umdf-ver: 
req.alt-api: WdfDeviceInitSetPowerPageable
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
ms.keywords: WdfDeviceInitSetPowerPageable
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceInitSetPowerPageable function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDeviceInitSetPowerPageable</b> method informs the power manager that the driver must be able to access <a href="wdf.creating_pageable_code_in_a_kmdf_driver">pageable</a> data while the system is transitioning between a sleeping state and the working (S0) state. </p>


## -syntax

````
VOID WdfDeviceInitSetPowerPageable(
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
<p>If your function driver or bus driver calls <b>WdfDeviceInitSetPowerPageable</b>, the system ensures that the paging file's device is in its working (D0) state when your driver's device <a href="wdf.a_device_enters_a_low_power_state">enters a low-power state</a> or <a href="wdf.a_device_returns_to_its_working_state">returns to its working state</a>. This allows your driver to access files, the registry, and paged pool during your device's power transitions. </p>

<p>By default, the framework enables access to pageable data for function drivers. The framework uses the parent device's setting for each child device that a bus driver enumerates, unless the bus driver calls either <b>WdfDeviceInitSetPowerPageable</b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff546147">WdfDeviceInitSetPowerNotPageable</a> for the child device. If you write a bus driver that calls <b>WdfDeviceInitSetPowerPageable</b> for a child device, no drivers in the child device's stack can call <b>WdfDeviceInitSetPowerNotPageable</b>. </p>

<p>Calling <b>WdfDeviceInitSetPowerPageable</b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff546147">WdfDeviceInitSetPowerNotPageable</a> from a filter driver has no effect. The framework uses the setting that the next-lower driver specifies.</p>

<p>Most drivers do not need to call <b>WdfDeviceInitSetPowerPageable</b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff546147">WdfDeviceInitSetPowerNotPageable</a>. Instead, you should let the framework use the default setting that is appropriate for your driver. However, your driver should call <b>WdfDeviceInitSetPowerNotPageable</b> if the driver is part of a driver stack that must not access pageable data during power transitions (such as the storage stack or the video stack), or if the driver is a bus driver that enumerates devices that might be storage or video devices. </p>

<p>If your driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff546142">WdfDeviceInitSetPowerInrush</a>, it must not call <b>WdfDeviceInitSetPowerPageable</b>. </p>

<p>Your driver must call <b>WdfDeviceInitSetPowerPageable</b> before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>.</p>

<p>For more information about calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>The following code example informs the power manager that a driver must be able to access pageable data while the system is transitioning between a sleeping state and the working (S0) state.</p>

<p>If your function driver or bus driver calls <b>WdfDeviceInitSetPowerPageable</b>, the system ensures that the paging file's device is in its working (D0) state when your driver's device <a href="wdf.a_device_enters_a_low_power_state">enters a low-power state</a> or <a href="wdf.a_device_returns_to_its_working_state">returns to its working state</a>. This allows your driver to access files, the registry, and paged pool during your device's power transitions. </p>

<p>By default, the framework enables access to pageable data for function drivers. The framework uses the parent device's setting for each child device that a bus driver enumerates, unless the bus driver calls either <b>WdfDeviceInitSetPowerPageable</b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff546147">WdfDeviceInitSetPowerNotPageable</a> for the child device. If you write a bus driver that calls <b>WdfDeviceInitSetPowerPageable</b> for a child device, no drivers in the child device's stack can call <b>WdfDeviceInitSetPowerNotPageable</b>. </p>

<p>Calling <b>WdfDeviceInitSetPowerPageable</b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff546147">WdfDeviceInitSetPowerNotPageable</a> from a filter driver has no effect. The framework uses the setting that the next-lower driver specifies.</p>

<p>Most drivers do not need to call <b>WdfDeviceInitSetPowerPageable</b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff546147">WdfDeviceInitSetPowerNotPageable</a>. Instead, you should let the framework use the default setting that is appropriate for your driver. However, your driver should call <b>WdfDeviceInitSetPowerNotPageable</b> if the driver is part of a driver stack that must not access pageable data during power transitions (such as the storage stack or the video stack), or if the driver is a bus driver that enumerates devices that might be storage or video devices. </p>

<p>If your driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff546142">WdfDeviceInitSetPowerInrush</a>, it must not call <b>WdfDeviceInitSetPowerPageable</b>. </p>

<p>Your driver must call <b>WdfDeviceInitSetPowerPageable</b> before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>.</p>

<p>For more information about calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>The following code example informs the power manager that a driver must be able to access pageable data while the system is transitioning between a sleeping state and the working (S0) state.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546147">WdfDeviceInitSetPowerNotPageable</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitSetPowerPageable method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
