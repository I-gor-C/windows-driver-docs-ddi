---
UID: NF.wdm.MmFreeMappingAddress
title: MmFreeMappingAddress
author: windows-driver-content
description: The MmFreeMappingAddress routine frees a range of virtual memory reserved by the MmAllocateMappingAddress routine.
old-location: kernel\mmfreemappingaddress.htm
ms.assetid: df5afc18-da83-46b4-b7ab-8cef4353b951
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmFreeMappingAddress
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
ms.keywords: MmFreeMappingAddress
req.iface: 
req.product: Windows 10 or later.
---

# MmFreeMappingAddress function



## -description
<p>The <b>MmFreeMappingAddress</b> routine frees a range of virtual memory reserved by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554475">MmAllocateMappingAddress</a> routine. </p>


## -syntax

````
VOID MmFreeMappingAddress(
  _In_ PVOID BaseAddress,
  _In_ ULONG PoolTag
);
````


## -parameters
<dl>

### -param <i>BaseAddress</i> [in]

<dd>
<p>Pointer to the beginning of the reserved memory buffer to free. This must be an address previously returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff554475">MmAllocateMappingAddress</a>.</p>
</dd>

### -param <i>PoolTag</i> [in]

<dd>
<p>Specifies the pool tag for the reserved memory buffer. This must be identical to the value specified in the <i>PoolTag</i> parameter of the call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff554475">MmAllocateMappingAddress</a> that reserved the buffer. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>MmFreeMappingAddress</b> frees a range of memory reserved by <a href="https://msdn.microsoft.com/library/windows/hardware/ff554475">MmAllocateMappingAddress</a>. If the memory range has already been mapped by <a href="https://msdn.microsoft.com/library/windows/hardware/ff554640">MmMapLockedPagesWithReservedMapping</a>, it must first be unmapped with <a href="https://msdn.microsoft.com/library/windows/hardware/ff556392">MmUnmapReservedMapping</a> before the memory range can be freed. </p>

<p><b>MmFreeMappingAddress</b> frees a range of memory reserved by <a href="https://msdn.microsoft.com/library/windows/hardware/ff554475">MmAllocateMappingAddress</a>. If the memory range has already been mapped by <a href="https://msdn.microsoft.com/library/windows/hardware/ff554640">MmMapLockedPagesWithReservedMapping</a>, it must first be unmapped with <a href="https://msdn.microsoft.com/library/windows/hardware/ff556392">MmUnmapReservedMapping</a> before the memory range can be freed. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554475">MmAllocateMappingAddress</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554640">MmMapLockedPagesWithReservedMapping</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556392">MmUnmapReservedMapping</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmFreeMappingAddress routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
