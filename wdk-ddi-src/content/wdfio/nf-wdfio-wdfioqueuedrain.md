---
UID: NF.wdfio.WdfIoQueueDrain
title: WdfIoQueueDrain function
author: windows-driver-content
description: The WdfIoQueueDrain method causes the framework to stop queuing I/O requests to an I/O queue, while allowing already-queued requests to be delivered and processed.
old-location: wdf\wdfioqueuedrain.htm
old-project: wdf
ms.assetid: 376579c6-545d-4f5a-8ba4-0046c0b2b755
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfIoQueueDrain
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfio.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfIoQueueDrain
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: ChangeQueueState, DriverCreate, EvtSurpriseRemoveNoSuspendQueue, KmdfIrql, KmdfIrql2, NoCancelFromEvtSurpriseRemove
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfIoQueueDrain function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfIoQueueDrain</b> method causes the framework to stop queuing I/O requests to an I/O queue, while allowing already-queued requests to be delivered and processed.



## -syntax

````
VOID WdfIoQueueDrain(
  _In_     WDFQUEUE               Queue,
  _In_opt_ PFN_WDF_IO_QUEUE_STATE DrainComplete,
  _In_opt_ WDFCONTEXT             Context
);
````


## -parameters

### -param Queue [in]

A handle to a framework queue object.


### -param DrainComplete [in, optional]

A pointer to a driver-supplied <a href="..\wdfio\nc-wdfio-evt_wdf_io_queue_state.md">EvtIoQueueState</a> callback function. This parameter is optional and can be <b>NULL</b>.


### -param Context [in, optional]

An untyped pointer to driver-supplied context information that the framework passes to the <a href="..\wdfio\nc-wdfio-evt_wdf_io_queue_state.md">EvtIoQueueState</a> callback function. This parameter is optional and can be <b>NULL</b>.


## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
After a driver calls <b>WdfIoQueueDrain</b>, the framework stops adding I/O requests to the specified queue. If the framework receives additional requests for the queue, it completes them with a completion status value of STATUS_INVALID_DEVICE_STATE.

If the driver supplies an <a href="..\wdfio\nc-wdfio-evt_wdf_io_queue_state.md">EvtIoQueueState</a> callback function, the framework calls it after all requests that were delivered to the driver have been completed or canceled.

The driver should not call another method that changes queue state, such as <a href="wdf.wdfioqueuepurge">WdfIoQueuePurge</a> or <a href="wdf.wdfioqueuestart">WdfIoQueueStart</a>, before the framework has called <a href="..\wdfio\nc-wdfio-evt_wdf_io_queue_state.md">EvtIoQueueState</a>.

If a driver specifies <b>NULL</b> for <i>DrainComplete</i>, the driver can call another state changing operation before requests are completed.

As a best practice, you should only call <b>WdfIoQueueDrain</b> when you are certain that the queue's pending I/O requests will complete in a timely fashion. Otherwise, use <a href="wdf.wdfioqueuepurge">WdfIoQueuePurge</a>. For more information, see <a href="wdf.managing_i_o_queues#purging_or_draining_an_i_o_queue#purging_or_draining_an_i_o_queue">Managing I/O Queues</a>.

After a driver has drained an I/O queue, it can restart the queue by calling <a href="wdf.wdfioqueuestart">WdfIoQueueStart</a>.

The following code example drains an I/O queue and calls a driver's <b>EvtIoQueueDrainComplete</b> function when all requests that were delivered to the driver have been completed or canceled.


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
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfio.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
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
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_changequeuestate">ChangeQueueState</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_evtsurpriseremovenosuspendqueue">EvtSurpriseRemoveNoSuspendQueue</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_nocancelfromevtsurpriseremove">NoCancelFromEvtSurpriseRemove</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfioqueuedrainsynchronously">WdfIoQueueDrainSynchronously</a>
</dt>
<dt>
<a href="wdf.wdfioqueuepurge">WdfIoQueuePurge</a>
</dt>
<dt>
<a href="..\wdfio\nc-wdfio-evt_wdf_io_queue_state.md">EvtIoQueueState</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoQueueDrain method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

