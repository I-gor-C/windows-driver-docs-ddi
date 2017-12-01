---
UID: NF.ks.KsQueueWorkItem
title: KsQueueWorkItem
author: windows-driver-content
description: The KsQueueWorkItem function queues the specified work item with a worker previous created by the KsRegisterWorker function.
old-location: stream\ksqueueworkitem.htm
old-project: stream
ms.assetid: a700979e-aee4-4bce-8f98-b44b864fbb43
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsQueueWorkItem
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
req.alt-api: KsQueueWorkItem
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

# KsQueueWorkItem function



## -description
<p>The <b>KsQueueWorkItem</b> function queues the specified work item with a worker previous created by the <a href="..\ks\nf-ks-ksregisterworker.md">KsRegisterWorker</a> function.</p>


## -syntax

````
NTSTATUS KsQueueWorkItem(
  _In_ PKSWORKER        Worker,
  _In_ PWORK_QUEUE_ITEM WorkItem
);
````


## -parameters
<dl>

### -param <i>Worker</i> [in]

<dd>
<p>Specifies the previously allocated worker.</p>
</dd>

### -param <i>WorkItem</i> [in]

<dd>
<p>Specifies the initialized work item to queue. This work item is only associated with the worker as long as the worker is on a queue. The work item must have been initialized by <a href="..\wdm\nf-wdm-ioallocateworkitem.md">IoAllocateWorkItem</a>.</p>
</dd>
</dl>

## -returns
<p>The <b>KsQueueWorkItem</b> function returns STATUS_SUCCESS if the work item was queued, or if unsuccessful the function returns an error when attempting to create a new worker if no threads are currently available.</p>

## -remarks
<p>The worker can only be on a queue in one place, so subsequent queuing of the worker must wait until the work item has begun executing. This function may be called at <b>DISPATCH_LEVEL</b>.</p>

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