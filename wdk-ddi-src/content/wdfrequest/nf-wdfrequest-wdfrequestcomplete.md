---
UID: NF.wdfrequest.WdfRequestComplete
title: WdfRequestComplete function
author: windows-driver-content
description: The WdfRequestComplete method completes a specified I/O request and supplies a completion status.
old-location: wdf\wdfrequestcomplete.htm
old-project: wdf
ms.assetid: cb5bfd4f-e45a-4894-acb4-0ece2de91510
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfRequestComplete
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
req.alt-api: WdfRequestComplete
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: BufAfterReqCompletedIntIoctl, BufAfterReqCompletedIntIoctlA, BufAfterReqCompletedIoctl, BufAfterReqCompletedIoctlA, BufAfterReqCompletedRead, BufAfterReqCompletedReadA, BufAfterReqCompletedWrite, BufAfterReqCompletedWriteA, CompleteCanceledReq, DeferredRequestCompleted, DoubleCompletion, DoubleCompletionLocal, DriverCreate, EvtIoStopCancel, EvtIoStopCompleteOrStopAck, EvtSurpriseRemoveNoRequestComplete, InvalidReqAccess, KmdfIrql, KmdfIrql2, MarkCancOnCancReqLocal, MdlAfterReqCompletedIntIoctl, MdlAfterReqCompletedIntIoctlA, MdlAfterReqCompletedIoctl, MdlAfterReqCompletedIoctlA, MdlAfterReqCompletedRead, MdlAfterReqCompletedReadA, MdlAfterReqCompletedWrite, MdlAfterReqCompletedWriteA, MemAfterReqCompletedIntIoctl, MemAfterReqCompletedIntIoctlA, MemAfterReqCompletedIoctl, MemAfterReqCompletedIoctlA, MemAfterReqCompletedRead, MemAfterReqCompletedReadA, MemAfterReqCompletedWrite, MemAfterReqCompletedWriteA, NoCancelFromEvtSurpriseRemove, ReqDelete, ReqIsCancOnCancReq, ReqNotCanceledLocal, ReqSendFail, RequestCompleted, RequestCompletedLocal
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfRequestComplete function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfRequestComplete</b> method completes a specified I/O request and supplies a completion status.



## -syntax

````
VOID WdfRequestComplete(
  _In_ WDFREQUEST Request,
  _In_ NTSTATUS   Status
);
````


## -parameters

### -param Request [in]

A handle to the framework request object that represents the I/O request that is being completed.


### -param Status [in]

An <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS value</a> that represents the completion status of the request. Valid status values include, but are not limited to, the following:




### -param STATUS_SUCCESS

The driver is successfully completing the request.


### -param STATUS_CANCELLED

The driver is canceling the request.


### -param STATUS_UNSUCCESSFUL

The driver has encountered an error while processing the request.

</dd>
</dl>

## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
After a driver calls <b>WdfRequestComplete</b>, higher-level drivers on the driver stack can call <a href="wdf.wdfrequestgetstatus">WdfRequestGetStatus</a> to obtain the completion status value that was specified for the <i>Status</i> parameter. Typically, drivers call <b>WdfRequestGetStatus</b> from within a <a href="..\wdfrequest\nc-wdfrequest-evt_wdf_request_completion_routine.md">CompletionRoutine</a> callback function.

After a call to <b>WdfRequestComplete</b> returns, the request handle is no longer valid unless the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548758">WdfObjectReference</a> to add one or more additional reference counts to the request object.  Note that after <b>WdfRequestComplete</b> returns, the driver must not attempt to access the associated WDM IRP structure, even if it has called <b>WdfObjectReference</b>.



After a driver calls <b>WdfRequestComplete</b>, the framework calls the driver's <a href="..\wdfobject\nc-wdfobject-evt_wdf_object_context_cleanup.md">EvtCleanupCallback</a> function for the request, if the driver has supplied one.

Instead of calling <b>WdfRequestComplete</b>, the driver can call <a href="wdf.wdfrequestcompletewithinformation">WdfRequestCompleteWithInformation</a> or <a href="wdf.wdfrequestcompletewithpriorityboost">WdfRequestCompleteWithPriorityBoost</a>.

When your driver calls <b>WdfRequestComplete</b>, the framework supplies a default value that the system uses to boost the run-time priority of the thread that requested the I/O operation. For information about default priority boost values, see <a href="wdf.specifying_priority_boosts_when_completing_i_o_requests">Specifying Priority Boosts When Completing I/O Requests</a>. Your driver can call <a href="wdf.wdfrequestcompletewithpriorityboost">WdfRequestCompleteWithPriorityBoost</a> to override the default priority boost value.

For more information about calling <b>WdfRequestComplete</b>, see <a href="wdf.completing_i_o_requests">Completing I/O Requests</a>.

The following code example is a section of a request handler. The request handler accepts only read and write requests, and it completes a each request with an error status if the request type is not read or write.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfrequest.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

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
IRQL

</th>
<td width="70%">
&lt;=DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_bufafterreqcompletedintioctl">BufAfterReqCompletedIntIoctl</a>, <a href="devtest.kmdf_bufafterreqcompletedintioctla">BufAfterReqCompletedIntIoctlA</a>, <a href="devtest.kmdf_bufafterreqcompletedioctl">BufAfterReqCompletedIoctl</a>, <a href="devtest.kmdf_bufafterreqcompletedioctla">BufAfterReqCompletedIoctlA</a>, <a href="devtest.kmdf_bufafterreqcompletedread">BufAfterReqCompletedRead</a>, <a href="devtest.kmdf_bufafterreqcompletedreada">BufAfterReqCompletedReadA</a>, <a href="devtest.kmdf_bufafterreqcompletedwrite">BufAfterReqCompletedWrite</a>, <a href="devtest.kmdf_bufafterreqcompletedwritea">BufAfterReqCompletedWriteA</a>, <a href="devtest.kmdf_completecanceledreq">CompleteCanceledReq</a>, <a href="devtest.kmdf_deferredrequestcompleted">DeferredRequestCompleted</a>, <a href="devtest.kmdf_doublecompletion">DoubleCompletion</a>, <a href="devtest.kmdf_doublecompletionlocal">DoubleCompletionLocal</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_evtiostopcancel">EvtIoStopCancel</a>, <a href="devtest.kmdf_evtiostopcompleteorstopack">EvtIoStopCompleteOrStopAck</a>, <a href="devtest.kmdf_evtsurpriseremovenorequestcomplete">EvtSurpriseRemoveNoRequestComplete</a>, <a href="devtest.kmdf_invalidreqaccess">InvalidReqAccess</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_markcanconcancreqlocal">MarkCancOnCancReqLocal</a>, <a href="devtest.kmdf_mdlafterreqcompletedintioctl">MdlAfterReqCompletedIntIoctl</a>, <a href="devtest.kmdf_mdlafterreqcompletedintioctla">MdlAfterReqCompletedIntIoctlA</a>, <a href="devtest.kmdf_mdlafterreqcompletedioctl">MdlAfterReqCompletedIoctl</a>, <a href="devtest.kmdf_mdlafterreqcompletedioctla">MdlAfterReqCompletedIoctlA</a>, <a href="devtest.kmdf_mdlafterreqcompletedread">MdlAfterReqCompletedRead</a>, <a href="devtest.kmdf_mdlafterreqcompletedreada">MdlAfterReqCompletedReadA</a>, <a href="devtest.kmdf_mdlafterreqcompletedwrite">MdlAfterReqCompletedWrite</a>, <a href="devtest.kmdf_mdlafterreqcompletedwritea">MdlAfterReqCompletedWriteA</a>, <a href="devtest.kmdf_memafterreqcompletedintioctl">MemAfterReqCompletedIntIoctl</a>, <a href="devtest.kmdf_memafterreqcompletedintioctla">MemAfterReqCompletedIntIoctlA</a>, <a href="devtest.kmdf_memafterreqcompletedioctl">MemAfterReqCompletedIoctl</a>, <a href="devtest.kmdf_memafterreqcompletedioctla">MemAfterReqCompletedIoctlA</a>, <a href="devtest.kmdf_memafterreqcompletedread">MemAfterReqCompletedRead</a>, <a href="devtest.kmdf_memafterreqcompletedreada">MemAfterReqCompletedReadA</a>, <a href="devtest.kmdf_memafterreqcompletedwrite">MemAfterReqCompletedWrite</a>, <a href="devtest.kmdf_memafterreqcompletedwritea">MemAfterReqCompletedWriteA</a>, <a href="devtest.kmdf_nocancelfromevtsurpriseremove">NoCancelFromEvtSurpriseRemove</a>, <a href="devtest.kmdf_reqdelete">ReqDelete</a>, <a href="devtest.kmdf_reqiscanconcancreq">ReqIsCancOnCancReq</a>, <a href="devtest.kmdf_reqnotcanceledlocal">ReqNotCanceledLocal</a>, <a href="devtest.kmdf_reqsendfail">ReqSendFail</a>, <a href="devtest.kmdf_requestcompleted">RequestCompleted</a>, <a href="devtest.kmdf_requestcompletedlocal">RequestCompletedLocal</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_request_parameters">WDF_REQUEST_PARAMETERS</a>
</dt>
<dt>
<a href="wdf.wdf_request_parameters_init">WDF_REQUEST_PARAMETERS_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548758">WdfObjectReference</a>
</dt>
<dt>
<a href="wdf.wdfrequestcompletewithinformation">WdfRequestCompleteWithInformation</a>
</dt>
<dt>
<a href="wdf.wdfrequestcompletewithpriorityboost">WdfRequestCompleteWithPriorityBoost</a>
</dt>
<dt>
<a href="wdf.wdfrequestgetstatus">WdfRequestGetStatus</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestComplete method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

