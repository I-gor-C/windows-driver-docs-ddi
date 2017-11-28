---
UID: NF.wdfqueryinterface.WdfDeviceAddQueryInterface
title: WdfDeviceAddQueryInterface
author: windows-driver-content
description: The WdfDeviceAddQueryInterface method creates a driver-defined interface that other drivers can query and use.
old-location: wdf\wdfdeviceaddqueryinterface.htm
old-project: wdf
ms.assetid: 6e811b5e-bd2a-473b-8e5c-52bfbd9b8f7c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfDeviceAddQueryInterface
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfqueryinterface.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDeviceAddQueryInterface
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

# WdfDeviceAddQueryInterface function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDeviceAddQueryInterface</b> method creates a driver-defined interface that other drivers can query and use.</p>


## -syntax

````
NTSTATUS WdfDeviceAddQueryInterface(
  _In_ WDFDEVICE                   Device,
  _In_ PWDF_QUERY_INTERFACE_CONFIG InterfaceConfig
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>InterfaceConfig</i> [in]

<dd>
<p>A pointer to a driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552439">WDF_QUERY_INTERFACE_CONFIG</a> structure that describes the interface.</p>
</dd>
</dl>

## -returns
<p><b>WdfDeviceAddQueryInterface</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The method was called at the wrong IRQL.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An input parameter (possibly including members of the WDF_QUERY_INTERFACE_CONFIG structure) was invalid.</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The size of the WDF_QUERY_INTERFACE_CONFIG structure was incorrect.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There was insufficient memory.</p>

<p> </p>

<p>For a list of additional return values, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.

</p>

<p>This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

</p>

<p>A system bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Drivers that create driver-defined interfaces typically call <b>WdfDeviceAddQueryInterface</b> from within an <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> or <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> callback function.</p>

<p>After a driver calls <b>WdfDeviceAddQueryInterface</b> to create a driver-defined interface, another framework-based driver can access the interface by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547289">WdfFdoQueryForInterface</a>.</p>

<p>For more information about driver-defined interfaces, see <a href="wdf.using_driver_defined_interfaces">Using Driver-Defined Interfaces</a>.</p>

<p>The following code example is from the <a href="wdf.sample_kmdf_drivers">Toaster</a> sample bus driver. This example creates a driver-defined interface that uses the toaster sample's TOASTER_INTERFACE_STANDARD structure.</p>

<p>Drivers that create driver-defined interfaces typically call <b>WdfDeviceAddQueryInterface</b> from within an <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> or <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> callback function.</p>

<p>After a driver calls <b>WdfDeviceAddQueryInterface</b> to create a driver-defined interface, another framework-based driver can access the interface by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547289">WdfFdoQueryForInterface</a>.</p>

<p>For more information about driver-defined interfaces, see <a href="wdf.using_driver_defined_interfaces">Using Driver-Defined Interfaces</a>.</p>

<p>The following code example is from the <a href="wdf.sample_kmdf_drivers">Toaster</a> sample bus driver. This example creates a driver-defined interface that uses the toaster sample's TOASTER_INTERFACE_STANDARD structure.</p>

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
<dt>Wdfqueryinterface.h (include Wdf.h)</dt>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552443">WDF_QUERY_INTERFACE_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546796">WdfDeviceInterfaceReferenceNoOp</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546790">WdfDeviceInterfaceDereferenceNoOp</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a>
</dt>
<dt>
<a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552439">WDF_QUERY_INTERFACE_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547289">WdfFdoQueryForInterface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceAddQueryInterface method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
