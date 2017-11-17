---
UID: NF.wudfddi.IWDFIoRequest.UnmarkCancelable
title: IWDFIoRequest::UnmarkCancelable
author: windows-driver-content
description: The UnmarkCancelable method disables the canceling of an I/O request.
old-location: wdf\iwdfiorequest_unmarkcancelable.htm
ms.assetid: 5a3fa72c-241e-4270-92eb-70f135d79871
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFIoRequest.UnmarkCancelable
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
ms.keywords: IWDFIoRequest, UnmarkCancelable, IWDFIoRequest::UnmarkCancelable
req.iface: IWDFIoRequest
req.product: Windows 10 or later.
---

# IWDFIoRequest::UnmarkCancelable method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>UnmarkCancelable</b> method disables the canceling of an I/O request.</p>


## -syntax

````
HRESULT  UnmarkCancelable();
````


## -parameters


## -returns
<p><b>UnmarkCancelable</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/5a3fa72c-241e-4270-92eb-70f135d79871">UnmarkCancelable</a> disabled use of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a> method that was previously registered through a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559146">IWDFIoRequest::MarkCancelable</a> method.</p><dl>
<dt><b>HRESULT_FROM_WIN32 (ERROR_OPERATION_ABORTED)</b></dt>
</dl><p>The request is currently being canceled.</p>

<p> </p>

<p><b>UnmarkCancelable</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/5a3fa72c-241e-4270-92eb-70f135d79871">UnmarkCancelable</a> disabled use of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a> method that was previously registered through a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559146">IWDFIoRequest::MarkCancelable</a> method.</p><dl>
<dt><b>HRESULT_FROM_WIN32 (ERROR_OPERATION_ABORTED)</b></dt>
</dl><p>The request is currently being canceled.</p>

<p> </p>

<p><b>UnmarkCancelable</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/5a3fa72c-241e-4270-92eb-70f135d79871">UnmarkCancelable</a> disabled use of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a> method that was previously registered through a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559146">IWDFIoRequest::MarkCancelable</a> method.</p><dl>
<dt><b>HRESULT_FROM_WIN32 (ERROR_OPERATION_ABORTED)</b></dt>
</dl><p>The request is currently being canceled.</p>

<p> </p>

## -remarks
<p>A driver can call <b>IWDFIoRequest::UnmarkCancelable</b> to disable cancellation of an I/O request, if the driver previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff559146">IWDFIoRequest::MarkCancelable</a> to enable cancellation of the request.</p>

<p>If the driver previously called <a href="https://msdn.microsoft.com/73e323a4-d40e-4414-92b7-310bfb0f6457">MarkCancelable</a>, the driver must call <b>UnmarkCancelable</b> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> outside of a call to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a> callback method.</p>

<p>However, the driver must not call <b>UnmarkCancelable</b> after <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a> calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh406719">Complete</a>.</p>

<p>If <b>UnmarkCancelable</b> returns HRESULT_FROM_WIN32(ERROR_OPERATION_ABORTED), and then <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a> completes the request, the driver must not subsequently use the request object.</p>

<p>If <b>UnmarkCancelable</b> returns HRESULT_FROM_WIN32(ERROR_OPERATION_ABORTED), the driver must not complete the request before the framework calls <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a>.  Otherwise, the framework might call the driver's <b>OnCancel</b> with an invalid request.</p>

<p>The following code example demonstrates how a driver might call <b>IWDFIoRequest::UnmarkCancelable</b> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a>, outside of a call to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a> method.</p>

<p>The example also shows how you can use <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a> to expedite the completion of a request. In this case, the <b>OnCancel</b> callback does not always complete/cancel the specified request.</p>

<p>In the next code example, the driver stores I/O requests in a driver-implemented queue object called <b>MyQueue</b>.  The driver’s <b>MyQueue</b> interface implements some basic methods to manipulate the queue, such as <b>IsEmpty</b>, <b>RemoveHead</b>, <b>Cleanup</b>, <b>GetFirstNodePosition</b>, <b>GetAt</b>, and <b>RemoveAt</b>.</p>

<p>The driver also defines a <b>CommandInformation</b> structure that holds a single I/O request from <b>MyQueue</b>.</p>

<p>  The <b>MyQueue::DeQueue</b> method removes an I/O request from the queue, calls <b>UnmarkCancelable</b> to disable canceling of the request, and then returns the request for processing.</p>

<p>Also see the code example on <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a>. While written for a KMDF driver, this example demonstrates how you can use the framework's <a href="wdf.using_automatic_synchronization">automatic synchronization</a> to manage synchronization between the cancel callback and another thread that calls the <i>Unmark</i> routine.</p>

<p>A driver can call <b>IWDFIoRequest::UnmarkCancelable</b> to disable cancellation of an I/O request, if the driver previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff559146">IWDFIoRequest::MarkCancelable</a> to enable cancellation of the request.</p>

<p>If the driver previously called <a href="https://msdn.microsoft.com/73e323a4-d40e-4414-92b7-310bfb0f6457">MarkCancelable</a>, the driver must call <b>UnmarkCancelable</b> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> outside of a call to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a> callback method.</p>

<p>However, the driver must not call <b>UnmarkCancelable</b> after <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a> calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh406719">Complete</a>.</p>

<p>If <b>UnmarkCancelable</b> returns HRESULT_FROM_WIN32(ERROR_OPERATION_ABORTED), and then <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a> completes the request, the driver must not subsequently use the request object.</p>

<p>If <b>UnmarkCancelable</b> returns HRESULT_FROM_WIN32(ERROR_OPERATION_ABORTED), the driver must not complete the request before the framework calls <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a>.  Otherwise, the framework might call the driver's <b>OnCancel</b> with an invalid request.</p>

<p>The following code example demonstrates how a driver might call <b>IWDFIoRequest::UnmarkCancelable</b> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a>, outside of a call to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a> method.</p>

<p>The example also shows how you can use <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a> to expedite the completion of a request. In this case, the <b>OnCancel</b> callback does not always complete/cancel the specified request.</p>

<p>In the next code example, the driver stores I/O requests in a driver-implemented queue object called <b>MyQueue</b>.  The driver’s <b>MyQueue</b> interface implements some basic methods to manipulate the queue, such as <b>IsEmpty</b>, <b>RemoveHead</b>, <b>Cleanup</b>, <b>GetFirstNodePosition</b>, <b>GetAt</b>, and <b>RemoveAt</b>.</p>

<p>The driver also defines a <b>CommandInformation</b> structure that holds a single I/O request from <b>MyQueue</b>.</p>

<p>  The <b>MyQueue::DeQueue</b> method removes an I/O request from the queue, calls <b>UnmarkCancelable</b> to disable canceling of the request, and then returns the request for processing.</p>

<p>Also see the code example on <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a>. While written for a KMDF driver, this example demonstrates how you can use the framework's <a href="wdf.using_automatic_synchronization">automatic synchronization</a> to manage synchronization between the cancel callback and another thread that calls the <i>Unmark</i> routine.</p>

<p>A driver can call <b>IWDFIoRequest::UnmarkCancelable</b> to disable cancellation of an I/O request, if the driver previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff559146">IWDFIoRequest::MarkCancelable</a> to enable cancellation of the request.</p>

<p>If the driver previously called <a href="https://msdn.microsoft.com/73e323a4-d40e-4414-92b7-310bfb0f6457">MarkCancelable</a>, the driver must call <b>UnmarkCancelable</b> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> outside of a call to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a> callback method.</p>

<p>However, the driver must not call <b>UnmarkCancelable</b> after <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a> calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh406719">Complete</a>.</p>

<p>If <b>UnmarkCancelable</b> returns HRESULT_FROM_WIN32(ERROR_OPERATION_ABORTED), and then <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a> completes the request, the driver must not subsequently use the request object.</p>

<p>If <b>UnmarkCancelable</b> returns HRESULT_FROM_WIN32(ERROR_OPERATION_ABORTED), the driver must not complete the request before the framework calls <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a>.  Otherwise, the framework might call the driver's <b>OnCancel</b> with an invalid request.</p>

<p>The following code example demonstrates how a driver might call <b>IWDFIoRequest::UnmarkCancelable</b> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a>, outside of a call to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a> method.</p>

<p>The example also shows how you can use <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a> to expedite the completion of a request. In this case, the <b>OnCancel</b> callback does not always complete/cancel the specified request.</p>

<p>In the next code example, the driver stores I/O requests in a driver-implemented queue object called <b>MyQueue</b>.  The driver’s <b>MyQueue</b> interface implements some basic methods to manipulate the queue, such as <b>IsEmpty</b>, <b>RemoveHead</b>, <b>Cleanup</b>, <b>GetFirstNodePosition</b>, <b>GetAt</b>, and <b>RemoveAt</b>.</p>

<p>The driver also defines a <b>CommandInformation</b> structure that holds a single I/O request from <b>MyQueue</b>.</p>

<p>  The <b>MyQueue::DeQueue</b> method removes an I/O request from the queue, calls <b>UnmarkCancelable</b> to disable canceling of the request, and then returns the request for processing.</p>

<p>Also see the code example on <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a>. While written for a KMDF driver, this example demonstrates how you can use the framework's <a href="wdf.using_automatic_synchronization">automatic synchronization</a> to manage synchronization between the cancel callback and another thread that calls the <i>Unmark</i> routine.</p>

<p>A driver can call <b>IWDFIoRequest::UnmarkCancelable</b> to disable cancellation of an I/O request, if the driver previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff559146">IWDFIoRequest::MarkCancelable</a> to enable cancellation of the request.</p>

<p>If the driver previously called <a href="https://msdn.microsoft.com/73e323a4-d40e-4414-92b7-310bfb0f6457">MarkCancelable</a>, the driver must call <b>UnmarkCancelable</b> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> outside of a call to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a> callback method.</p>

<p>However, the driver must not call <b>UnmarkCancelable</b> after <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a> calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh406719">Complete</a>.</p>

<p>If <b>UnmarkCancelable</b> returns HRESULT_FROM_WIN32(ERROR_OPERATION_ABORTED), and then <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a> completes the request, the driver must not subsequently use the request object.</p>

<p>If <b>UnmarkCancelable</b> returns HRESULT_FROM_WIN32(ERROR_OPERATION_ABORTED), the driver must not complete the request before the framework calls <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a>.  Otherwise, the framework might call the driver's <b>OnCancel</b> with an invalid request.</p>

<p>The following code example demonstrates how a driver might call <b>IWDFIoRequest::UnmarkCancelable</b> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a>, outside of a call to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a> method.</p>

<p>The example also shows how you can use <a href="https://msdn.microsoft.com/67c85eaa-bb47-4384-8e37-fdbbc879b352">OnCancel</a> to expedite the completion of a request. In this case, the <b>OnCancel</b> callback does not always complete/cancel the specified request.</p>

<p>In the next code example, the driver stores I/O requests in a driver-implemented queue object called <b>MyQueue</b>.  The driver’s <b>MyQueue</b> interface implements some basic methods to manipulate the queue, such as <b>IsEmpty</b>, <b>RemoveHead</b>, <b>Cleanup</b>, <b>GetFirstNodePosition</b>, <b>GetAt</b>, and <b>RemoveAt</b>.</p>

<p>The driver also defines a <b>CommandInformation</b> structure that holds a single I/O request from <b>MyQueue</b>.</p>

<p>  The <b>MyQueue::DeQueue</b> method removes an I/O request from the queue, calls <b>UnmarkCancelable</b> to disable canceling of the request, and then returns the request for processing.</p>

<p>Also see the code example on <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a>. While written for a KMDF driver, this example demonstrates how you can use the framework's <a href="wdf.using_automatic_synchronization">automatic synchronization</a> to manage synchronization between the cancel callback and another thread that calls the <i>Unmark</i> routine.</p>

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
<p>1.5</p>
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
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558985">IWDFIoRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559146">IWDFIoRequest::MarkCancelable</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest::UnmarkCancelable method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
