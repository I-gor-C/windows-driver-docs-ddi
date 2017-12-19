---
UID: NF.fltkernel.FltAllocateDeferredIoWorkItem
title: FltAllocateDeferredIoWorkItem function
author: windows-driver-content
description: FltAllocateDeferredIoWorkItem allocates a deferred-I/O work item.
old-location: ifsk\fltallocatedeferredioworkitem.htm
old-project: ifsk
ms.assetid: 25c03114-8e50-40a2-869a-08b11b7490be
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FltAllocateDeferredIoWorkItem
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltAllocateDeferredIoWorkItem
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
---

# FltAllocateDeferredIoWorkItem function



## -description
<b>FltAllocateDeferredIoWorkItem</b> allocates a deferred-I/O work item. 



## -syntax

````
PFLT_DEFERRED_IO_WORKITEM FltAllocateDeferredIoWorkItem(void);
````


## -parameters


## -returns
<b>FltAllocateDeferredIoWorkItem</b> returns <b>NULL</b> if there is insufficient memory in nonpaged pool to satisfy the request. Otherwise, it returns a pointer to the allocated work item. 

<b>FltAllocateDeferredIoWorkItem</b> returns <b>NULL</b> if there is insufficient memory in nonpaged pool to satisfy the request. Otherwise, it returns a pointer to the allocated work item. 

<b>FltAllocateDeferredIoWorkItem</b> returns <b>NULL</b> if there is insufficient memory in nonpaged pool to satisfy the request. Otherwise, it returns a pointer to the allocated work item. 


## -remarks
<b>FltAllocateDeferredIoWorkItem</b> allocates a deferred I/O work item from nonpaged pool. 

To insert this work item into a deferred I/O work queue, call <a href="ifsk.fltqueuedeferredioworkitem">FltQueueDeferredIoWorkItem</a>. 

To free the work item, a minifilter driver typically calls <a href="ifsk.fltfreedeferredioworkitem">FltFreeDeferredIoWorkItem</a> from the worker routine that was specified in <a href="ifsk.fltqueuedeferredioworkitem">FltQueueDeferredIoWorkItem</a>. 


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
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fltfreedeferredioworkitem">FltFreeDeferredIoWorkItem</a>
</dt>
<dt>
<a href="ifsk.fltqueuedeferredioworkitem">FltQueueDeferredIoWorkItem</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltAllocateDeferredIoWorkItem function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

