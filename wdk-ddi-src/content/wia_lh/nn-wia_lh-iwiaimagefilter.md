---
UID : NN:wia_lh.IWiaImageFilter
title : IWiaImageFilter
author : windows-driver-content
description : The IWiaImageFilter interface is an extension interface implemented by image processing filter developers and called by Microsoft Windows Image Acquisition (WIA).
old-location : image\iwiaimagefilter_interface.htm
old-project : image
ms.assetid : de74898b-ac04-468d-874d-7ca281e22a86
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
req.alt-api : IWiaImageFilter
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

# IWiaImageFilter interface

The <b>IWiaImageFilter</b> interface is an extension interface implemented by image processing filter developers and called by Microsoft Windows Image Acquisition (WIA).

## Methods

<p>The <b>IWiaImageFilter</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wia_lh.IWiaImageFilter.FilterPreviewImage](nf-wia_lh-iwiaimagefilter-filterpreviewimage.md) | The IWiaImageFilter::FilterPreviewImage method is called by the WIA Preview component, when an application calls the IWiaPreview::UpdatePreview method. |
| [wia_lh.IWiaImageFilter.InitializeFilter](nf-wia_lh-iwiaimagefilter-initializefilter.md) | The IWiaImageFilter::InitializeFilter method stores the references to pWiaItem2 and pWiaTransferCallback parameters passed into the method. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | wia_lh.h |
| **DLL** |  |