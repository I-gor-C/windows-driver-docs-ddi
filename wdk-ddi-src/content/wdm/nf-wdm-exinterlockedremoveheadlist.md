---
UID: NF.wdm.ExInterlockedRemoveHeadList
title: ExInterlockedRemoveHeadList
author: windows-driver-content
description: The ExInterlockedRemoveHeadList routine removes an entry from the beginning of a doubly linked list of LIST_ENTRY structures.
old-location: kernel\exinterlockedremoveheadlist.htm
old-project: kernel
ms.assetid: d024da2c-9629-4907-98b8-a29dc6022ac0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ExInterlockedRemoveHeadList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExInterlockedRemoveHeadList
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
req.irql: Any level (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# ExInterlockedRemoveHeadList function



## -description
<p>The <b>ExInterlockedRemoveHeadList</b> routine removes an entry from the beginning of a doubly linked list of <a href="kernel.list_entry">LIST_ENTRY</a> structures. </p>


## -syntax

````
PLIST_ENTRY ExInterlockedRemoveHeadList(
  _Inout_ PLIST_ENTRY ListHead,
  _Inout_ PKSPIN_LOCK Lock
);
````


## -parameters
<dl>

### -param <i>ListHead</i> [in, out]

<dd>
<p>A pointer to the <a href="kernel.list_entry">LIST_ENTRY</a> structure that serves as the list header.</p>
</dd>

### -param <i>Lock</i> [in, out]

<dd>
<p>A pointer to a <b>KSPIN_LOCK</b> structure that serves as the spin lock used to synchronize access to the list. The storage for the spin lock must be resident and must have been initialized by calling <a href="..\wdm\nf-wdm-keinitializespinlock.md">KeInitializeSpinLock</a>. You must use this spin lock only with the <b>ExInterlocked<i>Xxx</i>List</b> routines.</p>
</dd>
</dl>

## -returns
<p><b>ExInterlockedRemoveHeadList</b> returns a pointer to the <a href="kernel.list_entry">LIST_ENTRY</a> structure removed from the list. If the list was empty, the routine returns <b>NULL</b>.</p>

## -remarks
<p><b>ExInterlockedRemoveHeadList</b> performs a similar operation as <a href="..\wdm\nf-wdm-removeheadlist.md">RemoveHeadList</a>, but atomically. Do not mix atomic and non-atomic calls on the same list.</p>

<p>For more information about using this routine to implement a doubly linked list, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563802">Singly and Doubly Linked Lists</a>.</p>

<p>The <b>ExInterlockedRemoveHeadList</b> routine can be called at any IRQL. The storage for the <i>ListHead</i> parameter must be resident at all IRQLs.</p>

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
<p>Any level (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-exinterlockedinsertheadlist.md">ExInterlockedInsertHeadList</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exinterlockedinserttaillist.md">ExInterlockedInsertTailList</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-initializelisthead.md">InitializeListHead</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keinitializespinlock.md">KeInitializeSpinLock</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-removeheadlist.md">RemoveHeadList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExInterlockedRemoveHeadList routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
