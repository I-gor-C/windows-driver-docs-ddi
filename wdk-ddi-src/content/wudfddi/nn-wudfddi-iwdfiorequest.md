---
UID: NN.wudfddi.IWDFIoRequest
title: IWDFIoRequest
author: windows-driver-content
description: The IWDFIoRequest interface exposes an I/O request object.
old-location: wdf\iwdfiorequest.htm
old-project: wdf
ms.assetid: 3104284a-4277-4f05-ae3f-3b2bb3c3437d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFIoRequest
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
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IWDFIoRequest interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IWDFIoRequest</b> interface exposes an I/O request object.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFIoRequest</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff560200">IWDFObject</a>. <b>IWDFIoRequest</b> also has these types of members:</p>

<p>The <b>IWDFIoRequest</b> interface has these methods.</p>

<p>The <a href="wdf.iwdfiorequest_cancelsentrequest">CancelSentRequest</a> method attempts to cancel the I/O request that the driver previously submitted to an I/O target.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh406719">Complete</a> method completes an I/O request.</p>

<p>The <a href="wdf.iwdfiorequest_completewithinformation">CompleteWithInformation</a> method completes a request with the supplied information.</p>

<p>The <a href="wdf.iwdfiorequest_formatusingcurrenttype">FormatUsingCurrentType</a> method formats an I/O request so that the driver can forward it, unmodified, to the next-lower driver.</p>

<p>The <a href="wdf.iwdfiorequest_forwardtoioqueue">ForwardToIoQueue</a> method forwards (that is, requeues) an I/O request to one of the calling driver's I/O queues.</p>

<p>The <a href="wdf.iwdfiorequest_getcompletionparams">GetCompletionParams</a> method retrieves the parameters object for the completion of an I/O request object.</p>

<p>The <a href="wdf.iwdfiorequest_getcreateparameters">GetCreateParameters</a> method retrieves the request parameters for a create-type request.</p>

<p>The <a href="wdf.iwdfiorequest_getdeviceiocontrolparameters">GetDeviceIoControlParameters</a> method retrieves the request parameters for a device I/O control-type request.</p>

<p>The <a href="wdf.iwdfiorequest_getfileobject">GetFileObject</a> method retrieves a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a> interface that is associated with an I/O request.</p>

<p>The <a href="wdf.iwdfiorequest_getinputmemory">GetInputMemory</a> method retrieves the memory object that represents the input buffer in an I/O request.</p>

<p>The <a href="wdf.iwdfiorequest_getioqueue">GetIoQueue</a> method retrieves the I/O queue object that is associated with an I/O request.</p>

<p>The <a href="wdf.iwdfiorequest_getoutputmemory">GetOutputMemory</a> method retrieves the memory object that represents the output buffer for an I/O request.</p>

<p>The <a href="wdf.iwdfiorequest_getreadparameters">GetReadParameters</a> method retrieves the request parameters for a read-type request.</p>

<p>The <a href="wdf.iwdfiorequest_getrequestorprocessid">GetRequestorProcessId</a> method retrieves the identifier of the process that sent an I/O request.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/jj991813">GetType</a> method retrieves the type of operation that a request contains.</p>

<p>The <a href="wdf.iwdfiorequest_getwriteparameters">GetWriteParameters</a> method retrieves the request parameters for a write-type request.</p>

<p>The <a href="wdf.iwdfiorequest_impersonate">Impersonate</a> method registers the interface for the method that the framework should call for impersonation.</p>

<p>The <a href="wdf.iwdfiorequest_isfrom32bitprocess">IsFrom32BitProcess</a> method determines whether a request originated from a 32-bit process.</p>

<p>The <a href="wdf.iwdfiorequest_markcancelable">MarkCancelable</a> method enables the canceling of the I/O request.</p>

<p>The <a href="wdf.iwdfiorequest_send">Send</a> method sends a request to the specified I/O target.</p>

<p>The <a href="wdf.iwdfiorequest_setcompletioncallback">SetCompletionCallback</a> method registers the interface for the <a href="wdf.irequestcallbackrequestcompletion_oncompletion">OnCompletion</a> method that the framework should call when an I/O request completes.</p>

<p>The <a href="wdf.iwdfiorequest_setinformation">SetInformation</a> method sets the size of information for a request.</p>

<p>The <a href="wdf.iwdfiorequest_unmarkcancelable">UnmarkCancelable</a> method disables the canceling of an I/O request.</p>

<p> </p>

## -members
<p>The <b>IWDFIoRequest</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559067">IWDFIoRequest::CancelSentRequest</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_cancelsentrequest">CancelSentRequest</a> method attempts to cancel the I/O request that the driver previously submitted to an I/O target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh406719">Complete</a> method completes an I/O request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559074">IWDFIoRequest::CompleteWithInformation</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_completewithinformation">CompleteWithInformation</a> method completes a request with the supplied information.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559077">IWDFIoRequest::FormatUsingCurrentType</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_formatusingcurrenttype">FormatUsingCurrentType</a> method formats an I/O request so that the driver can forward it, unmodified, to the next-lower driver.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559081">IWDFIoRequest::ForwardToIoQueue</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_forwardtoioqueue">ForwardToIoQueue</a> method forwards (that is, requeues) an I/O request to one of the calling driver's I/O queues.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559084">IWDFIoRequest::GetCompletionParams</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_getcompletionparams">GetCompletionParams</a> method retrieves the parameters object for the completion of an I/O request object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559088">IWDFIoRequest::GetCreateParameters</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_getcreateparameters">GetCreateParameters</a> method retrieves the request parameters for a create-type request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559095">IWDFIoRequest::GetDeviceIoControlParameters</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_getdeviceiocontrolparameters">GetDeviceIoControlParameters</a> method retrieves the request parameters for a device I/O control-type request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559099">IWDFIoRequest::GetFileObject</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_getfileobject">GetFileObject</a> method retrieves a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a> interface that is associated with an I/O request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559100">IWDFIoRequest::GetInputMemory</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_getinputmemory">GetInputMemory</a> method retrieves the memory object that represents the input buffer in an I/O request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559103">IWDFIoRequest::GetIoQueue</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_getioqueue">GetIoQueue</a> method retrieves the I/O queue object that is associated with an I/O request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559112">IWDFIoRequest::GetOutputMemory</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_getoutputmemory">GetOutputMemory</a> method retrieves the memory object that represents the output buffer for an I/O request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559113">IWDFIoRequest::GetReadParameters</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_getreadparameters">GetReadParameters</a> method retrieves the request parameters for a read-type request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559118">IWDFIoRequest::GetRequestorProcessId</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_getrequestorprocessid">GetRequestorProcessId</a> method retrieves the identifier of the process that sent an I/O request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559124">IWDFIoRequest::GetType</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/jj991813">GetType</a> method retrieves the type of operation that a request contains.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559130">IWDFIoRequest::GetWriteParameters</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_getwriteparameters">GetWriteParameters</a> method retrieves the request parameters for a write-type request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559136">IWDFIoRequest::Impersonate</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_impersonate">Impersonate</a> method registers the interface for the method that the framework should call for impersonation.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559139">IWDFIoRequest::IsFrom32BitProcess</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_isfrom32bitprocess">IsFrom32BitProcess</a> method determines whether a request originated from a 32-bit process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559146">IWDFIoRequest::MarkCancelable</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_markcancelable">MarkCancelable</a> method enables the canceling of the I/O request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559149">IWDFIoRequest::Send</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_send">Send</a> method sends a request to the specified I/O target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559153">IWDFIoRequest::SetCompletionCallback</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_setcompletioncallback">SetCompletionCallback</a> method registers the interface for the <a href="wdf.irequestcallbackrequestcompletion_oncompletion">OnCompletion</a> method that the framework should call when an I/O request completes.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559159">IWDFIoRequest::SetInformation</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_setinformation">SetInformation</a> method sets the size of information for a request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559163">IWDFIoRequest::UnmarkCancelable</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiorequest_unmarkcancelable">UnmarkCancelable</a> method disables the canceling of an I/O request.</p>
</td>
</tr>
</table><p>The <a href="wdf.iwdfiorequest_cancelsentrequest">CancelSentRequest</a> method attempts to cancel the I/O request that the driver previously submitted to an I/O target.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh406719">Complete</a> method completes an I/O request.</p>

<p>The <a href="wdf.iwdfiorequest_completewithinformation">CompleteWithInformation</a> method completes a request with the supplied information.</p>

<p>The <a href="wdf.iwdfiorequest_formatusingcurrenttype">FormatUsingCurrentType</a> method formats an I/O request so that the driver can forward it, unmodified, to the next-lower driver.</p>

<p>The <a href="wdf.iwdfiorequest_forwardtoioqueue">ForwardToIoQueue</a> method forwards (that is, requeues) an I/O request to one of the calling driver's I/O queues.</p>

<p>The <a href="wdf.iwdfiorequest_getcompletionparams">GetCompletionParams</a> method retrieves the parameters object for the completion of an I/O request object.</p>

<p>The <a href="wdf.iwdfiorequest_getcreateparameters">GetCreateParameters</a> method retrieves the request parameters for a create-type request.</p>

<p>The <a href="wdf.iwdfiorequest_getdeviceiocontrolparameters">GetDeviceIoControlParameters</a> method retrieves the request parameters for a device I/O control-type request.</p>

<p>The <a href="wdf.iwdfiorequest_getfileobject">GetFileObject</a> method retrieves a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a> interface that is associated with an I/O request.</p>

<p>The <a href="wdf.iwdfiorequest_getinputmemory">GetInputMemory</a> method retrieves the memory object that represents the input buffer in an I/O request.</p>

<p>The <a href="wdf.iwdfiorequest_getioqueue">GetIoQueue</a> method retrieves the I/O queue object that is associated with an I/O request.</p>

<p>The <a href="wdf.iwdfiorequest_getoutputmemory">GetOutputMemory</a> method retrieves the memory object that represents the output buffer for an I/O request.</p>

<p>The <a href="wdf.iwdfiorequest_getreadparameters">GetReadParameters</a> method retrieves the request parameters for a read-type request.</p>

<p>The <a href="wdf.iwdfiorequest_getrequestorprocessid">GetRequestorProcessId</a> method retrieves the identifier of the process that sent an I/O request.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/jj991813">GetType</a> method retrieves the type of operation that a request contains.</p>

<p>The <a href="wdf.iwdfiorequest_getwriteparameters">GetWriteParameters</a> method retrieves the request parameters for a write-type request.</p>

<p>The <a href="wdf.iwdfiorequest_impersonate">Impersonate</a> method registers the interface for the method that the framework should call for impersonation.</p>

<p>The <a href="wdf.iwdfiorequest_isfrom32bitprocess">IsFrom32BitProcess</a> method determines whether a request originated from a 32-bit process.</p>

<p>The <a href="wdf.iwdfiorequest_markcancelable">MarkCancelable</a> method enables the canceling of the I/O request.</p>

<p>The <a href="wdf.iwdfiorequest_send">Send</a> method sends a request to the specified I/O target.</p>

<p>The <a href="wdf.iwdfiorequest_setcompletioncallback">SetCompletionCallback</a> method registers the interface for the <a href="wdf.irequestcallbackrequestcompletion_oncompletion">OnCompletion</a> method that the framework should call when an I/O request completes.</p>

<p>The <a href="wdf.iwdfiorequest_setinformation">SetInformation</a> method sets the size of information for a request.</p>

<p>The <a href="wdf.iwdfiorequest_unmarkcancelable">UnmarkCancelable</a> method disables the canceling of an I/O request.</p>

<p> </p>

## -remarks


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
<dt>Wudfddi.h</dt>
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