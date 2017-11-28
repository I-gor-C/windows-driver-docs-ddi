---
UID: NF.ks.KsIncrementCountedWorker
title: KsIncrementCountedWorker
author: windows-driver-content
description: Increments the current worker count, and optionally queues the counted work item with the worker previously created by KsRegisterCountedWorker.
old-location: stream\ksincrementcountedworker.htm
old-project: stream
ms.assetid: 282ffc00-ca62-4729-afe3-c13ea8069a18
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsIncrementCountedWorker
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
req.alt-api: KsIncrementCountedWorker
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

# KsIncrementCountedWorker function



## -description
<p>Increments the current worker count, and optionally queues the counted work item with the worker previously created by <a href="https://msdn.microsoft.com/library/windows/hardware/ff566770">KsRegisterCountedWorker</a>.</p>


## -syntax

````
ULONG KsIncrementCountedWorker(
  _In_ PKSWORKER Worker
);
````


## -parameters
<dl>

### -param <i>Worker</i> [in]

<dd>
<p>Contains the previously allocated worker.</p>
</dd>
</dl>

## -returns
<p>Returns the current counter. A count of one implies that a worker was actually scheduled.</p>

## -remarks
<p>This should be called after an addition has been made to the worker's list of tasks to perform. A corresponding call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff561660">KsDecrementCountedWorker</a> should be made within the work item after each task has been completed. This may be called at DISPATCH_LEVEL.</p>

<p>This should be called after an addition has been made to the worker's list of tasks to perform. A corresponding call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff561660">KsDecrementCountedWorker</a> should be made within the work item after each task has been completed. This may be called at DISPATCH_LEVEL.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561660">KsDecrementCountedWorker</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566770">KsRegisterCountedWorker</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsIncrementCountedWorker function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
