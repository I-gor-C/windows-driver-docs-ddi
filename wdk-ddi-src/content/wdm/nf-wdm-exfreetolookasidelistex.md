---
UID: NF.wdm.ExFreeToLookasideListEx
title: ExFreeToLookasideListEx
author: windows-driver-content
description: The ExFreeToLookasideListEx routine inserts an entry into a lookaside list, or, if the list is full, frees the allocated storage for the entry.
old-location: kernel\exfreetolookasidelistex.htm
old-project: kernel
ms.assetid: 37057400-7f4d-4274-b1ef-f03771cae34f
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ExFreeToLookasideListEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExFreeToLookasideListEx
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ExFreeToLookasideListEx function



## -description
<p>The <b>ExFreeToLookasideListEx</b> routine inserts an entry into a lookaside list, or, if the list is full, frees the allocated storage for the entry. </p>


## -syntax

````
VOID ExFreeToLookasideListEx(
  _Inout_ PLOOKASIDE_LIST_EX Lookaside,
  _In_    PVOID              Entry
);
````


## -parameters
<dl>

### -param <i>Lookaside</i> [in, out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554329">LOOKASIDE_LIST_EX</a> structure that describes a lookaside list. This structure was previously initialized by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545298">ExInitializeLookasideListEx</a> routine. </p>
</dd>

### -param <i>Entry</i> [in]

<dd>
<p>A pointer to the lookaside-list entry that is being freed.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>This routine frees a lookaside-list entry that was allocated by a previous call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544381">ExAllocateFromLookasideListEx</a> routine. <b>ExFreeToLookasideListEx</b> inserts the entry into the specified lookaside list, if space for the entry is available in the list. If the list is full (that is, it already contains the maximum number of entries, as determined by the operating system), <b>ExFreeToLookasideListEx</b> calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554324">LookasideListFreeEx</a> routine to free the storage for the specified entry, if the driver has provided such a routine. Otherwise, a default deallocation routine is used to free the entry.</p>

<p>For more information about lookaside lists, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565416">Using Lookaside Lists</a>.</p>

<p>This routine frees a lookaside-list entry that was allocated by a previous call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544381">ExAllocateFromLookasideListEx</a> routine. <b>ExFreeToLookasideListEx</b> inserts the entry into the specified lookaside list, if space for the entry is available in the list. If the list is full (that is, it already contains the maximum number of entries, as determined by the operating system), <b>ExFreeToLookasideListEx</b> calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554324">LookasideListFreeEx</a> routine to free the storage for the specified entry, if the driver has provided such a routine. Otherwise, a default deallocation routine is used to free the entry.</p>

<p>For more information about lookaside lists, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565416">Using Lookaside Lists</a>.</p>

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
<p>Available in Windows Vista and later versions of Windows.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544381">ExAllocateFromLookasideListEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545298">ExInitializeLookasideListEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554329">LOOKASIDE_LIST_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExFreeToLookasideListEx routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
