---
UID: NN:wudfusb.IWDFUsbTargetPipe
title: IWDFUsbTargetPipe
author: windows-driver-content
description: The IWDFUsbTargetPipe interface exposes a USB pipe (endpoint), which is also an I/O target.
old-location: wdf\iwdfusbtargetpipe.htm
old-project: wdf
ms.assetid: 16364b13-d902-4ba3-8d0a-c044946afa1e
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: wdf.iwdfusbtargetpipe, IWDFUsbTargetPipe interface, IWDFUsbTargetPipe interface, described, IWDFUsbTargetPipe, wudfusb/IWDFUsbTargetPipe, UMDFUSBref_985f9453-7475-4e9b-894c-5d4e7b8d3971.xml, umdf.iwdfusbtargetpipe
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfusb.h
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
req.lib: wudfusb.h
req.dll: WUDFx.dll
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	WUDFx.dll
apiname:
-	IWDFUsbTargetPipe
product: Windows
targetos: Windows
req.typenames: WDF_USB_REQUEST_TYPE, *PWDF_USB_REQUEST_TYPE
req.product: Windows 10 or later.
---

# IWDFUsbTargetPipe interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]


The <b>IWDFUsbTargetPipe</b> interface exposes a USB pipe (endpoint), which is also an I/O target.

## Methods

<p>The <b>IWDFUsbTargetPipe</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfusb.IWDFUsbTargetPipe.Abort](nf-wudfusb-iwdfusbtargetpipe-abort.md) | The Abort method aborts all pending transfers on a USB pipe. |
| [wudfusb.IWDFUsbTargetPipe.Flush](nf-wudfusb-iwdfusbtargetpipe-flush.md) | The Flush method discards any data that WinUsb saved when the device returned more data than the client requested. |
| [wudfusb.IWDFUsbTargetPipe.GetInformation](nf-wudfusb-iwdfusbtargetpipe-getinformation.md) | The GetInformation method retrieves information about a USB pipe (endpoint). |
| [wudfusb.IWDFUsbTargetPipe.GetType](nf-wudfusb-iwdfusbtargetpipe-gettype.md) | The GetType method retrieves the type of a USB pipe. |
| [wudfusb.IWDFUsbTargetPipe.IsInEndPoint](nf-wudfusb-iwdfusbtargetpipe-isinendpoint.md) | The IsInEndPoint method determines whether a USB pipe (endpoint) is an IN pipe. |
| [wudfusb.IWDFUsbTargetPipe.IsOutEndPoint](nf-wudfusb-iwdfusbtargetpipe-isoutendpoint.md) | The IsOutEndPoint method determines whether a USB pipe (endpoint) is an OUT pipe. |
| [wudfusb.IWDFUsbTargetPipe.Reset](nf-wudfusb-iwdfusbtargetpipe-reset.md) | The Reset method resets the data toggle and clears the stall condition on a USB pipe. |
| [wudfusb.IWDFUsbTargetPipe.RetrievePipePolicy](nf-wudfusb-iwdfusbtargetpipe-retrievepipepolicy.md) | The RetrievePipePolicy method retrieves a WinUsb pipe policy. |
| [wudfusb.IWDFUsbTargetPipe.SetPipePolicy](nf-wudfusb-iwdfusbtargetpipe-setpipepolicy.md) | The SetPipePolicy method sets the WinUsb pipe policy. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfusb.h |