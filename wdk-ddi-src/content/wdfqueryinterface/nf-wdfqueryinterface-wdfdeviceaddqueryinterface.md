---
UID: NF.wdfqueryinterface.WdfDeviceAddQueryInterface
title: WdfDeviceAddQueryInterface function
author: windows-driver-content
description: The WdfDeviceAddQueryInterface method creates a driver-defined interface that other drivers can query and use.
old-location: wdf\wdfdeviceaddqueryinterface.htm
old-project: wdf
ms.assetid: 6e811b5e-bd2a-473b-8e5c-52bfbd9b8f7c
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.product: Windows 10 or later.
---

# WdfDeviceAddQueryInterface function



## -description
<p class="CCE_Message">[Applies to KMDF only]
The <b>WdfDeviceAddQueryInterface</b> method creates a driver-defined interface that other drivers can query and use.


## -syntax

````
NTSTATUS WdfDeviceAddQueryInterface(
  _In_ WDFDEVICE                   Device,
  _In_ PWDF_QUERY_INTERFACE_CONFIG InterfaceConfig
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.

### -param InterfaceConfig [in]

A pointer to a driver-allocated <a href="wdf.wdf_query_interface_config">WDF_QUERY_INTERFACE_CONFIG</a> structure that describes the interface.

## -returns
<b>WdfDeviceAddQueryInterface</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:
<dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl>The method was called at the wrong IRQL.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An input parameter (possibly including members of the WDF_QUERY_INTERFACE_CONFIG structure) was invalid.
<dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl>The size of the WDF_QUERY_INTERFACE_CONFIG structure was incorrect.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>There was insufficient memory.

 

For a list of additional return values, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.



This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.



A system bug check occurs if the driver supplies an invalid object handle.



## -remarks
Drivers that create driver-defined interfaces typically call <b>WdfDeviceAddQueryInterface</b> from within an <a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a> or <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_prepare_hardware.md">EvtDevicePrepareHardware</a> callback function.

After a driver calls <b>WdfDeviceAddQueryInterface</b> to create a driver-defined interface, another framework-based driver can access the interface by calling <a href="wdf.wdffdoqueryforinterface">WdfFdoQueryForInterface</a>.

For more information about driver-defined interfaces, see <a href="wdf.using_driver_defined_interfaces">Using Driver-Defined Interfaces</a>.

The following code example is from the <a href="wdf.sample_kmdf_drivers">Toaster</a> sample bus driver. This example creates a driver-defined interface that uses the toaster sample's TOASTER_INTERFACE_STANDARD structure.

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
<dt>Wdfqueryinterface.h (include Wdf.h)</dt>
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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_query_interface_config_init">WDF_QUERY_INTERFACE_CONFIG_INIT</a>
</dt>
<dt>
<a href="wdf.wdfdeviceinterfacereferencenoop">WdfDeviceInterfaceReferenceNoOp</a>
</dt>
<dt>
<a href="wdf.wdfdeviceinterfacedereferencenoop">WdfDeviceInterfaceDereferenceNoOp</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_prepare_hardware.md">EvtDevicePrepareHardware</a>
</dt>
<dt>
<a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="wdf.wdf_query_interface_config">WDF_QUERY_INTERFACE_CONFIG</a>
</dt>
<dt>
<a href="wdf.wdffdoqueryforinterface">WdfFdoQueryForInterface</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceAddQueryInterface method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
