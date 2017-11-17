---
UID: NF.ks.KsRegisterWorker
title: KsRegisterWorker
author: windows-driver-content
description: The KsRegisterWorker function handles clients registering for use of a thread.
old-location: stream\ksregisterworker.htm
ms.assetid: b9c74a56-3f2c-4b94-8fb2-6b44075ec34b
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsRegisterWorker
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
ms.keywords: KsRegisterWorker
req.iface: 
---

# KsRegisterWorker function



## -description
<p>The <b>KsRegisterWorker</b> function handles clients registering for use of a thread. The function can create a new thread of the specified priority if there are currently no free threads available. This must be matched by a corresponding <b>KsUnregisterWorker</b> when thread use is completed. The function can only be called at PASSIVE_LEVEL.</p>


## -syntax

````
typedef PVOID PKSWORKER; 
````


## -parameters
<dl>

### -param <i>WorkQueueType</i> [in]

<dd>
<p>Specifies the priority of the thread to create. This is usually either CriticalWorkQueue<b>, </b>DelayedWorkQueue, or HyperCriticalWorkQueue<b>.</b></p>
</dd>

### -param <i>Worker</i> [out]

<dd>
<p>Location to put the opaque context that must be used when scheduling a work item. This contains the queue type and is used to synchronize completion of work items.</p>
</dd>
</dl>

## -returns
<p>The <b>KsRegisterWorker</b> function returns STATUS_SUCCESS if a worker was initialized, or if unsuccessful the function returns a thread or parameter error.</p>

## -remarks


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