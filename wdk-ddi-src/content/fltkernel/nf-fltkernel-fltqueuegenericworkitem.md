---
UID: NF.fltkernel.FltQueueGenericWorkItem
title: FltQueueGenericWorkItem
author: windows-driver-content
description: FltQueueGenericWorkItem posts a work item that is not associated with a specific I/O operation to a work queue.
old-location: ifsk\fltqueuegenericworkitem.htm
old-project: ifsk
ms.assetid: 30179fe1-e218-46cd-96a9-816ebab112bf
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltQueueGenericWorkItem
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
req.alt-api: FltQueueGenericWorkItem
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

# FltQueueGenericWorkItem function



## -description
<p><b>FltQueueGenericWorkItem</b> posts a work item that is not associated with a specific I/O operation to a work queue. </p>


## -syntax

````
NTSTATUS FltQueueGenericWorkItem(
  _In_     PFLT_GENERIC_WORKITEM         FltWorkItem,
  _In_     PVOID                         FltObject,
  _In_     PFLT_GENERIC_WORKITEM_ROUTINE WorkerRoutine,
  _In_     WORK_QUEUE_TYPE               QueueType,
  _In_opt_ PVOID                         Context
);
````


## -parameters
<dl>

### -param FltWorkItem [in]

<dd>
<p>Pointer to the work item to be added to the work queue. The work item must have been allocated by calling <a href="..\fltkernel\nf-fltkernel-fltallocategenericworkitem.md">FltAllocateGenericWorkItem</a>. </p>
</dd>

### -param FltObject [in]

<dd>
<p>Opaque filter (PFLT_FILTER) or instance (PFLT_INSTANCE) pointer for the caller. </p>
</dd>

### -param WorkerRoutine [in]

<dd>
<p>Pointer to a caller-supplied worker routine. This routine is declared as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef VOID
(*PFLT_GENERIC_WORKITEM_ROUTINE) (
 _In_ PFLT_GENERIC_WORKITEM FltWorkItem,
 _In_ PVOID FltObject,
 _In_opt_ PVOID Context
      );</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -param FltWorkItem

<dd>
<p>Opaque pointer to a generic work item structure. </p>
</dd>

### -param FltObject

<dd>
<p>Opaque filter pointer that was passed as the <i>FltObject</i> parameter of <b>FltQueueGenericWorkItem</b>. </p>
</dd>

### -param Context

<dd>
<p>Context information pointer that was passed as the <i>Context</i> parameter of <b>FltQueueGenericWorkItem</b>. This parameter is optional. </p>
</dd>
</dl>
</dd>

### -param QueueType [in]

<dd>
<p>Specifies the queue into which the work item that <i>FltWorkItem</i> points to is to be inserted. <i>QueueType</i> can be either of the following: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>CriticalWorkQueue</b></p>
</td>
<td>
<p>Insert the work item into the queue from which a system thread with a real-time priority attribute  processes the work item. </p>
</td>
</tr>
<tr>
<td>
<p><b>DelayedWorkQueue</b></p>
</td>
<td>
<p>Insert the work item into the queue from which a system thread with a variable priority attribute processes the work item. </p>
</td>
</tr>
</table>
<p> </p>
<p>The <i>QueueType</i> value <b>HyperCriticalWorkQueue</b> is reserved for system use. </p>
</dd>

### -param Context [in, optional]

<dd>
<p>Pointer to caller-defined context information to be passed as the <i>Context</i> parameter of the callback routine specified in the <i>WorkerRoutine</i> parameter. This parameter is optional.</p>
</dd>
</dl>

## -returns
<p><b>FltQueueGenericWorkItem</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The minifilter driver is being unloaded. This is an error code. </p>

<p> </p>

## -remarks
<p><b>FltQueueGenericWorkItem</b> inserts a work item that is not associated with a specific I/O operation into a system work queue. The specified <i>WorkerRoutine</i> callback routine is called in the context of a system thread, at IRQL PASSIVE_LEVEL. </p>

<p>To allocate a work item, call <a href="..\fltkernel\nf-fltkernel-fltallocategenericworkitem.md">FltAllocateGenericWorkItem</a>. </p>

<p>To free the work item when it is no longer needed, call <a href="..\fltkernel\nf-fltkernel-fltfreegenericworkitem.md">FltFreeGenericWorkItem</a>. </p>

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
<a href="..\fltkernel\nf-fltkernel-fltallocategenericworkitem.md">FltAllocateGenericWorkItem</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltfreegenericworkitem.md">FltFreeGenericWorkItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltQueueGenericWorkItem function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
