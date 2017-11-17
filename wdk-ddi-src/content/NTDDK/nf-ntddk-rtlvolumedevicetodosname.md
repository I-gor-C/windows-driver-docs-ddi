---
UID: NF.ntddk.RtlVolumeDeviceToDosName
title: RtlVolumeDeviceToDosName
author: windows-driver-content
description: The RtlVolumeDeviceToDosName routine is obsolete for Windows XP and later versions of Windows. Use IoVolumeDeviceToDosName instead.RtlVolumeDeviceToDosName returns the MS-DOS path for a specified device object that represents a file system volume.
old-location: kernel\rtlvolumedevicetodosname.htm
ms.assetid: e25db70f-04bf-4fb1-8ff5-2beb4c825797
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Obsolete for Microsoft Windows XP and later versions of Windows. Use IoVolumeDeviceToDosName instead.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlVolumeDeviceToDosName
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: 
ms.keywords: RtlVolumeDeviceToDosName
req.iface: 
---

# RtlVolumeDeviceToDosName function



## -description
<p>The <b>RtlVolumeDeviceToDosName</b> routine is <u>obsolete</u> for Windows XP and later versions of Windows. Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff550422">IoVolumeDeviceToDosName</a> instead.</p>
<p><b>RtlVolumeDeviceToDosName</b> returns the MS-DOS path for a specified device object that represents a file system volume.</p>


## -syntax

````
NTSTATUS RtlVolumeDeviceToDosName(
  _In_  PVOID           VolumeDeviceObject,
  _Out_ PUNICODE_STRING DosName
);
````


## -parameters
<dl>

### -param <i>VolumeDeviceObject</i> [in]

<dd>
<p>Pointer to a device object that represents a volume device object created by a storage class driver.</p>
</dd>

### -param <i>DosName</i> [out]

<dd>
<p>Pointer to a Unicode string containing the MS-DOS path of the volume device object specified by <i>VolumeDeviceObject</i>. </p>
</dd>
</dl>

## -returns
<p><b>RtlVolumeDeviceToDosName</b> returns STATUS_SUCCESS or an appropriate error status.</p>

## -remarks
<p>The behavior of this routine is identical to that of <a href="https://msdn.microsoft.com/library/windows/hardware/ff550422">IoVolumeDeviceToDosName</a>. For more information about how to use this routine, see <b>IoVolumeDeviceToDosName</b>.</p>

<p>Drivers that must work on older NT-based operating systems may use this routine. Drivers written for Windows XP and later must use <b>IoVolumeDeviceToDosName</b> instead.</p>

<p>The behavior of this routine is identical to that of <a href="https://msdn.microsoft.com/library/windows/hardware/ff550422">IoVolumeDeviceToDosName</a>. For more information about how to use this routine, see <b>IoVolumeDeviceToDosName</b>.</p>

<p>Drivers that must work on older NT-based operating systems may use this routine. Drivers written for Windows XP and later must use <b>IoVolumeDeviceToDosName</b> instead.</p>

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
<p>Obsolete for Microsoft Windows XP and later versions of Windows. Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff550422">IoVolumeDeviceToDosName</a> instead.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
</table>