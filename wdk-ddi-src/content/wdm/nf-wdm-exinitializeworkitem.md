---
UID: NF.wdm.ExInitializeWorkItem
title: ExInitializeWorkItem function
author: windows-driver-content
description: ExInitializeWorkItem initializes a work-queue item with a caller-supplied context and callback routine to be queued for execution when a system worker thread is given control.
old-location: ifsk\exinitializeworkitem.htm
old-project: ifsk
ms.assetid: e26e7e68-0d0c-42fe-9342-ebbf2bb8f830
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: ExInitializeWorkItem
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: FltKernel.h, Ntifs.h, Ntddk.h, Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExInitializeWorkItem
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
req.irql: Any level
req.product: Windows 10 or later.
---

# ExInitializeWorkItem function



## -description
<b>ExInitializeWorkItem</b> initializes a work-queue item with a caller-supplied context and callback routine to be queued for execution when a system worker thread is given control. 



## -syntax

````
VOID ExInitializeWorkItem(
  _In_ PWORK_QUEUE_ITEM       Item,
  _In_ PWORKER_THREAD_ROUTINE Routine,
  _In_ PVOID                  Context
);
````


## -parameters

### -param Item [in]

Pointer to a caller-allocated WORK_QUEUE_ITEM structure to be initialized. This structure must be allocated from nonpaged pool. The callback routine specified in the <i>Routine</i> parameter is responsible for freeing this work item when it is no longer needed by calling <a href="kernel.exfreepool">ExFreePool</a> or <a href="kernel.exfreepoolwithtag">ExFreePoolWithTag</a>. 


### -param Routine [in]

Pointer to a caller-defined routine that will be called to process the work item. This routine will be called in the context of a system thread at IRQL PASSIVE_LEVEL. This routine is declared as follows: 

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



### -param Parameter

Context information pointer that was passed in the <i>Context</i> parameter. 

</dd>
</dl>

### -param Context [in]

Pointer to caller-supplied context information to be passed to the callback routine specified in the <i>Routine</i> parameter. 


## -returns
None 


## -remarks
<b>ExInitializeWorkItem</b> initializes the work item with the specified callback routine and context pointer and <b>NULL</b> list pointers. 

To add the work item to a system work queue, call <a href="ifsk.exqueueworkitem">ExQueueWorkItem</a>. 

Work items are a limited resource, and drivers should only allocate them as needed. For example, do not allocate a work item in <a href="..\wdm\nc-wdm-driver_initialize.md">DriverEntry</a> for the driver's dedicated use. 

<b>ExInitializeWorkItem</b>
      and 
     <a href="ifsk.exqueueworkitem">ExQueueWorkItem</a>
      can only be used in cases where the specified work item is not associated with any device object or device stack. In all other cases, drivers should use 
     <a href="kernel.ioallocateworkitem">IoAllocateWorkItem</a>
     , 
     <a href="kernel.iofreeworkitem">IoFreeWorkItem</a>
     , and 
     <a href="kernel.ioqueueworkitem">IoQueueWorkItem</a>, because only these routines ensure that the device object associated with the specified work item remains available until the work item has been processed. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include FltKernel.h, Ntifs.h, Ntddk.h, or Wdm.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exfreepool">ExFreePool</a>
</dt>
<dt>
<a href="kernel.exfreepoolwithtag">ExFreePoolWithTag</a>
</dt>
<dt>
<a href="ifsk.exqueueworkitem">ExQueueWorkItem</a>
</dt>
<dt>
<a href="kernel.ioallocateworkitem">IoAllocateWorkItem</a>
</dt>
<dt>
<a href="kernel.iofreeworkitem">IoFreeWorkItem</a>
</dt>
<dt>
<a href="kernel.ioqueueworkitem">IoQueueWorkItem</a>
</dt>
<dt>
<a href="ifsk.work_queue_item">WORK_QUEUE_ITEM</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20ExInitializeWorkItem routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

