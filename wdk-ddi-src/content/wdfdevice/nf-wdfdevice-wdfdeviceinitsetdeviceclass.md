---
UID: NF:wdfdevice.WdfDeviceInitSetDeviceClass
title: WdfDeviceInitSetDeviceClass function
author: windows-driver-content
description: The WdfDeviceInitSetDeviceClass method specifies a GUID that identifies the device's device setup class.
old-location: wdf\wdfdeviceinitsetdeviceclass.htm
old-project: wdf
ms.assetid: c87a8368-3804-4a07-92c8-65a453d0808f
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: WdfDeviceInitSetDeviceClass
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
req.alt-api: WdfDeviceInitSetDeviceClass
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: ChildDeviceInitAPI, ControlDeviceInitAPI, DeviceInitAPI, DriverCreate, KmdfIrql, KmdfIrql2, PdoDeviceInitAPI
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.typenames: WDF_STATE_NOTIFICATION_TYPE
req.product: Windows 10 or later.
---

# WdfDeviceInitSetDeviceClass function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceInitSetDeviceClass</b> method specifies a GUID that identifies the device's <a href="devinst.device_setup_classes">device setup class</a>. 



## -syntax

````
VOID WdfDeviceInitSetDeviceClass(
  _In_       PWDFDEVICE_INIT DeviceInit,
  _In_ const GUID            *DeviceClassGuid
);
````


## -parameters

### -param DeviceInit [in]

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a> structure.


### -param DeviceClassGuid [in]

Pointer to a GUID that identifies a section of the registry containing possible overrides for the <i>DefaultSDDLString</i>, <i>DeviceType</i>, <i>DeviceCharacteristics</i>, and <i>Exclusive</i> parameters.

<div class="alert"><b>Note</b>    You should always specify a custom class GUID. You should not specify an existing class GUID. If you specify an existing class GUID, other drivers that attempt to specify that existing class GUID might fail to install or might install with incorrect security settings.</div>
<div> </div>

## -returns
None


## -remarks
The registry can contain values that override the values that a driver specifies when it calls <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitassignsddlstring.md">WdfDeviceInitAssignSDDLString</a>, <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetdevicetype.md">WdfDeviceInitSetDeviceType</a>, <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetcharacteristics.md">WdfDeviceInitSetCharacteristics</a>, and <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetexclusive.md">WdfDeviceInitSetExclusive</a>. The driver can call <b>WdfDeviceInitSetDeviceClass</b> to specify a GUID that identifies the section of the registry that contains the override values.

Typically, a driver calls <b>WdfDeviceInitSetDeviceClass</b> only if it is creating a <a href="wdf.using_control_device_objects">control device</a>. 

For more information about using the registry, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563755">Setting Device Object Registry Properties After Installation</a>.

If a driver calls <b>WdfDeviceInitSetDeviceClass</b>, it must do so before it calls <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>.

For more information about calling <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>, see <a href="https://msdn.microsoft.com/25023c19-a153-4bd4-9fb6-3a1bf85860aa">Creating a Framework Device Object</a>.

The following code example sets a device's setup class to the system device class.


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
<dt>Wdf01000.sys (see <a href="https://msdn.microsoft.com/51db6f3c-45cb-46a7-9dd4-2bab67893fea">Framework Library Versioning</a>.)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975068">ChildDeviceInitAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543531">ControlDeviceInitAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544843">DeviceInitAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550354">PdoDeviceInitAPI</a>
</td>
</tr>
</table>