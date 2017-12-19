---
UID: NF.wdm.RemoveHeadList~r1
title: RemoveHeadList function
author: windows-driver-content
description: The RemoveHeadList routine removes an entry from the beginning of a doubly linked list of LIST_ENTRY structures.
old-location: kernel\removeheadlist.htm
old-project: kernel
ms.assetid: 8748451c-3e57-4acf-b1e6-b80fe7f461d8
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
req.product: Windows 10 or later.
---

# RemoveHeadList function



## -description
The <b>RemoveHeadList</b> routine removes an entry from the beginning of a doubly linked list of <a href="kernel.list_entry">LIST_ENTRY</a> structures. 



## -syntax

````
PLIST_ENTRY RemoveHeadList(
  _Inout_ PLIST_ENTRY ListHead
);
````


## -parameters

### -param ListHead [in, out]

Pointer to the <a href="kernel.list_entry">LIST_ENTRY</a> structure that serves as the list header.


## -returns
<b>RemoveHeadList</b> returns a pointer to the entry removed from the list. If the list is empty, <b>RemoveHeadList</b> returns <i>ListHead</i>. 


## -remarks
<b>RemoveHeadList</b> removes the first entry from the list by setting <i>ListHead</i>-&gt;<b>Flink</b> to point to the second entry in the list. The routine sets the <b>Blink</b> member of the second entry to <i>ListHead</i>. In the event the list is empty, this is effectively a no-op.

For information about using this routine when implementing a doubly linked list, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563802">Singly and Doubly Linked Lists</a>.

Callers of <b>RemoveHeadList</b> can be running at any IRQL. If <b>RemoveHeadList</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for <i>ListHead</i> and the list entries must be resident.


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
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level (See Remarks section)

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_cancelspinlock">CancelSpinLock</a>, <a href="devtest.wdm_completerequest">CompleteRequest</a>, <a href="devtest.wdm_doublecompletion">DoubleCompletion</a>, <a href="devtest.wdm_ioallocatefree">IoAllocateFree</a>, <a href="devtest.wdm_ioreuseirp">IoReuseIrp</a>, <a href="devtest.wdm_irpprocessingcomplete">IrpProcessingComplete</a>, <a href="devtest.wdm_markinginterlockedqueuedirps">MarkingInterlockedQueuedIrps</a>, <a href="devtest.wdm_markingqueuedirps">MarkingQueuedIrps</a>, <a href="devtest.wdm_markirppending">MarkIrpPending</a>, <a href="devtest.wdm_markirppending2">MarkIrpPending2</a>, <a href="devtest.wdm_pendedcompletedrequest">PendedCompletedRequest</a>, <a href="devtest.wdm_pendedcompletedrequest2">PendedCompletedRequest2</a>, <a href="devtest.wdm_pendedcompletedrequest3">PendedCompletedRequest3</a>, <a href="devtest.wdm_pendedcompletedrequestex">PendedCompletedRequestEx</a>, <a href="devtest.wdm_removelock">RemoveLock</a>, <a href="devtest.wdm_removelockcheck">RemoveLockCheck</a>, <a href="devtest.wdm_removelockforward">RemoveLockForward</a>, <a href="devtest.wdm_removelockforward2">RemoveLockForward2</a>, <a href="devtest.wdm_removelockforwarddevicecontrol">RemoveLockForwardDeviceControl</a>, <a href="devtest.wdm_removelockforwarddevicecontrol2">RemoveLockForwardDeviceControl2</a>, <a href="devtest.wdm_removelockforwarddevicecontrolinternal">RemoveLockForwardDeviceControlInternal</a>, <a href="devtest.wdm_removelockforwarddevicecontrolinternal2">RemoveLockForwardDeviceControlInternal2</a>, <a href="devtest.wdm_removelockforwardread">RemoveLockForwardRead</a>, <a href="devtest.wdm_removelockforwardread2">RemoveLockForwardRead2</a>, <a href="devtest.wdm_removelockforwardwrite">RemoveLockForwardWrite</a>, <a href="devtest.wdm_removelockforwardwrite2">RemoveLockForwardWrite2</a>, <a href="devtest.wdm_removelockmnremove">RemoveLockMnRemove</a>, <a href="devtest.wdm_removelockmnsurpriseremove">RemoveLockMnSurpriseRemove</a>, <a href="devtest.wdm_removelockrelease2">RemoveLockRelease2</a>, <a href="devtest.wdm_removelockreleasecleanup">RemoveLockReleaseCleanup</a>, <a href="devtest.wdm_removelockreleaseclose">RemoveLockReleaseClose</a>, <a href="devtest.wdm_removelockreleasecreate">RemoveLockReleaseCreate</a>, <a href="devtest.wdm_removelockreleasedevicecontrol">RemoveLockReleaseDeviceControl</a>, <a href="devtest.wdm_removelockreleaseinternaldevicecontrol">RemoveLockReleaseInternalDeviceControl</a>, <a href="devtest.wdm_removelockreleasepnp">RemoveLockReleasePnp</a>, <a href="devtest.wdm_removelockreleasepower">RemoveLockReleasePower</a>, <a href="devtest.wdm_removelockreleaseread">RemoveLockReleaseRead</a>, <a href="devtest.wdm_removelockreleaseshutdown">RemoveLockReleaseShutdown</a>, <a href="devtest.wdm_removelockreleasesystemcontrol">RemoveLockReleaseSystemControl</a>, <a href="devtest.wdm_removelockreleasewrite">RemoveLockReleaseWrite</a>, <a href="devtest.kmdf_invalidreqaccesslocal">InvalidReqAccessLocal</a>, <a href="devtest.storport_doubleexfreepool">DoubleExFreePool</a>, <a href="devtest.ndis_init_ndisallocateioworkitem">Init_NdisAllocateIoWorkItem</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exinterlockedremoveheadlist">ExInterlockedRemoveHeadList</a>
</dt>
<dt>
<a href="kernel.initializelisthead">InitializeListHead</a>
</dt>
<dt>
<a href="kernel.islistempty">IsListEmpty</a>
</dt>
<dt>
<a href="kernel.removetaillist">RemoveTailList</a>
</dt>
<dt>
<a href="kernel.removeentrylist">RemoveEntryList</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RemoveHeadList routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

