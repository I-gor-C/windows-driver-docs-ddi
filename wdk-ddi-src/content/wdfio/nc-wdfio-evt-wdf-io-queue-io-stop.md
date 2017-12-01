---
UID: NC.wdfio.EVT_WDF_IO_QUEUE_IO_STOP
title: EVT_WDF_IO_QUEUE_IO_STOP
author: windows-driver-content
description: A driver's EvtIoStop event callback function completes, requeues, or suspends processing of a specified request because the request's I/O queue is being stopped.
old-location: wdf\evtiostop.htm
old-project: wdf
ms.assetid: 71a789f1-4f10-44c3-8bd0-a0ea74ec28ab
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_INTERRUPT_INFO, WDF_INTERRUPT_INFO, *PWDF_INTERRUPT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfio.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: EvtIoStop
req.alt-loc: Wdfio.h
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

# EVT_WDF_IO_QUEUE_IO_STOP callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>A driver's <i>EvtIoStop</i> event callback function completes, requeues, or suspends processing of a specified request because the request's I/O queue is being stopped.</p>


## -prototype

````
EVT_WDF_IO_QUEUE_IO_STOP EvtIoStop;

VOID EvtIoStop(
  _In_ WDFQUEUE   Queue,
  _In_ WDFREQUEST Request,
  _In_ ULONG      ActionFlags
)
{ ... }
````


## -parameters
<dl>

### -param <i>Queue</i> [in]

<dd>
<p>A handle to the framework queue object that is associated with the I/O request.</p>
</dd>

### -param <i>Request</i> [in]

<dd>
<p>A handle to a framework request object.</p>
</dd>

### -param <i>ActionFlags</i> [in]

<dd>
<p>A bitwise OR of one or more <a href="..\wudfddi_types\ne-wudfddi-types--wdf-request-stop-action-flags.md">WDF_REQUEST_STOP_ACTION_FLAGS</a>-typed flags that identify the reason that the callback function is being called and whether the request is cancelable.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A driver registers an <i>EvtIoStop</i> callback function when it calls <a href="..\wdfio\nf-wdfio-wdfioqueuecreate.md">WdfIoQueueCreate</a>. For more information about calling <b>WdfIoQueueCreate</b>, see <a href="wdf.creating_i_o_queues">Creating I/O Queues</a>.</p>

<p>If a driver registers an <i>EvtIoStop</i> callback function for an I/O queue, the framework calls it when the queue's underlying device is leaving its working (D0) state. The framework calls the <i>EvtIoStop</i> callback function for every I/O request that the driver has not <a href="https://msdn.microsoft.com/library/windows/hardware/dn265386">completed</a>, including requests that the driver <a href="wdf.request_ownership">owns</a> and those that it has <a href="wdf.forwarding_i_o_requests">forwarded</a> to an I/O target.</p>

<p>In  most cases, the <i>EvtIoStop</i> callback function <a href="wdf.completing_i_o_requests">completes</a>, <a href="wdf.canceling_i_o_requests">cancels</a>, or postpones further processing of the I/O request. </p>

<p>Typically, the driver does one of the following:</p>

<p>If the driver owns the I/O request, it calls <a href="..\wdfrequest\nf-wdfrequest-wdfrequestunmarkcancelable.md">WdfRequestUnmarkCancelable</a> (if the request is cancelable)  and either calls <a href="..\wdfrequest\nf-wdfrequest-wdfrequeststopacknowledge.md">WdfRequestStopAcknowledge</a> with a <i>Requeue</i> value of TRUE, or it calls  <a href="..\wdfrequest\nf-wdfrequest-wdfrequestcomplete.md">WdfRequestComplete</a> with a completion status value of STATUS_SUCCESS or STATUS_CANCELLED.</p>

<p>Before it can call <b>WdfRequest<i>Xxx</i></b> methods safely, the driver must make sure that its implementation of <i>EvtIoStop</i> has exclusive access to the request.   </p>

<p>In order to do that, the driver must synchronize access to the request to prevent other threads from manipulating the request concurrently.  The synchronization method you choose will depend on your driver's design.</p>

<p>For example, if the request is held in a shared context area, the <i>EvtIoStop</i> callback might acquire an internal driver lock, remove the request from the shared context, and then release the lock. At this point, the <i>EvtIoStop</i> callback owns the request and can safely complete or requeue the request.</p>

<p>Alternatively, the driver postpones further processing of the request and calls <a href="..\wdfrequest\nf-wdfrequest-wdfrequeststopacknowledge.md">WdfRequestStopAcknowledge</a> with a <i>Requeue</i> value of FALSE.</p>

<p>If the driver has forwarded the I/O request to an I/O target, it can call <a href="..\wdfrequest\nf-wdfrequest-wdfrequestcancelsentrequest.md">WdfRequestCancelSentRequest</a> to attempt to cancel the request.</p>

<p>Or, if the driver has forwarded the I/O request to a lower-level driver in its own driver stack, and the framework calls the driver's <i>EvtIoStop</i> callback with an <i>ActionFlags</i> value of <b>WdfRequestStopActionSuspend</b>, the driver can call <a href="..\wdfrequest\nf-wdfrequest-wdfrequeststopacknowledge.md">WdfRequestStopAcknowledge</a> with a <i>Requeue</i> value of FALSE. Before doing so, the driver should verify that the following conditions are met:<ul>
<li>The lower driver stops processing all outstanding I/O requests in response to receiving a device set-power IRP (Dx). </li>
<li> The driver's <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-completion-routine.md">CompletionRoutine</a> callback function can  complete requests while the device is in a low-power state.</li>
</ul>
</p>

<p>A driver might choose to take no action in <i>EvtIoStop</i> for requests that are guaranteed to complete in a small amount of time.</p>

<p>   In this case, the framework waits until the specified request is complete before moving the device (or system) to a lower power state or removing the device. Potentially, this inaction can prevent a system from entering its hibernation state or another low system power state. In extreme cases, it can cause the system to crash with bugcheck code 9F.</p>

<p>If the <a href="..\wudfddi_types\ne-wudfddi-types--wdf-request-stop-action-flags.md">WdfRequestStopRequestCancelable</a> flag is set in the <i>ActionFlags</i> parameter, the driver must call <a href="..\wdfrequest\nf-wdfrequest-wdfrequestunmarkcancelable.md">WdfRequestUnmarkCancelable</a> before it calls <a href="..\wdfrequest\nf-wdfrequest-wdfrequestcomplete.md">WdfRequestComplete</a> to complete (or cancel) the request or <a href="..\wdfrequest\nf-wdfrequest-wdfrequeststopacknowledge.md">WdfRequestStopAcknowledge</a> to requeue the request.</p>

<p>If the driver forwards an I/O request from one of its <a href="wdf.request_handlers">request handlers</a>
and specifies the <b>WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET</b> flag in the request's <a href="..\wdfrequest\ns-wdfrequest--wdf-request-send-options.md">WDF_REQUEST_SEND_OPTIONS</a> structure, the framework does not call the driver's <i>EvtIoStop</i> callback function for this request. However, if the driver forwards the same I/O request from another thread, the framework might call <i>EvtIoStop</i> for this request.</p>

<p>For more information about the <i>EvtIoStop</i> callback function, see <a href="wdf.using_power_managed_i_o_queues">Using Power-Managed I/O Queues</a>.</p>

<p>This callback function can be called at IRQL &lt;= DISPATCH_LEVEL, unless the <b>ExecutionLevel</b> member of the device or driver's <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure is set to <b>WdfExecutionLevelPassive</b>.</p>

<p>To define an <i>EvtIoStop</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtIoStop</i> callback function that is named <i>MyIoStop</i>, use the <b>EVT_WDF_IO_QUEUE_IO_STOP</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_IO_QUEUE_IO_STOP</b> function type is defined in the Wdfio.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_IO_QUEUE_IO_STOP</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfio\nf-wdfio-wdfioqueuecreate.md">WdfIoQueueCreate</a>
</dt>
<dt>
<a href="..\wdfrequest\nf-wdfrequest-wdfrequestcomplete.md">WdfRequestComplete</a>
</dt>
<dt>
<a href="..\wdfrequest\nf-wdfrequest-wdfrequeststopacknowledge.md">WdfRequestStopAcknowledge</a>
</dt>
<dt>
<a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\wudfddi_types\ne-wudfddi-types--wdf-request-stop-action-flags.md">WDF_REQUEST_STOP_ACTION_FLAGS</a>
</dt>
<dt>
<a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-resume.md">EvtIoResume</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_IO_QUEUE_IO_STOP callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
