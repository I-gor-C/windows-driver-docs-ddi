---
UID: NF.wdm.MmFreeMappingAddress
title: MmFreeMappingAddress function
author: windows-driver-content
description: The MmFreeMappingAddress routine frees a range of virtual memory reserved by the MmAllocateMappingAddress routine.
old-location: kernel\mmfreemappingaddress.htm
old-project: kernel
ms.assetid: df5afc18-da83-46b4-b7ab-8cef4353b951
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: MmFreeMappingAddress
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
req.product: Windows 10 or later.
---

# MmFreeMappingAddress function



## -description
The <b>MmFreeMappingAddress</b> routine frees a range of virtual memory reserved by the <a href="kernel.mmallocatemappingaddress">MmAllocateMappingAddress</a> routine. 


## -syntax

````
VOID MmFreeMappingAddress(
  _In_ PVOID BaseAddress,
  _In_ ULONG PoolTag
);
````


## -parameters

### -param BaseAddress [in]

Pointer to the beginning of the reserved memory buffer to free. This must be an address previously returned by <a href="kernel.mmallocatemappingaddress">MmAllocateMappingAddress</a>.

### -param PoolTag [in]

Specifies the pool tag for the reserved memory buffer. This must be identical to the value specified in the <i>PoolTag</i> parameter of the call to <a href="kernel.mmallocatemappingaddress">MmAllocateMappingAddress</a> that reserved the buffer. 

## -returns
None

## -remarks
<b>MmFreeMappingAddress</b> frees a range of memory reserved by <a href="kernel.mmallocatemappingaddress">MmAllocateMappingAddress</a>. If the memory range has already been mapped by <a href="kernel.mmmaplockedpageswithreservedmapping">MmMapLockedPagesWithReservedMapping</a>, it must first be unmapped with <a href="kernel.mmunmapreservedmapping">MmUnmapReservedMapping</a> before the memory range can be freed. 

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
Available in Windows XP and later versions of Windows. 
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
&lt;=APC_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.mmallocatemappingaddress">MmAllocateMappingAddress</a>
</dt>
<dt>
<a href="kernel.mmmaplockedpageswithreservedmapping">MmMapLockedPagesWithReservedMapping</a>
</dt>
<dt>
<a href="kernel.mmunmapreservedmapping">MmUnmapReservedMapping</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmFreeMappingAddress routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
