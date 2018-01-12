---
UID: NC:wdfdevice.PFN_WDFDEVICEINITSETPOWERPAGEABLE
title: PFN_WDFDEVICEINITSETPOWERPAGEABLE function
author: windows-driver-content
description: The WdfDeviceInitSetPowerPageable method informs the power manager that the driver must be able to access pageable data while the system is transitioning between a sleeping state and the working (S0) state.
old-location: wdf\wdfdeviceinitsetpowerpageable.htm
old-project: wdf
ms.assetid: 3a216c35-f6b7-483f-a330-d0a66edb9205
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: PFN_WDFDEVICEINITSETPOWERPAGEABLE
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
req.typenames: WDF_DEVICE_SHUTDOWN_FLAGS
req.product: Windows 10 or later.
---

# PFN_WDFDEVICEINITSETPOWERPAGEABLE function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceInitSetPowerPageable</b> method informs the power manager that the driver must be able to access <a href="wdf.creating_pageable_code_in_a_kmdf_driver">pageable</a> data while the system is transitioning between a sleeping state and the working (S0) state. 



## -syntax

````
VOID WdfDeviceInitSetPowerPageable(
  _In_ PWDFDEVICE_INIT DeviceInit
);
````


## -parameters

### -param DeviceInit [in]

A caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a> structure.


## -returns
None


## -remarks
If your function driver or bus driver calls <b>WdfDeviceInitSetPowerPageable</b>, the system ensures that the paging file's device is in its working (D0) state when your driver's device <a href="wdf.a_device_enters_a_low_power_state">enters a low-power state</a> or <a href="wdf.a_device_returns_to_its_working_state">returns to its working state</a>. This allows your driver to access files, the registry, and paged pool during your device's power transitions. 

By default, the framework enables access to pageable data for function drivers. The framework uses the parent device's setting for each child device that a bus driver enumerates, unless the bus driver calls either <b>WdfDeviceInitSetPowerPageable</b> or <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpowernotpageable.md">WdfDeviceInitSetPowerNotPageable</a> for the child device. If you write a bus driver that calls <b>WdfDeviceInitSetPowerPageable</b> for a child device, no drivers in the child device's stack can call <b>WdfDeviceInitSetPowerNotPageable</b>. 

Calling <b>WdfDeviceInitSetPowerPageable</b> or <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpowernotpageable.md">WdfDeviceInitSetPowerNotPageable</a> from a filter driver has no effect. The framework uses the setting that the next-lower driver specifies.

Most drivers do not need to call <b>WdfDeviceInitSetPowerPageable</b> or <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpowernotpageable.md">WdfDeviceInitSetPowerNotPageable</a>. Instead, you should let the framework use the default setting that is appropriate for your driver. However, your driver should call <b>WdfDeviceInitSetPowerNotPageable</b> if the driver is part of a driver stack that must not access pageable data during power transitions (such as the storage stack or the video stack), or if the driver is a bus driver that enumerates devices that might be storage or video devices. 

If your driver calls <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpowerinrush.md">WdfDeviceInitSetPowerInrush</a>, it must not call <b>WdfDeviceInitSetPowerPageable</b>. 

Your driver must call <b>WdfDeviceInitSetPowerPageable</b> before it calls <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>.

For more information about calling <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>, see <a href="https://msdn.microsoft.com/25023c19-a153-4bd4-9fb6-3a1bf85860aa">Creating a Framework Device Object</a>.

The following code example informs the power manager that a driver must be able to access pageable data while the system is transitioning between a sleeping state and the working (S0) state.


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

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpowernotpageable.md">WdfDeviceInitSetPowerNotPageable</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitSetPowerPageable method%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

