---
UID: NF.wdfdevice.WdfDeviceAssignMofResourceName
title: WdfDeviceAssignMofResourceName
author: windows-driver-content
description: The WdfDeviceAssignMofResourceName method registers a MOF resource name for a specified device.
old-location: wdf\wdfdeviceassignmofresourcename.htm
old-project: wdf
ms.assetid: b4ab0a7b-9c5a-4295-94fc-35310ca8e05b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfDeviceAssignMofResourceName
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
req.alt-api: WdfDeviceAssignMofResourceName
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceAssignMofResourceName function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDeviceAssignMofResourceName</b> method registers a MOF resource name for a specified device.</p>


## -syntax

````
NTSTATUS WdfDeviceAssignMofResourceName(
  _In_ WDFDEVICE        Device,
  _In_ PCUNICODE_STRING MofResourceName
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>MofResourceName</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure that specifies the name of a MOF resource. </p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, <b>WdfDeviceAssignMofResourceName</b> returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The driver has already called <a href="https://msdn.microsoft.com/library/windows/hardware/ff545897">WdfDeviceAssignMofResourceName</a>.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p> Insufficient memory is available.</p>

<p> </p>

<p>The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>A driver that provides a MOF file to support WMI must call <b>WdfDeviceAssignMofResourceName</b>, typically from within its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> or <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> callback function. The MOF resource name is the file name that the driver specifies in a <b>MofResource</b> statement in its resource script (RC) file. For more information about specifying a MOF resource name, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542012">Compiling a Driver's MOF File</a>.</p>

<p>A driver that <a href="wdf.enumerating_the_devices_on_a_bus">enumerates the devices on a bus</a> can call <b>WdfDeviceAssignMofResourceName</b> for the parent device, and the framework will use the parent's MOF resource name for child devices.</p>

<p>For more information about WMI, see <a href="wdf.supporting_wmi_in_kmdf_drivers">Supporting WMI in Framework-Based Drivers</a>.</p>

<p>The following code example declares a Unicode string that represents a MOF resource name and then registers the name.</p>

<p>A driver that provides a MOF file to support WMI must call <b>WdfDeviceAssignMofResourceName</b>, typically from within its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> or <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> callback function. The MOF resource name is the file name that the driver specifies in a <b>MofResource</b> statement in its resource script (RC) file. For more information about specifying a MOF resource name, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542012">Compiling a Driver's MOF File</a>.</p>

<p>A driver that <a href="wdf.enumerating_the_devices_on_a_bus">enumerates the devices on a bus</a> can call <b>WdfDeviceAssignMofResourceName</b> for the parent device, and the framework will use the parent's MOF resource name for child devices.</p>

<p>For more information about WMI, see <a href="wdf.supporting_wmi_in_kmdf_drivers">Supporting WMI in Framework-Based Drivers</a>.</p>

<p>The following code example declares a Unicode string that represents a MOF resource name and then registers the name.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>