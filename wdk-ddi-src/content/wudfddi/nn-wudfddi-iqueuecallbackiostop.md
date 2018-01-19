---
UID : NN:wudfddi.IQueueCallbackIoStop
title : IQueueCallbackIoStop
author : windows-driver-content
description : The IQueueCallbackIoStop interface contains a method that stops the processing of an I/O request from a queue.
old-location : wdf\iqueuecallbackiostop.htm
old-project : wdf
ms.assetid : 430ee7fd-cffb-452d-b2e8-0dc252987487
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
req.alt-api : IQueueCallbackIoStop
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

# IQueueCallbackIoStop interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IQueueCallbackIoStop</b> interface contains a method that stops the processing of an I/O request from a queue.

## Methods

<p>The <b>IQueueCallbackIoStop</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IQueueCallbackIoStop.OnIoStop](nf-wudfddi-iqueuecallbackiostop-oniostop.md) | The OnIoStop callback function stops the processing of the specified I/O request from the specified queue. |

## Remarks

A driver registers the <b>IQueueCallbackIoStop</b> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. </p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | wudfddi.h |
| **DLL** | WUDFx.dll |