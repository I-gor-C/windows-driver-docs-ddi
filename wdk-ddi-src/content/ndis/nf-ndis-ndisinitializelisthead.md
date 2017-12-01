---
UID: NF.ndis.NdisInitializeListHead
title: NdisInitializeListHead
author: windows-driver-content
description: The NdisInitializeListHead function initializes a doubly linked, driver-maintained queue.
old-location: netvista\ndisinitializelisthead.htm
old-project: netvista
ms.assetid: da3f5f28-2794-491b-a359-be8508b050bf
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisInitializeListHead
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisInitializeListHead (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisInitializeListHead (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisInitializeListHead
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
req.irql: Any level (see Remarks section)
req.iface: 
---

# NdisInitializeListHead function



## -description
<p>The 
  <b>NdisInitializeListHead</b> function initializes a doubly linked, driver-maintained queue.</p>


## -syntax

````
VOID NdisInitializeListHead(
  _In_ PLIST_ENTRY ListHead
);
````


## -parameters
<dl>

### -param <i>ListHead</i> [in]

<dd>
<p>A pointer to driver-allocated nonpaged storage for the head of the interlocked queue or
     list.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisInitializeListHead</b> can be called from a 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function or
    from a protocol driver's 
    <a href="netvista.driverentry_of_ndis_protocol_drivers">DriverEntry</a> routine
    if the driver queues requests internally. However, miniport drivers seldom set up internal queues because
    the NDIS library serializes requests and packets sent to miniport drivers.</p>

<p>Any NDIS driver that maintains an internal queue is responsible for synchronizing driver functions'
    accesses to queued entries. The 
    <b>NdisInterlocked<i>Xxx</i>List</b> functions ensure that only one driver function can access queued entries at any given moment,
    even if the driver is running on a multiprocessor computer, because the queue is protected by a
    caller-supplied spin lock.</p>

<p>For an interlocked queue, the driver also must provide nonpaged storage for a spin lock. It must
    initialize the spin lock with the 
    <a href="..\ndis\nf-ndis-ndisallocatespinlock.md">NdisAllocateSpinLock</a> function before
    passing a pointer to that spin lock to any of the 
    <b>NdisInterlocked<i>Xxx</i>List</b> functions.</p>

<p>Callers of <b>NdisInitializeListHead</b> can be running at any IRQL. If <b>NdisInitializeListHead</b> is called at IRQL &gt;= DISPATCH_LEVEL the storage for <i>ListHead</i> must be resident.</p>

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
   <a href="https://msdn.microsoft.com/de32c7bd-a9a5-4ef0-b924-01810cde18c0">NdisInitializeListHead (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisInitializeListHead (NDIS
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
<p>Any level (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.driverentry_of_ndis_protocol_drivers">DriverEntry of NDIS Protocol
   Drivers</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatespinlock.md">NdisAllocateSpinLock</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinterlockedinsertheadlist.md">
   NdisInterlockedInsertHeadList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinterlockedinserttaillist.md">
   NdisInterlockedInsertTailList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinterlockedremoveheadlist.md">
   NdisInterlockedRemoveHeadList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisInitializeListHead function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
