---
UID: NF.ntddk.MmIsAddressValid
title: MmIsAddressValid
author: windows-driver-content
description: The MmIsAddressValid routine checks whether a page fault will occur for a read or write operation at a given virtual address.Warning  We do not recommend using this function.
old-location: kernel\mmisaddressvalid.htm
old-project: kernel
ms.assetid: 328f9ffe-67ae-4ba5-98e4-b3b00068eb0e
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: MmIsAddressValid
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmIsAddressValid
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# MmIsAddressValid function



## -description
<p>The <b>MmIsAddressValid</b> routine checks whether a page fault will occur for a read or write operation at a given virtual address.</p>


## -syntax

````
BOOLEAN MmIsAddressValid(
  _In_ PVOID VirtualAddress
);
````


## -parameters
<dl>

### -param <i>VirtualAddress</i> [in]

<dd>
<p>A pointer to the nonpaged virtual address to check. The caller must ensure that this address cannot be paged out or deleted for the duration of this call. Even after the return from the call, you must not page out or delete this address. If you do page out or delete this address, the return value might be unreliable. Paging out or deleting this address might cause the computer to stop responding (that is, <i>crash</i>). </p>
</dd>
</dl>

## -returns
<p>If no page fault would occur from reading or writing at the given virtual address, <b>MmIsAddressValid</b> returns <b>TRUE</b>.</p>

## -remarks
<p>Even if <b>MmIsAddressValid</b> returns <b>TRUE</b>, accessing the address can cause page faults unless the memory has been locked down or the address is a valid nonpaged pool address. </p>

<p>Even if <b>MmIsAddressValid</b> returns <b>TRUE</b>, accessing the address can cause page faults unless the memory has been locked down or the address is a valid nonpaged pool address. </p>

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
<p>Available starting with Windows 2000.</p>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmIsAddressValid routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
