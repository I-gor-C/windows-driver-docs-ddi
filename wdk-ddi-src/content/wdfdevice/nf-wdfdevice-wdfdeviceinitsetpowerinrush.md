---
UID: NF.wdfdevice.WdfDeviceInitSetPowerInrush
title: WdfDeviceInitSetPowerInrush function
author: windows-driver-content
description: The WdfDeviceInitSetPowerInrush method informs the power manager that the specified device requires an inrush of current when it starts.
old-location: wdf\wdfdeviceinitsetpowerinrush.htm
old-project: wdf
ms.assetid: 91b29a5b-8bc0-44c0-8c48-2d023da12dcb
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
req.product: Windows 10 or later.
---

# WdfDeviceInitSetPowerInrush function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceInitSetPowerInrush</b> method informs the power manager that the specified device requires an inrush of current when it starts.



## -syntax

````
VOID WdfDeviceInitSetPowerInrush(
  _In_ PWDFDEVICE_INIT DeviceInit
);
````


## -parameters

### -param DeviceInit [in]

A caller-supplied pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure.


## -returns
None


## -remarks
To avoid overloading the system's power supply, the system starts devices that require an inrush of current one at a time.

If your driver calls <b>WdfDeviceInitSetPowerInrush</b>, the framework makes it <a href="wdf.creating_pageable_code_in_a_kmdf_driver">nonpageable</a> during power state transitions and the driver must not call <a href="wdf.wdfdeviceinitsetpowerpageable">WdfDeviceInitSetPowerPageable</a>. 

Your driver must call <b>WdfDeviceInitSetPowerInrush</b> before it calls <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>. For more information about calling <b>WdfDeviceCreate</b>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.

Calling <b>WdfDeviceInitSetPowerInrush</b> from a filter driver has no effect. For filter drivers, the framework uses the setting that the next-lower driver in the driver stack specifies.

The following code example informs the power manager that a device requires an inrush of current when it starts.


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
<a href="devtest.kmdf_childdeviceinitapi">ChildDeviceInitAPI</a>, <a href="devtest.kmdf_deviceinitapi">DeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_pdodeviceinitapi">PdoDeviceInitAPI</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitSetPowerInrush method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

