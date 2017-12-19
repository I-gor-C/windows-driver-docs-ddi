---
UID: NF.wdfdevice.WdfDeviceInitAssignName
title: WdfDeviceInitAssignName function
author: windows-driver-content
description: The WdfDeviceInitAssignName method assigns a device name to a device's device object.
old-location: wdf\wdfdeviceinitassignname.htm
old-project: wdf
ms.assetid: 70b86a0f-a77d-4c79-931d-d0407083e5b0
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfDeviceInitAssignName
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
req.alt-api: WdfDeviceInitAssignName
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: ChildDeviceInitAPI, ControlDeviceInitAPI, DeviceInitAPI, DriverCreate, InitFreeDeviceCallback, InitFreeDeviceCreate, InitFreeNull, KmdfIrql, KmdfIrql2, PdoDeviceInitAPI, PdoInitFreeDeviceCallback, PdoInitFreeDeviceCreate
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

# WdfDeviceInitAssignName function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceInitAssignName</b> method assigns a device name to a device's device object.



## -syntax

````
NTSTATUS WdfDeviceInitAssignName(
  _In_     PWDFDEVICE_INIT  DeviceInit,
  _In_opt_ PCUNICODE_STRING DeviceName
);
````


## -parameters

### -param DeviceInit [in]

A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure.


### -param DeviceName [in, optional]

A pointer to a <a href="kernel.unicode_string">UNICODE_STRING</a> structure that represents the device name.


## -returns
If <b>WdfDeviceInitAssignName</b> encounters no errors it returns STATUS_SUCCESS. Additional return values include:
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>The system cannot allocate space to store the device name.

 


## -remarks
If a driver calls <b>WdfDeviceInitAssignName</b>, it must do so before it calls <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>.

If a driver calls <b>WdfDeviceInitAssignName</b> to assign a name, the driver can subsequently call <b>WdfDeviceInitAssignName</b> with a <b>NULL</b> <i>DeviceName</i> parameter to clear the device name. If the device name is <b>NULL</b> and the device object requires a name (because it represents a PDO or a <a href="wdf.using_control_device_objects">control device</a>), the operating system will create a name. 

For more information about naming device objects, see <a href="wdf.controlling_device_access_in_kmdf_drivers">Controlling Device Access in Framework-Based Drivers</a>.

For more information about calling <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.

The following code example assigns an <a href="https://msdn.microsoft.com/dfcc7338-7c4d-4b4c-9a13-c76bfe82f5a9">NT device name</a> to a device.


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
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_childdeviceinitapi">ChildDeviceInitAPI</a>, <a href="devtest.kmdf_controldeviceinitapi">ControlDeviceInitAPI</a>, <a href="devtest.kmdf_deviceinitapi">DeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_initfreedevicecallback">InitFreeDeviceCallback</a>, <a href="devtest.kmdf_initfreedevicecreate">InitFreeDeviceCreate</a>, <a href="devtest.kmdf_initfreenull">InitFreeNull</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_pdodeviceinitapi">PdoDeviceInitAPI</a>, <a href="devtest.kmdf_pdoinitfreedevicecallback">PdoInitFreeDeviceCallback</a>, <a href="devtest.kmdf_pdoinitfreedevicecreate">PdoInitFreeDeviceCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfdeviceretrievedevicename">WdfDeviceRetrieveDeviceName</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitAssignName method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

