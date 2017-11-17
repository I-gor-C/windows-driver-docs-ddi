---
UID: NF.ndis.NdisInterlockedPushEntrySList
title: NdisInterlockedPushEntrySList
author: windows-driver-content
description: The NdisInterlockedPushEntrySList function inserts an entry at the head of a sequenced, singly linked list.
old-location: netvista\ndisinterlockedpushentryslist.htm
ms.assetid: 155604e9-45f6-4dd2-9373-90f689713c1a
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   
   NdisInterlockedPushEntrySList (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   
   NdisInterlockedPushEntrySList (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisInterlockedPushEntrySList
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
ms.keywords: NdisInterlockedPushEntrySList
req.iface: 
---

# NdisInterlockedPushEntrySList function



## -description
<p>The 
  <b>NdisInterlockedPushEntrySList</b> function inserts an entry at the head of a sequenced, singly linked
  list.</p>


## -syntax

````
PSINGLE_LIST_ENTRY NdisInterlockedPushEntrySList(
  _In_ PSLIST_HEADER      ListHead,
  _In_ PSINGLE_LIST_ENTRY ListEntry,
  _In_ PNDIS_SPIN_LOCK    Lock
);
````


## -parameters
<dl>

### -param <i>ListHead</i> [in]

<dd>
<p>A pointer to the head of the already initialized sequenced, singly linked list into which the
     specified entry is to be inserted.</p>
</dd>

### -param <i>ListEntry</i> [in]

<dd>
<p>A pointer to the entry to be inserted.</p>
</dd>

### -param <i>Lock</i> [in]

<dd>
<p>A pointer to a caller-supplied spin lock, not currently held by the caller.</p>
</dd>
</dl>

## -returns
<p><b>NdisInterlockedPushEntrySList</b> returns a pointer to the previous first entry in the list. If the
     list was previously empty, it returns <b>NULL</b>.</p>

## -remarks
<p>Before the driver's initial call the 
    <b>NdisInterlockedPushEntrySList</b> function, it must initialize the list head with the 
    <a href="https://msdn.microsoft.com/4f9a5f8c-5c7f-4ac5-a6ce-118de2b4a304">
    NdisInitializeSListHead</a> function.</p>

<p>A driver 
    <u>must not</u> be holding the given 
    <i>Lock</i> when it calls 
    <b>NdisInterlockedPushEntrySList</b>. If necessary, a driver must call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564524">NdisReleaseSpinLock</a> function before
    calling 
    <b>NdisInterlockedPushEntrySList</b>. 
    <b>NdisInterlockedPushEntrySList</b> must acquire this lock itself before it inserts 
    <i>ListEntry</i> at the head of the list to ensure that this operation is handled in a multiprocessor-safe
    way.</p>

<p>The caller must provide resident storage for the 
    <i>Lock</i>, which must be initialized with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561617">NdisAllocateSpinLock</a> function before
    the initial call to any 
    <b>NdisInterlocked..SList</b> routine.</p>

<p>Drivers that retry I/O operations should use a doubly linked interlocked queue and the 
    <b>NdisInterlockedInsert/Remove..List</b> functions, instead of an S-List.</p>

<p>If 
    <b>NdisInterlockedPushEntrySList</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for the 
    <i>ListHead</i> parameter and the list entries must be resident</p>

<p>Before the driver's initial call the 
    <b>NdisInterlockedPushEntrySList</b> function, it must initialize the list head with the 
    <a href="https://msdn.microsoft.com/4f9a5f8c-5c7f-4ac5-a6ce-118de2b4a304">
    NdisInitializeSListHead</a> function.</p>

<p>A driver 
    <u>must not</u> be holding the given 
    <i>Lock</i> when it calls 
    <b>NdisInterlockedPushEntrySList</b>. If necessary, a driver must call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564524">NdisReleaseSpinLock</a> function before
    calling 
    <b>NdisInterlockedPushEntrySList</b>. 
    <b>NdisInterlockedPushEntrySList</b> must acquire this lock itself before it inserts 
    <i>ListEntry</i> at the head of the list to ensure that this operation is handled in a multiprocessor-safe
    way.</p>

<p>The caller must provide resident storage for the 
    <i>Lock</i>, which must be initialized with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561617">NdisAllocateSpinLock</a> function before
    the initial call to any 
    <b>NdisInterlocked..SList</b> routine.</p>

<p>Drivers that retry I/O operations should use a doubly linked interlocked queue and the 
    <b>NdisInterlockedInsert/Remove..List</b> functions, instead of an S-List.</p>

<p>If 
    <b>NdisInterlockedPushEntrySList</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for the 
    <i>ListHead</i> parameter and the list entries must be resident</p>

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
   <a href="https://msdn.microsoft.com/a81422a6-04f7-448d-8ed9-09c91b6a5faa">
   NdisInterlockedPushEntrySList (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>
   NdisInterlockedPushEntrySList (NDIS 5.1)</b>) in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561617">NdisAllocateSpinLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562602">NdisFreeSpinLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562739">NdisInitializeSListHead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562760">NdisInterlockedPopEntrySList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564524">NdisReleaseSpinLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563753">NdisQueryDepthSList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisInterlockedPushEntrySList function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
