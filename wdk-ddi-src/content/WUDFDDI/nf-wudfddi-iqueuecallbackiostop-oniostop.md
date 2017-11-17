---
UID: NF.wudfddi.IQueueCallbackIoStop.OnIoStop
title: IQueueCallbackIoStop::OnIoStop
author: windows-driver-content
description: The OnIoStop callback function stops the processing of the specified I/O request from the specified queue.
old-location: wdf\iqueuecallbackiostop_oniostop.htm
ms.assetid: baa48d1b-b7da-4f89-b2e8-9a9ae2086527
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IQueueCallbackIoStop.OnIoStop
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: IQueueCallbackIoStop, OnIoStop, IQueueCallbackIoStop::OnIoStop
req.iface: IQueueCallbackIoStop
req.product: Windows 10 or later.
---

# IQueueCallbackIoStop::OnIoStop method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OnIoStop</b> callback function stops the processing of the specified I/O request from the specified queue. </p>


## -syntax

````
void OnIoStop(
  [in] IWDFIoQueue   *pWdfQueue,
  [in] IWDFIoRequest *pWdfRequest,
  [in] ULONG         ActionFlags
);
````


## -parameters
<dl>

### -param <i>pWdfQueue</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558943">IWDFIoQueue</a> interface for the I/O queue object that processing of the I/O request is stopped from. </p>
</dd>

### -param <i>pWdfRequest</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558985">IWDFIoRequest</a> interface that represents the framework request object whose processing is stopped. </p>
</dd>

### -param <i>ActionFlags</i> [in]

<dd>
<p>A valid bitwise OR of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561465">WDF_REQUEST_STOP_ACTION_FLAGS</a>-typed values that identifies the state of a stop action request.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A driver registers the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556868">IQueueCallbackIoStop</a> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. </p>

<p>If a driver registers an <b>OnIoStop</b> callback function for an I/O queue, the framework calls it when the queue's underlying device is leaving its working (D0) state. The framework calls the <b>OnIoStop</b> callback function for every I/O request that the driver has not completed, including requests that the driver owns and those that it has forwarded to an I/O target.</p>

<p>The <b>OnIoStop</b> callback function must complete, cancel, or postpone further processing of the I/O request. You must use the following rules:</p>

<p>If the driver owns the I/O request, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> to complete or cancel the request, or it must postpone further processing of the request and then call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559051">IWDFIoRequest2::StopAcknowledge</a>.</p>

<p>If the driver has forwarded the I/O request to an I/O target, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559067">IWDFIoRequest::CancelSentRequest</a> to attempt to cancel the request, or it must postpone further processing of the request and then call <a href="https://msdn.microsoft.com/af4ae2c0-b1e1-45af-bd0e-3b9a91566caa">StopAcknowledge</a>.</p>

<p>If the <b>WdfRequestStopRequestCancelable</b> flag is set in the <i>ActionFlags</i> parameter, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559163">IWDFIoRequest::UnmarkCancelable</a> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> to complete (or cancel) the request or calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559051">IWDFIoRequest2::StopAcknowledge</a> to requeue the request.</p>

<p>A driver registers the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556868">IQueueCallbackIoStop</a> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. </p>

<p>If a driver registers an <b>OnIoStop</b> callback function for an I/O queue, the framework calls it when the queue's underlying device is leaving its working (D0) state. The framework calls the <b>OnIoStop</b> callback function for every I/O request that the driver has not completed, including requests that the driver owns and those that it has forwarded to an I/O target.</p>

<p>The <b>OnIoStop</b> callback function must complete, cancel, or postpone further processing of the I/O request. You must use the following rules:</p>

<p>If the driver owns the I/O request, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> to complete or cancel the request, or it must postpone further processing of the request and then call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559051">IWDFIoRequest2::StopAcknowledge</a>.</p>

<p>If the driver has forwarded the I/O request to an I/O target, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559067">IWDFIoRequest::CancelSentRequest</a> to attempt to cancel the request, or it must postpone further processing of the request and then call <a href="https://msdn.microsoft.com/af4ae2c0-b1e1-45af-bd0e-3b9a91566caa">StopAcknowledge</a>.</p>

<p>If the <b>WdfRequestStopRequestCancelable</b> flag is set in the <i>ActionFlags</i> parameter, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559163">IWDFIoRequest::UnmarkCancelable</a> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> to complete (or cancel) the request or calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559051">IWDFIoRequest2::StopAcknowledge</a> to requeue the request.</p>

## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556868">IQueueCallbackIoStop</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558943">IWDFIoQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558985">IWDFIoRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559051">IWDFIoRequest2::StopAcknowledge</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561465">WDF_REQUEST_STOP_ACTION_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IQueueCallbackIoStop::OnIoStop method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
