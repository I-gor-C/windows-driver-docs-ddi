---
UID: NF.wdfrequest.WdfRequestForwardToIoQueue
title: WdfRequestForwardToIoQueue
author: windows-driver-content
description: The WdfRequestForwardToIoQueue method requeues an I/O request to one of the calling driver's I/O queues.
old-location: wdf\wdfrequestforwardtoioqueue.htm
ms.assetid: a98d7e74-8311-46bf-a0b9-a160f5675c3d
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfRequestForwardToIoQueue
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DeferredRequestCompleted, DriverCreate, InvalidReqAccess, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2, RequestCompleted, RequestCompletedLocal
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WdfRequestForwardToIoQueue
req.iface: 
req.product: Windows 10 or later.
---

# WdfRequestForwardToIoQueue function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfRequestForwardToIoQueue</b> method requeues an I/O request to one of the calling driver's I/O queues.</p>


## -syntax

````
NTSTATUS WdfRequestForwardToIoQueue(
  _In_ WDFREQUEST Request,
  _In_ WDFQUEUE   DestinationQueue
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>A handle to a framework request object.</p>
</dd>

### -param <i>DestinationQueue</i> [in]

<dd>
<p>A handle to a framework queue object.</p>
</dd>
</dl>

## -returns
<p><b>WdfRequestForwardToIoQueue</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>This value is returned if one of the following occurs:</p>

<p>The driver did not obtain the request from an I/O queue.</p>

<p>The source and destination queues are the same.</p>

<p>The source and destination queues do not belong to the same device.</p>

<p>The driver does not own the request.</p>

<p>The request is cancelable.</p><dl>
<dt><b>STATUS_WDF_BUSY</b></dt>
</dl><p>The destination queue is not accepting new requests.</p>

<p> </p>

<p>This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.


</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>The driver must <a href="wdf.request_ownership">own</a> the I/O request and must have obtained the request from one of its I/O queues.</p>

<p>The source and destination queues cannot be the same. In other words, the driver cannot call <b>WdfRequestForwardToIoQueue</b> to return a request to the queue that it came from. To requeue a request to the same queue, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff550012">WdfRequestRequeue</a>.</p>

<p>Both the source and destination queues must belong to the same device.</p>

<p>The request must not be cancelable. If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff549983">WdfRequestMarkCancelable</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549984">WdfRequestMarkCancelableEx</a> to make the request cancelable, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a> before calling <b>WdfRequestForwardToIoQueue</b>.</p>

<p>After the driver calls <b>WdfRequestForwardToIoQueue</b>, the driver does not own the requeued request until the framework delivers the request from the new queue to the driver. While the request is in the new queue, the framework owns the request and can cancel it without notifying the driver. </p>

<p>Before <b>WdfRequestForwardToIoQueue</b> returns, the following events can occur:</p>

<p>If the destination queue was empty, the framework can deliver the requeued I/O request to one of the destination queue's <a href="wdf.request_handlers">request handlers</a>.</p>

<p>If the source queue's <a href="wdf.dispatching_methods_for_i_o_requests">dispatching method</a> is sequential or parallel, the framework can deliver another request to one of the source queue's request handlers.</p>

<p>For more information about <b>WdfRequestForwardToIoQueue</b>, see <a href="wdf.requeuing_i_o_requests">Requeuing I/O Requests</a> and <a href="wdf.managing_i_o_queues">Managing I/O Queues</a>.</p>

<p>The following code example is an <a href="https://msdn.microsoft.com/3e3c4c53-e557-4bd1-8b7d-be59dde4b9ce">EvtIoDeviceControl</a> callback function from the <a href="wdf.sample_kmdf_drivers">PCIDRV</a> sample driver. If a received request contains an I/O control code of IOCTL_NDISPROT_INDICATE_STATUS, the driver calls <b>WdfRequestForwardToIoQueue</b> to move the request to a different I/O queue. </p>

<p>The driver must <a href="wdf.request_ownership">own</a> the I/O request and must have obtained the request from one of its I/O queues.</p>

<p>The source and destination queues cannot be the same. In other words, the driver cannot call <b>WdfRequestForwardToIoQueue</b> to return a request to the queue that it came from. To requeue a request to the same queue, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff550012">WdfRequestRequeue</a>.</p>

<p>Both the source and destination queues must belong to the same device.</p>

<p>The request must not be cancelable. If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff549983">WdfRequestMarkCancelable</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549984">WdfRequestMarkCancelableEx</a> to make the request cancelable, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a> before calling <b>WdfRequestForwardToIoQueue</b>.</p>

<p>After the driver calls <b>WdfRequestForwardToIoQueue</b>, the driver does not own the requeued request until the framework delivers the request from the new queue to the driver. While the request is in the new queue, the framework owns the request and can cancel it without notifying the driver. </p>

<p>Before <b>WdfRequestForwardToIoQueue</b> returns, the following events can occur:</p>

<p>If the destination queue was empty, the framework can deliver the requeued I/O request to one of the destination queue's <a href="wdf.request_handlers">request handlers</a>.</p>

<p>If the source queue's <a href="wdf.dispatching_methods_for_i_o_requests">dispatching method</a> is sequential or parallel, the framework can deliver another request to one of the source queue's request handlers.</p>

<p>For more information about <b>WdfRequestForwardToIoQueue</b>, see <a href="wdf.requeuing_i_o_requests">Requeuing I/O Requests</a> and <a href="wdf.managing_i_o_queues">Managing I/O Queues</a>.</p>

<p>The following code example is an <a href="https://msdn.microsoft.com/3e3c4c53-e557-4bd1-8b7d-be59dde4b9ce">EvtIoDeviceControl</a> callback function from the <a href="wdf.sample_kmdf_drivers">PCIDRV</a> sample driver. If a received request contains an I/O control code of IOCTL_NDISPROT_INDICATE_STATUS, the driver calls <b>WdfRequestForwardToIoQueue</b> to move the request to a different I/O queue. </p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfrequest.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544670">DeferredRequestCompleted</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547261">InvalidReqAccess</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547267">InvalidReqAccessLocal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551603">RequestCompleted</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551609">RequestCompletedLocal</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549983">WdfRequestMarkCancelable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549984">WdfRequestMarkCancelableEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550012">WdfRequestRequeue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4c3b08d2-bb25-40bd-b2fc-1b9ea2d452b3">EvtDestroyCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestForwardToIoQueue method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
