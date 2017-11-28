---
UID: NF.ndis.NdisInterlockedRemoveHeadList
title: NdisInterlockedRemoveHeadList
author: windows-driver-content
description: The NdisInterlockedRemoveHeadList function removes an entry, usually a packet, from the head of a doubly linked list so that access to the list is synchronized in a multiprocessor-safe way.
old-location: netvista\ndisinterlockedremoveheadlist.htm
old-project: netvista
ms.assetid: 85cbc158-7132-4666-8161-a78251a62e4d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisInterlockedRemoveHeadList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   
   NdisInterlockedRemoveHeadList (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   
   NdisInterlockedRemoveHeadList (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisInterlockedRemoveHeadList
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

# NdisInterlockedRemoveHeadList function



## -description
<p>The 
  <b>NdisInterlockedRemoveHeadList</b> function removes an entry, usually a packet, from the head of a doubly
  linked list so that access to the list is synchronized in a multiprocessor-safe way.</p>


## -syntax

````
PLIST_ENTRY NdisInterlockedRemoveHeadList(
  _In_ PLIST_ENTRY     ListHead,
  _In_ PNDIS_SPIN_LOCK SpinLock
);
````


## -parameters
<dl>

### -param <i>ListHead</i> [in]

<dd>
<p>A pointer to the head of the doubly linked list from which an entry is to be removed.</p>
</dd>

### -param <i>SpinLock</i> [in]

<dd>
<p>A pointer to a caller-supplied spin lock, used to synchronize access to the list.</p>
</dd>
</dl>

## -returns
<p><b>NdisInterlockedRemoveHeadList</b> returns a pointer to the dequeued entry. If the list was empty, it
     returns <b>NULL</b>.</p>

## -remarks
<p>Before calling any 
    <b>NdisInterlocked..List</b> function, a driver must initialize the variable at 
    <i>ListHead</i> with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562734">NdisInitializeListHead</a> function and
    the variable at 
    <i>SpinLock</i> with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561617">NdisAllocateSpinLock</a> function. The
    driver also must provide resident storage for these variables and for its internal queue.</p>

<p>Before calling 
    <b>NdisInterlockedRemoveHeadList</b>, entries are queued with one or more calls to the 
    <b>NdisInterlockedInsert..List</b> functions.</p>

<p>The caller-supplied spin lock prevents any other function from accessing the driver's internal queue
    while 
    <b>NdisInterlockedRemoveHeadList</b> is removing an entry, even when the driver is running on a
    multiprocessor computer.</p>

<p><b>NdisInterlockedRemoveHeadList</b> raises the IRQL to DISPATCH_LEVEL when it acquires the given spin
    lock and restores the original IRQL before it returns control. Consequently, any driver function that
    calls 
    <b>NdisInterlockedRemoveHeadList</b> cannot be pageable code.</p>

<p>To convert a returned value back to the address of the inserted entry, a driver can use the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff542043">CONTAINING_RECORD</a> macro.</p>

<p>If 
    <b>NdisInterlockedRemoveHeadList</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for the 
    <i>ListHead</i> parameter must be resident.</p>

<p>Before calling any 
    <b>NdisInterlocked..List</b> function, a driver must initialize the variable at 
    <i>ListHead</i> with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562734">NdisInitializeListHead</a> function and
    the variable at 
    <i>SpinLock</i> with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561617">NdisAllocateSpinLock</a> function. The
    driver also must provide resident storage for these variables and for its internal queue.</p>

<p>Before calling 
    <b>NdisInterlockedRemoveHeadList</b>, entries are queued with one or more calls to the 
    <b>NdisInterlockedInsert..List</b> functions.</p>

<p>The caller-supplied spin lock prevents any other function from accessing the driver's internal queue
    while 
    <b>NdisInterlockedRemoveHeadList</b> is removing an entry, even when the driver is running on a
    multiprocessor computer.</p>

<p><b>NdisInterlockedRemoveHeadList</b> raises the IRQL to DISPATCH_LEVEL when it acquires the given spin
    lock and restores the original IRQL before it returns control. Consequently, any driver function that
    calls 
    <b>NdisInterlockedRemoveHeadList</b> cannot be pageable code.</p>

<p>To convert a returned value back to the address of the inserted entry, a driver can use the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff542043">CONTAINING_RECORD</a> macro.</p>

<p>If 
    <b>NdisInterlockedRemoveHeadList</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for the 
    <i>ListHead</i> parameter must be resident.</p>

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
   <a href="https://msdn.microsoft.com/c43225c8-b3cd-4b7e-a3ce-0c01638e210c">
   NdisInterlockedRemoveHeadList (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>
   NdisInterlockedRemoveHeadList (NDIS 5.1)</b>) in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561617">NdisAllocateSpinLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562734">NdisInitializeListHead</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinterlockedinsertheadlist.md">
   NdisInterlockedInsertHeadList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinterlockedinserttaillist.md">
   NdisInterlockedInsertTailList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisInterlockedRemoveHeadList function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
