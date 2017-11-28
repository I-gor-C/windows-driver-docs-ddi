---
UID: NF.wdfrequest.WdfRequestCompleteWithInformation
title: WdfRequestCompleteWithInformation
author: windows-driver-content
description: The WdfRequestCompleteWithInformation method stores completion information and then completes a specified I/O request with a supplied completion status.
old-location: wdf\wdfrequestcompletewithinformation.htm
old-project: wdf
ms.assetid: dc8f5570-5bdd-492a-a830-e166f146879a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfRequestCompleteWithInformation
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
req.alt-api: WdfRequestCompleteWithInformation
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: BufAfterReqCompletedIntIoctl, BufAfterReqCompletedIntIoctlA, BufAfterReqCompletedIoctl, BufAfterReqCompletedIoctlA, BufAfterReqCompletedRead, BufAfterReqCompletedReadA, BufAfterReqCompletedWrite, BufAfterReqCompletedWriteA, CompleteCanceledReq, DeferredRequestCompleted, DoubleCompletion, DoubleCompletionLocal, DriverCreate, EvtIoStopCancel, EvtIoStopCompleteOrStopAck, EvtSurpriseRemoveNoRequestComplete, InvalidReqAccess, KmdfIrql, KmdfIrql2, MarkCancOnCancReqLocal, MdlAfterReqCompletedIntIoctl, MdlAfterReqCompletedIntIoctlA, MdlAfterReqCompletedIoctl, MdlAfterReqCompletedIoctlA, MdlAfterReqCompletedRead, MdlAfterReqCompletedReadA, MdlAfterReqCompletedWrite, MdlAfterReqCompletedWriteA, MemAfterReqCompletedIntIoctl, MemAfterReqCompletedIntIoctlA, MemAfterReqCompletedIoctl, MemAfterReqCompletedIoctlA, MemAfterReqCompletedRead, MemAfterReqCompletedReadA, MemAfterReqCompletedWrite, MemAfterReqCompletedWriteA, NoCancelFromEvtSurpriseRemove, ReqDelete, ReqIsCancOnCancReq, ReqNotCanceledLocal, ReqSendFail, RequestCompleted, RequestCompletedLocal
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

# WdfRequestCompleteWithInformation function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfRequestCompleteWithInformation</b> method stores completion information and then completes a specified I/O request with a supplied completion status.</p>


## -syntax

````
VOID WdfRequestCompleteWithInformation(
  _In_ WDFREQUEST Request,
  _In_ NTSTATUS   Status,
  _In_ ULONG_PTR  Information
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>A handle to the request object.</p>
</dd>

### -param <i>Status</i> [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS value</a> that represents the completion status of the request. Valid status values include, but are not limited to, the following:</p>
<p></p>
<dl>

### -param <a id="STATUS_SUCCESS"></a><a id="status_success"></a>STATUS_SUCCESS

<dd>
<p>The driver successfully completed the request.</p>
</dd>

### -param <a id="STATUS_CANCELLED"></a><a id="status_cancelled"></a>STATUS_CANCELLED

<dd>
<p>The driver canceled the request.</p>
</dd>

### -param <a id="STATUS_UNSUCCESSFUL"></a><a id="status_unsuccessful"></a>STATUS_UNSUCCESSFUL

<dd>
<p>The driver encountered an error while processing the request.</p>
</dd>
</dl>
</dd>

### -param <i>Information</i> [in]

<dd>
<p>Driver-defined completion status information for the request, such as the number of bytes that were transferred.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Calling <b>WdfRequestCompleteWithInformation</b> is equivalent to calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550032">WdfRequestSetInformation</a> and then calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a>.</p>

<p>After a call to <b>WdfRequestCompleteWithInformation</b> returns, the request handle is no longer valid unless the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548758">WdfObjectReference</a> to add one or more additional reference counts to the request object. Note that after <b>WdfRequestCompleteWithInformation</b> returns, the driver must not attempt to access the associated WDM IRP structure, even if it has called <b>WdfObjectReference</b>.</p>

<p>When your driver calls <b>WdfRequestCompleteWithInformation</b>, the framework supplies a default value that the system uses to boost the run-time priority of the thread that requested the I/O operation. For information about default priority boost values, see <a href="wdf.specifying_priority_boosts_when_completing_i_o_requests">Specifying Priority Boosts When Completing I/O Requests</a>. Your driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549949">WdfRequestCompleteWithPriorityBoost</a> to override the default priority boost value.</p>

<p>For more information about calling <b>WdfRequestCompleteWithInformation</b>, see <a href="wdf.completing_i_o_requests">Completing I/O Requests</a>.</p>

<p>The following code example shows how a driver for a USB device might call <b>WdfRequestCompleteWithInformation</b> in a <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-completion-routine.md">CompletionRoutine</a> callback function .</p>

<p>Calling <b>WdfRequestCompleteWithInformation</b> is equivalent to calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550032">WdfRequestSetInformation</a> and then calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a>.</p>

<p>After a call to <b>WdfRequestCompleteWithInformation</b> returns, the request handle is no longer valid unless the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548758">WdfObjectReference</a> to add one or more additional reference counts to the request object. Note that after <b>WdfRequestCompleteWithInformation</b> returns, the driver must not attempt to access the associated WDM IRP structure, even if it has called <b>WdfObjectReference</b>.</p>

<p>When your driver calls <b>WdfRequestCompleteWithInformation</b>, the framework supplies a default value that the system uses to boost the run-time priority of the thread that requested the I/O operation. For information about default priority boost values, see <a href="wdf.specifying_priority_boosts_when_completing_i_o_requests">Specifying Priority Boosts When Completing I/O Requests</a>. Your driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549949">WdfRequestCompleteWithPriorityBoost</a> to override the default priority boost value.</p>

<p>For more information about calling <b>WdfRequestCompleteWithInformation</b>, see <a href="wdf.completing_i_o_requests">Completing I/O Requests</a>.</p>

<p>The following code example shows how a driver for a USB device might call <b>WdfRequestCompleteWithInformation</b> in a <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-completion-routine.md">CompletionRoutine</a> callback function .</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975065">BufAfterReqCompletedIntIoctl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975066">BufAfterReqCompletedIntIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542316">BufAfterReqCompletedIoctl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542318">BufAfterReqCompletedIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542323">BufAfterReqCompletedRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542328">BufAfterReqCompletedReadA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542335">BufAfterReqCompletedWrite</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542340">BufAfterReqCompletedWriteA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543501">CompleteCanceledReq</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544670">DeferredRequestCompleted</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff819059">DoubleCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544928">DoubleCompletionLocal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545711">EvtIoStopCancel</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545713">EvtIoStopCompleteOrStopAck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975075">EvtSurpriseRemoveNoRequestComplete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547261">InvalidReqAccess</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549011">MarkCancOnCancReqLocal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549038">MdlAfterReqCompletedIntIoctl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549042">MdlAfterReqCompletedIntIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549047">MdlAfterReqCompletedIoctl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549056">MdlAfterReqCompletedIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549058">MdlAfterReqCompletedRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549065">MdlAfterReqCompletedReadA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549075">MdlAfterReqCompletedWrite</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549077">MdlAfterReqCompletedWriteA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549084">MemAfterReqCompletedIntIoctl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549090">MemAfterReqCompletedIntIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549096">MemAfterReqCompletedIoctl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549106">MemAfterReqCompletedIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549114">MemAfterReqCompletedRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549116">MemAfterReqCompletedReadA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549120">MemAfterReqCompletedWrite</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549125">MemAfterReqCompletedWriteA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975093">NoCancelFromEvtSurpriseRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551583">ReqDelete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551586">ReqIsCancOnCancReq</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551596">ReqNotCanceledLocal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551599">ReqSendFail</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551603">RequestCompleted</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551609">RequestCompletedLocal</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-completion-routine.md">CompletionRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552454">WDF_REQUEST_COMPLETION_PARAMS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553049">WDF_USB_REQUEST_COMPLETION_PARAMS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548758">WdfObjectReference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549949">WdfRequestCompleteWithPriorityBoost</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550032">WdfRequestSetInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestCompleteWithInformation method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
