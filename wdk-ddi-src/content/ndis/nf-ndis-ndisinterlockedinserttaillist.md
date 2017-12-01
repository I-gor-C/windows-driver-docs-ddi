---
UID: NF.ndis.NdisInterlockedInsertTailList
title: NdisInterlockedInsertTailList
author: windows-driver-content
description: The NdisInterlockedInsertTailList function inserts an entry, usually a packet, at the tail of a doubly linked list so that access to the list is synchronized in a multiprocessor-safe way.
old-location: netvista\ndisinterlockedinserttaillist.htm
old-project: netvista
ms.assetid: cc455bb1-3574-4dfb-9462-f2c67632132b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisInterlockedInsertTailList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see       NdisInterlockedInsertTailList (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see       NdisInterlockedInsertTailList (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisInterlockedInsertTailList
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: Any level
req.iface: 
---

# NdisInterlockedInsertTailList function



## -description
<p>The 
  <b>NdisInterlockedInsertTailList</b> function inserts an entry, usually a packet, at the tail of a doubly
  linked list so that access to the list is synchronized in a multiprocessor-safe way.</p>


## -syntax

````
PLIST_ENTRY NdisInterlockedInsertTailList(
  _In_ PLIST_ENTRY     ListHead,
  _In_ PLIST_ENTRY     ListEntry,
  _In_ PNDIS_SPIN_LOCK SpinLock
);
````


## -parameters
<dl>

### -param <i>ListHead</i> [in]

<dd>
<p>A pointer to the head of the doubly linked list into which an entry is to be inserted.</p>
</dd>

### -param <i>ListEntry</i> [in]

<dd>
<p>A pointer to the entry to be inserted at the end of the list.</p>
</dd>

### -param <i>SpinLock</i> [in]

<dd>
<p>A pointer to a caller-supplied spin lock, used to synchronize access to the list.</p>
</dd>
</dl>

## -returns
<p><b>NdisInterlockedInsertTailList</b> returns a pointer to the entry that was at the tail of the queue
     before the given entry was inserted. If the queue was empty, it returns <b>NULL</b>.</p>

## -remarks
<p>Before calling 
    <b>NdisInterlockedInsertTailList</b>, a driver must initialize the variable at 
    <i>ListHead</i> with the 
    <a href="..\ndis\nf-ndis-ndisinitializelisthead.md">NdisInitializeListHead</a> function and
    the variable at 
    <i>SpinLock</i> with the 
    <a href="..\ndis\nf-ndis-ndisallocatespinlock.md">NdisAllocateSpinLock</a> function. The
    driver also must provide resident storage for these variables and for its internal queue.</p>

<p>The caller-supplied spin lock prevents any other function from accessing the driver's internal queue
    while 
    <b>NdisInterlockedInsertTailList</b> is inserting the given entry, even when the driver is running on a
    multiprocessor machine.</p>

<p><b>NdisInterlockedInsertTailList</b> raises the IRQL to DISPATCH_LEVEL when it acquires the given spin
    lock and restores the original IRQL before it returns control. Consequently, any driver function that
    calls 
    <b>NdisInterlockedInsertTailList</b> cannot be pageable code.</p>

<p>To convert a returned value back to the address of the inserted entry, a driver can use the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff542043">CONTAINING_RECORD</a> macro.</p>

<p>If 
    <b>NdisInterlockedInsertTailList</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for the 
    <i>ListHead</i> parameter and the list entries must be resident.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/1eda279d-09ae-490d-9ffc-c027d4d421b3">
   NdisInterlockedInsertTailList (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>
   NdisInterlockedInsertTailList (NDIS 5.1)</b>) in Windows XP.</p>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542043">CONTAINING_RECORD</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatespinlock.md">NdisAllocateSpinLock</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinitializelisthead.md">NdisInitializeListHead</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinterlockedinsertheadlist.md">
   NdisInterlockedInsertHeadList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinterlockedremoveheadlist.md">
   NdisInterlockedRemoveHeadList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisInterlockedInsertTailList function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
