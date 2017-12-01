---
UID: NF.wdfio.WdfIoQueueReadyNotify
title: WdfIoQueueReadyNotify
author: windows-driver-content
description: The WdfIoQueueReadyNotify method registers (or deregisters) an event callback function that the framework calls each time a specified I/O queue that was previously empty receives one or more I/O requests.
old-location: wdf\wdfioqueuereadynotify.htm
old-project: wdf
ms.assetid: 0d48dce1-252f-4dc2-85a8-6c25e99ce0ba
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfIoQueueReadyNotify
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
req.alt-api: WdfIoQueueReadyNotify
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfIoQueueReadyNotify function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfIoQueueReadyNotify</b> method registers (or deregisters) an event callback function that the framework calls each time a specified I/O queue that was previously empty receives one or more I/O requests.</p>


## -syntax

````
NTSTATUS WdfIoQueueReadyNotify(
  _In_     WDFQUEUE               Queue,
  _In_opt_ PFN_WDF_IO_QUEUE_STATE QueueReady,
  _In_opt_ WDFCONTEXT             Context
);
````


## -parameters
<dl>

### -param <i>Queue</i> [in]

<dd>
<p>A handle to a framework queue object.</p>
</dd>

### -param <i>QueueReady</i> [in, optional]

<dd>
<p>A pointer to a driver-supplied <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md">EvtIoQueueState</a> callback function, if the driver is registering for ready notification, or <b>NULL</b> if the driver is deregistering. </p>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>An untyped pointer to driver-supplied context information that the framework passes to the <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md">EvtIoQueueState</a> callback function, if the driver is registering for ready notification, or <b>NULL</b> if the driver is deregistering. </p>
</dd>
</dl>

## -returns
<p><b>WdfIoQueueReadyNotify</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The driver supplied an invalid handle.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>This value is returned if one of the following occurs:</p>

<p>The <b>DispatchType</b> member of the specified I/O queue's <a href="..\wdfio\ns-wdfio--wdf-io-queue-config.md">WDF_IO_QUEUE_CONFIG</a> structure is not <b>WdfIoQueueDispatchManual</b>.</p>

<p>The driver had previously called <a href="..\wdfio\nf-wdfio-wdfioqueuereadynotify.md">WdfIoQueueReadyNotify</a> and registered an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md">EvtIoQueueState</a> callback function. </p>

<p>The driver is attempting to deregister its notification callback function, but a callback function is not registered or the driver has not called <a href="..\wdfio\nf-wdfio-wdfioqueuestop.md">WdfIoQueueStop</a> or <a href="..\wdfio\nf-wdfio-wdfioqueuestopsynchronously.md">WdfIoQueueStopSynchronously</a>.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>After a driver has called <b>WdfIoQueueReadyNotify</b> to register a <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md">EvtIoQueueState</a> callback function, the framework calls the callback function each time the specified queue's state changes from empty to non-empty. Specifically, the framework calls <i>EvtIoQueueState</i> when a request arrives on an empty queue, even if the driver still owns previously delivered requests from the queue that it has not yet completed.</p>

<p>The framework does not call <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md">EvtIoQueueState</a> while the specified queue is stopped. When the queue starts, the framework calls <i>EvtIoQueueState</i> if the queue is non-empty.</p>

<p>Your driver can call <b>WdfIoQueueReadyNotify</b> only for I/O queues that use the <a href="wdf.dispatching_methods_for_i_o_requests#manual_dispatching#manual_dispatching">manual dispatching</a> method. </p>

<p>The <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md">EvtIoQueueState</a> callback function typically calls <a href="..\wdfio\nf-wdfio-wdfioqueueretrievenextrequest.md">WdfIoQueueRetrieveNextRequest</a> or <a href="..\wdfio\nf-wdfio-wdfioqueueretrieverequestbyfileobject.md">WdfIoQueueRetrieveRequestByFileObject</a> in a loop to retrieve all of the requests that have arrived since the last time the callback function executed.</p>

<p>To stop the framework from calling the <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md">EvtIoQueueState</a> callback function, the driver must call <b>WdfIoQueueReadyNotify</b> again with the <i>QueueReady</i> parameter set to <b>NULL</b>. However, the driver must first call <a href="..\wdfio\nf-wdfio-wdfioqueuestop.md">WdfIoQueueStop</a> or <a href="..\wdfio\nf-wdfio-wdfioqueuestopsynchronously.md">WdfIoQueueStopSynchronously</a> to stop the I/O queue. The driver can subsequently call <a href="..\wdfio\nf-wdfio-wdfioqueuestart.md">WdfIoQueueStart</a> to restart the queue.</p>

<p>When a driver calls <b>WdfIoQueueReadyNotify</b> to register a <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md">EvtIoQueueState</a> callback function, it is possible for the framework to call the callback function before <b>WdfIoQueueReadyNotify</b> returns.</p>

<p>For more information about the <b>WdfIoQueueReadyNotify</b> method, see <a href="wdf.dispatching_methods_for_i_o_requests">Dispatching Methods for I/O Requests</a>.</p>

<p>The following code example registers a driver's <b>EvtIoQueueReady</b> function, so that this function will be called when the specified I/O queue receives an I/O request.</p>

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
<dt>Wdfio.h (include Wdf.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfio\nf-wdfio-wdfioqueueretrievenextrequest.md">WdfIoQueueRetrieveNextRequest</a>
</dt>
<dt>
<a href="..\wdfio\nf-wdfio-wdfioqueueretrieverequestbyfileobject.md">WdfIoQueueRetrieveRequestByFileObject</a>
</dt>
<dt>
<a href="..\wdfio\ns-wdfio--wdf-io-queue-config.md">WDF_IO_QUEUE_CONFIG</a>
</dt>
<dt>
<a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md">EvtIoQueueState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoQueueReadyNotify method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
