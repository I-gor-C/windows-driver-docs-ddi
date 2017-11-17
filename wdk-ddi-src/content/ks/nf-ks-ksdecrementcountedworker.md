---
UID: NF.ks.KsDecrementCountedWorker
title: KsDecrementCountedWorker
author: windows-driver-content
description: Decrements the current worker count of a worker previous created by KsRegisterCountedWorker. This should be called after each task within a worker has been completed.
old-location: stream\ksdecrementcountedworker.htm
ms.assetid: 2b38e4df-e5b6-480b-bd4e-62e059e26411
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
req.alt-api: KsDecrementCountedWorker
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
ms.keywords: KsDecrementCountedWorker
req.iface: 
---

# KsDecrementCountedWorker function



## -description
<p>Decrements the current worker count of a worker previous created by <a href="https://msdn.microsoft.com/library/windows/hardware/ff566770">KsRegisterCountedWorker</a>. This should be called after each task within a worker has been completed. </p>


## -syntax

````
ULONG KsDecrementCountedWorker(
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
<p>Returns the current counter. A count of zero implies that the task list has been completed.</p>

## -remarks
<p><b>KsDecrementCountedWorker</b> should be called after each task within a worker has been completed. A corresponding call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562678">KsIncrementCountedWorker</a> would have previously incremented the count. <b>KsDecrementCountedWorker</b> may be called at DISPATCH_LEVEL.</p>

<p><b>KsDecrementCountedWorker</b> should be called after each task within a worker has been completed. A corresponding call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562678">KsIncrementCountedWorker</a> would have previously incremented the count. <b>KsDecrementCountedWorker</b> may be called at DISPATCH_LEVEL.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562678">KsIncrementCountedWorker</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566770">KsRegisterCountedWorker</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsDecrementCountedWorker function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
