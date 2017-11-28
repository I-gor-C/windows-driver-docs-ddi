---
UID: NS.wdm._WORK_QUEUE_ITEM
title: WORK_QUEUE_ITEM
author: windows-driver-content
description: The WORK_QUEUE_ITEM structure is used to post a work items to a system work queue.
old-location: ifsk\work_queue_item.htm
old-project: ifsk
ms.assetid: 068ac200-55bb-4d7b-bc69-ad57d466a36b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: WORK_QUEUE_ITEM, WORK_QUEUE_ITEM, *PWORK_QUEUE_ITEM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WORK_QUEUE_ITEM
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# WORK_QUEUE_ITEM structure



## -description
<p>The WORK_QUEUE_ITEM structure is used to post a work items to a system work queue. <i>Use this structure with extreme caution. (See the following </i><b>Remarks</b><i> section.)</i></p>


## -syntax

````
typedef struct _WORK_QUEUE_ITEM {
  LIST_ENTRY             List;
  PWORKER_THREAD_ROUTINE WorkerRoutine;
  volatile PVOID         Parameter;
} WORK_QUEUE_ITEM, *PWORK_QUEUE_ITEM;
````


## -struct-fields
<dl>

### -field <b>List</b>

<dd>
<p>Doubly linked list structure. This structure is used to add the work item to the system work queue. </p>
</dd>

### -field <b>WorkerRoutine</b>

<dd>
<p>Pointer to a callback routine that processes this work item when the work item is dequeued. This callback routine is declared as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>VOID
(*PWORKER_THREAD_ROUTINE)(
    IN PVOID Parameter
    );</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -field <a id="Parameter"></a><a id="parameter"></a><a id="PARAMETER"></a><i>Parameter</i>

<dd>
<p>Context information pointer specified in the <b>Parameter</b> member. </p>
</dd>
</dl>
</dd>

### -field <b>Parameter</b>

<dd>
<p>Pointer to context information to be passed to the callback routine specified in the <b>WorkerRoutine</b> member. </p>
</dd>
</dl>

## -remarks
<p>To initialize a WORK_QUEUE_ITEM structure, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545327">ExInitializeWorkItem</a>. </p>

<p>To post the initialized work item to a system work queue, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff540216">ExQueueWorkItem</a>. </p>

<p><b>ExInitializeWorkItem</b><i> and </i><b>ExQueueWorkItem</b><i> can only be used in cases where the specified work item is not associated with any device object or device stack. In all other cases, drivers should use </i><a href="https://msdn.microsoft.com/library/windows/hardware/ff548276">IoAllocateWorkItem</a><i>, </i><a href="https://msdn.microsoft.com/library/windows/hardware/ff549133">IoFreeWorkItem</a><i>, and </i><a href="https://msdn.microsoft.com/library/windows/hardware/ff549466">IoQueueWorkItem</a><i>, because only these routines ensure that the device object associated with the specified work item remains available until the work item has been processed. </i></p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545327">ExInitializeWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540216">ExQueueWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548276">IoAllocateWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549133">IoFreeWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549466">IoQueueWorkItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20WORK_QUEUE_ITEM structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
