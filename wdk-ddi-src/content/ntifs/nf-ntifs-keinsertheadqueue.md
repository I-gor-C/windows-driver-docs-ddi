---
UID: NF.ntifs.KeInsertHeadQueue
title: KeInsertHeadQueue function
author: windows-driver-content
description: The KeInsertHeadQueue routine inserts an entry at the head of the given queue if it cannot immediately use the entry to satisfy a thread wait.
old-location: ifsk\keinsertheadqueue.htm
old-project: ifsk
ms.assetid: 82e0bf14-b751-4919-b8d0-26fc7c5598a8
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: KeInsertHeadQueue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeInsertHeadQueue
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
---

# KeInsertHeadQueue function



## -description
The <b>KeInsertHeadQueue</b> routine inserts an entry at the head of the given queue if it cannot immediately use the entry to satisfy a thread wait. 



## -syntax

````
LONG KeInsertHeadQueue(
  _Inout_ PRKQUEUE    Queue,
  _Inout_ PLIST_ENTRY Entry
);
````


## -parameters

### -param Queue [in, out]

Pointer to an initialized queue object for which the caller provides resident storage in nonpaged pool. This structure is defined as follows:

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _KQUEUE {
    DISPATCHER_HEADER Header;
    LIST_ENTRY EntryListHead;
    ULONG CurrentCount;
    ULONG MaximumCount;
    LIST_ENTRY ThreadListHead;
} KQUEUE, *PKQUEUE, *RESTRICTED_POINTER PRKQUEUE;</pre>
</td>
</tr>
</table></span></div>
<table>
<tr>
<th>Member</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<b>Header</b>

</td>
<td>
Queue header

</td>
</tr>
<tr>
<td>
<b>EntryListHead</b>

</td>
<td>
Pointer to the first entry in the queue

</td>
</tr>
<tr>
<td>
<b>CurrentCount</b>

</td>
<td>
Number of entries in the queue

</td>
</tr>
<tr>
<td>
<b>MaximumCount</b>

</td>
<td>
Maximum number of entries the queue can contain

</td>
</tr>
<tr>
<td>
<b>ThreadListHead</b>

</td>
<td>
Pointer to the first entry in the thread list

</td>
</tr>
</table>
 


### -param Entry [in, out]

Pointer to the queue entry that is to be inserted. This pointer must be a resident system-space address. 


## -returns
<b>KeInsertHeadQueue</b> returns the previous signal state of the given queue. If it was set to zero (not signaled) before <b>KeInsertHeadQueue</b> was called, <b>KeInsertHeadQueue</b> returns zero, meaning that no entries were queued. If it was nonzero (signaled), <b>KeInsertHeadQueue</b> returns the number of entries that were queued before <b>KeInsertHeadQueue</b> was called. 


## -remarks
Entries to be queued by <b>KeInsertHeadQueue</b> must be allocated from nonpaged pool. For example, memory for caller-defined entries can be allocated with <a href="kernel.exallocatepoolwithtag">ExAllocatePoolWithTag</a>. If the caller allocates entries of a fixed size, creating a lookaside list with <a href="kernel.exinitializenpagedlookasidelist">ExInitializeNPagedLookasideList</a> and allocating from it with <a href="kernel.exallocatefromnpagedlookasidelist">ExAllocateFromNPagedLookasideList</a> is more efficient than making frequent calls to <b>ExAllocatePoolWithTag</b>, particularly for entries whose size is not a multiple of PAGE_SIZE. 

If any threads are waiting on the queue object when <b>KeInsertHeadQueue</b> is called, a single thread's wait is satisfied by this call. The thread is dispatched for execution with the given <i>Entry</i> pointer. 

If no threads are currently waiting on the queue object when <b>KeInsertHeadQueue</b> is called, the given entry is inserted in the queue and the queue object's signal state is incremented. 

For more information about using driver-managed internal queues, see <a href="kernel.driver_managed_queues">Driver-Managed Queues</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exallocatefromnpagedlookasidelist">ExAllocateFromNPagedLookasideList</a>
</dt>
<dt>
<a href="kernel.exallocatepoolwithtag">ExAllocatePoolWithTag</a>
</dt>
<dt>
<a href="kernel.exinitializenpagedlookasidelist">ExInitializeNPagedLookasideList</a>
</dt>
<dt>
<a href="ifsk.keinitializequeue">KeInitializeQueue</a>
</dt>
<dt>
<a href="ifsk.keinsertqueue">KeInsertQueue</a>
</dt>
<dt>
<a href="ifsk.keremovequeue">KeRemoveQueue</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20KeInsertHeadQueue routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

