---
UID : NN:wudfusb.IUsbTargetPipeContinuousReaderCallbackReadersFailed
title : IUsbTargetPipeContinuousReaderCallbackReadersFailed
author : windows-driver-content
description : IUsbTargetPipeContinuousReaderCallbackReadersFailed is a driver-supplied interface.
old-location : wdf\iusbtargetpipecontinuousreadercallbackreadersfailed.htm
old-project : wdf
ms.assetid : d0b68976-f7aa-4b0d-b6bb-258ad2c2e506
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.iusbtargetpipecontinuousreadercallbackreadersfailed, IUsbTargetPipeContinuousReaderCallbackReadersFailed interface, IUsbTargetPipeContinuousReaderCallbackReadersFailed interface, described, IUsbTargetPipeContinuousReaderCallbackReadersFailed, wudfusb/IUsbTargetPipeContinuousReaderCallbackReadersFailed, UMDFUSBref_c38e329c-f04a-4675-ad3b-25677fddedf9.xml, umdf.iusbtargetpipecontinuousreadercallbackreadersfailed
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wudfusb.h
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
req.lib : wudfusb.h
req.dll : WUDFx.dll
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WDF_USB_REQUEST_TYPE, *PWDF_USB_REQUEST_TYPE
req.product : Windows 10 or later.
---

# IUsbTargetPipeContinuousReaderCallbackReadersFailed interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]


<b>IUsbTargetPipeContinuousReaderCallbackReadersFailed</b> is a driver-supplied interface.

## Methods

<p>The <b>IUsbTargetPipeContinuousReaderCallbackReadersFailed</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfusb.IUsbTargetPipeContinuousReaderCallbackReadersFailed.OnReaderFailure](nf-wudfusb-iusbtargetpipecontinuousreadercallbackreadersfailed-onreaderfailure.md) | A driver's OnReaderFailure event callback function informs the driver that a continuous reader has reported an error while processing a read request. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wudfusb.h |