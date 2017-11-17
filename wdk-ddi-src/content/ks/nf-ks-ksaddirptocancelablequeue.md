---
UID: NF.ks.KsAddIrpToCancelableQueue
title: KsAddIrpToCancelableQueue
author: windows-driver-content
description: The KsAddIrpToCancelableQueue function adds an IRP to a queue of cancelable IRPs, thus allowing the IRP to be canceled. If the IRP had been previously set to a canceled state, the KsAddIrpToCancelableQueue function completes the canceling of that IRP.
old-location: stream\ksaddirptocancelablequeue.htm
ms.assetid: 399ca0d6-6355-40f8-ac2c-c69d7ae699e1
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
req.alt-api: KsAddIrpToCancelableQueue
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
ms.keywords: KsAddIrpToCancelableQueue
req.iface: 
---

# KsAddIrpToCancelableQueue function



## -description
<p>The <b>KsAddIrpToCancelableQueue</b> function adds an IRP to a queue of cancelable IRPs, thus allowing the IRP to be canceled. If the IRP had been previously set to a canceled state, the <b>KsAddIrpToCancelableQueue </b>function completes the canceling of that IRP. </p>


## -syntax

````
VOID KsAddIrpToCancelableQueue(
  _Inout_  PLIST_ENTRY           QueueHead,
  _In_     PKSPIN_LOCK           SpinLock,
  _In_     PIRP                  Irp,
  _In_     KSLIST_ENTRY_LOCATION ListLocation,
  _In_opt_ PDRIVER_CANCEL        DriverCancel
);
````


## -parameters
<dl>

### -param <i>QueueHead</i> [in, out]

<dd>
<p>Specifies the driver-allocated storage for the head of the queue on which to add the IRP.</p>
</dd>

### -param <i>SpinLock</i> [in]

<dd>
<p>Points to driver's spin lock for queue access to the queue specified at <i>QueueHead</i>. A copy of this pointer is kept in the IRP's KSQUEUE_SPINLOCK_IRP_STORAGE(Irp) for use by the cancel routine, if necessary.</p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>Specifies the IRP to add to the queue specified at <i>QueueHead</i>.</p>
</dd>

### -param <i>ListLocation</i> [in]

<dd>
<p>Indicates whether this IRP should be placed at the beginning or end of the queue. This value must be KsListEntryTail or KsListEntryHead.</p>
</dd>

### -param <i>DriverCancel</i> [in, optional]

<dd>
<p>Optional parameter that specifies a driver-supplied cancel routine to use. If this is <b>NULL</b>, the standard <a href="https://msdn.microsoft.com/library/windows/hardware/ff561011">KsCancelRoutine</a> is used.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If the IRP has been put into a cancel state when this routine is called, <b>KsAddIrpToCancelableQueue</b> will immediately call the cancel routine specified at <i>DriverCancel</i>, or if no routine was specified at <i>DriverCancel </i>the default streaming cancel routine is called.</p>

<p>The <b>KsAddIrpToCancelableQueue</b> function allows IRPs to be canceled even before being placed on a cancel list, or when being moved from one list to another. This function can be called at IRQ level DISPATCH_LEVEL or lower unless the driver-allocated queue and all entries in the queue are system-resident or allocated from resident storage.</p>

<p>The function does not use the cancel spin lock to add items to the list. Access to the list is synchronized using the provided spin lock and relies on atomic operations on Irp-&gt;CancelRoutine.</p>

<p>If the IRP has been put into a cancel state when this routine is called, <b>KsAddIrpToCancelableQueue</b> will immediately call the cancel routine specified at <i>DriverCancel</i>, or if no routine was specified at <i>DriverCancel </i>the default streaming cancel routine is called.</p>

<p>The <b>KsAddIrpToCancelableQueue</b> function allows IRPs to be canceled even before being placed on a cancel list, or when being moved from one list to another. This function can be called at IRQ level DISPATCH_LEVEL or lower unless the driver-allocated queue and all entries in the queue are system-resident or allocated from resident storage.</p>

<p>The function does not use the cancel spin lock to add items to the list. Access to the list is synchronized using the provided spin lock and relies on atomic operations on Irp-&gt;CancelRoutine.</p>

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