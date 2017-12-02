---
UID: NF.wdm.ExFreeToNPagedLookasideList
title: ExFreeToNPagedLookasideList
author: windows-driver-content
description: The ExFreeToNPagedLookasideList routine returns a nonpaged entry to the given lookaside list or to nonpaged pool.
old-location: kernel\exfreetonpagedlookasidelist.htm
old-project: kernel
ms.assetid: 8abd72f1-0537-4624-b3d4-2de51c4d4daa
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ExFreeToNPagedLookasideList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExFreeToNPagedLookasideList
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: SpIrql
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ExFreeToNPagedLookasideList function



## -description
<p>The <b>ExFreeToNPagedLookasideList</b> routine returns a nonpaged entry to the given lookaside list or to nonpaged pool.</p>


## -syntax

````
 VOID ExFreeToNPagedLookasideList(
  _Inout_ PNPAGED_LOOKASIDE_LIST Lookaside,
  _In_    PVOID                  Entry
);
````


## -parameters
<dl>

### -param Lookaside [in, out]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556431">NPAGED_LOOKASIDE_LIST</a> structure for the lookaside list, which the caller already initialized with <a href="..\wdm\nf-wdm-exinitializenpagedlookasidelist.md">ExInitializeNPagedLookasideList</a>. </p>
</dd>

### -param Entry [in]

<dd>
<p>A pointer to the entry to be freed. The caller obtained this pointer from a preceding call to <a href="..\wdm\nf-wdm-exallocatefromnpagedlookasidelist.md">ExAllocateFromNPagedLookasideList</a>. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>ExFreeToNPagedLookasideList</b> is the reciprocal of <b>ExAllocateFromNPagedLookasideList</b>. It releases a caller-allocated entry back to the caller's lookaside list or to nonpaged pool when that entry is no longer in use.</p>

<p>The same entry can be reallocated or another entry allocated later with a subsequent call to <b>ExAllocateFromNPagedLookasideList</b>. The user of the lookaside list can allocate and free such entries dynamically on an as-needed basis until it calls <b>ExDeleteNPagedLookasideList</b>, which releases any outstanding entries in the list before it clears the system state for the given lookaside list and returns control.</p>

<p>If the specified lookaside list has not yet reached the system-determined maximum number of entries, <b>ExFreeToNPagedLookasideList</b> inserts the given entry at the front of the list. Otherwise, the buffer at <i>Entry</i> is released to nonpaged pool using the caller-supplied <i>Free</i> routine, if any, that was set up when the lookaside list was initialized or <b>ExFreePool</b>.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565416">Using Lookaside Lists</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.storport_spirql">SpIrql</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556431">NPAGED_LOOKASIDE_LIST</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exallocatefromnpagedlookasidelist.md">ExAllocateFromNPagedLookasideList</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exdeletenpagedlookasidelist.md">ExDeleteNPagedLookasideList</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exinitializenpagedlookasidelist.md">ExInitializeNPagedLookasideList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExFreeToNPagedLookasideList routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
