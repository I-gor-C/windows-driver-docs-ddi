---
UID: NF.wudfddi.IWDFIoRequest.Send
title: IWDFIoRequest::Send
author: windows-driver-content
description: The Send method sends a request to the specified I/O target.
old-location: wdf\iwdfiorequest_send.htm
old-project: wdf
ms.assetid: f916b414-9cd9-4745-a021-07c810d0d68b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFIoRequest, Send, IWDFIoRequest::Send
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
req.alt-api: IWDFIoRequest.Send
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

# IWDFIoRequest::Send method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>Send</b> method sends a request to the specified I/O target.</p>


## -syntax

````
HRESULT Send(
  [in] IWDFIoTarget *pIoTarget,
  [in] ULONG        Flags,
  [in] LONGLONG     Timeout
);
````


## -parameters
<dl>

### -param <i>pIoTarget</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559170">IWDFIoTarget</a> interface for the I/O target object, which typically represents a lower driver in the stack. </p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A valid bitwise OR of <a href="https://msdn.microsoft.com/library/windows/hardware/ff552493">WDF_REQUEST_SEND_OPTIONS_FLAGS</a>-typed flags.</p>
</dd>

### -param <i>Timeout</i> [in]

<dd>
<p>The amount of time, in system time units (100-nanosecond intervals), that can elapse before the framework automatically cancels the I/O request.</p>
<ul>
<li>
<p>If the value is negative, the expiration time is relative to the current system time.</p>
</li>
<li>
<p>If the value is positive, the expiration time is specified as an absolute time (which is relative to January 1, 1601).</p>
</li>
<li>
<p>If the value is zero, the framework does not time out the request.</p>
</li>
</ul>
<p>Relative expiration times are not affected by any changes to the system time that might occur within the specified time-out period. Absolute expiration times reflect system time changes.</p>
</dd>
</dl>

## -returns
<p><b>Send</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

<p>Note that the return value represents the status of the <b>Send</b> method's attempt to send the I/O request to the I/O target. The return value does not represent the completion status of the I/O request. Your driver must use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560292">IWDFRequestCompletionParams</a> interface to obtain the I/O request's completion status.</p>

## -remarks
<p>If <b>Send</b> returns an error code, the driver should typically complete the request with the error code that <b>Send</b> returned, as the code in the following Example section shows.</p>

<p>If your driver sets the WDF_REQUEST_SEND_OPTION_SYNCHRONOUS flag in the <i>Flags</i> parameter, and if <b>Send</b> successfully sends the I/O request to the I/O target, <b>Send</b> returns after the I/O target completes the I/O request. In this case, <b>Send</b> returns S_OK and the driver can immediately call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559084">IWDFIoRequest::GetCompletionParams</a> to obtain the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560292">IWDFRequestCompletionParams</a> interface. The code example at <b>IWDFIoRequest::GetCompletionParams</b> shows a call to <b>Send</b> with the WDF_REQUEST_SEND_OPTION_SYNCHRONOUS flag set.</p>

<p>If your driver does not set the WDF_REQUEST_SEND_OPTION_SYNCHRONOUS flag, and if <b>Send</b> successfully sends the I/O request to the I/O target, <b>Send</b> returns S_OK while the I/O target is still processing the I/O request asynchronously. In this case, the driver provides an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556905">IRequestCallbackRequestCompletion::OnCompletion</a> callback function that the framework calls after the I/O target completes the I/O request. Typically, the <b>OnCompletion</b> callback function calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff559084">IWDFIoRequest::GetCompletionParams</a>. The code example in the following Example section shows a call to <b>Send</b> without the WDF_REQUEST_SEND_OPTION_SYNCHRONOUS flag.</p>

<p>A driver cannot call <b>Send</b> to send an I/O request to a USB pipe, if the driver has configured a <a href="wdf.working_with_usb_pipes_in_umdf">continuous reader</a> for the pipe.</p>

<p>The following code example forwards a request to a device's I/O target.</p>

<p>If <b>Send</b> returns an error code, the driver should typically complete the request with the error code that <b>Send</b> returned, as the code in the following Example section shows.</p>

<p>If your driver sets the WDF_REQUEST_SEND_OPTION_SYNCHRONOUS flag in the <i>Flags</i> parameter, and if <b>Send</b> successfully sends the I/O request to the I/O target, <b>Send</b> returns after the I/O target completes the I/O request. In this case, <b>Send</b> returns S_OK and the driver can immediately call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559084">IWDFIoRequest::GetCompletionParams</a> to obtain the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560292">IWDFRequestCompletionParams</a> interface. The code example at <b>IWDFIoRequest::GetCompletionParams</b> shows a call to <b>Send</b> with the WDF_REQUEST_SEND_OPTION_SYNCHRONOUS flag set.</p>

<p>If your driver does not set the WDF_REQUEST_SEND_OPTION_SYNCHRONOUS flag, and if <b>Send</b> successfully sends the I/O request to the I/O target, <b>Send</b> returns S_OK while the I/O target is still processing the I/O request asynchronously. In this case, the driver provides an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556905">IRequestCallbackRequestCompletion::OnCompletion</a> callback function that the framework calls after the I/O target completes the I/O request. Typically, the <b>OnCompletion</b> callback function calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff559084">IWDFIoRequest::GetCompletionParams</a>. The code example in the following Example section shows a call to <b>Send</b> without the WDF_REQUEST_SEND_OPTION_SYNCHRONOUS flag.</p>

<p>A driver cannot call <b>Send</b> to send an I/O request to a USB pipe, if the driver has configured a <a href="wdf.working_with_usb_pipes_in_umdf">continuous reader</a> for the pipe.</p>

<p>The following code example forwards a request to a device's I/O target.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556905">IRequestCallbackRequestCompletion::OnCompletion</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561462">WDF_REQUEST_SEND_OPTIONS_FLAGS (UMDF)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559084">IWDFIoRequest::GetCompletionParams</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559170">IWDFIoTarget</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest::Send method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
