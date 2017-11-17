---
UID: NF.ntddk.MmCopyMemory
title: MmCopyMemory
author: windows-driver-content
description: The MmCopyMemory routine copies the specified range of virtual or physical memory into the caller-supplied buffer.
old-location: kernel\mmcopymemory.htm
ms.assetid: 2B5492CD-B24D-44B5-BDAE-0B43A1AF1FCA
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmCopyMemory
req.alt-loc: ntoskrnl.lib,ntoskrnl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: MmCopyMemory
req.iface: 
---

# MmCopyMemory function



## -description
<p>The <b>MmCopyMemory</b> routine copies the specified range of virtual or physical memory into the caller-supplied buffer.</p>


## -syntax

````
NTSTATUS MmCopyMemory(
  _In_  PVOID           TargetAddress,
  _In_  MM_COPY_ADDRESS SourceAddress,
  _In_  SIZE_T          NumberOfBytes,
  _In_  ULONG           Flags,
  _Out_ PSIZE_T         NumberOfBytesTransferred
);
````


## -parameters
<dl>

### -param <i>TargetAddress</i> [in]

<dd>
<p>A pointer to a caller-supplied buffer. This buffer must be in nonpageable  memory.</p>
</dd>

### -param <i>SourceAddress</i> [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/dn342885">MM_COPY_ADDRESS</a> structure, passed by value, that contains either the virtual address or the physical address of the data to be copied to the buffer pointed to by <i>TargetAddress</i>.</p>
</dd>

### -param <i>NumberOfBytes</i> [in]

<dd>
<p>The number of bytes to copy from <i>SourceAddress</i> to <i>TargetAddress</i>.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Flags that indicate whether <i>SourceAddress</i> is a virtual address or a physical address. The following flag bits are defined for this parameter.</p>
<table>
<tr>
<th>Flag bit</th>
<th>Description</th>
</tr>
<tr>
<td>MM_COPY_MEMORY_PHYSICAL</td>
<td><i>SourceAddress</i> specifies a physical address.</td>
</tr>
<tr>
<td>MM_COPY_MEMORY_VIRTUAL</td>
<td><i>SourceAddress</i> specifies a virtual address.</td>
</tr>
</table>
<p> </p>
<p>These two flag bits are mutually exclusive. The caller must set one or the other, but not both.</p>
</dd>

### -param <i>NumberOfBytesTransferred</i> [out]

<dd>
<p>A pointer to a location to which the routine writes the number of bytes successfully copied from the <i>SourceAddress</i> location to the buffer at <i>TargetAddress</i>.</p>
</dd>
</dl>

## -returns
<p><b>MmCopyMemory</b> returns STATUS_SUCCESS if the entire range has been copied successfully. Otherwise, an error status is returned and the caller must inspect the output value pointed to by the <i>NumberOfBytesTransferred</i> parameter to determine how many bytes were actually copied.</p>

## -remarks
<p>Kernel-mode drivers can call this routine to safely access arbitrary physical or virtual addresses.</p>

<p>If the MM_COPY_MEMORY_PHYSICAL flag is set, <i>SourceAddress</i> should point to regular memory that is under control of the operating system. <b>MmCopyMemory</b> will return an error status code for physical addresses that refer to I/O space, which includes memory-mapped devices and firmware tables. To access physical memory in I/O space, drivers can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554618">MmMapIoSpace</a> routine.</p>

<p>If the MM_COPY_MEMORY_VIRTUAL flag is set, <i>SourceAddress</i> can point to either a buffer in system address space, or a buffer in the user address space of the current process. If the caller does not control the lifetime of the allocation containing the specified source address, <b>MmCopyMemory</b> might fail or might return inconsistent data, but will not cause a system crash—even for system addresses that are invalid and would trigger a bug check if referenced directly. <b>MmCopyMemory</b> will return an error status code for system virtual addresses that refer to I/O space.</p>

<p>If memory at the virtual address specified by <i>SourceAddress</i> is not resident, <b>MmCopyMemory</b> will try to make it resident.</p>

<p>Kernel-mode drivers can call this routine to safely access arbitrary physical or virtual addresses.</p>

<p>If the MM_COPY_MEMORY_PHYSICAL flag is set, <i>SourceAddress</i> should point to regular memory that is under control of the operating system. <b>MmCopyMemory</b> will return an error status code for physical addresses that refer to I/O space, which includes memory-mapped devices and firmware tables. To access physical memory in I/O space, drivers can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554618">MmMapIoSpace</a> routine.</p>

<p>If the MM_COPY_MEMORY_VIRTUAL flag is set, <i>SourceAddress</i> can point to either a buffer in system address space, or a buffer in the user address space of the current process. If the caller does not control the lifetime of the allocation containing the specified source address, <b>MmCopyMemory</b> might fail or might return inconsistent data, but will not cause a system crash—even for system addresses that are invalid and would trigger a bug check if referenced directly. <b>MmCopyMemory</b> will return an error status code for system virtual addresses that refer to I/O space.</p>

<p>If memory at the virtual address specified by <i>SourceAddress</i> is not resident, <b>MmCopyMemory</b> will try to make it resident.</p>

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
<dt>Ntddk.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn342885">MM_COPY_ADDRESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554618">MmMapIoSpace</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmCopyMemory routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
