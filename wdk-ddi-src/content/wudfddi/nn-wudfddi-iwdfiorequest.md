---
UID: NN:wudfddi.IWDFIoRequest
title: IWDFIoRequest
author: windows-driver-content
description: The IWDFIoRequest interface exposes an I/O request object.
old-location: wdf\iwdfiorequest.htm
old-project: wdf
ms.assetid: 3104284a-4277-4f05-ae3f-3b2bb3c3437d
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IWDFIoRequest, IWDFIoRequest interface, IWDFIoRequest interface, described, UMDFRequestObjectRef_65cbf2de-e966-4eb3-8f3f-2012dba23d99.xml, umdf.iwdfiorequest, wdf.iwdfiorequest, wudfddi/IWDFIoRequest
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: wudfddi.h
req.dll: WUDFx.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WUDFx.dll
api_name:
-	IWDFIoRequest
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFIoRequest interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFIoRequest</b> interface exposes an I/O request object.

## Methods

<p>The <b>IWDFIoRequest</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDFIoRequest::CancelSentRequest](nf-wudfddi-iwdfiorequest-cancelsentrequest.md) | The CancelSentRequest method attempts to cancel the I/O request that the driver previously submitted to an I/O target. |
| [IWDFIoRequest::Complete](nf-wudfddi-iwdfiorequest-complete.md) | The Complete method completes an I/O request. |
| [IWDFIoRequest::CompleteWithInformation](nf-wudfddi-iwdfiorequest-completewithinformation.md) | The CompleteWithInformation method completes a request with the supplied information. |
| [IWDFIoRequest::FormatUsingCurrentType](nf-wudfddi-iwdfiorequest-formatusingcurrenttype.md) | The FormatUsingCurrentType method formats an I/O request so that the driver can forward it, unmodified, to the next-lower driver. |
| [IWDFIoRequest::ForwardToIoQueue](nf-wudfddi-iwdfiorequest-forwardtoioqueue.md) | The ForwardToIoQueue method forwards (that is, requeues) an I/O request to one of the calling driver's I/O queues. |
| [IWDFIoRequest::GetCompletionParams](nf-wudfddi-iwdfiorequest-getcompletionparams.md) | The GetCompletionParams method retrieves the parameters object for the completion of an I/O request object. |
| [IWDFIoRequest::GetCreateParameters](nf-wudfddi-iwdfiorequest-getcreateparameters.md) | The GetCreateParameters method retrieves the request parameters for a create-type request. |
| [IWDFIoRequest::GetDeviceIoControlParameters](nf-wudfddi-iwdfiorequest-getdeviceiocontrolparameters.md) | The GetDeviceIoControlParameters method retrieves the request parameters for a device I/O control-type request. |
| [IWDFIoRequest::GetFileObject](nf-wudfddi-iwdfiorequest-getfileobject.md) | The GetFileObject method retrieves a pointer to the IWDFFile interface that is associated with an I/O request. |
| [IWDFIoRequest::GetInputMemory](nf-wudfddi-iwdfiorequest-getinputmemory.md) | The GetInputMemory method retrieves the memory object that represents the input buffer in an I/O request. |
| [IWDFIoRequest::GetIoQueue](nf-wudfddi-iwdfiorequest-getioqueue.md) | The GetIoQueue method retrieves the I/O queue object that is associated with an I/O request. |
| [IWDFIoRequest::GetOutputMemory](nf-wudfddi-iwdfiorequest-getoutputmemory.md) | The GetOutputMemory method retrieves the memory object that represents the output buffer for an I/O request. |
| [IWDFIoRequest::GetReadParameters](nf-wudfddi-iwdfiorequest-getreadparameters.md) | The GetReadParameters method retrieves the request parameters for a read-type request. |
| [IWDFIoRequest::GetRequestorProcessId](nf-wudfddi-iwdfiorequest-getrequestorprocessid.md) | The GetRequestorProcessId method retrieves the identifier of the process that sent an I/O request. |
| [IWDFIoRequest::GetType](nf-wudfddi-iwdfiorequest-gettype.md) | The GetType method retrieves the type of operation that a request contains. |
| [IWDFIoRequest::GetWriteParameters](nf-wudfddi-iwdfiorequest-getwriteparameters.md) | The GetWriteParameters method retrieves the request parameters for a write-type request. |
| [IWDFIoRequest::Impersonate](nf-wudfddi-iwdfiorequest-impersonate.md) | The Impersonate method registers the interface for the method that the framework should call for impersonation. |
| [IWDFIoRequest::IsFrom32BitProcess](nf-wudfddi-iwdfiorequest-isfrom32bitprocess.md) | The IsFrom32BitProcess method determines whether a request originated from a 32-bit process. |
| [IWDFIoRequest::MarkCancelable](nf-wudfddi-iwdfiorequest-markcancelable.md) | The MarkCancelable method enables the canceling of the I/O request. |
| [IWDFIoRequest::Send](nf-wudfddi-iwdfiorequest-send.md) | The Send method sends a request to the specified I/O target. |
| [IWDFIoRequest::SetCompletionCallback](nf-wudfddi-iwdfiorequest-setcompletioncallback.md) | The SetCompletionCallback method registers the interface for the OnCompletion method that the framework should call when an I/O request completes. |
| [IWDFIoRequest::SetInformation](nf-wudfddi-iwdfiorequest-setinformation.md) | The SetInformation method sets the size of information for a request. |
| [IWDFIoRequest::UnmarkCancelable](nf-wudfddi-iwdfiorequest-unmarkcancelable.md) | The UnmarkCancelable method disables the canceling of an I/O request. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h |