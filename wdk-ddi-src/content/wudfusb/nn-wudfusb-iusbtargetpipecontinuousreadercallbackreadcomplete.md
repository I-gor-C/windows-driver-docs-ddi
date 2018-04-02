---
UID: NN:wudfusb.IUsbTargetPipeContinuousReaderCallbackReadComplete
title: IUsbTargetPipeContinuousReaderCallbackReadComplete
author: windows-driver-content
description: IUsbTargetPipeContinuousReaderCallbackReadComplete is a driver-supplied interface.
old-location: wdf\iusbtargetpipecontinuousreadercallbackreadcomplete.htm
old-project: wdf
ms.assetid: 953048ab-872c-4b94-8aef-bcfcb86ea4d8
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IUsbTargetPipeContinuousReaderCallbackReadComplete, IUsbTargetPipeContinuousReaderCallbackReadComplete interface, IUsbTargetPipeContinuousReaderCallbackReadComplete interface, described, UMDFUSBref_bb387411-90fe-4347-910f-4c0fa535a309.xml, umdf.iusbtargetpipecontinuousreadercallbackreadcomplete, wdf.iusbtargetpipecontinuousreadercallbackreadcomplete, wudfusb/IUsbTargetPipeContinuousReaderCallbackReadComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfusb.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	wudfusb.h
api_name:
-	IUsbTargetPipeContinuousReaderCallbackReadComplete
product:
- Windows
targetos: Windows
req.typenames: WDF_USB_REQUEST_TYPE, *PWDF_USB_REQUEST_TYPE
req.product: Windows 10 or later.
---

# IUsbTargetPipeContinuousReaderCallbackReadComplete interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]


<b>IUsbTargetPipeContinuousReaderCallbackReadComplete</b> is a driver-supplied interface.

## Methods

<p>The <b>IUsbTargetPipeContinuousReaderCallbackReadComplete</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion](nf-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete-onreadercompletion.md) | A driver's OnReaderCompletion event callback function informs the driver that a continuous reader has successfully completed a read request. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wudfusb.h |