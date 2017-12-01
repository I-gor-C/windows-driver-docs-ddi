---
UID: NF.ndis.NdisInterlockedPopEntrySList
title: NdisInterlockedPopEntrySList
author: windows-driver-content
description: The NdisInterlockedPopEntrySList function removes the first entry from a sequenced, singly linked list.
old-location: netvista\ndisinterlockedpopentryslist.htm
old-project: netvista
ms.assetid: 22f79bc7-49e1-43ba-8dff-8847b9a9bcca
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisInterlockedPopEntrySList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisInterlockedPopEntrySList   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisInterlockedPopEntrySList   (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisInterlockedPopEntrySList
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
req.iface: 
---

# NdisInterlockedPopEntrySList function



## -description
<p>The
  <b>NdisInterlockedPopEntrySList</b> function removes the first entry from a sequenced, singly linked
  list.</p>


## -syntax

````
PSINGLE_LIST_ENTRY NdisInterlockedPopEntrySList(
  _In_ PSLIST_HEADER   ListHead,
  _In_ PNDIS_SPIN_LOCK Lock
);
````


## -parameters
<dl>

### -param <i>ListHead</i> [in]

<dd>
<p>A pointer to the head of the already initialized sequenced, singly linked list from which the
     entry is to be returned.</p>
</dd>

### -param <i>Lock</i> [in]

<dd>
<p>A pointer to a caller-supplied spin lock, not currently held by the caller.</p>
</dd>
</dl>

## -returns
<p><b>NdisInterlockedPopEntrySList</b> returns a pointer to the first entry in the list. If the list was
     empty, this routine returns <b>NULL</b>.</p>

## -remarks
<p>A driver 
    <u>must not</u> be holding the given 
    <i>Lock</i> when it calls 
    <b>NdisInterlockedPopEntrySList</b>. If necessary, the driver should call the 
    <a href="..\ndis\nf-ndis-ndisreleasespinlock.md">NdisReleaseSpinLock</a> function before
    making this call. 
    <b>NdisInterlockedPopEntrySList</b> itself must acquire this spin lock to remove the first entry in the
    S-List, if any, in a multiprocessor-safe way.</p>

<p>The caller must provide resident storage for the 
    <i>Lock</i>, which must be initialized with the 
    <a href="..\ndis\nf-ndis-ndisallocatespinlock.md">NdisAllocateSpinLock</a> function before
    the initial call to any 
    <b>NdisInterlocked..SList</b> function.</p>

<p>If 
    <b>NdisInterlockedPopEntrySList</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for the 
    <i>ListHead</i> parameter must be resident.</p>

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
   <a href="https://msdn.microsoft.com/233bc698-d9d2-43d6-9a6d-20f539e9df37">NdisInterlockedPopEntrySList
   (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisInterlockedPopEntrySList
   (NDIS 5.1)</b>) in Windows XP.</p>
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
<a href="..\ndis\nf-ndis-ndisallocatespinlock.md">NdisAllocateSpinLock</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfreespinlock.md">NdisFreeSpinLock</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinitializeslisthead.md">NdisInitializeSListHead</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinterlockedpushentryslist.md">
   NdisInterlockedPushEntrySList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisreleasespinlock.md">NdisReleaseSpinLock</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisquerydepthslist.md">NdisQueryDepthSList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisInterlockedPopEntrySList function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
