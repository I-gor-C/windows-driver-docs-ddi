---
UID: NF.ntifs.KeInitializeQueue
title: KeInitializeQueue
author: windows-driver-content
description: The KeInitializeQueue routine initializes a queue object on which threads can wait for entries.
old-location: ifsk\keinitializequeue.htm
ms.assetid: 8dd47333-679a-482b-bd45-1e73505b3fea
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeInitializeQueue
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
ms.keywords: KeInitializeQueue
req.iface: 
---

# KeInitializeQueue function



## -description
<p>The <b>KeInitializeQueue</b> routine initializes a queue object on which threads can wait for entries. </p>


## -syntax

````
VOID KeInitializeQueue(
  _Out_ PRKQUEUE Queue,
  _In_  ULONG    Count
);
````


## -parameters
<dl>

### -param <i>Queue</i> [out]

<dd>
<p>Pointer to a KQUEUE structure for which the caller must provide resident storage in nonpaged pool. This structure is defined as follows:</p>
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
<p><b>Header</b></p>
</td>
<td>
<p>Queue header.</p>
</td>
</tr>
<tr>
<td>
<p><b>EntryListHead</b></p>
</td>
<td>
<p>Pointer to the first entry in the queue.</p>
</td>
</tr>
<tr>
<td>
<p><b>CurrentCount</b></p>
</td>
<td>
<p>Current number of threads waiting on the queue.</p>
</td>
</tr>
<tr>
<td>
<p><b>MaximumCount</b></p>
</td>
<td>
<p>Maximum number of concurrent threads the queue can satisfy waits for.</p>
</td>
</tr>
<tr>
<td>
<p><b>ThreadListHead</b></p>
</td>
<td>
<p>Pointer to the first entry in the thread list.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Count</i> [in]

<dd>
<p>The maximum number of threads for which the waits on the queue object can be satisfied concurrently. If this parameter is not supplied, the number of processors in the machine is used.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Usually the caller of <b>KeInitializeQueue</b> also creates a set of dedicated threads to queue and dequeue its entries. Such a caller can specify an explicit <i>Count</i> to prevent too many of its dedicated threads from waiting concurrently on its queue object. </p>

<p><b>KeInitializeQueue</b> sets the queue object's initial signal state to Not Signaled.</p>

<p>For more information about using driver-managed internal queues, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544165">Driver-Managed Queues</a>. </p>

<p>Usually the caller of <b>KeInitializeQueue</b> also creates a set of dedicated threads to queue and dequeue its entries. Such a caller can specify an explicit <i>Count</i> to prevent too many of its dedicated threads from waiting concurrently on its queue object. </p>

<p><b>KeInitializeQueue</b> sets the queue object's initial signal state to Not Signaled.</p>

<p>For more information about using driver-managed internal queues, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544165">Driver-Managed Queues</a>. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548276">IoAllocateWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549466">IoQueueWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549570">KeInsertQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549605">KeRemoveQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549638">KeRundownQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559932">PsCreateSystemThread</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20KeInitializeQueue routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
