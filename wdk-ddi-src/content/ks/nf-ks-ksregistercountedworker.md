---
UID: NF.ks.KsRegisterCountedWorker
title: KsRegisterCountedWorker
author: windows-driver-content
description: Handles clients registering for use of a thread.
old-location: stream\ksregistercountedworker.htm
old-project: stream
ms.assetid: acec8050-44bd-4082-9875-d504135e1b9f
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsRegisterCountedWorker
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsRegisterCountedWorker
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
req.iface: 
---

# KsRegisterCountedWorker function



## -description
<p>Handles clients registering for use of a thread.</p>


## -syntax

````
NTSTATUS KsRegisterCountedWorker(
  _In_  WORK_QUEUE_TYPE  WorkQueueType,
  _In_  PWORK_QUEUE_ITEM CountedWorkItem,
  _Out_ PKSWORKER        *Worker
);
````


## -parameters
<dl>

### -param <i>WorkQueueType</i> [in]

<dd>
<p>Contains the priority of the work thread. This is normally one of the following: CriticalWorkQueue, DelayedWorkQueue, or HyperCriticalWorkQueue.</p>
</dd>

### -param <i>CountedWorkItem</i> [in]

<dd>
<p>Contains a pointer to the work queue item that will be queued as needed based on the current count value.</p>
</dd>

### -param <i>Worker</i> [out]

<dd>
<p>Contains the opaque context that must be used when scheduling a work item. Also contains the queue type, and is used to synchronize completion of work items.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if a worker was initialized.</p>

## -remarks
<p>This must be matched by a corresponding <a href="https://msdn.microsoft.com/library/windows/hardware/ff567209">KsUnregisterWorker</a> when thread use is completed. This function resembles <a href="https://msdn.microsoft.com/library/windows/hardware/ff566775">KsRegisterWorker</a>, with the addition of passing the work item that will always be queued. This is to be used with <a href="https://msdn.microsoft.com/library/windows/hardware/ff562678">KsIncrementCountedWorker</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff561660">KsDecrementCountedWorker</a> in order to minimize the number of work items queued, and reduce mutual exclusion code necessary in a work item needed to serialize access against multiple work item threads. The worker queue can still be used to queue other work items. This may only be called at PASSIVE_LEVEL.</p>

<p>This must be matched by a corresponding <a href="https://msdn.microsoft.com/library/windows/hardware/ff567209">KsUnregisterWorker</a> when thread use is completed. This function resembles <a href="https://msdn.microsoft.com/library/windows/hardware/ff566775">KsRegisterWorker</a>, with the addition of passing the work item that will always be queued. This is to be used with <a href="https://msdn.microsoft.com/library/windows/hardware/ff562678">KsIncrementCountedWorker</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff561660">KsDecrementCountedWorker</a> in order to minimize the number of work items queued, and reduce mutual exclusion code necessary in a work item needed to serialize access against multiple work item threads. The worker queue can still be used to queue other work items. This may only be called at PASSIVE_LEVEL.</p>

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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>