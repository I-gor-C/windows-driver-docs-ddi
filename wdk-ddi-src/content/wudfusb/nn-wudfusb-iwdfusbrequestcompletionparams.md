---
UID : NN:wudfusb.IWDFUsbRequestCompletionParams
title : IWDFUsbRequestCompletionParams
author : windows-driver-content
description : The IWDFUsbRequestCompletionParams interface exposes the parameters object for the completion of a USB request object. The parameters object is primarily required for asynchronous I/O and layered drivers.
old-location : wdf\iwdfusbrequestcompletionparams.htm
old-project : wdf
ms.assetid : 50a0c8c9-06c6-48c9-a799-0949cf415f6e
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.iwdfusbrequestcompletionparams, IWDFUsbRequestCompletionParams interface, IWDFUsbRequestCompletionParams interface, described, IWDFUsbRequestCompletionParams, wudfusb/IWDFUsbRequestCompletionParams, UMDFRequestObjectRef_f55ce370-f488-405f-a104-9a85fcab6cbb.xml, umdf.iwdfusbrequestcompletionparams
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wudfusb.h
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

# IWDFUsbRequestCompletionParams interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFUsbRequestCompletionParams</b> interface exposes the parameters object for the completion of a USB request object. The parameters object is primarily required for asynchronous I/O and layered drivers.

## Methods

<p>The <b>IWDFUsbRequestCompletionParams</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfusb.IWDFUsbRequestCompletionParams.GetCompletedUsbRequestType](nf-wudfusb-iwdfusbrequestcompletionparams-getcompletedusbrequesttype.md) | The GetCompletedUsbRequestType method retrieves the type of operation that the request to be completed contains. |
| [wudfusb.IWDFUsbRequestCompletionParams.GetDeviceControlTransferParameters](nf-wudfusb-iwdfusbrequestcompletionparams-getdevicecontroltransferparameters.md) | The GetDeviceControlTransferParameters method retrieves parameters that are associated with the completion of a device I/O control request. |
| [wudfusb.IWDFUsbRequestCompletionParams.GetPipeReadParameters](nf-wudfusb-iwdfusbrequestcompletionparams-getpipereadparameters.md) | The GetPipeReadParameters method retrieves parameters that are associated with the completion of a read request. |
| [wudfusb.IWDFUsbRequestCompletionParams.GetPipeWriteParameters](nf-wudfusb-iwdfusbrequestcompletionparams-getpipewriteparameters.md) | The GetPipeWriteParameters method retrieves parameters that are associated with the completion of a write request. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfusb.h |