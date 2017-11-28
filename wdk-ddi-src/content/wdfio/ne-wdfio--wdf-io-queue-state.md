---
UID: NE.wdfio._WDF_IO_QUEUE_STATE
title: WDF_IO_QUEUE_STATE
author: windows-driver-content
description: The WDF_IO_QUEUE_STATE enumeration type identifies the status of a framework queue object. The enumerators are used as bit masks.
old-location: wdf\wdf_io_queue_state.htm
old-project: wdf
ms.assetid: d89c4d4c-d3c2-47fc-9eb8-e2eb8424d5cc
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_INTERRUPT_INFO, WDF_INTERRUPT_INFO, *PWDF_INTERRUPT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfio.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_IO_QUEUE_STATE
req.alt-loc: wdfio.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# WDF_IO_QUEUE_STATE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_IO_QUEUE_STATE</b> enumeration type identifies the status of a framework queue object. The enumerators are used as bit masks.</p>


## -syntax

````
typedef enum _WDF_IO_QUEUE_STATE { 
  WdfIoQueueAcceptRequests    = 0x01,
  WdfIoQueueDispatchRequests  = 0x02,
  WdfIoQueueNoRequests        = 0x04,
  WdfIoQueueDriverNoRequests  = 0x08,
  WdfIoQueuePnpHeld           = 0x10
} WDF_IO_QUEUE_STATE;
````


## -enum-fields
<dl>

### -field <a id="WdfIoQueueAcceptRequests"></a><a id="wdfioqueueacceptrequests"></a><a id="WDFIOQUEUEACCEPTREQUESTS"></a><b>WdfIoQueueAcceptRequests</b>

<dd>
<p>If set, the I/O queue can accept new I/O requests from the I/O manager and requests that are forwarded by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545920">WdfDeviceConfigureRequestDispatching</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff549958">WdfRequestForwardToIoQueue</a> (or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549959">WdfRequestForwardToParentDeviceIoQueue</a>) methods. </p>
<p>If not set, the framework cancels requests from the I/O manager and <a href="https://msdn.microsoft.com/library/windows/hardware/ff545920">WdfDeviceConfigureRequestDispatching</a> and fails requests from <a href="https://msdn.microsoft.com/library/windows/hardware/ff549958">WdfRequestForwardToIoQueue</a> (or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549959">WdfRequestForwardToParentDeviceIoQueue</a>) with STATUS_WDF_BUSY.</p>
</dd>

### -field <a id="WdfIoQueueDispatchRequests"></a><a id="wdfioqueuedispatchrequests"></a><a id="WDFIOQUEUEDISPATCHREQUESTS"></a><b>WdfIoQueueDispatchRequests</b>

<dd>
<p>If set, the framework delivers the queue's requests to the driver (unless the <b>WdfIoQueuePnpHeld</b> bit is also set). If not set, the driver cannot obtain requests from the queue. </p>
</dd>

### -field <a id="WdfIoQueueNoRequests"></a><a id="wdfioqueuenorequests"></a><a id="WDFIOQUEUENOREQUESTS"></a><b>WdfIoQueueNoRequests</b>

<dd>
<p>If set, the I/O queue is empty.</p>
</dd>

### -field <a id="WdfIoQueueDriverNoRequests"></a><a id="wdfioqueuedrivernorequests"></a><a id="WDFIOQUEUEDRIVERNOREQUESTS"></a><b>WdfIoQueueDriverNoRequests</b>

<dd>
<p>If set, all requests that have been delivered to the driver have been completed. </p>
</dd>

### -field <a id="WdfIoQueuePnpHeld"></a><a id="wdfioqueuepnpheld"></a><a id="WDFIOQUEUEPNPHELD"></a><b>WdfIoQueuePnpHeld</b>

<dd>
<p>If set, the framework has stopped delivering requests to the driver because the underlying device is not in its working (D0) state.</p>
</dd>
</dl>

## -remarks
<p>The WDF_IO_QUEUE_STATE enumeration type is used as the return value for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548437">WdfIoQueueGetState</a> method.</p>

<p>The following functions are defined in <i>wdfio.h</i>:</p>

<p></p><dl>
<dt><a id="WDF_IO_QUEUE_DRAINED_State__"></a><a id="wdf_io_queue_drained_state__"></a><a id="WDF_IO_QUEUE_DRAINED_STATE__"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552363">WDF_IO_QUEUE_DRAINED</a>(<i>State</i>) </dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is drained; that is, the queue is empty, is not accepting new requests, and all requests that were in the queue have been delivered to the driver.</p>
</dd>
<dt><a id="WDF_IO_QUEUE_IDLE_State_"></a><a id="wdf_io_queue_idle_state_"></a><a id="WDF_IO_QUEUE_IDLE_STATE_"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552368">WDF_IO_QUEUE_IDLE</a>(<i>State</i>)</dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is idle; that is, the queue contains no requests and all delivered requests have been completed or canceled.</p>
</dd>
<dt><a id="WDF_IO_QUEUE_PURGED_State_"></a><a id="wdf_io_queue_purged_state_"></a><a id="WDF_IO_QUEUE_PURGED_STATE_"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552369">WDF_IO_QUEUE_PURGED</a>(<i>State</i>)</dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is purged; that is, the queue is empty, is not accepting new requests, and all requests that were in the queue have been canceled.</p>
</dd>
<dt><a id="WDF_IO_QUEUE_READY_State_"></a><a id="wdf_io_queue_ready_state_"></a><a id="WDF_IO_QUEUE_READY_STATE_"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552371">WDF_IO_QUEUE_READY</a>(<i>State</i>)</dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is ready; that is, the queue can accept and dispatch requests. </p>
</dd>
<dt><a id="WDF_IO_QUEUE_STOPPED_State_"></a><a id="wdf_io_queue_stopped_state_"></a><a id="WDF_IO_QUEUE_STOPPED_STATE_"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552375">WDF_IO_QUEUE_STOPPED</a>(<i>State</i>)</dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is stopped; that is, it can accept new requests but the framework is not delivering them to the driver.</p>
</dd>
</dl><p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is drained; that is, the queue is empty, is not accepting new requests, and all requests that were in the queue have been delivered to the driver.</p>

<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is idle; that is, the queue contains no requests and all delivered requests have been completed or canceled.</p>

<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is purged; that is, the queue is empty, is not accepting new requests, and all requests that were in the queue have been canceled.</p>

<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is ready; that is, the queue can accept and dispatch requests. </p>

<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is stopped; that is, it can accept new requests but the framework is not delivering them to the driver.</p>

<p>The WDF_IO_QUEUE_STATE enumeration type is used as the return value for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548437">WdfIoQueueGetState</a> method.</p>

<p>The following functions are defined in <i>wdfio.h</i>:</p>

<p></p><dl>
<dt><a id="WDF_IO_QUEUE_DRAINED_State__"></a><a id="wdf_io_queue_drained_state__"></a><a id="WDF_IO_QUEUE_DRAINED_STATE__"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552363">WDF_IO_QUEUE_DRAINED</a>(<i>State</i>) </dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is drained; that is, the queue is empty, is not accepting new requests, and all requests that were in the queue have been delivered to the driver.</p>
</dd>
<dt><a id="WDF_IO_QUEUE_IDLE_State_"></a><a id="wdf_io_queue_idle_state_"></a><a id="WDF_IO_QUEUE_IDLE_STATE_"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552368">WDF_IO_QUEUE_IDLE</a>(<i>State</i>)</dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is idle; that is, the queue contains no requests and all delivered requests have been completed or canceled.</p>
</dd>
<dt><a id="WDF_IO_QUEUE_PURGED_State_"></a><a id="wdf_io_queue_purged_state_"></a><a id="WDF_IO_QUEUE_PURGED_STATE_"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552369">WDF_IO_QUEUE_PURGED</a>(<i>State</i>)</dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is purged; that is, the queue is empty, is not accepting new requests, and all requests that were in the queue have been canceled.</p>
</dd>
<dt><a id="WDF_IO_QUEUE_READY_State_"></a><a id="wdf_io_queue_ready_state_"></a><a id="WDF_IO_QUEUE_READY_STATE_"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552371">WDF_IO_QUEUE_READY</a>(<i>State</i>)</dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is ready; that is, the queue can accept and dispatch requests. </p>
</dd>
<dt><a id="WDF_IO_QUEUE_STOPPED_State_"></a><a id="wdf_io_queue_stopped_state_"></a><a id="WDF_IO_QUEUE_STOPPED_STATE_"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552375">WDF_IO_QUEUE_STOPPED</a>(<i>State</i>)</dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is stopped; that is, it can accept new requests but the framework is not delivering them to the driver.</p>
</dd>
</dl><p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is drained; that is, the queue is empty, is not accepting new requests, and all requests that were in the queue have been delivered to the driver.</p>

<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is idle; that is, the queue contains no requests and all delivered requests have been completed or canceled.</p>

<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is purged; that is, the queue is empty, is not accepting new requests, and all requests that were in the queue have been canceled.</p>

<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is ready; that is, the queue can accept and dispatch requests. </p>

<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is stopped; that is, it can accept new requests but the framework is not delivering them to the driver.</p>

<p>The WDF_IO_QUEUE_STATE enumeration type is used as the return value for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548437">WdfIoQueueGetState</a> method.</p>

<p>The following functions are defined in <i>wdfio.h</i>:</p>

<p></p><dl>
<dt><a id="WDF_IO_QUEUE_DRAINED_State__"></a><a id="wdf_io_queue_drained_state__"></a><a id="WDF_IO_QUEUE_DRAINED_STATE__"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552363">WDF_IO_QUEUE_DRAINED</a>(<i>State</i>) </dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is drained; that is, the queue is empty, is not accepting new requests, and all requests that were in the queue have been delivered to the driver.</p>
</dd>
<dt><a id="WDF_IO_QUEUE_IDLE_State_"></a><a id="wdf_io_queue_idle_state_"></a><a id="WDF_IO_QUEUE_IDLE_STATE_"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552368">WDF_IO_QUEUE_IDLE</a>(<i>State</i>)</dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is idle; that is, the queue contains no requests and all delivered requests have been completed or canceled.</p>
</dd>
<dt><a id="WDF_IO_QUEUE_PURGED_State_"></a><a id="wdf_io_queue_purged_state_"></a><a id="WDF_IO_QUEUE_PURGED_STATE_"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552369">WDF_IO_QUEUE_PURGED</a>(<i>State</i>)</dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is purged; that is, the queue is empty, is not accepting new requests, and all requests that were in the queue have been canceled.</p>
</dd>
<dt><a id="WDF_IO_QUEUE_READY_State_"></a><a id="wdf_io_queue_ready_state_"></a><a id="WDF_IO_QUEUE_READY_STATE_"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552371">WDF_IO_QUEUE_READY</a>(<i>State</i>)</dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is ready; that is, the queue can accept and dispatch requests. </p>
</dd>
<dt><a id="WDF_IO_QUEUE_STOPPED_State_"></a><a id="wdf_io_queue_stopped_state_"></a><a id="WDF_IO_QUEUE_STOPPED_STATE_"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff552375">WDF_IO_QUEUE_STOPPED</a>(<i>State</i>)</dt>
<dd>
<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is stopped; that is, it can accept new requests but the framework is not delivering them to the driver.</p>
</dd>
</dl><p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is drained; that is, the queue is empty, is not accepting new requests, and all requests that were in the queue have been delivered to the driver.</p>

<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is idle; that is, the queue contains no requests and all delivered requests have been completed or canceled.</p>

<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is purged; that is, the queue is empty, is not accepting new requests, and all requests that were in the queue have been canceled.</p>

<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is ready; that is, the queue can accept and dispatch requests. </p>

<p>Returns <b>TRUE</b> if the <i>State</i> value indicates that the queue is stopped; that is, it can accept new requests but the framework is not delivering them to the driver.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548437">WdfIoQueueGetState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_IO_QUEUE_STATE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
