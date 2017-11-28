---
UID: NF.wdfrequest.WdfRequestIsCanceled
title: WdfRequestIsCanceled
author: windows-driver-content
description: The WdfRequestIsCanceled method determines whether the I/O manager has attempted to cancel a specified I/O request.
old-location: wdf\wdfrequestiscanceled.htm
old-project: wdf
ms.assetid: 73ec4bf1-ba48-4b51-8824-61ce42f9708d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfRequestIsCanceled
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
req.alt-api: WdfRequestIsCanceled
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2, ReqIsCancOnCancReq
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

# WdfRequestIsCanceled function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfRequestIsCanceled</b> method determines whether the I/O manager has attempted to cancel a specified I/O request.</p>


## -syntax

````
BOOLEAN WdfRequestIsCanceled(
  _In_ WDFREQUEST Request
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>A handle to a framework request object.</p>
</dd>
</dl>

## -returns
<p><b>WdfRequestIsCanceled</b> returns <b>TRUE</b> if the I/O manager has attempted to cancel the specified I/O request. This method may return <b>TRUE</b> even if the calling driver does not own the request.  If the driver does not own the request, it should not call <b>WdfRequestIsCanceled</b>. See additional information in Remarks.</p>

<p><b>WdfRequestIsCanceled</b> returns <b>FALSE</b> for one of the following reasons: </p>

<p>
<ul>
<li>The I/O manager has not attempted to cancel the request.</li>
<li>The calling driver does not own the request. 
</li>
<li>The calling driver has called the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549983">WdfRequestMarkCancelable</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549984">WdfRequestMarkCancelableEx</a> method. 
</li>
</ul>
</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>If your driver has not called <a href="https://msdn.microsoft.com/library/windows/hardware/ff549983">WdfRequestMarkCancelable</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549984">WdfRequestMarkCancelableEx</a> to register an <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-cancel.md">EvtRequestCancel</a> callback function, but if you want your driver to determine if the I/O manager has attempted to cancel an I/O request, the driver can call <b>WdfRequestIsCanceled</b>.</p>

<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff549983">WdfRequestMarkCancelable</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549984">WdfRequestMarkCancelableEx</a>, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a> before calling <b>WdfRequestIsCanceled</b>.</p>

<p>A driver can call <b>WdfRequestIsCanceled</b> for a request only if the driver <a href="wdf.request_ownership">owns</a> the I/O request. </p>

<p>If <b>WdfRequestIsCanceled</b> returns <b>TRUE</b>, your driver should cancel the request by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a> with a <i>Status</i> parameter of STATUS_CANCELLED. If the driver attempts to complete a request that it does not own, the driver can cause the system to crash.</p>

<p>For more information about <b>WdfRequestIsCanceled</b>, see <a href="wdf.canceling_i_o_requests">Canceling I/O Requests</a>
</p>

<p>The following code example calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a> if <b>WdfRequestIsCanceled</b> returns <b>TRUE</b>.</p>

<p>If your driver has not called <a href="https://msdn.microsoft.com/library/windows/hardware/ff549983">WdfRequestMarkCancelable</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549984">WdfRequestMarkCancelableEx</a> to register an <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-cancel.md">EvtRequestCancel</a> callback function, but if you want your driver to determine if the I/O manager has attempted to cancel an I/O request, the driver can call <b>WdfRequestIsCanceled</b>.</p>

<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff549983">WdfRequestMarkCancelable</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549984">WdfRequestMarkCancelableEx</a>, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a> before calling <b>WdfRequestIsCanceled</b>.</p>

<p>A driver can call <b>WdfRequestIsCanceled</b> for a request only if the driver <a href="wdf.request_ownership">owns</a> the I/O request. </p>

<p>If <b>WdfRequestIsCanceled</b> returns <b>TRUE</b>, your driver should cancel the request by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a> with a <i>Status</i> parameter of STATUS_CANCELLED. If the driver attempts to complete a request that it does not own, the driver can cause the system to crash.</p>

<p>For more information about <b>WdfRequestIsCanceled</b>, see <a href="wdf.canceling_i_o_requests">Canceling I/O Requests</a>
</p>

<p>The following code example calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a> if <b>WdfRequestIsCanceled</b> returns <b>TRUE</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551586">ReqIsCancOnCancReq</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549983">WdfRequestMarkCancelable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549984">WdfRequestMarkCancelableEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550035">WdfRequestUnmarkCancelable</a>
</dt>
<dt>
<a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-cancel.md">EvtRequestCancel</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestIsCanceled method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
