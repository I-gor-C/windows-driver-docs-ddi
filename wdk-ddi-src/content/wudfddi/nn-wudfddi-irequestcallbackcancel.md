---
UID : NN:wudfddi.IRequestCallbackCancel
title : IRequestCallbackCancel
author : windows-driver-content
description : A driver is notified when an I/O request that the driver is currently processing is to be canceled.
old-location : wdf\irequestcallbackcancel.htm
old-project : wdf
ms.assetid : d6aec38c-6cbb-494c-9fa4-10b6f4a30ae0
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.irequestcallbackcancel, IRequestCallbackCancel interface, IRequestCallbackCancel interface, described, IRequestCallbackCancel, wudfddi/IRequestCallbackCancel, UMDFRequestObjectRef_6f54b76d-812d-437c-8c02-7d9e3e177b90.xml, umdf.irequestcallbackcancel
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wudfddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : wudfddi.h
req.dll : WUDFx.dll
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PPOWER_ACTION, POWER_ACTION"
req.product : Windows 10 or later.
---

# IRequestCallbackCancel interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

A driver is notified when an I/O request that the driver is currently processing is to be canceled. The driver is notified when an application calls the Microsoft Win32 <b>CancelIo</b>, <b>CancelIoEx</b>, or <b>CancelSynchronousIo</b> function. The driver can handle the notification by registering the <b>IRequestCallbackCancel</b> interface.

## Methods

<p>The <b>IRequestCallbackCancel</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IRequestCallbackCancel.OnCancel](nf-wudfddi-irequestcallbackcancel-oncancel.md) | The OnCancel method is called when an application cancels an I/O operation through the Microsoft Win32 CancelIo, CancelIoEx, or CancelSynchronousIo function. |

## Remarks

A driver registers the <b>IRequestCallbackCancel</b> interface when it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559146">IWDFIoRequest::MarkCancelable</a> method to enable the canceling of an I/O request. For more information about how to cancel I/O requests, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/canceling-i-o-requests">Canceling I/O Requests</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | wudfddi.h |
| **DLL** | WUDFx.dll |