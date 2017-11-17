---
UID: NF.wdfdevice.WdfDeviceQueryProperty
title: WdfDeviceQueryProperty
author: windows-driver-content
description: The WdfDeviceQueryProperty method retrieves a specified device property.
old-location: wdf\wdfdevicequeryproperty.htm
ms.assetid: be05a5b5-e895-402b-bf0a-cbdb75fdef1d
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfDeviceQueryProperty
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: WdfDeviceQueryProperty
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceQueryProperty function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfDeviceQueryProperty</b> method retrieves a specified device property.</p>


## -syntax

````
NTSTATUS WdfDeviceQueryProperty(
  _In_  WDFDEVICE                Device,
  _In_  DEVICE_REGISTRY_PROPERTY DeviceProperty,
  _In_  ULONG                    BufferLength,
  _Out_ PVOID                    PropertyBuffer,
  _Out_ PULONG                   ResultLength
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>DeviceProperty</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/a17b4a88-45e8-45e7-b879-2f41b97be368">DEVICE_REGISTRY_PROPERTY</a>-typed enumerator that identifies the device property to be retrieved.</p>
</dd>

### -param <i>BufferLength</i> [in]

<dd>
<p>The size, in bytes, of the buffer that is pointed to by <i>PropertyBuffer</i>.</p>
</dd>

### -param <i>PropertyBuffer</i> [out]

<dd>
<p>A caller-supplied pointer to a caller-allocated buffer that receives the requested information. The pointer can be <b>NULL</b> if the <i>BufferLength</i> parameter is zero.</p>
</dd>

### -param <i>ResultLength</i> [out]

<dd>
<p>A caller-supplied location that, on return, contains the size, in bytes, of the information that the method stored in <i>PropertyBuffer</i>. If the function's return value is STATUS_BUFFER_TOO_SMALL, this location receives the required buffer size.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, <b>WdfDeviceQueryProperty</b> returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The supplied buffer is too small to receive the information.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The specified <i>DeviceProperty</i> value is invalid</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The device's drivers have not yet reported the device's properties.</p>

<p> </p>

<p>The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>Before receiving device property data, drivers typically call the <b>WdfDeviceQueryProperty</b> method just to obtain the required buffer size. For some properties, the data size can change between when the required size is returned and when the driver calls <b>WdfDeviceQueryProperty</b> again. Therefore, drivers should call <b>WdfDeviceQueryProperty</b> inside a loop that executes until the return status is not STATUS_BUFFER_TOO_SMALL. </p>

<p>It is best to use <b>WdfDeviceQueryProperty</b> only if the required buffer size is known and unchanging, because in that case the driver has to call <b>WdfDeviceQueryProperty</b> only once. If the required buffer size is unknown or varies, the driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545882">WdfDeviceAllocAndQueryProperty</a>. </p>

<p>Alternatively, you can use <a href="https://msdn.microsoft.com/library/windows/hardware/dn265608">WdfDeviceQueryPropertyEx</a> to access device properties that are exposed through the Unified Property Model.</p>

<p>The following code example obtains a device's <b>DevicePropertyBusTypeGuid</b> property. The example calls <b>WdfDeviceQueryProperty</b> instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff545882">WdfDeviceAllocAndQueryProperty</a> because the length of a GUID is known.</p>

<p>Before receiving device property data, drivers typically call the <b>WdfDeviceQueryProperty</b> method just to obtain the required buffer size. For some properties, the data size can change between when the required size is returned and when the driver calls <b>WdfDeviceQueryProperty</b> again. Therefore, drivers should call <b>WdfDeviceQueryProperty</b> inside a loop that executes until the return status is not STATUS_BUFFER_TOO_SMALL. </p>

<p>It is best to use <b>WdfDeviceQueryProperty</b> only if the required buffer size is known and unchanging, because in that case the driver has to call <b>WdfDeviceQueryProperty</b> only once. If the required buffer size is unknown or varies, the driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545882">WdfDeviceAllocAndQueryProperty</a>. </p>

<p>Alternatively, you can use <a href="https://msdn.microsoft.com/library/windows/hardware/dn265608">WdfDeviceQueryPropertyEx</a> to access device properties that are exposed through the Unified Property Model.</p>

<p>The following code example obtains a device's <b>DevicePropertyBusTypeGuid</b> property. The example calls <b>WdfDeviceQueryProperty</b> instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff545882">WdfDeviceAllocAndQueryProperty</a> because the length of a GUID is known.</p>

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
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
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
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545882">WdfDeviceAllocAndQueryProperty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547254">WdfFdoInitQueryProperty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceQueryProperty method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
