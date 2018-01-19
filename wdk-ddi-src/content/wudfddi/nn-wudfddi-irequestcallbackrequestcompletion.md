---
UID : NN:wudfddi.IRequestCallbackRequestCompletion
title : IRequestCallbackRequestCompletion
author : windows-driver-content
description : A driver implements the IRequestCallbackRequestCompletion interface to complete a request object.
old-location : wdf\irequestcallbackrequestcompletion.htm
old-project : wdf
ms.assetid : 65803145-8043-4902-981a-9dbbda2d69e9
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : IWDFWorkItem, IWDFWorkItem::GetParentObject, GetParentObject
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
req.alt-api : IRequestCallbackRequestCompletion
req.alt-loc : wudfddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : WUDFx.dll
req.irql : 
req.typenames : "*PPOWER_ACTION, POWER_ACTION"
req.product : Windows 10 or later.
---

# IRequestCallbackRequestCompletion interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

A driver implements the <b>IRequestCallbackRequestCompletion</b> interface to complete a request object.

## Methods

<p>The <b>IRequestCallbackRequestCompletion</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IRequestCallbackRequestCompletion.OnCompletion](nf-wudfddi-irequestcallbackrequestcompletion-oncompletion.md) | The OnCompletion method completes the specified request. |

## Remarks

A driver registers the <b>IRequestCallbackRequestCompletion</b> interface when it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559153">IWDFIoRequest::SetCompletionCallback</a> method. For more information about how a driver completes an I/O request, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/completing-i-o-requests">Completing I/O Requests</a>.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | wudfddi.h |
| **DLL** | WUDFx.dll |