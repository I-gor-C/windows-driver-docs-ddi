---
UID: NF.wdfio.WdfIoQueueStopAndPurge
title: WdfIoQueueStopAndPurge
author: windows-driver-content
description: The WdfIoQueueStopAndPurge method prevents an I/O queue from delivering new requests and cancels existing unprocessed requests and driver-owned cancellable requests, but the queue receives and stores new requests.
old-location: wdf\wdfioqueuestopandpurge.htm
old-project: wdf
ms.assetid: 3A9CF1BD-77F1-4F4C-AEB5-0E77B67C45D3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfIoQueueStopAndPurge
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfio.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.0
req.alt-api: WdfIoQueueStopAndPurge
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: ChangeQueueState, DriverCreate, EvtSurpriseRemoveNoSuspendQueue, NoCancelFromEvtSurpriseRemove
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfIoQueueStopAndPurge function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>
   The <b>WdfIoQueueStopAndPurge</b> method prevents an I/O queue from delivering new requests and cancels existing unprocessed requests and driver-owned cancellable requests, but the queue receives and stores new requests.</p>


## -syntax

````
void WdfIoQueueStopAndPurge(
  _In_     WDFQUEUE               Queue,
  _In_opt_ PFN_WDF_IO_QUEUE_STATE  StopAndPurgeComplete,
  _In_opt_ WDFCONTEXT              Context
);
````


## -parameters
<dl>

### -param <i>Queue</i> [in]

<dd>
<p>A handle to a framework queue object.</p>
</dd>

### -param <i> StopAndPurgeComplete</i> [in, optional]

<dd>
<p>A pointer to a driver-supplied <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md">EvtIoQueueState</a> callback function. This parameter is optional and can be NULL.</p>
</dd>

### -param <i> Context</i> [in, optional]

<dd>
<p>An untyped pointer to driver-supplied context information that the framework passes to the <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md">EvtIoQueueState</a> callback function. This parameter is optional and can be NULL.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>
   The <b>WdfIoQueueStopAndPurge</b> method prevents an I/O queue from delivering I/O requests to the driver while allowing new requests to be added to the queue.
  In addition, it cancels unprocessed requests in the queue and driver-owned cancellable requests (requests that were delivered to the driver that driver has not completed or requeued). If new requests are added while <b>WdfIoQueueStopAndPurge</b> is in progress, these new requests are not delivered until driver calls <a href="..\wdfio\nf-wdfio-wdfioqueuestart.md">WdfIoQueueStart</a>.</p>

<p>In contrast, the <a href="..\wdfio\nf-wdfio-wdfioqueuestop.md">WdfIoQueueStop</a> method does not cancel unprocessed requests in the queue or driver-owned cancellable requests.</p>

<p>If this method causes the framework to cancel an unprocessed request in a queue, the framework calls the driver's <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-canceled-on-queue.md">EvtIoCanceledOnQueue</a> callback function for that queue, if the driver has supplied one.</p>

<p>
    If the driver supplies an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md">EvtIoQueueState</a> callback function, the framework calls it after all requests that were delivered to the driver have been completed or canceled.</p>

<p>The <b>WdfIoQueueStopAndPurge</b> method enables the queue to receive new requests, even if the queue was not receiving new requests before the driver called <b>WdfIoQueueStopAndPurge</b>. For example, a driver might call <a href="..\wdfio\nf-wdfio-wdfioqueuedrain.md">WdfIoQueueDrain</a>, which causes the framework to stop adding new I/O requests to the queue. The driver's subsequent call of <b>WdfIoQueueStopAndPurge</b> causes the framework to resume adding requests to the queue.</p>

<p>
In contrast, <a href="..\wdfio\nf-wdfio-wdfioqueuepurge.md">WdfIoQueuePurge</a> causes the framework to stop adding I/O requests to the specified queue.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

<p>The following code example stops and purges a specified I/O queue. After all requests that were delivered to the driver have been completed or canceled, the framework calls a driver's EvtIoQueueStateStopAndPurge function.</p>

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
<p>1.11</p>
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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_changequeuestate">ChangeQueueState</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_evtsurpriseremovenosuspendqueue">EvtSurpriseRemoveNoSuspendQueue</a>, <a href="devtest.kmdf_nocancelfromevtsurpriseremove">NoCancelFromEvtSurpriseRemove</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfio\nf-wdfio-wdfioqueuestopandpurgesynchronously.md">WdfIoQueueStopAndPurgeSynchronously</a>
</dt>
<dt>
<a href="..\wdfio\nf-wdfio-wdfioqueuestart.md">WdfIoQueueStart</a>
</dt>
<dt>
<a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md">EvtIoQueueState</a>
</dt>
<dt>
<a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-canceled-on-queue.md">EvtIoCanceledOnQueue</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoQueueStopAndPurge method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
