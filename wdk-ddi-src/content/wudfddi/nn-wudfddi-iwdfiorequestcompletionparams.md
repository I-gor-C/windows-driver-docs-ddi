---
UID : NN:wudfddi.IWDFIoRequestCompletionParams
title : IWDFIoRequestCompletionParams
author : windows-driver-content
description : The IWDFIoRequestCompletionParams interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or asynchronous I/O operation completes.
old-location : wdf\iwdfiorequestcompletionparams.htm
old-project : wdf
ms.assetid : 36bed6be-7202-4dff-989d-57d790b8eb52
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.iwdfiorequestcompletionparams, IWDFIoRequestCompletionParams interface, IWDFIoRequestCompletionParams interface, described, IWDFIoRequestCompletionParams, wudfddi/IWDFIoRequestCompletionParams, UMDFRequestObjectRef_0670626e-575e-482b-bed6-da7d7d86495d.xml, umdf.iwdfiorequestcompletionparams
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wudfddi.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 1.5
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : Unavailable in UMDF 2.0 and later.
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

# IWDFIoRequestCompletionParams interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFIoRequestCompletionParams</b> interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or asynchronous I/O operation completes.

## Methods

<p>The <b>IWDFIoRequestCompletionParams</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IWDFIoRequestCompletionParams.GetIoctlParameters](nf-wudfddi-iwdfiorequestcompletionparams-getioctlparameters.md) | The GetIoctlParameters method retrieves parameters that are associated with the completion of a device I/O control request. |
| [wudfddi.IWDFIoRequestCompletionParams.GetReadParameters](nf-wudfddi-iwdfiorequestcompletionparams-getreadparameters.md) | The GetReadParameters method retrieves parameters that are associated with the completion of a read request. |
| [wudfddi.IWDFIoRequestCompletionParams.GetWriteParameters](nf-wudfddi-iwdfiorequestcompletionparams-getwriteparameters.md) | The GetWriteParameters method retrieves parameters that are associated with the completion of a write request. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h |
| **DLL** | WUDFx.dll |