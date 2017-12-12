---
UID: NF.ndis.NdisInitializeSListHead
title: NdisInitializeSListHead macro
author: windows-driver-content
description: The NdisInitializeSListHead function initializes the head of a sequenced, interlocked, singly linked list.
old-location: netvista\ndisinitializeslisthead.htm
old-project: netvista
ms.assetid: 4f9a5f8c-5c7f-4ac5-a6ce-118de2b4a304
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisInitializeSListHead
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisInitializeSListHead (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisInitializeSListHead (NDIS   5.1)) in Windows XP.
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
---

# NdisInitializeSListHead macro



## -description
The 
  <b>NdisInitializeSListHead</b> function initializes the head of a sequenced, interlocked, singly linked
  list.



## -syntax

````
VOID NdisInitializeSListHead(
  [in] PSLIST_HEADER SListHead
);
````


## -parameters

### -param SListHead [in]

A pointer to the caller-supplied list head to be initialized, which must be in resident
     memory. The structure must be 16-byte aligned on 64-bit platforms.


## -remarks
<b>NdisInitializeSListHead</b> zero-initializes the opaque list head at 
    <i>SListHead</i> and sets the first-entry pointer to <b>NULL</b>.

The sequence number in an S-List is incremented each time an entry is inserted to, or removed from,
    the list.

All entries in an S-List must be nonpaged.

Any driver that uses an S-List must provide a spin lock to the 
    <a href="netvista.ndisinterlockedpushentryslist">
    NdisInterlockedPushEntrySList</a> and 
    <a href="netvista.ndisinterlockedpopentryslist">
    NdisInterlockedPopEntrySList</a> functions. Before its initial call to either of these functions, the
    driver must initialize the spin lock with the 
    <a href="netvista.ndisallocatespinlock">NdisAllocateSpinLock</a> function. To
    prevent deadlocks, the driver 
    <u>must not be holding this spin lock</u> when it makes subsequent calls to 
    <b>NdisInterlockedPushEntrySList</b> and 
    <b>NdisInterlockedPopEntrySList</b>.

To manage a pool of fixed-size entries from nonpaged memory, consider using a lookaside list instead
    of an S-List.

Drivers that retry I/O operations should use a doubly linked interlocked queue and the <a href="netvista.ndisinterlockedinsertheadlist">NdisInterlockedInsertHeadList</a>,  <a href="netvista.ndisinterlockedinserttaillist">NdisInterlockedInsertTailList</a>, and   <a href="netvista.ndisinterlockedremoveheadlist">NdisInterlockedRemoveHeadList</a> functions, rather than an S-List.

If 
    <b>NdisInitializeSListHead</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for the 
    <i>SListHead</i> parameter must be resident.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/65510f80-5014-4fb0-9115-09fa9898b321">NdisInitializeSListHead (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisInitializeSListHead (NDIS
   5.1)</b>) in Windows XP.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndisinitializenpagedlookasidelist">
   NdisInitializeNPagedLookasideList</a>
</dt>
<dt>
<a href="netvista.ndisinterlockedpopentryslist">NdisInterlockedPopEntrySList</a>
</dt>
<dt>
<a href="netvista.ndisinterlockedpushentryslist">
   NdisInterlockedPushEntrySList</a>
</dt>
<dt>
<a href="netvista.ndisquerydepthslist">NdisQueryDepthSList</a>
</dt>
<dt>
<a href="netvista.ndisqueueioworkitem">NdisQueueIoWorkItem</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisInitializeSListHead macro%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

