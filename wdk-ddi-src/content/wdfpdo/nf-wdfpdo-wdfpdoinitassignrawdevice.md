---
UID: NF.wdfpdo.WdfPdoInitAssignRawDevice
title: WdfPdoInitAssignRawDevice function
author: windows-driver-content
description: The WdfPdoInitAssignRawDevice method indicates that the calling driver can support a specified device in raw mode.
old-location: wdf\wdfpdoinitassignrawdevice.htm
old-project: wdf
ms.assetid: 419912d0-40d0-4fa9-be3b-770875271640
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfPdoInitAssignRawDevice
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
req.alt-api: WdfPdoInitAssignRawDevice
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: ChildDeviceInitAPI, DriverCreate, InitFreeDeviceCallback, InitFreeDeviceCreate, InitFreeNull, KmdfIrql, KmdfIrql2,  PdoDeviceInitAPI, PdoInitFreeDeviceCallback, PdoInitFreeDeviceCreate
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

# WdfPdoInitAssignRawDevice function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfPdoInitAssignRawDevice</b> method indicates that the calling driver can support a specified device in raw mode.



## -syntax

````
NTSTATUS WdfPdoInitAssignRawDevice(
  _In_       PWDFDEVICE_INIT DeviceInit,
  _In_ const GUID            *DeviceClassGuid
);
````


## -parameters

### -param DeviceInit [in]

A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure.


### -param DeviceClassGuid [in]

A pointer to a GUID that identifies a <a href="devinst.device_setup_classes">device setup class</a>.

<div class="alert"><b>Note</b>    You should always specify a custom class GUID. You should not specify an existing class GUID. If you specify an existing class GUID, other drivers that attempt to specify that existing class GUID might fail to install or might install with incorrect security settings.</div>
<div> </div>
For more information, see the following Remarks section.


## -returns
If the operation succeeds, the method returns STATUS_SUCCESS. Otherwise it returns STATUS_INVALID_PARAMETER.


## -remarks
The driver must call <b>WdfPdoInitAssignRawDevice</b> before calling <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>. For more information about calling <b>WdfDeviceCreate</b>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.

The registry can contain values that override the values that a driver specifies when it calls <a href="wdf.wdfdeviceinitassignsddlstring">WdfDeviceInitAssignSDDLString</a>, <a href="wdf.wdfdeviceinitsetdevicetype">WdfDeviceInitSetDeviceType</a>, <a href="wdf.wdfdeviceinitsetcharacteristics">WdfDeviceInitSetCharacteristics</a>, and <a href="wdf.wdfdeviceinitsetexclusive">WdfDeviceInitSetExclusive</a>. The <b>WdfPdoInitAssignRawDevice</b> method's <i>DeviceClassGuid</i> parameter specifies a GUID that identifies the section of the registry that contains the override values. The <i>DeviceClassGuid</i> parameter only identifies a section of the registry and does not actually set the <a href="devinst.device_setup_classes">device setup class</a> for the device. The <a href="devinst.inf_version_section">INF Version section</a> in your device and driver's INF file sets the device setup class. Typically, the <i>DeviceClassGuid</i> parameter's GUID should match the GUID that the <b>INF Version section</b> specifies. 

For more information about using the registry, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563755">Setting Device Object Registry Properties After Installation</a>.

The following snippet from the kmdf_enumswitches driver sample indicates that a driver can support the specified device in raw mode.


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
<a href="devtest.kmdf_childdeviceinitapi">ChildDeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_initfreedevicecallback">InitFreeDeviceCallback</a>, <a href="devtest.kmdf_initfreedevicecreate">InitFreeDeviceCreate</a>, <a href="devtest.kmdf_initfreenull">InitFreeNull</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>,  <a href="devtest.kmdf_pdodeviceinitapi">PdoDeviceInitAPI</a>, <a href="devtest.kmdf_pdoinitfreedevicecallback">PdoInitFreeDeviceCallback</a>, <a href="devtest.kmdf_pdoinitfreedevicecreate">PdoInitFreeDeviceCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfdeviceinitassignsddlstring">WdfDeviceInitAssignSDDLString</a>
</dt>
<dt>
<a href="wdf.wdfdeviceinitsetdevicetype">WdfDeviceInitSetDeviceType</a>
</dt>
<dt>
<a href="wdf.wdfdeviceinitsetcharacteristics">WdfDeviceInitSetCharacteristics</a>
</dt>
<dt>
<a href="wdf.wdfdeviceinitsetexclusive">WdfDeviceInitSetExclusive</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfPdoInitAssignRawDevice method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

