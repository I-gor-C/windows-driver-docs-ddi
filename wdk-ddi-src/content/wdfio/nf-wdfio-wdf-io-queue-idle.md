---
UID: NF.wdfio.WDF_IO_QUEUE_IDLE
title: WDF_IO_QUEUE_IDLE
author: windows-driver-content
description: The WDF_IO_QUEUE_IDLE function returns TRUE if an I/O queue's state indicates that the queue is drained.
old-location: wdf\wdf_io_queue_idle.htm
old-project: wdf
ms.assetid: 9ad3be79-13ca-4bcb-b686-09e7563610f9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_IO_QUEUE_IDLE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfio.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_IO_QUEUE_IDLE
req.alt-loc: None,None.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: None
req.dll: 
req.irql: Any IRQL.
req.iface: 
req.product: Windows 10 or later.
---

# WDF_IO_QUEUE_IDLE function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_IO_QUEUE_IDLE</b> function returns <b>TRUE</b> if an I/O queue's state indicates that the queue is drained.</p>


## -syntax

````
BOOLEAN WDF_IO_QUEUE_IDLE(
  _In_ WDF_IO_QUEUE_STATE State
);
````


## -parameters
<dl>

### -param <i>State</i> [in]

<dd>
<p>A <a href="..\wudfddi_types\ne-wudfddi-types--wdf-io-queue-state.md">WDF_IO_QUEUE_STATE</a>-typed value that <a href="..\wdfio\nf-wdfio-wdfioqueuegetstate.md">WdfIoQueueGetState</a> returns.</p>
</dd>
</dl>

## -returns
<p><b>WDF_IO_QUEUE_IDLE</b> returns <b>TRUE</b> if the specified queue state indicates that the queue is idle. Otherwise, the function returns <b>FALSE</b>.</p>

## -remarks
<p>An I/O queue is idle if the queue contains no I/O requests, and if all delivered requests have been completed or canceled. </p>

<p>Your driver can call <b>WDF_IO_QUEUE_IDLE</b> after it has called <a href="..\wdfio\nf-wdfio-wdfioqueuegetstate.md">WdfIoQueueGetState</a>.</p>

<p>For more information about I/O queue states, see <a href="..\wudfddi_types\ne-wudfddi-types--wdf-io-queue-state.md">WDF_IO_QUEUE_STATE</a>.</p>

<p>The following code example is a routine that returns <b>TRUE</b> if a specified I/O queue is idle.</p>

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
<dt>None</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any IRQL.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfio\nf-wdfio-wdf-io-queue-drained.md">WDF_IO_QUEUE_DRAINED</a>
</dt>
<dt>
<a href="..\wdfio\nf-wdfio-wdf-io-queue-purged.md">WDF_IO_QUEUE_PURGED</a>
</dt>
<dt>
<a href="..\wdfio\nf-wdfio-wdf-io-queue-ready.md">WDF_IO_QUEUE_READY</a>
</dt>
<dt>
<a href="..\wdfio\nf-wdfio-wdf-io-queue-stopped.md">WDF_IO_QUEUE_STOPPED</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_IO_QUEUE_IDLE function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
