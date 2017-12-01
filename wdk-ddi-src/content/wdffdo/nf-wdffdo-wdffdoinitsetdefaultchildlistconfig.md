---
UID: NF.wdffdo.WdfFdoInitSetDefaultChildListConfig
title: WdfFdoInitSetDefaultChildListConfig
author: windows-driver-content
description: The WdfFdoInitSetDefaultChildListConfig method configures a bus driver's default child list.
old-location: wdf\wdffdoinitsetdefaultchildlistconfig.htm
old-project: wdf
ms.assetid: 656a0c58-dd12-4417-a781-464d1670592c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfFdoInitSetDefaultChildListConfig
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
req.alt-api: WdfFdoInitSetDefaultChildListConfig
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: ChildListConfiguration, DeviceInitAPI, DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfFdoInitSetDefaultChildListConfig function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfFdoInitSetDefaultChildListConfig</b> method configures a bus driver's default child list.</p>


## -syntax

````
VOID WdfFdoInitSetDefaultChildListConfig(
  _Inout_  PWDFDEVICE_INIT        DeviceInit,
  _In_     PWDF_CHILD_LIST_CONFIG Config,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES DefaultChildListAttributes
);
````


## -parameters
<dl>

### -param <i>DeviceInit</i> [in, out]

<dd>
<p>A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure that the driver obtained from its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function.</p>
</dd>

### -param <i>Config</i> [in]

<dd>
<p>A pointer to a driver-allocated <a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-list-config.md">WDF_CHILD_LIST_CONFIG</a> structure.</p>
</dd>

### -param <i>DefaultChildListAttributes</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure that contains object attributes for the child-list object that represents the driver's default child list. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A bus driver must call <b>WdfFdoInitSetDefaultChildListConfig</b> before calling <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a> for the functional device object (FDO). For more information about calling <b>WdfDeviceCreate</b>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>For more information about the <b>WdfFdoInitSetDefaultChildListConfig</b> method, see <a href="wdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a>.</p>

<p>The following code example initializes a <a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-list-config.md">WDF_CHILD_LIST_CONFIG</a> structure and then calls <b>WdfFdoInitSetDefaultChildListConfig</b>. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_childlistconfiguration">ChildListConfiguration</a>, <a href="devtest.kmdf_deviceinitapi">DeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistcreate.md">WdfChildListCreate</a>
</dt>
<dt>
<a href="..\wdfchildlist\nf-wdfchildlist-wdf-child-list-config-init.md">WDF_CHILD_LIST_CONFIG_INIT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfFdoInitSetDefaultChildListConfig method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
