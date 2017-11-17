---
UID: NF.ndis.NdisInitializeSListHead
title: NdisInitializeSListHead
author: windows-driver-content
description: The NdisInitializeSListHead function initializes the head of a sequenced, interlocked, singly linked list.
old-location: netvista\ndisinitializeslisthead.htm
ms.assetid: 4f9a5f8c-5c7f-4ac5-a6ce-118de2b4a304
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisInitializeSListHead (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisInitializeSListHead (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisInitializeSListHead
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
ms.keywords: NdisInitializeSListHead
req.iface: 
---

# NdisInitializeSListHead function



## -description
<p>The 
  <b>NdisInitializeSListHead</b> function initializes the head of a sequenced, interlocked, singly linked
  list.</p>


## -syntax

````
VOID NdisInitializeSListHead(
  _In_ PSLIST_HEADER SListHead
);
````


## -parameters
<dl>

### -param <i>SListHead</i> [in]

<dd>
<p>A pointer to the caller-supplied list head to be initialized, which must be in resident
     memory. The structure must be 16-byte aligned on 64-bit platforms.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisInitializeSListHead</b> zero-initializes the opaque list head at 
    <i>SListHead</i> and sets the first-entry pointer to <b>NULL</b>.</p>

<p>The sequence number in an S-List is incremented each time an entry is inserted to, or removed from,
    the list.</p>

<p>All entries in an S-List must be nonpaged.</p>

<p>Any driver that uses an S-List must provide a spin lock to the 
    <a href="https://msdn.microsoft.com/155604e9-45f6-4dd2-9373-90f689713c1a">
    NdisInterlockedPushEntrySList</a> and 
    <a href="https://msdn.microsoft.com/22f79bc7-49e1-43ba-8dff-8847b9a9bcca">
    NdisInterlockedPopEntrySList</a> functions. Before its initial call to either of these functions, the
    driver must initialize the spin lock with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561617">NdisAllocateSpinLock</a> function. To
    prevent deadlocks, the driver 
    <u>must not be holding this spin lock</u> when it makes subsequent calls to 
    <b>NdisInterlockedPushEntrySList</b> and 
    <b>NdisInterlockedPopEntrySList</b>.</p>

<p>To manage a pool of fixed-size entries from nonpaged memory, consider using a lookaside list instead
    of an S-List.</p>

<p>Drivers that retry I/O operations should use a doubly linked interlocked queue and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562754">NdisInterlockedInsertHeadList</a>,  <a href="https://msdn.microsoft.com/library/windows/hardware/ff562755">NdisInterlockedInsertTailList</a>, and   <a href="https://msdn.microsoft.com/library/windows/hardware/ff562771">NdisInterlockedRemoveHeadList</a> functions, rather than an S-List.</p>

<p>If 
    <b>NdisInitializeSListHead</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for the 
    <i>SListHead</i> parameter must be resident.</p>

<p><b>NdisInitializeSListHead</b> zero-initializes the opaque list head at 
    <i>SListHead</i> and sets the first-entry pointer to <b>NULL</b>.</p>

<p>The sequence number in an S-List is incremented each time an entry is inserted to, or removed from,
    the list.</p>

<p>All entries in an S-List must be nonpaged.</p>

<p>Any driver that uses an S-List must provide a spin lock to the 
    <a href="https://msdn.microsoft.com/155604e9-45f6-4dd2-9373-90f689713c1a">
    NdisInterlockedPushEntrySList</a> and 
    <a href="https://msdn.microsoft.com/22f79bc7-49e1-43ba-8dff-8847b9a9bcca">
    NdisInterlockedPopEntrySList</a> functions. Before its initial call to either of these functions, the
    driver must initialize the spin lock with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561617">NdisAllocateSpinLock</a> function. To
    prevent deadlocks, the driver 
    <u>must not be holding this spin lock</u> when it makes subsequent calls to 
    <b>NdisInterlockedPushEntrySList</b> and 
    <b>NdisInterlockedPopEntrySList</b>.</p>

<p>To manage a pool of fixed-size entries from nonpaged memory, consider using a lookaside list instead
    of an S-List.</p>

<p>Drivers that retry I/O operations should use a doubly linked interlocked queue and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562754">NdisInterlockedInsertHeadList</a>,  <a href="https://msdn.microsoft.com/library/windows/hardware/ff562755">NdisInterlockedInsertTailList</a>, and   <a href="https://msdn.microsoft.com/library/windows/hardware/ff562771">NdisInterlockedRemoveHeadList</a> functions, rather than an S-List.</p>

<p>If 
    <b>NdisInitializeSListHead</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for the 
    <i>SListHead</i> parameter must be resident.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/65510f80-5014-4fb0-9115-09fa9898b321">NdisInitializeSListHead (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisInitializeSListHead (NDIS
   5.1)</b>) in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/d240f2cc-18a6-4c2d-889f-e25a9486d5fe">
   NdisInitializeNPagedLookasideList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562760">NdisInterlockedPopEntrySList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/155604e9-45f6-4dd2-9373-90f689713c1a">
   NdisInterlockedPushEntrySList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563753">NdisQueryDepthSList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563775">NdisQueueIoWorkItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisInitializeSListHead function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
