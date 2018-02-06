---
UID: NF:wia_lh.IWiaImageFilter.FilterPreviewImage
title: IWiaImageFilter::FilterPreviewImage method
author: windows-driver-content
description: The IWiaImageFilter::FilterPreviewImage method is called by the WIA Preview component, when an application calls the IWiaPreview::UpdatePreview method.
old-location: image\iwiaimagefilter_filterpreviewimage.htm
old-project: image
ms.assetid: 92e4ea13-156b-4d5e-8268-ddb45f6d7b50
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: FilterPreviewImage method [Imaging Devices], IWiaImageFilter interface, FilterPreviewImage, FilterPreviewImage method [Imaging Devices], IWiaImageFilter interface [Imaging Devices], FilterPreviewImage method, wia_lh/IWiaImageFilter::FilterPreviewImage, IWiaErrorHandler_22a9ad6b-b9f4-49e5-9c62-2d32fbaf3d02.xml, IWiaImageFilter, IWiaImageFilter::FilterPreviewImage, image.iwiaimagefilter_filterpreviewimage
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wia_lh.h
req.include-header: Wia_lh.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
req.lib: wia_lh.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	wia_lh.h
apiname:
-	IWiaImageFilter.FilterPreviewImage
product: Windows
targetos: Windows
req.typenames: "*PBMP_IMAGE_INFO, BMP_IMAGE_INFO"
req.product: Windows 10 or later.
---


# FilterPreviewImage method
The <b>IWiaImageFilter::FilterPreviewImage</b> method is called by the WIA Preview component, when an application calls the <b>IWiaPreview::UpdatePreview</b> method.

## Syntax

````
HRESULT  FilterPreviewImage(
  [in] IWiaItem2   *pWiaChildItem2,
  [in] RECT        InputImageExtents,
  [in] IStream     *pInputStream
    
);
````

## Parameters

`lFlags`



`pWiaChildItem2`

Pointer to the item that the image process is to process. This item must be a child item of the item specified in the pWiaItem2 parameter, which was passed into the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543916">IWiaImageFilter::InitializeFilter</a> method.

`InputImageExtents`

Structure that contains the upper-left and lower-right coordinates of a rectangle that represents the boundaries of the preview image on the flatbed's platen. This is also the coordinates for the image data that is passed into the <i>pInputStream</i> parameter .

`pInputStream`

Pointer to the IStream preview image.


## Return Value

Returns S_OK on success, or a standard COM error code on failure.

## Remarks

This method cannot be invoked directly by the application.

The <b>IStream </b>and <b>IWiaPreview</b> interfaces are described in the Microsoft Windows SDK documentation.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Target Platform** | Desktop |
| **Header** | wia_lh.h (include Wia_lh.h) |
| **Library** | wia_lh.h |