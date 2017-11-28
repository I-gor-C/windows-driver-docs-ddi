---
UID: NF.wudfddi.IWDFIoRequest.SetCompletionCallback
title: IWDFIoRequest::SetCompletionCallback
author: windows-driver-content
description: The SetCompletionCallback method registers the interface for the OnCompletion method that the framework should call when an I/O request completes.
old-location: wdf\iwdfiorequest_setcompletioncallback.htm
old-project: wdf
ms.assetid: 316b8b75-91ca-4866-b66d-3f66f20126df
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFIoRequest, SetCompletionCallback, IWDFIoRequest::SetCompletionCallback
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFIoRequest.SetCompletionCallback
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
req.iface: IWDFIoRequest
req.product: Windows 10 or later.
---

# IWDFIoRequest::SetCompletionCallback method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>SetCompletionCallback</b> method registers the interface for the <a href="wdf.irequestcallbackrequestcompletion_oncompletion">OnCompletion</a> method that the framework should call when an I/O request completes.</p>


## -syntax

````
void SetCompletionCallback(
  [in]           IRequestCallbackRequestCompletion *pCompletionCallback,
  [in, optional] void                              *pContext
);
````


## -parameters
<dl>

### -param <i>pCompletionCallback</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556904">IRequestCallbackRequestCompletion</a> interface whose <a href="wdf.irequestcallbackrequestcompletion_oncompletion">OnCompletion</a> method the framework calls after the I/O request completes. Beginning with version 1.9 of UMDF, the driver can specify <b>NULL</b> to deregister a previously registered <b>OnCompletion</b> method.</p>
</dd>

### -param <i>pContext</i> [in, optional]

<dd>
<p>A pointer to a buffer that contains context information that is related to the request completion. The framework passes this context information in a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556905">IRequestCallbackRequestCompletion::OnCompletion</a> method. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If a driver that forwards an I/O request requires notification when the lower-level driver completes the request, the driver can provide a completion routine and call <b>SetCompletionCallback</b> to register the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556904">IRequestCallbackRequestCompletion</a> interface for the completion routine. The framework calls the completion routine after the lower-level driver completes the I/O request.</p>

<p>For a code example of how to use the <b>SetCompletionCallback</b> method, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559149">IWDFIoRequest::Send</a>.</p>

<p>If a driver that forwards an I/O request requires notification when the lower-level driver completes the request, the driver can provide a completion routine and call <b>SetCompletionCallback</b> to register the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556904">IRequestCallbackRequestCompletion</a> interface for the completion routine. The framework calls the completion routine after the lower-level driver completes the I/O request.</p>

<p>For a code example of how to use the <b>SetCompletionCallback</b> method, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559149">IWDFIoRequest::Send</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556904">IRequestCallbackRequestCompletion</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556905">IRequestCallbackRequestCompletion::OnCompletion</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559149">IWDFIoRequest::Send</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest::SetCompletionCallback method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
