---
UID: NF.rxworkq.RxDispatchToWorkerThread
title: RxDispatchToWorkerThread
author: windows-driver-content
description: RxDispatchToWorkerThread invokes a routine in the context of a worker thread. The memory for the WORK_QUEUE_ITEM is allocated by this routine.
old-location: ifsk\rxdispatchtoworkerthread.htm
old-project: ifsk
ms.assetid: 426d28fa-abfe-44d9-9b15-119f92367b40
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxDispatchToWorkerThread
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
req.alt-api: RxDispatchToWorkerThread
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

# RxDispatchToWorkerThread function



## -description
<p><b>RxDispatchToWorkerThread</b> invokes a routine in the context of a worker thread. The memory for the WORK_QUEUE_ITEM is allocated by this routine.  </p>


## -syntax

````
NTSTATUS RxDispatchToWorkerThread(
  _In_ PRDBSS_DEVICE_OBJECT     pMRxDeviceObject,
  _In_ WORK_QUEUE_TYPE          WorkQueueType,
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
<p>The type of the work queue representing the priority of the task. The <i>WorkQueueType</i> parameter can be one of can be one of the following enumerations for WORK_QUEUE_TYPE:</p>
<p></p>
<dl>

### -param <a id="CriticalWorkQueue"></a><a id="criticalworkqueue"></a><a id="CRITICALWORKQUEUE"></a>CriticalWorkQueue

<dd>
<p>Insert the WORK_QUEUE_ITEM into the queue from which a system thread with a real-time priority attribute will process the work item.</p>
</dd>

### -param <a id="DelayedWorkQueue"></a><a id="delayedworkqueue"></a><a id="DELAYEDWORKQUEUE"></a>DelayedWorkQueue

<dd>
<p>Insert the WORK_QUEUE_ITEM into the queue from which a system thread with a variable priority attribute will process the work item.</p>
</dd>

### -param <a id="HyperCriticalWorkQueue"></a><a id="hypercriticalworkqueue"></a><a id="HYPERCRITICALWORKQUEUE"></a>HyperCriticalWorkQueue

<dd>
<p>Insert the WORK_QUEUE_ITEM into the queue from which a system thread will process the work item so that the routine to be invoked is not blocked.</p>
</dd>
</dl>
</dd>

### -param <i>Routine</i> [in]

<dd>
<p>A pointer to the routine to be invoked.</p>
</dd>

### -param <i>pContext</i> [in]

<dd>
<p>A pointer to a context parameter associated with the work item to complete that is passed to the driver.</p>
</dd>
</dl>

## -returns
<p><b>RxDispatchToWorkerThread</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The item could not be dispatched.</p>

<p> </p>

## -remarks
<p>There are two common cases of dispatching operations to worker threads:</p>

<p>For a very infrequent operation, space can be conserved by dynamically allocating and freeing memory for the work queue item when its is needed. The <b>RxDispatchToWorkerThread</b> routine would be used in this case </p>

<p>When an operation is going to be repeatedly dispatched, time is conserved by allocating in advance the WORK_QUEUE_ITEM as part of the data structure to be dispatched and using this pre-allocated memory repeatedly. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff554620">RxPostToWorkerThread</a> routine would be used in this case </p>

<p>The trade off between the two dispatching operations is time versus space (memory usage).</p>

<p>The <b>RxDispatchToWorkerThread</b> invokes a routine in the context of a worker thread. The memory for the WORK_QUEUE_ITEM is allocated by the <b>RxDispatchToWorkerThread</b> routine from non-paged pool memory. Hence this routine can fail if insufficient resources are available. </p>

<p>The current implementation of the <b>RxDispatchToWorkerThread </b>routine queues work onto the same processor from which the call originated. </p>

<p>If the <b>RxDispatchToWorkerThread </b>routine fails on a debug build, the <b>_RxLog</b> routine is called with details of the error. If the <b>RxDispatchToWorkerThread </b>routine fails and WMI is enabled in the kernel, details of the error will be logged with WMI.</p>

<p>There are two common cases of dispatching operations to worker threads:</p>

<p>For a very infrequent operation, space can be conserved by dynamically allocating and freeing memory for the work queue item when its is needed. The <b>RxDispatchToWorkerThread</b> routine would be used in this case </p>

<p>When an operation is going to be repeatedly dispatched, time is conserved by allocating in advance the WORK_QUEUE_ITEM as part of the data structure to be dispatched and using this pre-allocated memory repeatedly. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff554620">RxPostToWorkerThread</a> routine would be used in this case </p>

<p>The trade off between the two dispatching operations is time versus space (memory usage).</p>

<p>The <b>RxDispatchToWorkerThread</b> invokes a routine in the context of a worker thread. The memory for the WORK_QUEUE_ITEM is allocated by the <b>RxDispatchToWorkerThread</b> routine from non-paged pool memory. Hence this routine can fail if insufficient resources are available. </p>

<p>The current implementation of the <b>RxDispatchToWorkerThread </b>routine queues work onto the same processor from which the call originated. </p>

<p>If the <b>RxDispatchToWorkerThread </b>routine fails on a debug build, the <b>_RxLog</b> routine is called with details of the error. If the <b>RxDispatchToWorkerThread </b>routine fails and WMI is enabled in the kernel, details of the error will be logged with WMI.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554620">RxPostToWorkerThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554734">RxSpinDownMRxDispatcher</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxDispatchToWorkerThread routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
