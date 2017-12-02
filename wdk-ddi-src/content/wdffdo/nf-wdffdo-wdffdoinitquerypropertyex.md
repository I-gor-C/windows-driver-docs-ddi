---
UID: NF.wdffdo.WdfFdoInitQueryPropertyEx
title: WdfFdoInitQueryPropertyEx
author: windows-driver-content
description: The WdfFdoInitQueryPropertyEx method retrieves a specified device property.
old-location: wdf\wdffdoinitquerypropertyex.htm
old-project: wdf
ms.assetid: C8377EE4-A7A1-4063-A7DC-53D0D8C6E0C3
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfFdoInitQueryPropertyEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdffdo.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.13
req.umdf-ver: 2.0
req.alt-api: WdfFdoInitQueryPropertyEx
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: 
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

# WdfFdoInitQueryPropertyEx function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfFdoInitQueryPropertyEx</b> method retrieves a specified device property.</p>


## -syntax

````
NTSTATUS WdfFdoInitQueryPropertyEx(
  _In_  PWDFDEVICE_INIT           DeviceInit,
  _In_  PWDF_DEVICE_PROPERTY_DATA DeviceProperty,
  _In_  ULONG                     BufferLength,
  _Out_ PVOID                     PropertyBuffer,
  _Out_ PULONG                    ResultLength,
  _Out_ PDEVPROPTYPE              Type
);
````


## -parameters
<dl>

### -param DeviceInit [in]

<dd>
<p>A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure that the driver obtained from its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function.</p>
</dd>

### -param DeviceProperty [in]

<dd>
<p>A pointer to a <a href="..\wdfdevice\ns-wdfdevice--wdf-device-property-data.md">WDF_DEVICE_PROPERTY_DATA</a> structure that identifies the device property to be retrieved.</p>
</dd>

### -param BufferLength [in]

<dd>
<p>The size, in bytes, of the buffer that is pointed to by <i>PropertyBuffer</i>.</p>
</dd>

### -param PropertyBuffer [out]

<dd>
<p>A caller-supplied pointer to a caller-allocated buffer that receives the requested information. The pointer can be <b>NULL</b> if the <i>BufferLength</i> parameter is zero.</p>
</dd>

### -param ResultLength [out]

<dd>
<p>A caller-supplied location that, on return, contains the 
                  size, in bytes, of the information that the method stored in 
                  <i>PropertyBuffer</i>. If the function's return value is 
                  <b>STATUS_BUFFER_TOO_SMALL</b>, this location receives the required 
                  buffer size.</p>
</dd>

### -param Type [out]

<dd>
<p>A pointer to a <b>DEVPROPTYPE</b> variable that, on return, contains the property type value
                  of the property 
                  data stored in <i>PropertyBuffer</i>.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, <b>WdfFdoInitQueryPropertyEx</b> returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The supplied buffer is too small to receive the information.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The specified <i>DeviceProperty</i> value is invalid.</p>

<p> </p>

<p>The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>Before receiving device property data, drivers typically call the <b>WdfFdoInitQueryPropertyEx</b> method just to obtain the required buffer size. For some properties, the data size can change between when the required size is returned and when the driver calls <b>WdfFdoInitQueryPropertyEx</b> again. Therefore, drivers should call <b>WdfFdoInitQueryPropertyEx</b> inside a loop that executes until the return status is not STATUS_BUFFER_TOO_SMALL. </p>

<p>It is best to use <b>WdfFdoInitQueryPropertyEx</b> only if the required buffer size is known and unchanging, because in that case the driver has to call <b>WdfFdoInitQueryPropertyEx</b> only once. If the required buffer size is unknown or varies, the driver should call <a href="..\wdffdo\nf-wdffdo-wdffdoinitallocandquerypropertyex.md">WdfFdoInitAllocAndQueryPropertyEx</a>. </p>

<p>The driver can call <b>WdfFdoInitQueryPropertyEx</b> only before calling <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>. For more information about calling <b>WdfDeviceCreate</b>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>After calling <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>, a driver can obtain device property information by calling <a href="..\wdfdevice\nf-wdfdevice-wdfdevicequerypropertyex.md">WdfDeviceQueryPropertyEx</a>.</p>

<p>For information about related methods, see <a href="wdf.accessing_the_unified_device_property_model">Accessing the Unified Device Property Model</a>.</p>

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
<p>1.13</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\wdffdo\nf-wdffdo-wdffdoinitqueryproperty.md">WdfFdoInitQueryProperty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfFdoInitQueryPropertyEx method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
