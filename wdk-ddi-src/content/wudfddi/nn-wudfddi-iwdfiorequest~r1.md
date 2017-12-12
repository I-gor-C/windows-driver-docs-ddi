---
UID: NN.wudfddi.IWDFIoRequest~r1
title: IWDFIoRequest
author: windows-driver-content
description: The IWDFIoRequest interface exposes an I/O request object.
old-location: wdf\iwdfiorequest.htm
old-project: wdf
ms.assetid: 3104284a-4277-4f05-ae3f-3b2bb3c3437d
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, POWER_ACTION, *PPOWER_ACTION
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
req.product: Windows 10 or later.
---

# IWDFIoRequest interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFIoRequest</b> interface exposes an I/O request object.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFIoRequest</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a>. <b>IWDFIoRequest</b> also has these types of members:

The <b>IWDFIoRequest</b> interface has these methods.

The <a href="wdf.iwdfiorequest_cancelsentrequest">CancelSentRequest</a> method attempts to cancel the I/O request that the driver previously submitted to an I/O target.

The <a href="wdf.iwdfiorequest_complete">Complete</a> method completes an I/O request.

The <a href="wdf.iwdfiorequest_completewithinformation">CompleteWithInformation</a> method completes a request with the supplied information.

The <a href="wdf.iwdfiorequest_formatusingcurrenttype">FormatUsingCurrentType</a> method formats an I/O request so that the driver can forward it, unmodified, to the next-lower driver.

The <a href="wdf.iwdfiorequest_forwardtoioqueue">ForwardToIoQueue</a> method forwards (that is, requeues) an I/O request to one of the calling driver's I/O queues.

The <a href="wdf.iwdfiorequest_getcompletionparams">GetCompletionParams</a> method retrieves the parameters object for the completion of an I/O request object.

The <a href="wdf.iwdfiorequest_getcreateparameters">GetCreateParameters</a> method retrieves the request parameters for a create-type request.

The <a href="wdf.iwdfiorequest_getdeviceiocontrolparameters">GetDeviceIoControlParameters</a> method retrieves the request parameters for a device I/O control-type request.

The <a href="wdf.iwdfiorequest_getfileobject">GetFileObject</a> method retrieves a pointer to the <a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a> interface that is associated with an I/O request.

The <a href="wdf.iwdfiorequest_getinputmemory">GetInputMemory</a> method retrieves the memory object that represents the input buffer in an I/O request.

The <a href="wdf.iwdfiorequest_getioqueue">GetIoQueue</a> method retrieves the I/O queue object that is associated with an I/O request.

The <a href="wdf.iwdfiorequest_getoutputmemory">GetOutputMemory</a> method retrieves the memory object that represents the output buffer for an I/O request.

The <a href="wdf.iwdfiorequest_getreadparameters">GetReadParameters</a> method retrieves the request parameters for a read-type request.

The <a href="wdf.iwdfiorequest_getrequestorprocessid">GetRequestorProcessId</a> method retrieves the identifier of the process that sent an I/O request.

The <a href="wdf.iwdfiorequest_gettype">GetType</a> method retrieves the type of operation that a request contains.

The <a href="wdf.iwdfiorequest_getwriteparameters">GetWriteParameters</a> method retrieves the request parameters for a write-type request.

The <a href="wdf.iwdfiorequest_impersonate">Impersonate</a> method registers the interface for the method that the framework should call for impersonation.

The <a href="wdf.iwdfiorequest_isfrom32bitprocess">IsFrom32BitProcess</a> method determines whether a request originated from a 32-bit process.

The <a href="wdf.iwdfiorequest_markcancelable">MarkCancelable</a> method enables the canceling of the I/O request.

The <a href="wdf.iwdfiorequest_send">Send</a> method sends a request to the specified I/O target.

The <a href="wdf.iwdfiorequest_setcompletioncallback">SetCompletionCallback</a> method registers the interface for the <a href="wdf.irequestcallbackrequestcompletion_oncompletion">OnCompletion</a> method that the framework should call when an I/O request completes.

The <a href="wdf.iwdfiorequest_setinformation">SetInformation</a> method sets the size of information for a request.

The <a href="wdf.iwdfiorequest_unmarkcancelable">UnmarkCancelable</a> method disables the canceling of an I/O request.

 


## -members
The <b>IWDFIoRequest</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_cancelsentrequest">IWDFIoRequest::CancelSentRequest</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_cancelsentrequest">CancelSentRequest</a> method attempts to cancel the I/O request that the driver previously submitted to an I/O target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_complete">IWDFIoRequest::Complete</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_complete">Complete</a> method completes an I/O request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_completewithinformation">IWDFIoRequest::CompleteWithInformation</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_completewithinformation">CompleteWithInformation</a> method completes a request with the supplied information.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_formatusingcurrenttype">IWDFIoRequest::FormatUsingCurrentType</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_formatusingcurrenttype">FormatUsingCurrentType</a> method formats an I/O request so that the driver can forward it, unmodified, to the next-lower driver.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_forwardtoioqueue">IWDFIoRequest::ForwardToIoQueue</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_forwardtoioqueue">ForwardToIoQueue</a> method forwards (that is, requeues) an I/O request to one of the calling driver's I/O queues.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_getcompletionparams">IWDFIoRequest::GetCompletionParams</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_getcompletionparams">GetCompletionParams</a> method retrieves the parameters object for the completion of an I/O request object.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_getcreateparameters">IWDFIoRequest::GetCreateParameters</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_getcreateparameters">GetCreateParameters</a> method retrieves the request parameters for a create-type request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_getdeviceiocontrolparameters">IWDFIoRequest::GetDeviceIoControlParameters</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_getdeviceiocontrolparameters">GetDeviceIoControlParameters</a> method retrieves the request parameters for a device I/O control-type request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_getfileobject">IWDFIoRequest::GetFileObject</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_getfileobject">GetFileObject</a> method retrieves a pointer to the <a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a> interface that is associated with an I/O request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_getinputmemory">IWDFIoRequest::GetInputMemory</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_getinputmemory">GetInputMemory</a> method retrieves the memory object that represents the input buffer in an I/O request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_getioqueue">IWDFIoRequest::GetIoQueue</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_getioqueue">GetIoQueue</a> method retrieves the I/O queue object that is associated with an I/O request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_getoutputmemory">IWDFIoRequest::GetOutputMemory</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_getoutputmemory">GetOutputMemory</a> method retrieves the memory object that represents the output buffer for an I/O request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_getreadparameters">IWDFIoRequest::GetReadParameters</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_getreadparameters">GetReadParameters</a> method retrieves the request parameters for a read-type request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_getrequestorprocessid">IWDFIoRequest::GetRequestorProcessId</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_getrequestorprocessid">GetRequestorProcessId</a> method retrieves the identifier of the process that sent an I/O request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_gettype">IWDFIoRequest::GetType</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_gettype">GetType</a> method retrieves the type of operation that a request contains.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_getwriteparameters">IWDFIoRequest::GetWriteParameters</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_getwriteparameters">GetWriteParameters</a> method retrieves the request parameters for a write-type request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_impersonate">IWDFIoRequest::Impersonate</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_impersonate">Impersonate</a> method registers the interface for the method that the framework should call for impersonation.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_isfrom32bitprocess">IWDFIoRequest::IsFrom32BitProcess</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_isfrom32bitprocess">IsFrom32BitProcess</a> method determines whether a request originated from a 32-bit process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_markcancelable">IWDFIoRequest::MarkCancelable</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_markcancelable">MarkCancelable</a> method enables the canceling of the I/O request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_send">IWDFIoRequest::Send</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_send">Send</a> method sends a request to the specified I/O target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_setcompletioncallback">IWDFIoRequest::SetCompletionCallback</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_setcompletioncallback">SetCompletionCallback</a> method registers the interface for the <a href="wdf.irequestcallbackrequestcompletion_oncompletion">OnCompletion</a> method that the framework should call when an I/O request completes.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_setinformation">IWDFIoRequest::SetInformation</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_setinformation">SetInformation</a> method sets the size of information for a request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequest_unmarkcancelable">IWDFIoRequest::UnmarkCancelable</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequest_unmarkcancelable">UnmarkCancelable</a> method disables the canceling of an I/O request.

</td>
</tr>
</table>The <a href="wdf.iwdfiorequest_cancelsentrequest">CancelSentRequest</a> method attempts to cancel the I/O request that the driver previously submitted to an I/O target.

The <a href="wdf.iwdfiorequest_complete">Complete</a> method completes an I/O request.

The <a href="wdf.iwdfiorequest_completewithinformation">CompleteWithInformation</a> method completes a request with the supplied information.

The <a href="wdf.iwdfiorequest_formatusingcurrenttype">FormatUsingCurrentType</a> method formats an I/O request so that the driver can forward it, unmodified, to the next-lower driver.

The <a href="wdf.iwdfiorequest_forwardtoioqueue">ForwardToIoQueue</a> method forwards (that is, requeues) an I/O request to one of the calling driver's I/O queues.

The <a href="wdf.iwdfiorequest_getcompletionparams">GetCompletionParams</a> method retrieves the parameters object for the completion of an I/O request object.

The <a href="wdf.iwdfiorequest_getcreateparameters">GetCreateParameters</a> method retrieves the request parameters for a create-type request.

The <a href="wdf.iwdfiorequest_getdeviceiocontrolparameters">GetDeviceIoControlParameters</a> method retrieves the request parameters for a device I/O control-type request.

The <a href="wdf.iwdfiorequest_getfileobject">GetFileObject</a> method retrieves a pointer to the <a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a> interface that is associated with an I/O request.

The <a href="wdf.iwdfiorequest_getinputmemory">GetInputMemory</a> method retrieves the memory object that represents the input buffer in an I/O request.

The <a href="wdf.iwdfiorequest_getioqueue">GetIoQueue</a> method retrieves the I/O queue object that is associated with an I/O request.

The <a href="wdf.iwdfiorequest_getoutputmemory">GetOutputMemory</a> method retrieves the memory object that represents the output buffer for an I/O request.

The <a href="wdf.iwdfiorequest_getreadparameters">GetReadParameters</a> method retrieves the request parameters for a read-type request.

The <a href="wdf.iwdfiorequest_getrequestorprocessid">GetRequestorProcessId</a> method retrieves the identifier of the process that sent an I/O request.

The <a href="wdf.iwdfiorequest_gettype">GetType</a> method retrieves the type of operation that a request contains.

The <a href="wdf.iwdfiorequest_getwriteparameters">GetWriteParameters</a> method retrieves the request parameters for a write-type request.

The <a href="wdf.iwdfiorequest_impersonate">Impersonate</a> method registers the interface for the method that the framework should call for impersonation.

The <a href="wdf.iwdfiorequest_isfrom32bitprocess">IsFrom32BitProcess</a> method determines whether a request originated from a 32-bit process.

The <a href="wdf.iwdfiorequest_markcancelable">MarkCancelable</a> method enables the canceling of the I/O request.

The <a href="wdf.iwdfiorequest_send">Send</a> method sends a request to the specified I/O target.

The <a href="wdf.iwdfiorequest_setcompletioncallback">SetCompletionCallback</a> method registers the interface for the <a href="wdf.irequestcallbackrequestcompletion_oncompletion">OnCompletion</a> method that the framework should call when an I/O request completes.

The <a href="wdf.iwdfiorequest_setinformation">SetInformation</a> method sets the size of information for a request.

The <a href="wdf.iwdfiorequest_unmarkcancelable">UnmarkCancelable</a> method disables the canceling of an I/O request.

 


## -remarks


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
1.5

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h</dt>
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