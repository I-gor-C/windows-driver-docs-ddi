---
UID: NF.ntddk.IoVolumeDeviceToDosName
title: IoVolumeDeviceToDosName function
author: windows-driver-content
description: The IoVolumeDeviceToDosName routine returns the MS-DOS path for a specified device object that represents a file system volume.
old-location: kernel\iovolumedevicetodosname.htm
old-project: kernel
ms.assetid: f860d0ad-f971-4ba7-93fb-20fe8831fc90
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: IoVolumeDeviceToDosName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows XP. Drivers that must work in earlier versions of Windows NT-based operating systems can use RtlVolumeDeviceToDosName, which behaves identically.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoVolumeDeviceToDosName
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
req.irql: PASSIVE_LEVEL
---

# IoVolumeDeviceToDosName function



## -description
The <b>IoVolumeDeviceToDosName</b> routine returns the MS-DOS path for a specified device object that represents a file system volume.


## -syntax

````
NTSTATUS IoVolumeDeviceToDosName(
  _In_  PVOID           VolumeDeviceObject,
  _Out_ PUNICODE_STRING DosName
);
````


## -parameters

### -param VolumeDeviceObject [in]

A pointer to a device object that represents a volume device object created by a storage class driver.

### -param DosName [out]

A pointer to a caller-allocated <a href="kernel.unicode_string">UNICODE_STRING</a> structure. If the call is successful, <b>IoVolumeDeviceToDosName</b> sets the values of the <b>Length</b>, <b>MaximumLength</b>, and <b>Buffer</b> members of this structure. On exit, the <b>Buffer</b> member points to a wide-character, null-terminated string that contains the MS-DOS path of the volume device object specified by <i>VolumeDeviceObject</i>. For more information, see Remarks.

## -returns
<b>IoVolumeDeviceToDosName</b> returns STATUS_SUCCESS if the call is successful. Possible error return values include the following status codes.
<dl>
<dt>STATUS_INVALID_PARAMETER</dt>
</dl>The routine failed due to invalid parameter values passed by the caller.
<dl>
<dt>STATUS_INSUFFICIENT_RESOURCES</dt>
</dl>The routine failed to allocate resources required for this operation.

 

## -remarks
<b>IoVolumeDeviceToDosName</b> allocates the string buffer pointed to by the <b>Buffer</b> member of the <a href="kernel.unicode_string">UNICODE_STRING</a> structure that the <i>DosName</i> parameter points to. After this buffer is no longer required, a caller of this routine should call the <a href="kernel.exfreepool">ExFreePool</a> routine to free the buffer.

Starting with Windows Vista, you must ensure that APCs are <u>not</u> disabled before calling this routine. The <a href="kernel.keareallapcsdisabled">KeAreAllApcsDisabled</a> routine can be used to verify that APCs are not disabled.

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
Available starting with Windows XP. Drivers that must work in earlier versions of Windows NT-based operating systems can use <a href="kernel.rtlvolumedevicetodosname">RtlVolumeDeviceToDosName</a>, which behaves identically.
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
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exfreepool">ExFreePool</a>
</dt>
<dt>
<a href="kernel.keareallapcsdisabled">KeAreAllApcsDisabled</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoVolumeDeviceToDosName routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
