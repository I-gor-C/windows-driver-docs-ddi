---
UID: NF.aux_klib.AuxKlibQueryModuleInformation
title: AuxKlibQueryModuleInformation
author: windows-driver-content
description: The AuxKlibQueryModuleInformation routine retrieves information about the image modules that the operating system has loaded.
old-location: kernel\auxklibquerymoduleinformation.htm
old-project: kernel
ms.assetid: 5e267d53-4e92-4c94-8a59-93d3c79574dd
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: AuxKlibQueryModuleInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: aux_klib.h
req.include-header: Aux_klib.h
req.target-type: Universal
req.target-min-winverclnt: Supported starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AuxKlibQueryModuleInformation
req.alt-loc: Aux_Klib.lib,Aux_Klib.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Aux_Klib.lib
req.dll: 
req.irql: 
req.iface: 
---

# AuxKlibQueryModuleInformation function



## -description
<p>The <b>AuxKlibQueryModuleInformation</b> routine retrieves information about the image modules that the operating system has loaded.</p>


## -syntax

````
NTSTATUS AuxKlibQueryModuleInformation(
  _Inout_   PULONG BufferSize,
  _In_      ULONG  ElementSize,
  _Out_opt_ PVOID  QueryInfo
);
````


## -parameters
<dl>

### -param <i>BufferSize</i> [in, out]

<dd>
<p>A pointer to a location that contains or receives a buffer size, in bytes. If <i>QueryInfo</i> is <b>NULL</b>, the location receives the number of bytes that the driver must allocate for the array that receives the retrieved information. If <i>QueryInfo</i> is not <b>NULL</b>, the location must contain the specified number of bytes. </p>
</dd>

### -param <i>ElementSize</i> [in]

<dd>
<p>The size, in bytes, of each element of the array that <i>QueryInfo</i> points to. This value must be <b>sizeof</b>(<b>AUX_MODULE_BASIC_INFO</b>) or <b>sizeof</b>(<b>AUX_MODULE_EXTENDED_INFO</b>).</p>
</dd>

### -param <i>QueryInfo</i> [out, optional]

<dd>
<p>A pointer to an array of <a href="..\aux_klib\ns-aux-klib--aux-module-basic-info.md">AUX_MODULE_BASIC_INFO</a> or <a href="..\aux_klib\ns-aux-klib--aux-module-extended-info.md">AUX_MODULE_EXTENDED_INFO</a> structures that receives information about loaded image modules. If this pointer is <b>NULL</b>, <b>AuxKlibQueryModuleInformation</b> writes the required buffer size to the location that <i>BufferSize</i> points to.</p>
</dd>
</dl>

## -returns
<p><b>AuxKlibQueryModuleInformation</b> returns STATUS_SUCCESS if the operation succeeds. <b>AuxKlibQueryModuleInformation</b> returns STATUS_BUFFER_TOO_SMALL if the <i>QueryInfo</i> pointer is not <b>NULL</b> and the driver-supplied <i>BufferSize</i> value is too small.</p>

<p>The routine might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>To obtain information about the operating system's loaded image modules, a driver must:</p>

<p>Call <b>AuxKlibQueryModuleInformation</b> with a <b>NULL</b> <i>QueryInfo</i> pointer. After <b>AuxKlibQueryModuleInformation</b> returns, the location that the <i>BufferSize</i> parameter points to will contain the number of bytes that the driver will have to allocate for the array.</p>

<p>Call a memory allocation routine, such as <a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>, to allocate a buffer for the array. </p>

<p>Call <b>AuxKlibQueryModuleInformation</b> again. This time, the <i>QueryInfo</i> pointer must contain the address of the allocated buffer. After <b>AuxKlibQueryModuleInformation</b> returns, the buffer contains an array of module information. </p>

<p>The number of loaded modules can change between the first and second calls to <b>AuxKlibQueryModuleInformation</b>. As a result, the second call to <b>AuxKlibQueryModuleInformation</b> might return STATUS_BUFFER_TOO_SMALL even if the driver allocates a buffer that is based on the size that was obtained from the first call.</p>

<p>If a call to <b>AuxKlibQueryModuleInformation</b> succeeds, the routine writes an <b>ImageBase</b> value to each element in the <i>QueryInfo</i> array. Each <b>ImageBase</b> value is a pointer to the base of a loaded driver image. This pointer remains valid only while the driver remains loaded. The caller should assume that the driver can be unloaded at any time unless the caller can guarantee otherwise. For example, a driver might be unloaded between a call to <b>AuxKlibQueryModuleInformation</b> that obtains a pointer to the driver image and a call to <a href="..\aux_klib\nf-aux-klib-auxklibgetimageexportdirectory.md">AuxKlibGetImageExportDirectory</a> that uses this pointer.</p>

<p>Drivers must call <a href="..\aux_klib\nf-aux-klib-auxklibinitialize.md">AuxKlibInitialize</a> before calling <b>AuxKlibQueryModuleInformation</b>.</p>

<p>The following code example illustrates the steps that are listed in the preceding Remarks section.</p>

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
<p>Supported starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Aux_klib.h (include Aux_klib.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Aux_Klib.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\aux_klib\ns-aux-klib--aux-module-basic-info.md">AUX_MODULE_BASIC_INFO</a>
</dt>
<dt>
<a href="..\aux_klib\ns-aux-klib--aux-module-extended-info.md">AUX_MODULE_EXTENDED_INFO</a>
</dt>
<dt>
<a href="..\aux_klib\nf-aux-klib-auxklibgetimageexportdirectory.md">AuxKlibGetImageExportDirectory</a>
</dt>
<dt>
<a href="..\aux_klib\nf-aux-klib-auxklibinitialize.md">AuxKlibInitialize</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20AuxKlibQueryModuleInformation routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
