---
UID: NF.wdm.RemoveHeadList~r1
title: RemoveHeadList
author: windows-driver-content
description: The RemoveHeadList routine removes an entry from the beginning of a doubly linked list of LIST_ENTRY structures.
old-location: kernel\removeheadlist.htm
old-project: kernel
ms.assetid: 8748451c-3e57-4acf-b1e6-b80fe7f461d8
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RemoveHeadList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RemoveHeadList
req.alt-loc: Wdm.h
req.ddi-compliance: CancelSpinLock, CompleteRequest, DoubleCompletion, IoAllocateFree, IoReuseIrp, IrpProcessingComplete, MarkingInterlockedQueuedIrps, MarkingQueuedIrps, MarkIrpPending, MarkIrpPending2, PendedCompletedRequest, PendedCompletedRequest2, PendedCompletedRequest3, PendedCompletedRequestEx, RemoveLock, RemoveLockCheck, RemoveLockForward, RemoveLockForward2, RemoveLockForwardDeviceControl, RemoveLockForwardDeviceControl2, RemoveLockForwardDeviceControlInternal, RemoveLockForwardDeviceControlInternal2, RemoveLockForwardRead, RemoveLockForwardRead2, RemoveLockForwardWrite, RemoveLockForwardWrite2, RemoveLockMnRemove, RemoveLockMnSurpriseRemove, RemoveLockRelease2, RemoveLockReleaseCleanup, RemoveLockReleaseClose, RemoveLockReleaseCreate, RemoveLockReleaseDeviceControl, RemoveLockReleaseInternalDeviceControl, RemoveLockReleasePnp, RemoveLockReleasePower, RemoveLockReleaseRead, RemoveLockReleaseShutdown, RemoveLockReleaseSystemControl, RemoveLockReleaseWrite, InvalidReqAccessLocal, DoubleExFreePool, Init_NdisAllocateIoWorkItem
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level (See Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# RemoveHeadList function



## -description
<p>The <b>RemoveHeadList</b> routine removes an entry from the beginning of a doubly linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff554296">LIST_ENTRY</a> structures. </p>


## -syntax

````
PLIST_ENTRY RemoveHeadList(
  _Inout_ PLIST_ENTRY ListHead
);
````


## -parameters
<dl>

### -param <i>ListHead</i> [in, out]

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554296">LIST_ENTRY</a> structure that serves as the list header.</p>
</dd>
</dl>

## -returns
<p><b>RemoveHeadList</b> returns a pointer to the entry removed from the list. If the list is empty, <b>RemoveHeadList</b> returns <i>ListHead</i>. </p>

## -remarks
<p><b>RemoveHeadList</b> removes the first entry from the list by setting <i>ListHead</i>-&gt;<b>Flink</b> to point to the second entry in the list. The routine sets the <b>Blink</b> member of the second entry to <i>ListHead</i>. In the event the list is empty, this is effectively a no-op.</p>

<p>For information about using this routine when implementing a doubly linked list, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563802">Singly and Doubly Linked Lists</a>.</p>

<p>Callers of <b>RemoveHeadList</b> can be running at any IRQL. If <b>RemoveHeadList</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for <i>ListHead</i> and the list entries must be resident.</p>

<p><b>RemoveHeadList</b> removes the first entry from the list by setting <i>ListHead</i>-&gt;<b>Flink</b> to point to the second entry in the list. The routine sets the <b>Blink</b> member of the second entry to <i>ListHead</i>. In the event the list is empty, this is effectively a no-op.</p>

<p>For information about using this routine when implementing a doubly linked list, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563802">Singly and Doubly Linked Lists</a>.</p>

<p>Callers of <b>RemoveHeadList</b> can be running at any IRQL. If <b>RemoveHeadList</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for <i>ListHead</i> and the list entries must be resident.</p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level (See Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh454175">CancelSpinLock</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975143">CompleteRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff819059">DoubleCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975154">IoAllocateFree</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549661">IoReuseIrp</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547325">IrpProcessingComplete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549015">MarkingInterlockedQueuedIrps</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549016">MarkingQueuedIrps</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549018">MarkIrpPending</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549021">MarkIrpPending2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550374">PendedCompletedRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975198">PendedCompletedRequest2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975199">PendedCompletedRequest3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975200">PendedCompletedRequestEx</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975206">RemoveLock</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975207">RemoveLockCheck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975208">RemoveLockForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975209">RemoveLockForward2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975210">RemoveLockForwardDeviceControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975211">RemoveLockForwardDeviceControl2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975212">RemoveLockForwardDeviceControlInternal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975213">RemoveLockForwardDeviceControlInternal2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975214">RemoveLockForwardRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975215">RemoveLockForwardRead2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975216">RemoveLockForwardWrite</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975217">RemoveLockForwardWrite2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975232">RemoveLockMnRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975234">RemoveLockMnSurpriseRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975236">RemoveLockRelease2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975237">RemoveLockReleaseCleanup</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975238">RemoveLockReleaseClose</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975239">RemoveLockReleaseCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975240">RemoveLockReleaseDeviceControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975241">RemoveLockReleaseInternalDeviceControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975242">RemoveLockReleasePnp</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975243">RemoveLockReleasePower</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975244">RemoveLockReleaseRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975245">RemoveLockReleaseShutdown</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975246">RemoveLockReleaseSystemControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975247">RemoveLockReleaseWrite</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547267">InvalidReqAccessLocal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454214">DoubleExFreePool</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975103">Init_NdisAllocateIoWorkItem</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545427">ExInterlockedRemoveHeadList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547799">InitializeListHead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551789">IsListEmpty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561036">RemoveTailList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561029">RemoveEntryList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RemoveHeadList routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
