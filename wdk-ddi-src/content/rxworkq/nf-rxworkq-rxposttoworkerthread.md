---
UID: NF.rxworkq.RxPostToWorkerThread
title: RxPostToWorkerThread
author: windows-driver-content
description: RxPostToWorkerThread invokes a routine passed as a parameter in the context of a worker thread. Memory for the WORK_QUEUE_ITEM must be allocated by the caller.
old-location: ifsk\rxposttoworkerthread.htm
old-project: ifsk
ms.assetid: 0fc9fb57-219e-4a3d-bc82-904ab8657d66
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxPostToWorkerThread
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxworkq.h
req.include-header: Rxworkq.h, Rxstruc.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxPostToWorkerThread
req.alt-loc: rxworkq.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# RxPostToWorkerThread function



## -description
<p><b>RxPostToWorkerThread</b> invokes a routine passed as a parameter in the context of a worker thread. Memory for the WORK_QUEUE_ITEM must be allocated by the caller.</p>


## -syntax

````
NTSTATUS RxPostToWorkerThread(
  _In_ PRDBSS_DEVICE_OBJECT     pMRxDeviceObject,
  _In_ WORK_QUEUE_TYPE          WorkQueueType,
  _In_ PRX_WORK_QUEUE_ITEM      pWorkQueueItem,
  _In_ PRX_WORKERTHREAD_ROUTINE Routine,
  _In_ PVOID                    pContext
);
````


## -parameters
<dl>

### -param <i>pMRxDeviceObject</i> [in]

<dd>
<p>A pointer to the device object of the corresponding network mini-redirector driver.</p>
</dd>

### -param <i>WorkQueueType</i> [in]

<dd>
<p>The type of the work queue that represents the priority of the task. This parameter can be one of the following values:</p>
<p></p>
<dl>

### -param <a id="CriticalWorkQueue"></a><a id="criticalworkqueue"></a><a id="CRITICALWORKQUEUE"></a><b>CriticalWorkQueue</b>

<dd>
<p>Insert WORK_QUEUE_ITEM into the queue from which a system thread with a real-time priority attribute will process the work item.</p>
</dd>

### -param <a id="DelayedWorkQueue"></a><a id="delayedworkqueue"></a><a id="DELAYEDWORKQUEUE"></a><b>DelayedWorkQueue</b>

<dd>
<p>Insert WORK_QUEUE_ITEM into the queue from which a system thread with a variable priority attribute will process the work item.</p>
</dd>

### -param <a id="HyperCriticalWorkQueue"></a><a id="hypercriticalworkqueue"></a><a id="HYPERCRITICALWORKQUEUE"></a><b>HyperCriticalWorkQueue</b>

<dd>
<p>Insert WORK_QUEUE_ITEM into the queue from which a system thread will process the work item so that the routine to invoke is not blocked.</p>
</dd>
</dl>
</dd>

### -param <i>pWorkQueueItem</i> [in]

<dd>
<p>A pointer to WORK_QUEUE_ITEM.</p>
</dd>

### -param <i>Routine</i> [in]

<dd>
<p>A pointer to the routine to invoke.</p>
</dd>

### -param <i>pContext</i> [in]

<dd>
<p>A pointer to a context parameter associated with the work item to complete that is passed to the driver.</p>
</dd>
</dl>

## -returns
<p><b>RxDispatchToWorkerThread</b> returns STATUS_SUCCESS on success or one of the following error code on failure: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The item could not be dispatched.</p>

<p> </p>

## -remarks
<p>There are two common cases of dispatching operations to worker threads. The trade-off between the following two dispatching operations is time versus space (memory usage):</p>

<p>When an operation is going to be repeatedly dispatched, time is conserved by allocating in advance the WORK_QUEUE_ITEM structure as part of the data structure to be dispatched. In this case, use the <b>RxPostToWorkerThread</b> routine. </p>

<p>For an infrequent operation, you can conserve space by dynamically allocating and freeing memory for the work queue item when it is needed. In this case, use the <a href="..\rxworkq\nf-rxworkq-rxdispatchtoworkerthread.md">RxDispatchToWorkerThread</a> routine. </p>

<p>The <b>RxPostToWorkerThread</b> routine invokes a routine in the context of a worker thread. The memory for the WORK_QUEUE_ITEM structure must be allocated from non-paged pool memory by the calling routine. </p>

<p>The current implementation of the <b>RxPostToWorkerThread </b>routine queues work onto the same processor from which the call originated. </p>

<p>If the <b>RxPostToWorkerThread </b>routine fails on a debug build, the <a href="..\rxlog\nf-rxlog--rxlog.md">_RxLog</a> routine is called with details of the error. If the <b>RxPostToWorkerThread </b>routine fails and WMI is enabled in the kernel, details of the error will be logged with WMI.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Rxworkq.h (include Rxworkq.h, Rxstruc.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\rxlog\nf-rxlog--rxlog.md">_RxLog</a>
</dt>
<dt>
<a href="..\rxworkq\nf-rxworkq-rxdispatchtoworkerthread.md">RxDispatchToWorkerThread</a>
</dt>
<dt>
<a href="..\rxworkq\nf-rxworkq-rxspindownmrxdispatcher.md">RxSpinDownMRxDispatcher</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxPostToWorkerThread routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
