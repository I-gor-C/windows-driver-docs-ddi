---
UID: NF.ks.KsRegisterCountedWorker
title: KsRegisterCountedWorker function
author: windows-driver-content
description: Handles clients registering for use of a thread.
old-location: stream\ksregistercountedworker.htm
old-project: stream
ms.assetid: acec8050-44bd-4082-9875-d504135e1b9f
ms.author: windowsdriverdev
ms.date: 12/14/2017
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
---

# KsRegisterCountedWorker function



## -description
Handles clients registering for use of a thread.



## -syntax

````
NTSTATUS KsRegisterCountedWorker(
  _In_  WORK_QUEUE_TYPE  WorkQueueType,
  _In_  PWORK_QUEUE_ITEM CountedWorkItem,
  _Out_ PKSWORKER        *Worker
);
````


## -parameters

### -param WorkQueueType [in]

Contains the priority of the work thread. This is normally one of the following: CriticalWorkQueue, DelayedWorkQueue, or HyperCriticalWorkQueue.


### -param CountedWorkItem [in]

Contains a pointer to the work queue item that will be queued as needed based on the current count value.


### -param Worker [out]

Contains the opaque context that must be used when scheduling a work item. Also contains the queue type, and is used to synchronize completion of work items.


## -returns
Returns STATUS_SUCCESS if a worker was initialized.


## -remarks
This must be matched by a corresponding <a href="stream.ksunregisterworker">KsUnregisterWorker</a> when thread use is completed. This function resembles <a href="stream.ksregisterworker">KsRegisterWorker</a>, with the addition of passing the work item that will always be queued. This is to be used with <a href="stream.ksincrementcountedworker">KsIncrementCountedWorker</a> and <a href="stream.ksdecrementcountedworker">KsDecrementCountedWorker</a> in order to minimize the number of work items queued, and reduce mutual exclusion code necessary in a work item needed to serialize access against multiple work item threads. The worker queue can still be used to queue other work items. This may only be called at PASSIVE_LEVEL.


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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>