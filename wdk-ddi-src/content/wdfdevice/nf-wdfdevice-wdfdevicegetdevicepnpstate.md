---
UID: NF.wdfdevice.WdfDeviceGetDevicePnpState
title: WdfDeviceGetDevicePnpState function
author: windows-driver-content
description: The WdfDeviceGetDevicePnpState method returns the current state of the framework's Plug and Play state machine for a specified device.
old-location: wdf\wdfdevicegetdevicepnpstate.htm
old-project: wdf
ms.assetid: 25936ed9-d213-458f-bbc8-90eedea9ba02
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfDeviceGetDevicePnpState
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
req.alt-api: WdfDeviceGetDevicePnpState
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
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceGetDevicePnpState function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceGetDevicePnpState</b> method returns the current state of the framework's Plug and Play state machine for a specified device.



## -syntax

````
WDF_DEVICE_PNP_STATE WdfDeviceGetDevicePnpState(
  _In_ WDFDEVICE Device
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.


## -returns
<b>WdfDeviceGetDevicePnpState</b> returns a <a href="wdf.wdf_device_pnp_state">WDF_DEVICE_PNP_STATE</a>-typed enumerator that identifies the current state of the framework's Plug and Play state machine for the specified device.

A bug check occurs if the driver supplies an invalid object handle.


## -remarks
Most drivers do not need to be aware of the state of the framework's Plug and Play state machine. For more information about the framework's state machines, see <a href="wdf.state_machines_in_the_framework">State Machines in the Framework</a>.

The following code example obtains the current state of the framework's Plug and Play state machine for a specified device.


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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfdevicegetdevicepowerpolicystate">WdfDeviceGetDevicePowerPolicyState</a>
</dt>
<dt>
<a href="wdf.wdfdevicegetdevicepowerstate">WdfDeviceGetDevicePowerState</a>
</dt>
<dt>
<a href="wdf.wdfdevstatenormalize">WdfDevStateNormalize</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceGetDevicePnpState method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

