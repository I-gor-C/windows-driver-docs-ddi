---
UID: NF.rxcontx.__RxSynchronizeBlockingOperations
title: __RxSynchronizeBlockingOperations
author: windows-driver-content
description: __RxSynchronizeBlockingOperations synchronizes blocking I/O requests to the same work queue.
old-location: ifsk\__rxsynchronizeblockingoperations.htm
old-project: ifsk
ms.assetid: e957f8bc-2ce3-4b9c-819e-ee068b39c4a0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: __RxSynchronizeBlockingOperations
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxcontx.h
req.include-header: Rxcontx.h
req.target-type: Desktop
req.target-min-winverclnt: The __RxSynchronizeBlockingOperations routine is only available on Windows Server 2003.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: __RxSynchronizeBlockingOperations
req.alt-loc: rxcontx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# __RxSynchronizeBlockingOperations function



## -description
<p><b>__RxSynchronizeBlockingOperations</b> synchronizes blocking I/O requests to the same work queue. </p>


## -syntax

````
NTSTATUS __RxSynchronizeBlockingOperations(
  _Inout_ PRX_CONTEXT RxContext,
  _In_    PFCB        Fcb,
  _Inout_ PLIST_ENTRY BlockingIoQ,
  _In_    BOOLEAN     DropFcbLock
);
````


## -parameters
<dl>

### -param <i>RxContext</i> [in, out]

<dd>
<p>A pointer to the RX_CONTEXT of the operation being synchronized. </p>
</dd>

### -param <i>Fcb</i> [in]

<dd>
<p>A pointer to the FCB. </p>
</dd>

### -param <i>BlockingIoQ</i> [in, out]

<dd>
<p>A pointer to the LIST_ENTRY for the queue. </p>
</dd>

### -param <i>DropFcbLock</i> [in]

<dd>
<p>A Boolean value that indicates if the FCB resource should be released. If this parameter is <b>TRUE</b>, then the FCB resource will be released. </p>
</dd>
</dl>

## -returns
<p><b>__RxSynchronizeBlockingOperations</b> returns STATUS_SUCCESS on success or an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_CANCELLED</b></dt>
</dl><p>The I/O request and the associated RX_CONTEXT was canceled.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The <i>RxContext</i> was for an asynchronous operation and the <i>RxContext</i> has been added to the queue.</p>

<p> </p>

## -remarks
<p>The<b> __RxSynchronizeBlockingOperations</b> routine synchronizes blocking I/O requests to the same work queue. RDBSS uses <b>__RxSynchronizeBlockingOperations</b> internally to synchronize named pipe operations. The work queue is the queue referenced by the file object extension (FOBX) associated with the <i>Fcb</i>. </p>

<p>A network mini-redirector may use <b>__RxSynchronizeBlockingOperations</b> to synchronize operations on a separate queue that is maintained by the network mini-redirector. </p>

<p>If <i>RxContext</i> is marked for an asynchronous operation, <b>__RxSynchronizeBlockingOperations</b> will add the <i>RxContext</i> to the queue and return STATUS_PENDING. If <i>RxContext</i> is marked for a synchronous operation, <b>__RxSynchronizeBlockingOperations</b> will block and <i>RxContext</i> is resumed when a call is made to <a href="..\rxcontx\nf-rxcontx-rxresumeblockedoperations-serially.md">RxResumeBlockedOperations_Serially</a>. </p>

<p>If the blocking I/O request was canceled, <b>__RxSynchronizeBlockingOperations</b> returns STATUS_CANCELLED to indicate the error.</p>

<p>The <b>SyncEvent</b> member of the RX_CONTEXT structure pointed to by <i>RxContext</i> must have been reset before calling <b>__RxSynchronizeBlockingOperations</b>. The FCB resource must be locked before calling <b>__RxSynchronizeBlockingOperations</b> if the <i>DropFcbLock</i> parameter is set to <b>TRUE</b>. </p>

<p>The following two macros are defined on Windows Server 2003 or later for calling <b>__RxSynchronizeBlockingOperations</b>:</p>

<p><b>RxSynchronizeBlockingOperations</b> - calls with the <i>DropFcbLock</i> parameter set to <b>FALSE</b>. </p>

<p><b>RxSynchronizeBlockingOperationsAndDropFcbLock</b> - calls with the <i>DropFcbLock</i> parameter set to <b>TRUE</b>. </p>

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
<p>The __RxSynchronizeBlockingOperations routine is only available on Windows Server 2003. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Rxcontx.h (include Rxcontx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\rxprocs\nf-rxprocs-rxcompleterequest-real.md">RxCompleteRequest_Real</a>
</dt>
<dt>
<a href="..\rxcontx\nf-rxcontx-rxcreaterxcontext.md">RxCreateRxContext</a>
</dt>
<dt>
<a href="..\rxprocs\nf-rxprocs-rxdereference.md">RxDereference</a>
</dt>
<dt>
<a href="..\rxcontx\nf-rxcontx-rxdereferenceanddeleterxcontext-real.md">RxDereferenceAndDeleteRxContext_Real</a>
</dt>
<dt>
<a href="..\rxcontx\nf-rxcontx-rxinitializecontext.md">RxInitializeContext</a>
</dt>
<dt>
<a href="..\rxcontx\nf-rxcontx-rxpreparecontextforreuse.md">RxPrepareContextForReuse</a>
</dt>
<dt>
<a href="..\rxcontx\nf-rxcontx-rxresumeblockedoperations-serially.md">RxResumeBlockedOperations_Serially</a>
</dt>
<dt>
<a href="ifsk.__rxsynchronizeblockingoperationsmaybedroppingfcblock">__RxSynchronizeBlockingOperationsMaybeDroppingFcbLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20__RxSynchronizeBlockingOperations function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
