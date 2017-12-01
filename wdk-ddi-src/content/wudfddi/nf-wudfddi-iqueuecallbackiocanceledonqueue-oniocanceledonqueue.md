---
UID: NF.wudfddi.IQueueCallbackIoCanceledOnQueue.OnIoCanceledOnQueue
title: IQueueCallbackIoCanceledOnQueue::OnIoCanceledOnQueue
author: windows-driver-content
description: A driver's OnIoCanceledOnQueue event callback function informs the driver that an I/O request was canceled while it was in an I/O queue.
old-location: wdf\iqueuecallbackiocanceledonqueue_oniocanceledonqueue.htm
old-project: wdf
ms.assetid: 901ff312-d1bb-46bf-b8e6-6abc47fa3c7f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IQueueCallbackIoCanceledOnQueue, OnIoCanceledOnQueue, IQueueCallbackIoCanceledOnQueue::OnIoCanceledOnQueue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IQueueCallbackIoCanceledOnQueue.OnIoCanceledOnQueue
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: IQueueCallbackIoCanceledOnQueue
req.product: Windows 10 or later.
---

# IQueueCallbackIoCanceledOnQueue::OnIoCanceledOnQueue method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>A driver's <b>OnIoCanceledOnQueue</b> event callback function informs the driver that an I/O request was canceled while it was in an I/O queue.</p>


## -syntax

````
void OnIoCanceledOnQueue(
  [in] IWDFIoQueue   *pWdfQueue,
  [in] IWDFIoRequest *pWdfRequest
);
````


## -parameters
<dl>

### -param <i>pWdfQueue</i> [in]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfioqueue.md">IWDFIoQueue</a> interface for the I/O queue that the I/O request was in when it was canceled. </p>
</dd>

### -param <i>pWdfRequest</i> [in]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfiorequest.md">IWDFIoRequest</a> interface for the I/O request. </p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>A driver registers an I/O queue's <a href="..\wudfddi\nn-wudfddi-iqueuecallbackiocanceledonqueue.md">IQueueCallbackIoCanceledOnQueue</a> interface and <b>OnIoCanceledOnQueue</b> callback function when the driver calls the <a href="wdf.iwdfdevice_createioqueue">IWDFDevice::CreateIoQueue</a>. For more information about how to register the interface, see <a href="..\wudfddi\nn-wudfddi-iqueuecallbackiocanceledonqueue.md">IQueueCallbackIoCanceledOnQueue</a>.</p>

<p>If a driver registers an <b>OnIoCanceledOnQueue</b> callback function for an I/O queue, the framework calls the callback function if a request handler receives an I/O request from an I/O queue, the driver calls <a href="wdf.iwdfiorequest_forwardtoioqueue">IWDFIoRequest::ForwardToIoQueue</a> or <a href="wdf.iwdfiorequest2_requeue">IWDFIoRequest2::Requeue</a> to requeue the request to the I/O queue for which the <b>OnIoCanceledOnQueue</b> callback function is registered, and the associated I/O operation is subsequently canceled.</p>

<p>After the framework calls the <b>OnIoCanceledOnQueue</b> callback function, the driver owns the request object and, therefore, must <a href="https://msdn.microsoft.com/library/windows/hardware/hh406716">cancel</a> the request.</p>

<p>The framework does not call the driver's <b>OnIoCanceledOnQueue</b> callback function for I/O requests that the framework has never delivered to the driver.</p>

<p>The framework calls an <b>OnIoCanceledOnQueue</b> callback function as soon as it determines that an I/O request has been canceled, regardless of the <a href="wdf.configuring_dispatch_mode_for_an_i_o_queue">dispatching method</a> that the driver has set for the I/O queue. Therefore, the framework can call an <b>OnIoCanceledOnQueue</b> callback function for a request in a queue that uses sequential dispatching, even if the driver currently owns another request from the queue.</p>

<p>For more information about the <b>OnIoCanceledOnQueue</b> callback function, see <a href="wdf.canceling_i_o_requests">Canceling I/O Requests</a>.</p>

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
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-iqueuecallbackiocanceledonqueue.md">IQueueCallbackIoCanceledOnQueue</a>
</dt>
<dt>
<a href="wdf.iwdfdevice_createioqueue">IWDFDevice::CreateIoQueue</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest_forwardtoioqueue">IWDFIoRequest::ForwardToIoQueue</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IQueueCallbackIoCanceledOnQueue::OnIoCanceledOnQueue method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
