---
UID: NF.wdffdo.WdfFdoInitSetFilter
title: WdfFdoInitSetFilter function
author: windows-driver-content
description: The WdfFdoInitSetFilter method identifies the calling driver as an upper-level or lower-level filter driver, for a specified device.
old-location: wdf\wdffdoinitsetfilter.htm
old-project: wdf
ms.assetid: 6e195025-4e70-44fa-a12d-0a98417381a0
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfFdoInitSetFilter
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdffdo.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfFdoInitSetFilter
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DeviceInitAPI, DriverCreate, DrvAckIoStop, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfFdoInitSetFilter function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfFdoInitSetFilter</b> method identifies the calling driver as an upper-level or lower-level <a href="https://msdn.microsoft.com/4def5503-bb0e-4bae-b048-4c8d25d62020">filter driver</a>, for a specified device.



## -syntax

````
VOID WdfFdoInitSetFilter(
  _In_ PWDFDEVICE_INIT DeviceInit
);
````


## -parameters

### -param DeviceInit [in]

A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure that the driver obtained from its <a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a> callback function.


## -returns
None


## -remarks
Filter drivers typically process some I/O requests, but they simply pass most requests to the next driver in the driver stack. If the framework receives a request for one of your driver's devices, and if the driver has not created an I/O queue to receive requests that match the request type, the way the framework processes the request depends on whether the driver has called <b>WdfFdoInitSetFilter</b>:

If a driver calls <b>WdfFdoInitSetFilter</b>, the driver framework forwards the request to the next driver.

If a driver does not call <b>WdfFdoInitSetFilter</b>, the framework completes the request with a status value of STATUS_INVALID_DEVICE_REQUEST.

If a driver calls <b>WdfFdoInitSetFilter</b>, it should not call <a href="wdf.wdfdeviceinitsetiotype">WdfDeviceInitSetIoType</a>, <a href="wdf.wdfdeviceinitsetpowerinrush">WdfDeviceInitSetPowerInrush</a>, or <a href="wdf.wdfdeviceinitsetpowerpageable">WdfDeviceInitSetPowerPageable</a> because the framework ignores the information provided by these calls. Instead, the framework obtains this information from the next-lower device object in the driver's <a href="wdf.wdm_concepts_for_kmdf_drivers#device_stacks#device_stacks">device stack</a>.

The driver must call <b>WdfFdoInitSetFilter</b> before calling <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>. For more information about calling <b>WdfDeviceCreate</b>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>. In addition, the driver must call <b>WdfFdoInitSetFilter</b> before returning from its <a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a> callback function.

For more information about <b>WdfFdoInitSetFilter</b>, see <a href="wdf.creating_device_objects_in_a_filter_driver">Creating Device Objects in a Filter Driver</a>, <a href="wdf.creating_i_o_queues">Creating I/O Queues</a> and <a href="wdf.forwarding_i_o_requests">Forwarding I/O Requests</a>.

The following code example identifies the calling driver as a filter driver for the specified device.


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
<dt>Wdffdo.h (include Wdf.h)</dt>
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
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_deviceinitapi">DeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_drvackiostop">DrvAckIoStop</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfFdoInitSetFilter method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

