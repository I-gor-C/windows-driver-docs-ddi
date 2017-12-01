---
UID: NF.wdfdevice.WdfDeviceRemoveDependentUsageDeviceObject
title: WdfDeviceRemoveDependentUsageDeviceObject
author: windows-driver-content
description: The WdfDeviceRemoveDependentUsageDeviceObject method indicates that a specified device no longer depends on another device when the specified device is used to store special files.
old-location: wdf\wdfdeviceremovedependentusagedeviceobject.htm
old-project: wdf
ms.assetid: d9569b4b-ad71-46dd-b421-8493f595f030
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfDeviceRemoveDependentUsageDeviceObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.9
req.umdf-ver: 
req.alt-api: WdfDeviceRemoveDependentUsageDeviceObject
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceRemoveDependentUsageDeviceObject function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDeviceRemoveDependentUsageDeviceObject</b> method indicates that a specified device no longer depends on another device when the specified device is used to store <a href="..\wdfdevice\ne-wdfdevice--wdf-special-file-type.md">special files</a>. </p>


## -syntax

````
VOID WdfDeviceRemoveDependentUsageDeviceObject(
  _In_ WDFDEVICE      Device,
  _In_ PDEVICE_OBJECT DependentDevice
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>DependentDevice</i> [in]

<dd>
<p>A pointer to a caller-supplied <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> structure that identifies a device that <i>Device</i> depends on.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>Your driver can call <b>WdfDeviceRemoveDependentUsageDeviceObject</b> to remove a device dependency that a previous call to <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceadddependentusagedeviceobject.md">WdfDeviceAddDependentUsageDeviceObject</a> created.</p>

<p>For more information about <b>WdfDeviceRemoveDependentUsageDeviceObject</b> and <b>WdfDeviceRemoveDependentUsageDeviceObject</b>, see <a href="wdf.supporting_special_files">Supporting Special Files</a>. </p>

<p>The following code example removes a device (<b>pDeviceObject</b>) from the list of devices that another device (<b>device</b>) depends on.</p>

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
<p>1.9</p>
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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdfdeviceadddependentusagedeviceobject.md">WdfDeviceAddDependentUsageDeviceObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceRemoveDependentUsageDeviceObject method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
