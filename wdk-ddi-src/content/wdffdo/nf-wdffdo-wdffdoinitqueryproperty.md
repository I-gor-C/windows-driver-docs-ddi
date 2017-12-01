---
UID: NF.wdffdo.WdfFdoInitQueryProperty
title: WdfFdoInitQueryProperty
author: windows-driver-content
description: The WdfFdoInitQueryProperty method retrieves a specified device property.
old-location: wdf\wdffdoinitqueryproperty.htm
old-project: wdf
ms.assetid: e58def50-3e35-43d9-9f7e-31283256b204
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfFdoInitQueryProperty
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
req.alt-api: WdfFdoInitQueryProperty
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DeviceInitAPI, DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfFdoInitQueryProperty function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfFdoInitQueryProperty</b> method retrieves a specified device property.</p>


## -syntax

````
NTSTATUS WdfFdoInitQueryProperty(
  _In_  PWDFDEVICE_INIT          DeviceInit,
  _In_  DEVICE_REGISTRY_PROPERTY DeviceProperty,
  _In_  ULONG                    BufferLength,
  _Out_ PVOID                    PropertyBuffer,
  _Out_ PULONG                   ResultLength
);
````


## -parameters
<dl>

### -param <i>DeviceInit</i> [in]

<dd>
<p>A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure that the driver obtained from its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function.</p>
</dd>

### -param <i>DeviceProperty</i> [in]

<dd>
<p>A <a href="kernel.device_registry_property">DEVICE_REGISTRY_PROPERTY</a>-typed enumerator value that identifies the device property to be retrieved.</p>
</dd>

### -param <i>BufferLength</i> [in]

<dd>
<p>The size, in bytes, of the buffer that is pointed to by <i>PropertyBuffer</i>.</p>
</dd>

### -param <i>PropertyBuffer</i> [out]

<dd>
<p>A caller-supplied pointer to a caller-allocated buffer that receives the requested device property. This pointer can be <b>NULL</b> if the <i>BufferLength</i> parameter is zero.</p>
</dd>

### -param <i>ResultLength</i> [out]

<dd>
<p>A caller-supplied location that, on return, contains the size, in bytes, of the information that <b>WdfFdoInitQueryProperty</b> stored in <i>PropertyBuffer</i>. If this method's return value is STATUS_BUFFER_TOO_SMALL, <i>ResultLength</i> receives the required buffer size.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The supplied buffer is too small to receive the information.
</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The specified <i>DeviceProperty</i> value is invalid.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure was not obtained from the driver's <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function.</p>

<p> </p>

<p>The method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>Before receiving device property data, drivers typically must make an initial call to <b>WdfFdoInitQueryProperty</b> to obtain the required buffer size. For some properties, the data size can change between the time that the required size is returned and the time that the driver calls this routine again. Therefore, drivers should call <b>WdfFdoInitQueryProperty</b> inside a loop that executes until the return status is not STATUS_BUFFER_TOO_SMALL. </p>

<p>It is best to use <b>WdfFdoInitQueryProperty</b> only if the required buffer size is known and unchanging, because in that case the driver has to call <b>WdfFdoInitQueryProperty</b> only once. If the required buffer size is unknown or varies, the driver should call <a href="..\wdffdo\nf-wdffdo-wdffdoinitallocandqueryproperty.md">WdfFdoInitAllocAndQueryProperty</a>. </p>

<p>The driver can call <b>WdfFdoInitQueryProperty</b> only before calling <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>. For more information about calling <b>WdfDeviceCreate</b>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>After calling <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>, a driver can obtain device property information by calling <a href="..\wdfdevice\nf-wdfdevice-wdfdevicequeryproperty.md">WdfDeviceQueryProperty</a>.</p>

<p>For more information about the <b>WdfFdoInitQueryProperty</b> method, see <a href="wdf.creating_device_objects_in_a_function_driver">Creating Device Objects in a Function Driver</a>.</p>

<p>Alternatively, you can use <a href="..\wdffdo\nf-wdffdo-wdffdoinitquerypropertyex.md">WdfFdoInitQueryPropertyEx</a> to access device properties that are exposed through the Unified Property Model.</p>

<p>The following code example obtains a Unicode string that represents the name of a device's enumerator and returns <b>TRUE</b> if the string is "PCI".</p>

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
<a href="devtest.kmdf_deviceinitapi">DeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdffdo\nf-wdffdo-wdffdoinitallocandqueryproperty.md">WdfFdoInitAllocAndQueryProperty</a>
</dt>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdfdevicequeryproperty.md">WdfDeviceQueryProperty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfFdoInitQueryProperty method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
