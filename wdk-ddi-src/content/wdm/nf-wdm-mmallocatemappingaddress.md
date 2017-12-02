---
UID: NF.wdm.MmAllocateMappingAddress
title: MmAllocateMappingAddress
author: windows-driver-content
description: The MmAllocateMappingAddress routine reserves a range of system virtual address space of the specified size.
old-location: kernel\mmallocatemappingaddress.htm
old-project: kernel
ms.assetid: e8d5fea6-d0fd-4dc4-b8ec-10c72381285b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: MmAllocateMappingAddress
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmAllocateMappingAddress
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
req.irql: <=APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# MmAllocateMappingAddress function



## -description
<p>The <b>MmAllocateMappingAddress</b> routine reserves a range of system virtual address space of the specified size.</p>


## -syntax

````
PVOID MmAllocateMappingAddress(
  _In_ SIZE_T NumberOfBytes,
  _In_ ULONG  PoolTag
);
````


## -parameters
<dl>

### -param NumberOfBytes [in]

<dd>
<p>Specifies the number of bytes to reserve. </p>
</dd>

### -param PoolTag [in]

<dd>
<p>Specifies a four-character tag used to identify the buffer. Use a distinct <i>PoolTag</i> tag for each allocation code path. For a description of pool tags, see <a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>. </p>
</dd>
</dl>

## -returns
<p><b>MmAllocateMappingAddress</b> returns a pointer to the beginning of the reserved memory buffer.</p>

## -remarks
<p><b>MmAllocateMappingAddress</b> reserves a system virtual address range for the caller to use. No physical memory is allocated for the virtual address range and the virtual memory cannot be accessed until it is mapped by the <a href="..\wdm\nf-wdm-mmmaplockedpageswithreservedmapping.md">MmMapLockedPagesWithReservedMapping</a> routine. The caller unmaps the reserved memory range by calling the <a href="..\wdm\nf-wdm-mmunmapreservedmapping.md">MmUnmapReservedMapping</a> routine. Finally, the caller can free the reserved range by calling <a href="..\wdm\nf-wdm-mmfreemappingaddress.md">MmFreeMappingAddress</a>. </p>

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
<p>Available in Windows XP and later versions of Windows. </p>
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
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-mmfreemappingaddress.md">MmFreeMappingAddress</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-mmmaplockedpageswithreservedmapping.md">MmMapLockedPagesWithReservedMapping</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-mmunmapreservedmapping.md">MmUnmapReservedMapping</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmAllocateMappingAddress routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
