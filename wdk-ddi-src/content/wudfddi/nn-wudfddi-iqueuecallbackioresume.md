---
UID : NN:wudfddi.IQueueCallbackIoResume
title : IQueueCallbackIoResume
author : windows-driver-content
description : The IQueueCallbackIoResume interface contains a method that resumes the processing of an I/O request from a queue.
old-location : wdf\iqueuecallbackioresume.htm
old-project : wdf
ms.assetid : 3f27f104-7a06-4f81-9605-2a47c7de7e01
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.iqueuecallbackioresume, IQueueCallbackIoResume interface, IQueueCallbackIoResume interface, described, IQueueCallbackIoResume, wudfddi/IQueueCallbackIoResume, UMDFQueueObjectRef_3ee832e4-15ba-4c39-bb77-38ebbc91983d.xml, umdf.iqueuecallbackioresume
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

# IQueueCallbackIoResume interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IQueueCallbackIoResume</b> interface contains a method that resumes the processing of an I/O request from a queue.

A driver registers the <b>IQueueCallbackIoResume</b> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue.

## Methods

<p>The <b>IQueueCallbackIoResume</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IQueueCallbackIoResume.OnIoResume](nf-wudfddi-iqueuecallbackioresume-onioresume.md) | The OnIoResume method resumes the processing of the specified I/O request from the specified queue. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | wudfddi.h |
| **DLL** | WUDFx.dll |