---
UID: NF.wdffdo.WdfFdoInitWdmGetPhysicalDevice
title: WdfFdoInitWdmGetPhysicalDevice
author: windows-driver-content
description: The WdfFdoInitWdmGetPhysicalDevice method retrieves a device's WDM physical device object (PDO).
old-location: wdf\wdffdoinitwdmgetphysicaldevice.htm
old-project: wdf
ms.assetid: eba64244-50ff-4c59-a30f-46874c683e63
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfFdoInitWdmGetPhysicalDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdffdo.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfFdoInitWdmGetPhysicalDevice
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DeviceInitAPI, DriverCreate, KmdfIrql, KmdfIrql2
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

# WdfFdoInitWdmGetPhysicalDevice function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfFdoInitWdmGetPhysicalDevice</b> method retrieves a device's WDM physical device object (PDO).</p>


## -syntax

````
PDEVICE_OBJECT WdfFdoInitWdmGetPhysicalDevice(
  _In_ PWDFDEVICE_INIT DeviceInit
);
````


## -parameters
<dl>

### -param <i>DeviceInit</i> [in]

<dd>
<p>A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure that the driver obtained from its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns a pointer to a <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> structure. Otherwise the method returns <b>NULL</b>.</p>

## -remarks
<p>The driver must call <b>WdfFdoInitWdmGetPhysicalDevice</b> before calling <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>. For more information about calling <b>WdfDeviceCreate</b>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>For more information about the <b>WdfFdoInitWdmGetPhysicalDevice</b> method, see <a href="wdf.creating_device_objects_in_a_function_driver">Creating Device Objects in a Function Driver</a>.</p>

<p>The following code example obtains a pointer to a DEVICE_OBJECT structure that represents a device's WDM PDO.</p>

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
<dt>Wdffdo.h (include Wdf.h)</dt>
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
<a href="devtest.kmdf_deviceinitapi">DeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>