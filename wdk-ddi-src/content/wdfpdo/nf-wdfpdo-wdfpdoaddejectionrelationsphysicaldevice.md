---
UID: NF.wdfpdo.WdfPdoAddEjectionRelationsPhysicalDevice
title: WdfPdoAddEjectionRelationsPhysicalDevice function
author: windows-driver-content
description: The WdfPdoAddEjectionRelationsPhysicalDevice method indicates that a specified device is ejected when another specified device is ejected.
old-location: wdf\wdfpdoaddejectionrelationsphysicaldevice.htm
old-project: wdf
ms.assetid: 23a9ab2a-be8e-40ff-8654-adf170adc6f2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfPdoAddEjectionRelationsPhysicalDevice
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
req.alt-api: WdfPdoAddEjectionRelationsPhysicalDevice
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

# WdfPdoAddEjectionRelationsPhysicalDevice function



## -description
<p class="CCE_Message">[Applies to KMDF only]
The <b>WdfPdoAddEjectionRelationsPhysicalDevice</b> method indicates that a specified device is ejected when another specified device is ejected.


## -syntax

````
NTSTATUS WdfPdoAddEjectionRelationsPhysicalDevice(
  _In_ WDFDEVICE      Device,
  _In_ PDEVICE_OBJECT PhysicalDevice
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.

### -param PhysicalDevice [in]

A pointer to a caller-supplied <a href="kernel.device_object">DEVICE_OBJECT</a> structure that represents a physical device object (PDO).

## -returns
If the operation succeeds, the method returns STATUS_SUCCESS. Additional return values include:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An input parameter is <b>NULL</b>.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>A memory allocation failed.

 

The method might also return other<a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505"> NTSTATUS values</a>.

A system bug check occurs if the driver supplies an invalid object handle.

## -remarks
The <i>PhysicalDevice</i> parameter points to a PDO of a device that is ejected when the device that is identified by <i>Device</i> is ejected. Typically, both devices are controlled by the calling driver. Do not report the child devices of <i>Device</i> because when the PnP manager ejects a parent device, it also ejects the device's children.

For more information, see <a href="wdf.supporting_ejectable_devices">Supporting Ejectable Devices</a>.

The following code example adds a device that the <b>pPhysicalDeviceObject</b> structure represents to the list of devices that are ejected when the device that <b>device</b> specifies is ejected.

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
<a href="wdf.wdfpdoremoveejectionrelationsphysicaldevice">WdfPdoRemoveEjectionRelationsPhysicalDevice</a>
</dt>
<dt>
<a href="wdf.wdfpdoclearejectionrelationsdevices">WdfPdoClearEjectionRelationsDevices</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfPdoAddEjectionRelationsPhysicalDevice method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
