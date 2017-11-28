---
UID: NF.wudfddi.IWDFIoRequest2.StopAcknowledge
title: IWDFIoRequest2::StopAcknowledge
author: windows-driver-content
description: The StopAcknowledge method informs the framework that the driver has stopped processing a specified I/O request.
old-location: wdf\iwdfiorequest2_stopacknowledge.htm
old-project: wdf
ms.assetid: af4ae2c0-b1e1-45af-bd0e-3b9a91566caa
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFIoRequest2, StopAcknowledge, IWDFIoRequest2::StopAcknowledge
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
req.alt-api: IWDFIoRequest2.StopAcknowledge
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
req.iface: IWDFIoRequest2
req.product: Windows 10 or later.
---

# IWDFIoRequest2::StopAcknowledge method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>StopAcknowledge</b> method informs the framework that the driver has stopped processing a specified I/O request.</p>


## -syntax

````
void StopAcknowledge(
  [in] BOOL Requeue
);
````


## -parameters
<dl>

### -param <i>Requeue</i> [in]

<dd>
<p>A Boolean value that, if <b>TRUE</b>, causes the framework to requeue the request into the queue so that the framework will deliver it to the driver again. If <b>FALSE</b>, the framework does not requeue the request. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>If a driver registers an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556871">IQueueCallbackIoStop::OnIoStop</a> callback function for an I/O queue, the framework calls it when the queue's underlying device is leaving its working (D0) state. The framework calls this callback function for every I/O request that the driver owns at the time when the queue is being stopped. The driver must complete, cancel, or postpone processing of each request by doing one of the following: </p>

<p>If the driver owns the request, it can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> to complete or cancel the request.</p>

<p>If the driver has forwarded the request to an I/O target, it can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559067">IWDFIoRequest::CancelSentRequest</a> to attempt to cancel the request.</p>

<p>If the driver postpones processing the request, it must call <b>StopAcknowledge</b>.</p>

<p>If your driver calls <b>StopAcknowledge</b>, it must call this method from within its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556871">IQueueCallbackIoStop::OnIoStop</a> callback function.</p>

<p>If the driver does not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> or <b>StopAcknowledge</b> for every request that an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556871">IQueueCallbackIoStop::OnIoStop</a> callback function receives, the framework does not allow the device to leave its working (D0) state. Potentially, this inaction can prevent a system from entering its hibernation state or another low system power state. </p>

<p>When a driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556871">IQueueCallbackIoStop::OnIoStop</a> callback function calls <b>StopAcknowledge</b>, it can set the <i>Requeue</i> parameter to <b>TRUE</b> or <b>FALSE</b>: </p>

<p>Setting <i>Requeue</i> to <b>TRUE</b> causes the framework to place the request back into its I/O queue.</p>

<p>When the underlying device returns to its working (D0) state, the framework will redeliver the request to the driver. </p>

<p>Setting <i>Requeue</i> to <b>FALSE</b> causes ownership of the request to remain with the driver. The driver must stop doing any I/O processing that requires hardware access. </p>

<p>When the underlying device returns to its working (D0) state, the framework will call the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556865">IQueueCallbackIoResume::OnIoResume</a> callback function, so that the driver can continue processing the request.</p>

<p>If the driver had previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff559146">IWDFIoRequest::MarkCancelable</a>, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559163">IWDFIoRequest::UnmarkCancelable</a> before calling <b>StopAcknowledge</b> with <i>Requeue</i> set to <b>TRUE</b>.</p>

<p>Before calling <b>StopAcknowledge</b>, the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556871">IQueueCallbackIoStop::OnIoStop</a> callback function must stop all processing of the I/O request that requires accessing the underlying device, because the device is about to enter a low-power state.</p>

<p>The following code example is an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556871">IQueueCallbackIoStop::OnIoStop</a> callback function that checks to see if a received request is cancelable and, if it is, calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff559163">IWDFIoRequest::UnmarkCancelable</a>. If <b>IWDFIoRequest::UnmarkCancelable</b> returns HRESULT_FROM_WIN32(ERROR_OPERATION_ABORTED), the example just returns because the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a> callback function will handle the request. Otherwise, the example calls <b>StopAcknowledge</b> and specifies <b>FALSE</b> so that the framework will eventually call the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556865">IQueueCallbackIoResume::OnIoResume</a> callback function. </p>

<p>If a driver registers an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556871">IQueueCallbackIoStop::OnIoStop</a> callback function for an I/O queue, the framework calls it when the queue's underlying device is leaving its working (D0) state. The framework calls this callback function for every I/O request that the driver owns at the time when the queue is being stopped. The driver must complete, cancel, or postpone processing of each request by doing one of the following: </p>

<p>If the driver owns the request, it can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> to complete or cancel the request.</p>

<p>If the driver has forwarded the request to an I/O target, it can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559067">IWDFIoRequest::CancelSentRequest</a> to attempt to cancel the request.</p>

<p>If the driver postpones processing the request, it must call <b>StopAcknowledge</b>.</p>

<p>If your driver calls <b>StopAcknowledge</b>, it must call this method from within its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556871">IQueueCallbackIoStop::OnIoStop</a> callback function.</p>

<p>If the driver does not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> or <b>StopAcknowledge</b> for every request that an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556871">IQueueCallbackIoStop::OnIoStop</a> callback function receives, the framework does not allow the device to leave its working (D0) state. Potentially, this inaction can prevent a system from entering its hibernation state or another low system power state. </p>

<p>When a driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556871">IQueueCallbackIoStop::OnIoStop</a> callback function calls <b>StopAcknowledge</b>, it can set the <i>Requeue</i> parameter to <b>TRUE</b> or <b>FALSE</b>: </p>

<p>Setting <i>Requeue</i> to <b>TRUE</b> causes the framework to place the request back into its I/O queue.</p>

<p>When the underlying device returns to its working (D0) state, the framework will redeliver the request to the driver. </p>

<p>Setting <i>Requeue</i> to <b>FALSE</b> causes ownership of the request to remain with the driver. The driver must stop doing any I/O processing that requires hardware access. </p>

<p>When the underlying device returns to its working (D0) state, the framework will call the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556865">IQueueCallbackIoResume::OnIoResume</a> callback function, so that the driver can continue processing the request.</p>

<p>If the driver had previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff559146">IWDFIoRequest::MarkCancelable</a>, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559163">IWDFIoRequest::UnmarkCancelable</a> before calling <b>StopAcknowledge</b> with <i>Requeue</i> set to <b>TRUE</b>.</p>

<p>Before calling <b>StopAcknowledge</b>, the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556871">IQueueCallbackIoStop::OnIoStop</a> callback function must stop all processing of the I/O request that requires accessing the underlying device, because the device is about to enter a low-power state.</p>

<p>The following code example is an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556871">IQueueCallbackIoStop::OnIoStop</a> callback function that checks to see if a received request is cancelable and, if it is, calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff559163">IWDFIoRequest::UnmarkCancelable</a>. If <b>IWDFIoRequest::UnmarkCancelable</b> returns HRESULT_FROM_WIN32(ERROR_OPERATION_ABORTED), the example just returns because the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556903">IRequestCallbackCancel::OnCancel</a> callback function will handle the request. Otherwise, the example calls <b>StopAcknowledge</b> and specifies <b>FALSE</b> so that the framework will eventually call the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556865">IQueueCallbackIoResume::OnIoResume</a> callback function. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558988">IWDFIoRequest2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556865">IQueueCallbackIoResume::OnIoResume</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556871">IQueueCallbackIoStop::OnIoStop</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest2::StopAcknowledge method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
