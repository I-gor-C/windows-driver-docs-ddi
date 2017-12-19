---
UID: NF.wudfddi.IWDFIoRequest2.IsCanceled
title: IWDFIoRequest2::IsCanceled method
author: windows-driver-content
description: The IsCanceled method determines whether the I/O manager has attempted to cancel an I/O request.
old-location: wdf\iwdfiorequest2_iscanceled.htm
old-project: wdf
ms.assetid: 68523fcb-bb0d-492f-b6ae-3dab4f6aa637
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFIoRequest2, IWDFIoRequest2::IsCanceled, IsCanceled
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFIoRequest2.IsCanceled
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
req.irql: 
req.product: Windows 10 or later.
---

# IWDFIoRequest2::IsCanceled method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IsCanceled</b> method determines whether the I/O manager has attempted to cancel an I/O request.



## -syntax

````
BOOL IsCanceled();
````


## -parameters


## -returns
<b>IsCanceled</b> returns <b>TRUE</b> if the I/O manager has attempted to cancel the I/O request. This method returns <b>FALSE</b> for any of the following reasons:


<ul>
<li>The I/O manager has not attempted to cancel the request.</li>
<li>The calling driver does not own the request. 
</li>
<li>The calling driver has called the <a href="wdf.iwdfiorequest_markcancelable">IWDFIoRequest::MarkCancelable</a> method.</li>
</ul>


<b>IsCanceled</b> returns <b>TRUE</b> if the I/O manager has attempted to cancel the I/O request. This method returns <b>FALSE</b> for any of the following reasons:


<ul>
<li>The I/O manager has not attempted to cancel the request.</li>
<li>The calling driver does not own the request. 
</li>
<li>The calling driver has called the <a href="wdf.iwdfiorequest_markcancelable">IWDFIoRequest::MarkCancelable</a> method.</li>
</ul>


<b>IsCanceled</b> returns <b>TRUE</b> if the I/O manager has attempted to cancel the I/O request. This method returns <b>FALSE</b> for any of the following reasons:


<ul>
<li>The I/O manager has not attempted to cancel the request.</li>
<li>The calling driver does not own the request. 
</li>
<li>The calling driver has called the <a href="wdf.iwdfiorequest_markcancelable">IWDFIoRequest::MarkCancelable</a> method.</li>
</ul>



## -remarks
If your driver has not called <a href="wdf.iwdfiorequest_markcancelable">IWDFIoRequest::MarkCancelable</a> to register an <a href="wdf.irequestcallbackcancel_oncancel">IRequestCallbackCancel::OnCancel</a> callback function, but if you want your driver to determine if the I/O manager has attempted to cancel an I/O request, the driver can call <b>IsCanceled</b>.

A driver can call <b>IsCanceled</b> for a request only if the driver owns the I/O request. If the driver has called <a href="wdf.iwdfiorequest_markcancelable">IWDFIoRequest::MarkCancelable</a>, it must call <a href="wdf.iwdfiorequest_unmarkcancelable">IWDFIoRequest::UnmarkCancelable</a> before calling <b>IsCanceled</b>.

If <b>IsCanceled</b> returns <b>TRUE</b>, your driver should cancel the request by calling <a href="wdf.iwdfiorequest_complete">IWDFIoRequest::Complete</a> with the <i>CompletionStatus</i> parameter set to HRESULT_FROM_WIN32(ERROR_OPERATION_ABORTED).

For more information about <b>IsCanceled</b>, see <a href="wdf.canceling_i_o_requests">Canceling I/O Requests</a>.

In the following code example, if <b>IsCanceled</b> returns <b>TRUE</b>, the driver completes the I/O request by calling <a href="wdf.iwdfiorequest_complete">IWDFIoRequest::Complete</a> with a completion status of HRESULT_FROM_WIN32(ERROR_OPERATION_ABORTED).


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.9

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

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
<a href="wdf.irequestcallbackcancel_oncancel">IRequestCallbackCancel::OnCancel</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest_markcancelable">IWDFIoRequest::MarkCancelable</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest_unmarkcancelable">IWDFIoRequest::UnmarkCancelable</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest2::IsCanceled method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
