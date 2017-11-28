---
UID: NF.wdffdo.WdfFdoQueryForInterface
title: WdfFdoQueryForInterface
author: windows-driver-content
description: The WdfFdoQueryForInterface method obtains access to another driver's GUID-identified interface.
old-location: wdf\wdffdoqueryforinterface.htm
old-project: wdf
ms.assetid: 12bbc77b-c1cd-4899-aff2-e18e0d58b6b9
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfFdoQueryForInterface
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
req.alt-api: WdfFdoQueryForInterface
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

# WdfFdoQueryForInterface function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfFdoQueryForInterface</b> method obtains access to another driver's GUID-identified interface.</p>


## -syntax

````
NTSTATUS WdfFdoQueryForInterface(
  _In_     WDFDEVICE  Device,
  _In_     LPCGUID    InterfaceType,
  _Out_    PINTERFACE Interface,
  _In_     USHORT     Size,
  _In_     USHORT     Version,
  _In_opt_ PVOID      InterfaceSpecificData
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>InterfaceType</i> [in]

<dd>
<p>A pointer to a GUID that identifies the interface.</p>
</dd>

### -param <i>Interface</i> [out]

<dd>
<p>A pointer to a driver-allocated structure that receives the requested interface. This structure is defined by the driver that exports the requested interface and must begin with an <a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a> structure.</p>
</dd>

### -param <i>Size</i> [in]

<dd>
<p>The size, in bytes, of the driver-allocated structure that represents the requested interface.</p>
</dd>

### -param <i>Version</i> [in]

<dd>
<p>The version number of the requested interface. The format of this value is defined by the driver that exports the requested interface.</p>
</dd>

### -param <i>InterfaceSpecificData</i> [in, optional]

<dd>
<p>Additional interface-specific information. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The device object is invalid or if the <i>Device</i>, <i>InterfaceType</i>, or <i>Interface</i> parameter is <b>NULL</b>. 
</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The framework could not allocate a request to send to another driver. </p>

<p> </p>

<p>The method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A system bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>Your driver can call <b>WdfFdoQueryForInterface</b> to obtain access to a driver-defined interface that was created by a driver that is in the same driver stack that your driver is in. To access a driver-defined interface that was created by a driver that is in a different driver stack, your driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548640">WdfIoTargetQueryForInterface</a>.</p>

<p>Framework-based drivers define interfaces by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545870">WdfDeviceAddQueryInterface</a>. </p>

<p>For more information about <b>WdfFdoQueryForInterface</b>, see <a href="wdf.using_driver_defined_interfaces">Using Driver-Defined Interfaces</a>.</p>

<p>The following code example is from the <a href="wdf.sample_kmdf_drivers">Toaster</a> sample function driver. This example obtains access to an interface that the toaster sample bus driver defines.</p>

<p>Your driver can call <b>WdfFdoQueryForInterface</b> to obtain access to a driver-defined interface that was created by a driver that is in the same driver stack that your driver is in. To access a driver-defined interface that was created by a driver that is in a different driver stack, your driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548640">WdfIoTargetQueryForInterface</a>.</p>

<p>Framework-based drivers define interfaces by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545870">WdfDeviceAddQueryInterface</a>. </p>

<p>For more information about <b>WdfFdoQueryForInterface</b>, see <a href="wdf.using_driver_defined_interfaces">Using Driver-Defined Interfaces</a>.</p>

<p>The following code example is from the <a href="wdf.sample_kmdf_drivers">Toaster</a> sample function driver. This example obtains access to an interface that the toaster sample bus driver defines.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548640">WdfIoTargetQueryForInterface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfFdoQueryForInterface method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
