---
UID: NF.fltkernel.FltEnumerateInstanceInformationByDeviceObject
title: FltEnumerateInstanceInformationByDeviceObject
author: windows-driver-content
description: The FltEnumerateInstanceInformationByDeviceObject routine provides information about minifilter driver instances and legacy filter drivers that are attached to the volume related to a specified device object.
old-location: ifsk\fltenumerateinstanceinformationbydeviceobject.htm
ms.assetid: 3E7754A3-3A7A-4036-B524-CBA40EF22048
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltEnumerateInstanceInformationByDeviceObject
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: FltEnumerateInstanceInformationByDeviceObject
req.iface: 
---

# FltEnumerateInstanceInformationByDeviceObject function



## -description
<p>The <b>FltEnumerateInstanceInformationByDeviceObject</b> routine provides information about minifilter driver instances and legacy filter drivers that are attached to the volume related to a specified device object.</p>


## -syntax

````
NTSTATUS FltEnumerateInstanceInformationByDeviceObject(
  _In_  PDEVICE_OBJECT             DeviceObject,
  _In_  ULONG                      Index,
  _In_  INSTANCE_INFORMATION_CLASS InformationClass,
  _Out_ PVOID                      Buffer,
  _In_  ULONG                      BufferSize,
  _Out_ PULONG                     BytesReturned
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>The device object for the related file object or volume.</p>
</dd>

### -param <i>Index</i> [in]

<dd>
<p>Zero-based index of the minifilter driver instance or legacy filter driver for which the information is requested.</p>
</dd>

### -param <i>InformationClass</i> [in]

<dd>
<p>Type of information to be returned for the minifilter driver instance or legacy filter driver. This parameter can have one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>InstanceBasicInformation</b></p>
</td>
<td>
<p>The buffer pointed to by the <i>Buffer</i> parameter receives an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548176">INSTANCE_BASIC_INFORMATION</a> structure for a minifilter instance.  Legacy filter drivers are ignored.</p>
</td>
</tr>
<tr>
<td>
<p><b>InstanceFullInformation</b></p>
</td>
<td>
<p>The buffer pointed to by the <i>Buffer</i> parameter receives an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548185">INSTANCE_FULL_INFORMATION</a> structure for a minifilter instance.  Legacy filter drivers are ignored.</p>
</td>
</tr>
<tr>
<td>
<p><b>InstancePartialInformation</b></p>
</td>
<td>
<p>The buffer pointed to by the <i>Buffer</i> parameter receives an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548190">INSTANCE_PARTIAL_INFORMATION</a> structure for a minifilter instance.  Legacy filter drivers are ignored.</p>
</td>
</tr>
<tr>
<td>
<p><b>InstanceAggregateStandardInformation</b></p>
</td>
<td>
<p>The buffer pointed to by the <i>Buffer</i> parameter receives an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548172">INSTANCE_AGGREGATE_STANDARD_INFORMATION</a> structure for a minifilter driver instance or legacy filter driver.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer that receives the requested information. The type of the information returned in the buffer is defined by the <i>InformationClass</i> parameter.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Size, in bytes, of the buffer that the <i>Buffer</i> parameter points to. The caller should set this parameter according to the given <i>InformationClass</i> value.</p>
</dd>

### -param <i>BytesReturned</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives the number of bytes returned in the buffer that <i>Buffer </i>points to. If the input value of <i>BufferSize</i> is too small, <b>FltEnumerateInstanceInformationByDeviceObject</b> returns <b>STATUS_BUFFER_TOO_SMALL</b> and sets this variable to the number of bytes required to store the requested information. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>FltEnumerateInstanceInformationByDeviceObject</b> returns <b>STATUS_SUCCESS</b> or an appropriate <b>NTSTATUS</b> value, such as one of the following: </p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer that the <i>Buffer</i> parameter points to is not large enough to store the requested information. </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>A matching minifilter instance was found, but it is being torn down.  Note that this return value does not apply to legacy filter drivers because legacy filter drivers cannot be unloaded.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid value was specified for the <i>InformationClass</i> parameter.</p><dl>
<dt><b>STATUS_NO_MORE_ENTRIES</b></dt>
</dl><p>There are no more entries in the volume's instance/filter list.</p><dl>
<dt><b>STATUS_FLT_VOLUME_NOT_FOUND</b></dt>
</dl><p>No related volume was found for <i>DeviceObject</i>.</p><dl>
<dt><b>STATUS_FLT_INTERNAL_ERROR</b></dt>
</dl><p><i>DeviceObject</i>  is not a valid volume device object.</p>

<p>-or-</p>

<p>The volume related to <i>DeviceObject</i> was registered but   does not have any filter instances attached.</p>

<p> </p>

## -remarks
<p>Using the <i>Index</i> parameter is simply a way for <b>FltEnumerateInstanceInformationByDeviceObject</b> to select among minifilter driver instances and legacy filter drivers in the instance/filter list for the volume that is related to <i>DeviceObject</i>. Because the minifilter driver instances in the instance/filter list can change at any time, two calls to <b>FltEnumerateInstanceInformationByDeviceObject</b> with the same <i>Index</i> and <i>DeviceObject</i> values are not guaranteed to return the same result.</p>

<p>This routine will return both legacy filter driver information and minifilter driver instance information when the value of the <i>InformationClass</i> parameter is <b>InstanceAggregateStandardInformation</b>.</p>

<p>Using the <i>Index</i> parameter is simply a way for <b>FltEnumerateInstanceInformationByDeviceObject</b> to select among minifilter driver instances and legacy filter drivers in the instance/filter list for the volume that is related to <i>DeviceObject</i>. Because the minifilter driver instances in the instance/filter list can change at any time, two calls to <b>FltEnumerateInstanceInformationByDeviceObject</b> with the same <i>Index</i> and <i>DeviceObject</i> values are not guaranteed to return the same result.</p>

<p>This routine will return both legacy filter driver information and minifilter driver instance information when the value of the <i>InformationClass</i> parameter is <b>InstanceAggregateStandardInformation</b>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542071">FltEnumerateInstanceInformationByFilter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542082">FltEnumerateInstanceInformationByVolume</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967697">FltEnumerateInstanceInformationByVolumeName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltEnumerateInstanceInformationByDeviceObject routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
