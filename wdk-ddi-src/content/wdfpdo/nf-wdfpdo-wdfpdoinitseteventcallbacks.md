---
UID: NF.wdfpdo.WdfPdoInitSetEventCallbacks
title: WdfPdoInitSetEventCallbacks function
author: windows-driver-content
description: The WdfPdoInitSetEventCallbacks method registers a bus driver's event callback functions.
old-location: wdf\wdfpdoinitseteventcallbacks.htm
old-project: wdf
ms.assetid: 7ce47eab-c1d7-4a0d-accb-c8a925aa3d1d
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfPdoInitSetEventCallbacks
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfpdo.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfPdoInitSetEventCallbacks
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: ChildDeviceInitAPI, DriverCreate, KmdfIrql, KmdfIrql2, PdoDeviceInitAPI
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfPdoInitSetEventCallbacks function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfPdoInitSetEventCallbacks</b> method registers a bus driver's event callback functions.



## -syntax

````
VOID WdfPdoInitSetEventCallbacks(
  _In_ PWDFDEVICE_INIT          DeviceInit,
  _In_ PWDF_PDO_EVENT_CALLBACKS DispatchTable
);
````


## -parameters

### -param DeviceInit [in]

A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure.


### -param DispatchTable [in]

A pointer to a caller-allocated <a href="wdf.wdf_pdo_event_callbacks">WDF_PDO_EVENT_CALLBACKS</a> structure.


## -returns
None


## -remarks
The bus driver must allocate a <a href="wdf.wdf_pdo_event_callbacks">WDF_PDO_EVENT_CALLBACKS</a> structure and fill in the structure with pointers to the driver's event callback functions.

The driver must call <b>WdfPdoInitSetEventCallbacks</b> before calling <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>. For more information about calling <b>WdfPdoInitSetEventCallbacks</b> and <b>WdfDeviceCreate</b>, see <a href="wdf.creating_device_objects_in_a_bus_driver">Creating Device Objects in a Bus Driver</a>.

The following code example initializes a <a href="wdf.wdf_pdo_event_callbacks">WDF_PDO_EVENT_CALLBACKS</a> structure and then calls <b>WdfPdoInitSetEventCallbacks</b>.


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
<dt>Wdfpdo.h (include Wdf.h)</dt>
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
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_childdeviceinitapi">ChildDeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_pdodeviceinitapi">PdoDeviceInitAPI</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_pdo_event_callbacks_init">WDF_PDO_EVENT_CALLBACKS_INIT</a>
</dt>
<dt>
<a href="wdf.wdfpdoinitallocate">WdfPdoInitAllocate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfPdoInitSetEventCallbacks method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

