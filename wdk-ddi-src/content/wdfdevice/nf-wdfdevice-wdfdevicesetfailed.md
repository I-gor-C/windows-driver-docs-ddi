---
UID: NF.wdfdevice.WdfDeviceSetFailed
title: WdfDeviceSetFailed function
author: windows-driver-content
description: The WdfDeviceSetFailed method informs the framework that the driver encountered a hardware or software error that is associated with a specified device.
old-location: wdf\wdfdevicesetfailed.htm
old-project: wdf
ms.assetid: 87fbceab-d08c-4da7-a257-1454f84c04b7
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDeviceSetFailed
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfDeviceSetFailed
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceSetFailed function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]
The <b>WdfDeviceSetFailed</b> method informs the framework that the driver encountered a hardware or software error that is associated with a specified device.


## -syntax

````
VOID WdfDeviceSetFailed(
  _In_ WDFDEVICE                Device,
  _In_ WDF_DEVICE_FAILED_ACTION FailedAction
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.

### -param FailedAction [in]

A <a href="wdf.wdf_device_failed_action">WDF_DEVICE_FAILED_ACTION</a>-typed enumerator that indicates whether the framework should attempt to reload the specified device's drivers.

## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.

## -remarks
If a driver encounters an unrecoverable hardware or software error, it must call <b>WdfDeviceSetFailed</b> so that the system can unload the device's drivers.

Starting in UMDF version 2.15, a UMDF driver can request that the the underlying bus driver re-enumerate it by calling <b>WdfDeviceSetFailed</b> with <i>FailedAction</i> set to <b>WdfDeviceFailedAttemptRestart</b>. The bus driver must support the <a href="kernel.guid_reenumerate_self_interface_standard">GUID_REENUMERATE_SELF_INTERFACE_STANDARD</a> interface.

Alternatively, a UMDF driver can set <i>FailedAction</i> to <b>WdfDeviceFailedNoRestart</b>.

For more information about <b>WdfDeviceSetFailed</b>, see <a href="wdf.reporting_device_failures">Reporting Device Failures</a>.

The following code example informs the framework that a failure has occurred. If the specified device's drivers are not supporting other devices, the framework will unload the drivers and then attempt to reload them.

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
Minimum UMDF version
</th>
<td width="70%">
2.0
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
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>