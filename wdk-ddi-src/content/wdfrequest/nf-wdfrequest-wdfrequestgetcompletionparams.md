---
UID: NF.wdfrequest.WdfRequestGetCompletionParams
title: WdfRequestGetCompletionParams
author: windows-driver-content
description: The WdfRequestGetCompletionParams method retrieves the I/O completion parameters that are associated with a specified framework request object.
old-location: wdf\wdfrequestgetcompletionparams.htm
old-project: wdf
ms.assetid: 167bb0f3-a484-443b-8bc4-bb2bbcecc19a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfRequestGetCompletionParams
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
req.alt-api: WdfRequestGetCompletionParams
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, InvalidReqAccess, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfRequestGetCompletionParams function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfRequestGetCompletionParams</b> method retrieves the I/O completion parameters that are associated with a specified framework request object.</p>


## -syntax

````
VOID WdfRequestGetCompletionParams(
  _In_  WDFREQUEST                     Request,
  _Out_ PWDF_REQUEST_COMPLETION_PARAMS Params
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>A handle to a framework request object.</p>
</dd>

### -param <i>Params</i> [out]

<dd>
<p>A pointer to a caller-supplied <a href="..\wdfrequest\ns-wdfrequest--wdf-request-completion-params.md">WDF_REQUEST_COMPLETION_PARAMS</a> structure.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>After a driver has called <a href="..\wdfrequest\nf-wdfrequest-wdfrequestsend.md">WdfRequestSend</a> to synchronously or asynchronously send an I/O request to an I/O target, and after the I/O target has <a href="https://msdn.microsoft.com/library/windows/hardware/dn265386">completed</a> the I/O request, the driver can call <b>WdfRequestGetCompletionParams</b> to obtain the I/O request's completion parameters.</p>

<p>The completion parameters structure contains valid information only if the driver has formatted the request by calling one of the <b>WdfIoTargetFormat</b><i>Xxx</i> methods. For example, see <a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetformatrequestforread.md">WdfIoTargetFormatRequestForRead</a>.</p>

<p>Note that if your driver calls one of the methods that sends I/O requests to I/O targets only synchronously (such as <a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendreadsynchronously.md">WdfIoTargetSendReadSynchronously</a>), the driver must <i>not</i> call <b>WdfRequestGetCompletionParams</b>.</p>

<p>The <b>WdfRequestGetCompletionParams</b> method copies the I/O request's completion parameters into the specified <a href="..\wdfrequest\ns-wdfrequest--wdf-request-completion-params.md">WDF_REQUEST_COMPLETION_PARAMS</a> structure.</p>

<p>If a driver sends an I/O request asynchronously, it typically calls this method from within a <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-completion-routine.md">CompletionRoutine</a> callback function.</p>

<p>For more information about <b>WdfRequestGetCompletionParams</b>, see <a href="wdf.completing_i_o_requests">Completing I/O Requests</a>.</p>

<p>The following code example initializes a <a href="..\wdfrequest\ns-wdfrequest--wdf-request-completion-params.md">WDF_REQUEST_COMPLETION_PARAMS</a> structure and then calls <b>WdfRequestGetCompletionParams</b>.</p>

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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_invalidreqaccess">InvalidReqAccess</a>, <a href="devtest.kmdf_invalidreqaccesslocal">InvalidReqAccessLocal</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfrequest\ns-wdfrequest--wdf-request-completion-params.md">WDF_REQUEST_COMPLETION_PARAMS</a>
</dt>
<dt>
<a href="..\wdfrequest\nf-wdfrequest-wdf-request-completion-params-init.md">WDF_REQUEST_COMPLETION_PARAMS_INIT</a>
</dt>
<dt>
<a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-completion-routine.md">CompletionRoutine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestGetCompletionParams method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
