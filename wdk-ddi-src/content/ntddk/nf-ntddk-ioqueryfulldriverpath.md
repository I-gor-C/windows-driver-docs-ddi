---
UID: NF.ntddk.IoQueryFullDriverPath
title: IoQueryFullDriverPath
author: windows-driver-content
description: The IoQueryFullDriverPath routine retrieves the full path name of the binary file that is loaded for the specified driver object.
old-location: kernel\ioqueryfulldriverpath.htm
old-project: kernel
ms.assetid: 2F73ECD7-EC58-43A9-89F8-E0268510A498
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoQueryFullDriverPath
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoQueryFullDriverPath
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
req.irql: <= APC_LEVEL
req.iface: 
---

# IoQueryFullDriverPath function



## -description
<p>The <b>IoQueryFullDriverPath</b> routine retrieves the full path name of the binary file that is loaded for the specified driver object.</p>


## -syntax

````
NTSTATUS IoQueryFullDriverPath(
  _In_  PDRIVER_OBJECT  DriverObject,
  _Out_ PUNICODE_STRING FullPath
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a> structure. This structure must be the driver object for the calling driver.</p>
</dd>

### -param <i>FullPath</i> [out]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure. On successful return, this structure contains the path name.</p>
</dd>
</dl>

## -returns
<p><b>IoQueryFullDriverPath</b> returns STATUS_SUCCESS if the call successfully fetches the path name. Possible error return values include the following status codes.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The target driver object does not belong to the caller.</p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>The driver object has no section (loaded memory image) associated with it.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Insufficient resources are available to perform the requested operation.</p>

<p> </p>

## -remarks
<p>A driver can call this routine to query for the full path name of its binary file, but not for the full path name of the binary file for another driver. If the driver object pointed to by the <i>DriverObject</i> parameter does not belong to the calling driver, the call fails and the routine returns an error code.</p>

<p>The caller allocates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure pointed to by the <i>FullPath</i> parameter, but does not need to initialize this structure. <b>IoQueryFullDriverPath</b> assumes that the original contents of this structure are invalid and overwrites them. This routine allocates a string buffer from paged system memory, sets the <b>Buffer</b> member of the structure to point to this buffer, and sets the <b>MaximumLength</b> and <b>Buffer</b> members to describe the buffer and its contents.</p>

<p>The caller is responsible for freeing the storage pointed to by <i>FullPath</i>-&gt;<b>Buffer</b> when the full path string is no longer needed. Typically, the caller frees this storage by calling a routine such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>.</p>

<p>A driver can call this routine to query for the full path name of its binary file, but not for the full path name of the binary file for another driver. If the driver object pointed to by the <i>DriverObject</i> parameter does not belong to the calling driver, the call fails and the routine returns an error code.</p>

<p>The caller allocates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure pointed to by the <i>FullPath</i> parameter, but does not need to initialize this structure. <b>IoQueryFullDriverPath</b> assumes that the original contents of this structure are invalid and overwrites them. This routine allocates a string buffer from paged system memory, sets the <b>Buffer</b> member of the structure to point to this buffer, and sets the <b>MaximumLength</b> and <b>Buffer</b> members to describe the buffer and its contents.</p>

<p>The caller is responsible for freeing the storage pointed to by <i>FullPath</i>-&gt;<b>Buffer</b> when the full path string is no longer needed. Typically, the caller frees this storage by calling a routine such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>.</p>

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
<p>Available starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoQueryFullDriverPath routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
