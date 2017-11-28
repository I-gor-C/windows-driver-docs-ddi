---
UID: NF.wdfrequest.WdfRequestStopAcknowledge
title: WdfRequestStopAcknowledge
author: windows-driver-content
description: The WdfRequestStopAcknowledge method informs the framework that the driver has stopped processing a specified I/O request.
old-location: wdf\wdfrequeststopacknowledge.htm
old-project: wdf
ms.assetid: 70f90cfd-9828-41a6-a7f9-6b0033e46b74
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfRequestStopAcknowledge
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfRequestStopAcknowledge
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DeferredRequestCompleted, DriverCreate, EvtIoStopCancel, EvtIoStopCompleteOrStopAck, EvtIoStopResume, KmdfIrql, KmdfIrql2, RequestCompleted, RequestCompletedLocal, StopAckWithinEvtIoStop
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfRequestStopAcknowledge function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfRequestStopAcknowledge</b> method informs the framework that the driver has stopped processing a specified I/O request.</p>


## -syntax

````
VOID WdfRequestStopAcknowledge(
  _In_ WDFREQUEST Request,
  _In_ BOOLEAN    Requeue
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>A handle to a framework request object.</p>
</dd>

### -param <i>Requeue</i> [in]

<dd>
<p>A Boolean value that, if <b>TRUE</b>, causes the framework to requeue the request into the queue so that the framework will deliver it to the driver again. If <b>FALSE</b>, the framework does not requeue the request. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>If a driver registers an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function for an I/O queue, the framework calls it when the queue's underlying device is leaving its working (D0) state. The framework calls the <i>EvtIoStop</i> callback function for every I/O request that the driver has not <a href="https://msdn.microsoft.com/library/windows/hardware/dn265386">completed</a>, including requests that the driver <a href="wdf.request_ownership">owns</a> and those that it has <a href="wdf.forwarding_i_o_requests">forwarded</a> to an I/O target. The driver must complete, cancel, or postpone processing of each request by doing one of the following: </p>

<p>If the driver owns the request, it can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a> to complete or cancel the request.</p>

<p>If the driver has forwarded the request to an I/O target, it can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549941">WdfRequestCancelSentRequest</a> to attempt to cancel the request.</p>

<p>If the driver postpones processing the request, it must call <b>WdfRequestStopAcknowledge</b>.</p>

<p>If your driver calls <b>WdfRequestStopAcknowledge</b>, it must call this method from within its <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function.</p>

<p>The framework does not allow the device to leave its working (D0) state until the driver has completed, canceled, or postponed every request that an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function receives.  Potentially, this inaction can prevent a system from entering its hibernation state or another low system power state.</p>

<p>When a driver's <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function calls <b>WdfRequestStopAcknowledge</b>, it can set the <i>Requeue</i> parameter to <b>TRUE</b> or <b>FALSE</b>: </p>

<p>Setting <i>Requeue</i> to <b>TRUE</b> causes the framework to place the request back into its I/O queue.</p>

<p>When the underlying device returns to its working (D0) state, the framework will redeliver the request to the driver. </p>

<p>Setting <i>Requeue</i> to <b>FALSE</b> causes the framework not to requeue the request. If the driver <a href="wdf.request_ownership">owns</a> the request, ownership remains with the driver. If the driver has forwarded the request, the driver is responsible for handling the request when it is completed. The driver must stop doing any I/O processing that requires hardware access. </p>

<p>When the underlying device returns to its working (D0) state, the framework will call the driver's <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-resume.md">EvtIoResume</a> callback function, so that the driver can continue processing the request.</p>

<p>If the driver had previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff549983">WdfRequestMarkCancelable</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549984">WdfRequestMarkCancelableEx</a>, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a> before calling <b>WdfRequestStopAcknowledge</b> with <i>Requeue</i> set to <b>TRUE</b>.</p>

<p>Before calling <b>WdfRequestStopAcknowledge</b>, the driver's <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function must stop all processing of the I/O request that requires accessing the underlying device, because the device is about to enter a low-power state.</p>

<p>For more information about the <b>WdfRequestStopAcknowledge</b> method, see <a href="wdf.using_power_managed_i_o_queues">Using Power-Managed I/O Queues</a>.</p>

<p>If a driver calls <b>WdfRequestStopAcknowledge</b> with <i>Requeue</i> set to <b>TRUE</b>, it must previously call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a>.</p>

<p>The following code example is an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function that checks to see if a received request is cancelable and, if it is, calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a>. If <b>WdfRequestUnmarkCancelable</b> returns STATUS_CANCELLED, the example just returns because the driver's <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-cancel.md">EvtRequestCancel</a> callback function will handle the request. Otherwise, the example calls <b>WdfRequestStopAcknowledge</b> and specifies <b>TRUE</b> so that the framework requeues the request when the underlying device returns to its working (D0) state.</p>

<p>Typically, if a driver calls <b>WdfRequestStopAcknowledge</b> with <i>Requeue</i> set to <b>FALSE</b>, it leaves the request cancelable.</p>

<p>The following code example is an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function that calls <b>WdfRequestStopAcknowledge</b> and specifies <b>FALSE</b> so that the framework eventually calls the driver's <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-resume.md">EvtIoResume</a> callback function, where the driver resumes processing of the request.</p>

<p>You might use code like this if it is acceptable to halt processing of a specific request and continue it later, rather than having the request redelivered and restarting processing from the beginning.</p>

<p>If a driver registers an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function for an I/O queue, the framework calls it when the queue's underlying device is leaving its working (D0) state. The framework calls the <i>EvtIoStop</i> callback function for every I/O request that the driver has not <a href="https://msdn.microsoft.com/library/windows/hardware/dn265386">completed</a>, including requests that the driver <a href="wdf.request_ownership">owns</a> and those that it has <a href="wdf.forwarding_i_o_requests">forwarded</a> to an I/O target. The driver must complete, cancel, or postpone processing of each request by doing one of the following: </p>

<p>If the driver owns the request, it can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a> to complete or cancel the request.</p>

<p>If the driver has forwarded the request to an I/O target, it can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549941">WdfRequestCancelSentRequest</a> to attempt to cancel the request.</p>

<p>If the driver postpones processing the request, it must call <b>WdfRequestStopAcknowledge</b>.</p>

<p>If your driver calls <b>WdfRequestStopAcknowledge</b>, it must call this method from within its <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function.</p>

<p>The framework does not allow the device to leave its working (D0) state until the driver has completed, canceled, or postponed every request that an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function receives.  Potentially, this inaction can prevent a system from entering its hibernation state or another low system power state.</p>

<p>When a driver's <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function calls <b>WdfRequestStopAcknowledge</b>, it can set the <i>Requeue</i> parameter to <b>TRUE</b> or <b>FALSE</b>: </p>

<p>Setting <i>Requeue</i> to <b>TRUE</b> causes the framework to place the request back into its I/O queue.</p>

<p>When the underlying device returns to its working (D0) state, the framework will redeliver the request to the driver. </p>

<p>Setting <i>Requeue</i> to <b>FALSE</b> causes the framework not to requeue the request. If the driver <a href="wdf.request_ownership">owns</a> the request, ownership remains with the driver. If the driver has forwarded the request, the driver is responsible for handling the request when it is completed. The driver must stop doing any I/O processing that requires hardware access. </p>

<p>When the underlying device returns to its working (D0) state, the framework will call the driver's <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-resume.md">EvtIoResume</a> callback function, so that the driver can continue processing the request.</p>

<p>If the driver had previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff549983">WdfRequestMarkCancelable</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549984">WdfRequestMarkCancelableEx</a>, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a> before calling <b>WdfRequestStopAcknowledge</b> with <i>Requeue</i> set to <b>TRUE</b>.</p>

<p>Before calling <b>WdfRequestStopAcknowledge</b>, the driver's <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function must stop all processing of the I/O request that requires accessing the underlying device, because the device is about to enter a low-power state.</p>

<p>For more information about the <b>WdfRequestStopAcknowledge</b> method, see <a href="wdf.using_power_managed_i_o_queues">Using Power-Managed I/O Queues</a>.</p>

<p>If a driver calls <b>WdfRequestStopAcknowledge</b> with <i>Requeue</i> set to <b>TRUE</b>, it must previously call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a>.</p>

<p>The following code example is an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function that checks to see if a received request is cancelable and, if it is, calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a>. If <b>WdfRequestUnmarkCancelable</b> returns STATUS_CANCELLED, the example just returns because the driver's <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-cancel.md">EvtRequestCancel</a> callback function will handle the request. Otherwise, the example calls <b>WdfRequestStopAcknowledge</b> and specifies <b>TRUE</b> so that the framework requeues the request when the underlying device returns to its working (D0) state.</p>

<p>Typically, if a driver calls <b>WdfRequestStopAcknowledge</b> with <i>Requeue</i> set to <b>FALSE</b>, it leaves the request cancelable.</p>

<p>The following code example is an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function that calls <b>WdfRequestStopAcknowledge</b> and specifies <b>FALSE</b> so that the framework eventually calls the driver's <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-resume.md">EvtIoResume</a> callback function, where the driver resumes processing of the request.</p>

<p>You might use code like this if it is acceptable to halt processing of a specific request and continue it later, rather than having the request redelivered and restarting processing from the beginning.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544670">DeferredRequestCompleted</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545711">EvtIoStopCancel</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545713">EvtIoStopCompleteOrStopAck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545721">EvtIoStopResume</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551603">RequestCompleted</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551609">RequestCompletedLocal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552846">StopAckWithinEvtIoStop</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a>
</dt>
<dt>
<a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-cancel.md">EvtRequestCancel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestStopAcknowledge method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
