---
UID: NF.wdffdo.WdfFdoInitAllocAndQueryProperty
title: WdfFdoInitAllocAndQueryProperty
author: windows-driver-content
description: The WdfFdoInitAllocAndQueryProperty method allocates a buffer and retrieves a specified device property.
old-location: wdf\wdffdoinitallocandqueryproperty.htm
old-project: wdf
ms.assetid: 9c275d89-e01d-445b-8c60-ae5268cd28c3
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfFdoInitAllocAndQueryProperty
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdffdo.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfFdoInitAllocAndQueryProperty
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DeviceInitAPI, DriverCreate, KmdfIrql, KmdfIrql2
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfFdoInitAllocAndQueryProperty function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfFdoInitAllocAndQueryProperty</b> method allocates a buffer and retrieves a specified device property.</p>


## -syntax

````
NTSTATUS WdfFdoInitAllocAndQueryProperty(
  _In_     PWDFDEVICE_INIT          DeviceInit,
  _In_     DEVICE_REGISTRY_PROPERTY DeviceProperty,
  _In_     POOL_TYPE                PoolType,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES   PropertyMemoryAttributes,
  _Out_    WDFMEMORY                *PropertyMemory
);
````


## -parameters
<dl>

### -param <i>DeviceInit</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a> structure that the driver obtained from its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function.</p>
</dd>

### -param <i>DeviceProperty</i> [in]

<dd>
<p>A <a href="kernel.device_registry_property">DEVICE_REGISTRY_PROPERTY</a>-typed enumerator value that identifies the device property to be retrieved.</p>
</dd>

### -param <i>PoolType</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a>-typed enumerator value that specifies the type of memory to be allocated.</p>
</dd>

### -param <i>PropertyMemoryAttributes</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure that describes object attributes for the memory object that <b>WdfFdoInitAllocAndQueryProperty</b> will allocate. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>PropertyMemory</i> [out]

<dd>
<p>A pointer to a WDFMEMORY-typed location that receives a handle to a framework memory object. </p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER or STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The specified <i>DeviceProperty</i> value is invalid.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a> structure was not obtained from driver's <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function.</p>

<p> </p>

<p>The method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>The driver must call <b>WdfFdoInitAllocAndQueryProperty</b> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>. For more information about calling <b>WdfDeviceCreate</b>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>After calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>, a driver can obtain device property information by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545882">WdfDeviceAllocAndQueryProperty</a>.</p>

<p>For more information about the <b>WdfFdoInitAllocAndQueryProperty</b> method, see <a href="wdf.creating_device_objects_in_a_function_driver">Creating Device Objects in a Function Driver</a>.</p>

<p>Alternatively, you can use <a href="https://msdn.microsoft.com/library/windows/hardware/dn265612">WdfFdoInitAllocAndQueryPropertyEx</a> to access device properties that are exposed through the Unified Property Model.</p>

<p>The following code example calls <b>WdfFdoInitAllocAndQueryProperty</b> to obtain a handle to a framework memory object that contains the name of a device's setup class. Then, the example calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548715">WdfMemoryGetBuffer</a> to obtain a pointer to the buffer that contains the setup class name's Unicode string.</p>

<p>The driver must call <b>WdfFdoInitAllocAndQueryProperty</b> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>. For more information about calling <b>WdfDeviceCreate</b>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>After calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>, a driver can obtain device property information by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545882">WdfDeviceAllocAndQueryProperty</a>.</p>

<p>For more information about the <b>WdfFdoInitAllocAndQueryProperty</b> method, see <a href="wdf.creating_device_objects_in_a_function_driver">Creating Device Objects in a Function Driver</a>.</p>

<p>Alternatively, you can use <a href="https://msdn.microsoft.com/library/windows/hardware/dn265612">WdfFdoInitAllocAndQueryPropertyEx</a> to access device properties that are exposed through the Unified Property Model.</p>

<p>The following code example calls <b>WdfFdoInitAllocAndQueryProperty</b> to obtain a handle to a framework memory object that contains the name of a device's setup class. Then, the example calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548715">WdfMemoryGetBuffer</a> to obtain a pointer to the buffer that contains the setup class name's Unicode string.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544843">DeviceInitAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfFdoInitAllocAndQueryProperty method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
