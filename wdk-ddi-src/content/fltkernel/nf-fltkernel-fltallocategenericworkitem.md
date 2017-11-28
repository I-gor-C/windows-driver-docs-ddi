---
UID: NF.fltkernel.FltAllocateGenericWorkItem
title: FltAllocateGenericWorkItem
author: windows-driver-content
description: FltAllocateGenericWorkItem allocates a generic work item.
old-location: ifsk\fltallocategenericworkitem.htm
old-project: ifsk
ms.assetid: 1be555a5-9fa7-4179-8a36-803b8792db86
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltAllocateGenericWorkItem
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
req.alt-api: FltAllocateGenericWorkItem
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# FltAllocateGenericWorkItem function



## -description
<p><b>FltAllocateGenericWorkItem</b> allocates a generic work item. </p>


## -syntax

````
PFLT_GENERIC_WORKITEM FltAllocateGenericWorkItem(void);
````


## -parameters


## -returns
<p><b>FltAllocateGenericWorkItem</b> returns <b>NULL</b> if there is insufficient memory in nonpaged pool to satisfy the request. Otherwise, it returns a pointer to the allocated work item. </p>

<p><b>FltAllocateGenericWorkItem</b> returns <b>NULL</b> if there is insufficient memory in nonpaged pool to satisfy the request. Otherwise, it returns a pointer to the allocated work item. </p>

<p><b>FltAllocateGenericWorkItem</b> returns <b>NULL</b> if there is insufficient memory in nonpaged pool to satisfy the request. Otherwise, it returns a pointer to the allocated work item. </p>

## -remarks
<p><b>FltAllocateGenericWorkItem</b> allocates a generic work item from nonpaged pool. </p>

<p>To insert this work item into a work queue, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543452">FltQueueGenericWorkItem</a>. </p>

<p>To free the work item, a minifilter driver typically calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff542971">FltFreeGenericWorkItem</a> from the worker routine that was specified in <a href="https://msdn.microsoft.com/library/windows/hardware/ff543452">FltQueueGenericWorkItem</a>. </p>

<p><b>FltAllocateGenericWorkItem</b> allocates a generic work item from nonpaged pool. </p>

<p>To insert this work item into a work queue, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543452">FltQueueGenericWorkItem</a>. </p>

<p>To free the work item, a minifilter driver typically calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff542971">FltFreeGenericWorkItem</a> from the worker routine that was specified in <a href="https://msdn.microsoft.com/library/windows/hardware/ff543452">FltQueueGenericWorkItem</a>. </p>

<p><b>FltAllocateGenericWorkItem</b> allocates a generic work item from nonpaged pool. </p>

<p>To insert this work item into a work queue, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543452">FltQueueGenericWorkItem</a>. </p>

<p>To free the work item, a minifilter driver typically calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff542971">FltFreeGenericWorkItem</a> from the worker routine that was specified in <a href="https://msdn.microsoft.com/library/windows/hardware/ff543452">FltQueueGenericWorkItem</a>. </p>

<p><b>FltAllocateGenericWorkItem</b> allocates a generic work item from nonpaged pool. </p>

<p>To insert this work item into a work queue, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543452">FltQueueGenericWorkItem</a>. </p>

<p>To free the work item, a minifilter driver typically calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff542971">FltFreeGenericWorkItem</a> from the worker routine that was specified in <a href="https://msdn.microsoft.com/library/windows/hardware/ff543452">FltQueueGenericWorkItem</a>. </p>

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
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542971">FltFreeGenericWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543452">FltQueueGenericWorkItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltAllocateGenericWorkItem function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
