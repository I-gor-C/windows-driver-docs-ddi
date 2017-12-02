---
UID: NF.ks.KsUnregisterWorker
title: KsUnregisterWorker
author: windows-driver-content
description: The KsUnregisterWorker function allows clients to unregister a worker.
old-location: stream\ksunregisterworker.htm
old-project: stream
ms.assetid: 789b12db-7f51-426f-8f43-d3a3e43d85b3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsUnregisterWorker
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
req.alt-api: KsUnregisterWorker
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

# KsUnregisterWorker function



## -description
<p>The <b>KsUnregisterWorker</b> function allows clients to unregister a worker. The function can destroy threads, depending on the number of threads in use. This must only be used after successful execution of <b>KsRegisterWorker</b>. The function can only be called at PASSIVE_LEVEL.</p>


## -syntax

````
VOID KsUnregisterWorker(
  _In_ PKSWORKER Worker
);
````


## -parameters
<dl>

### -param Worker [in]

<dd>
<p>Specifies the previously allocated worker to be unregistered. The function will wait until any outstanding work item is completed.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The client must ensure that outstanding I/O initiated on any worker thread has been completed before unregistering the worker has been completed. This means canceling or completing outstanding I/O either before unregistering the worker, or before the worker item returns from its callback for the last time and is unregistered. Unregistering of a worker will wait for any currently queued work items to complete before returning. </p>

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