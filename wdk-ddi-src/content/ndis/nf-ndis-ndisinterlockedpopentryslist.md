---
UID: NF.ndis.NdisInterlockedPopEntrySList
title: NdisInterlockedPopEntrySList macro
author: windows-driver-content
description: The NdisInterlockedPopEntrySList function removes the first entry from a sequenced, singly linked list.
old-location: netvista\ndisinterlockedpopentryslist.htm
old-project: NetVista
ms.assetid: 22f79bc7-49e1-43ba-8dff-8847b9a9bcca
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NdisInterlockedPopEntrySList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
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
---

# NdisInterlockedPopEntrySList macro



## -description
The
  <b>NdisInterlockedPopEntrySList</b> function removes the first entry from a sequenced, singly linked
  list.



## -syntax

````
PSINGLE_LIST_ENTRY NdisInterlockedPopEntrySList(
  [in] PSLIST_HEADER   ListHead,
  [in] PNDIS_SPIN_LOCK Lock
);
````


## -parameters

### -param ListHead [in]

A pointer to the head of the already initialized sequenced, singly linked list from which the
     entry is to be returned.


### -param Lock [in]

A pointer to a caller-supplied spin lock, not currently held by the caller.


## -remarks
A driver 
    <u>must not</u> be holding the given 
    <i>Lock</i> when it calls 
    <b>NdisInterlockedPopEntrySList</b>. If necessary, the driver should call the 
    <a href="netvista.ndisreleasespinlock">NdisReleaseSpinLock</a> function before
    making this call. 
    <b>NdisInterlockedPopEntrySList</b> itself must acquire this spin lock to remove the first entry in the
    S-List, if any, in a multiprocessor-safe way.

The caller must provide resident storage for the 
    <i>Lock</i>, which must be initialized with the 
    <a href="netvista.ndisallocatespinlock">NdisAllocateSpinLock</a> function before
    the initial call to any 
    <b>NdisInterlocked..SList</b> function.

If 
    <b>NdisInterlockedPopEntrySList</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for the 
    <i>ListHead</i> parameter must be resident.


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
   <a href="https://msdn.microsoft.com/233bc698-d9d2-43d6-9a6d-20f539e9df37">NdisInterlockedPopEntrySList
   (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisInterlockedPopEntrySList
   (NDIS 5.1)</b>) in Windows XP.

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
<a href="netvista.ndisallocatespinlock">NdisAllocateSpinLock</a>
</dt>
<dt>
<a href="netvista.ndisfreespinlock">NdisFreeSpinLock</a>
</dt>
<dt>
<a href="netvista.ndisinitializeslisthead">NdisInitializeSListHead</a>
</dt>
<dt>
<a href="netvista.ndisinterlockedpushentryslist">
   NdisInterlockedPushEntrySList</a>
</dt>
<dt>
<a href="netvista.ndisreleasespinlock">NdisReleaseSpinLock</a>
</dt>
<dt>
<a href="netvista.ndisquerydepthslist">NdisQueryDepthSList</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NdisInterlockedPopEntrySList macro%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

