---
UID: NF.ntddk.RtlVolumeDeviceToDosName
title: RtlVolumeDeviceToDosName function
author: windows-driver-content
description: The RtlVolumeDeviceToDosName routine is obsolete for Windows XP and later versions of Windows. Use IoVolumeDeviceToDosName instead.RtlVolumeDeviceToDosName returns the MS-DOS path for a specified device object that represents a file system volume.
old-location: kernel\rtlvolumedevicetodosname.htm
old-project: kernel
ms.assetid: e25db70f-04bf-4fb1-8ff5-2beb4c825797
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: RtlVolumeDeviceToDosName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
---

# RtlVolumeDeviceToDosName function



## -description
The <b>RtlVolumeDeviceToDosName</b> routine is <u>obsolete</u> for Windows XP and later versions of Windows. Use <a href="kernel.iovolumedevicetodosname">IoVolumeDeviceToDosName</a> instead.

<b>RtlVolumeDeviceToDosName</b> returns the MS-DOS path for a specified device object that represents a file system volume.



## -syntax

````
NTSTATUS RtlVolumeDeviceToDosName(
  _In_  PVOID           VolumeDeviceObject,
  _Out_ PUNICODE_STRING DosName
);
````


## -parameters

### -param VolumeDeviceObject [in]

Pointer to a device object that represents a volume device object created by a storage class driver.


### -param DosName [out]

Pointer to a Unicode string containing the MS-DOS path of the volume device object specified by <i>VolumeDeviceObject</i>. 


## -returns
<b>RtlVolumeDeviceToDosName</b> returns STATUS_SUCCESS or an appropriate error status.


## -remarks
The behavior of this routine is identical to that of <a href="kernel.iovolumedevicetodosname">IoVolumeDeviceToDosName</a>. For more information about how to use this routine, see <b>IoVolumeDeviceToDosName</b>.

Drivers that must work on older NT-based operating systems may use this routine. Drivers written for Windows XP and later must use <b>IoVolumeDeviceToDosName</b> instead.


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
Version

</th>
<td width="70%">
Obsolete for Microsoft Windows XP and later versions of Windows. Use <a href="kernel.iovolumedevicetodosname">IoVolumeDeviceToDosName</a> instead.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
</table>