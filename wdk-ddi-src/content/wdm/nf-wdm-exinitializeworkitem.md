---
UID: NF.wdm.ExInitializeWorkItem
title: ExInitializeWorkItem
author: windows-driver-content
description: ExInitializeWorkItem initializes a work-queue item with a caller-supplied context and callback routine to be queued for execution when a system worker thread is given control.
old-location: ifsk\exinitializeworkitem.htm
old-project: ifsk
ms.assetid: e26e7e68-0d0c-42fe-9342-ebbf2bb8f830
ms.author: windowsdriverdev
ms.date: 11/14/2017
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
req.iface: 
req.product: Windows 10 or later.
---

# ExInitializeWorkItem function



## -description
<p><b>ExInitializeWorkItem</b> initializes a work-queue item with a caller-supplied context and callback routine to be queued for execution when a system worker thread is given control. </p>


## -syntax

````
VOID ExInitializeWorkItem(
  _In_ PWORK_QUEUE_ITEM       Item,
  _In_ PWORKER_THREAD_ROUTINE Routine,
  _In_ PVOID                  Context
);
````


## -parameters
<dl>

### -param <i>Item</i> [in]

<dd>
<p>Pointer to a caller-allocated WORK_QUEUE_ITEM structure to be initialized. This structure must be allocated from nonpaged pool. The callback routine specified in the <i>Routine</i> parameter is responsible for freeing this work item when it is no longer needed by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff544593">ExFreePoolWithTag</a>. </p>
</dd>

### -param <i>Routine</i> [in]

<dd>
<p>Pointer to a caller-defined routine that will be called to process the work item. This routine will be called in the context of a system thread at IRQL PASSIVE_LEVEL. This routine is declared as follows: </p>
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

### -param <a id="Parameter"></a><a id="parameter"></a><a id="PARAMETER"></a><i>Parameter</i>

<dd>
<p>Context information pointer that was passed in the <i>Context</i> parameter. </p>
</dd>
</dl>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>Pointer to caller-supplied context information to be passed to the callback routine specified in the <i>Routine</i> parameter. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p><b>ExInitializeWorkItem</b> initializes the work item with the specified callback routine and context pointer and <b>NULL</b> list pointers. </p>

<p>To add the work item to a system work queue, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff540216">ExQueueWorkItem</a>. </p>

<p>Work items are a limited resource, and drivers should only allocate them as needed. For example, do not allocate a work item in <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> for the driver's dedicated use. </p>

<p><b>ExInitializeWorkItem</b>
      and 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff540216">ExQueueWorkItem</a>
      can only be used in cases where the specified work item is not associated with any device object or device stack. In all other cases, drivers should use 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff548276">IoAllocateWorkItem</a>
     , 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff549133">IoFreeWorkItem</a>
     , and 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff549466">IoQueueWorkItem</a>, because only these routines ensure that the device object associated with the specified work item remains available until the work item has been processed. 
</p>

<p><b>ExInitializeWorkItem</b> initializes the work item with the specified callback routine and context pointer and <b>NULL</b> list pointers. </p>

<p>To add the work item to a system work queue, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff540216">ExQueueWorkItem</a>. </p>

<p>Work items are a limited resource, and drivers should only allocate them as needed. For example, do not allocate a work item in <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> for the driver's dedicated use. </p>

<p><b>ExInitializeWorkItem</b>
      and 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff540216">ExQueueWorkItem</a>
      can only be used in cases where the specified work item is not associated with any device object or device stack. In all other cases, drivers should use 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff548276">IoAllocateWorkItem</a>
     , 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff549133">IoFreeWorkItem</a>
     , and 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff549466">IoQueueWorkItem</a>, because only these routines ensure that the device object associated with the specified work item remains available until the work item has been processed. 
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include FltKernel.h, Ntifs.h, Ntddk.h, or Wdm.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544593">ExFreePoolWithTag</a>
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
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557304">WORK_QUEUE_ITEM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20ExInitializeWorkItem routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
