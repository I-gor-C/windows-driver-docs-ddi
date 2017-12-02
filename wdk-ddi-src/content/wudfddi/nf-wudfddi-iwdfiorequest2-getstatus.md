---
UID: NF.wudfddi.IWDFIoRequest2.GetStatus
title: IWDFIoRequest2::GetStatus
author: windows-driver-content
description: The GetStatus method returns the status of an I/O request.
old-location: wdf\iwdfiorequest2_getstatus.htm
old-project: wdf
ms.assetid: 20b10edb-3294-4cc7-91bc-07df565a9cf2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFIoRequest2, GetStatus, IWDFIoRequest2::GetStatus
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
req.alt-api: IWDFIoRequest2.GetStatus
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

# IWDFIoRequest2::GetStatus method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>GetStatus</b> method returns the status of an I/O request.</p>


## -syntax

````
HRESULT GetStatus();
````


## -parameters


## -returns
<p><b>GetStatus</b> returns an HRESULT-typed status value, This value indicates the current status of the I/O request that the <a href="..\wudfddi\nn-wudfddi-iwdfiorequest2.md">IWDFIoRequest2</a> interface represents. </p>

<p><b>GetStatus</b> returns an HRESULT-typed status value, This value indicates the current status of the I/O request that the <a href="..\wudfddi\nn-wudfddi-iwdfiorequest2.md">IWDFIoRequest2</a> interface represents. </p>

<p><b>GetStatus</b> returns an HRESULT-typed status value, This value indicates the current status of the I/O request that the <a href="..\wudfddi\nn-wudfddi-iwdfiorequest2.md">IWDFIoRequest2</a> interface represents. </p>

## -remarks
<p>A driver can call <b>GetStatus</b> after it has called <a href="wdf.iwdfiorequest_send">IWDFIoRequest::Send</a> to send an I/O request to an I/O target. </p>

<p>If a driver's call to <a href="wdf.iwdfiorequest_send">Send</a> succeeds, <b>GetStatus</b> returns the status value that is set by the driver that completes the specified request.</p>

<p>If the driver specifies WDF_REQUEST_SEND_OPTION_SYNCHRONOUS for a request when it calls <a href="wdf.iwdfiorequest_send">Send</a>, the driver can call <b>GetStatus</b> (or <a href="wdf.iwdfiorequest_getcompletionparams">IWDFIoRequest::GetCompletionParams</a>) immediately after calling <b>Send</b>.</p>

<p>If the driver does not specify WDF_REQUEST_SEND_OPTION_SYNCHRONOUS when it calls <a href="wdf.iwdfiorequest_send">Send</a>, the driver typically calls <b>GetStatus</b> (or <a href="wdf.iwdfiorequest_getcompletionparams">IWDFIoRequest::GetCompletionParams</a>) from within an <a href="wdf.irequestcallbackrequestcompletion_oncompletion">IRequestCallbackRequestCompletion::OnCompletion</a> callback function.</p>

<p>If a driver's call to <a href="wdf.iwdfiorequest_send">Send</a> fails, <b>Send</b> returns a status value that the framework has set to describe the failure. The driver can call <b>GetStatus</b> (but not<a href="wdf.iwdfiorequest_getcompletionparams">IWDFIoRequest::GetCompletionParams</a>) to obtain the current status of the request, but in this case <b>GetStatus</b> returns the same failure code that <b>Send</b> returned.</p>

<p>For more information about request completion, see <a href="wdf.completing_i_o_requests">Completing I/O Requests</a>.</p>

<p>The following code example sends an I/O request to an I/O target. If the call to <a href="wdf.iwdfiorequest_send">Send</a> succeeds, the example obtains the <a href="..\wudfddi\nn-wudfddi-iwdfiorequest2.md">IWDFIoRequest2</a> interface, calls <b>GetStatus</b> to obtain the request's status value, and then calls <a href="wdf.iwdfiorequest_completewithinformation">IWDFIoRequest::CompleteWithInformation</a> to complete the I/O request.</p>

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
<a href="..\wudfddi\nn-wudfddi-iwdfiorequest2.md">IWDFIoRequest2</a>
</dt>
<dt>
<a href="wdf.irequestcallbackrequestcompletion_oncompletion">IRequestCallbackRequestCompletion::OnCompletion</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest_completewithinformation">IWDFIoRequest::CompleteWithInformation</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest_getcompletionparams">IWDFIoRequest::GetCompletionParams</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest_send">IWDFIoRequest::Send</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest2::GetStatus method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
