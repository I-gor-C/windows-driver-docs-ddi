---
UID : NN:wia_lh.IWiaTransferCallback
title : IWiaTransferCallback
author : windows-driver-content
description : The IWiaTransferCallback interface is implemented by image processing filter developers and called by Microsoft Windows Image Acquisition (WIA).
old-location : image\iwiatransfercallback_interface.htm
old-project : image
ms.assetid : c85e5faa-b14b-4775-a5cc-cec5e20dc974
ms.author : windowsdriverdev
ms.date : 1/17/2018
ms.keywords : IWiaTransferCallback, IWiaTransferCallback::TransferCallback, TransferCallback
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wia_lh.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IWiaTransferCallback
req.alt-loc : wia_lh.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : BMP_IMAGE_INFO, *PBMP_IMAGE_INFO
req.product : Windows 10 or later.
---

# IWiaTransferCallback interface

The <b>IWiaTransferCallback</b> interface is implemented by image processing filter developers and called by Microsoft Windows Image Acquisition (WIA).

This interface's methods are called as a result of an application calling <b>IWiaTransfer::Download</b> or the preview component's <b>IWiaPreview::GetNewPreview</b>.

This interface is available in Windows Vista and later operating system versions.

The methods on this interface depend on the <b>IWiaTransfer</b> and <b>IWiaPreview</b> interfaces, both of which are described in the Microsoft Windows SDK documentation.

## Methods

<p>The <b>IWiaTransferCallback</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wia_lh.IWiaTransferCallback.GetNextStream](nf-wia_lh-iwiatransfercallback-getnextstream.md) | The IWiaTransferCallback::GetNextStream method is implemented by an image processing filter. |
| [wia_lh.IWiaTransferCallback.TransferCallback](nf-wia_lh-iwiatransfercallback-transfercallback.md) | The IWiaTransferCallback::TransferCallback method is implemented by an image processing filter. It is called by the WIA service as a result of an application calling IWiaTransfer::Download or the preview component's IWiaPreview::GetNewPreview. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | wia_lh.h |
| **DLL** |  |