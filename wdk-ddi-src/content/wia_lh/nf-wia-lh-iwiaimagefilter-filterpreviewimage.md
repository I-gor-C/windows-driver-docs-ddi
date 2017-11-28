---
UID: NF.wia_lh.IWiaImageFilter.FilterPreviewImage
title: IWiaImageFilter::FilterPreviewImage
author: windows-driver-content
description: The IWiaImageFilter::FilterPreviewImage method is called by the WIA Preview component, when an application calls the IWiaPreview::UpdatePreview method.
old-location: image\iwiaimagefilter_filterpreviewimage.htm
old-project: image
ms.assetid: 92e4ea13-156b-4d5e-8268-ddb45f6d7b50
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWiaImageFilter, FilterPreviewImage, IWiaImageFilter::FilterPreviewImage
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wia_lh.h
req.include-header: Wia_lh.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaImageFilter.FilterPreviewImage
req.alt-loc: wia_lh.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IWiaImageFilter
req.product: Windows 10 or later.
---

# IWiaImageFilter::FilterPreviewImage method



## -description
<p>The <b>IWiaImageFilter::FilterPreviewImage</b> method is called by the WIA Preview component, when an application calls the <b>IWiaPreview::UpdatePreview</b> method.</p>


## -syntax

````
HRESULT  FilterPreviewImage(
  [in] IWiaItem2   *pWiaChildItem2,
  [in] RECT        InputImageExtents,
  [in] IStream     *pInputStream
    
);
````


## -parameters
<dl>

### -param <i>pWiaChildItem2</i> [in]

<dd>
<p>Pointer to the item that the image process is to process. This item must be a child item of the item specified in the pWiaItem2 parameter, which was passed into the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543916">IWiaImageFilter::InitializeFilter</a> method. 
</p>
</dd>

### -param <i>InputImageExtents</i> [in]

<dd>
<p>Structure that contains the upper-left and lower-right coordinates of a rectangle that represents the boundaries of the preview image on the flatbed's platen. This is also the coordinates for the image data that is passed into the <i>pInputStream</i> parameter .</p>
</dd>

### -param <i>pInputStream
    </i> [in]

<dd>
<p>Pointer to the IStream preview image. </p>
</dd>
</dl>

## -returns
<p>Returns S_OK on success, or a standard COM error code on failure.</p>

## -remarks
<p>This method cannot be invoked directly by the application.</p>

<p>The <b>IStream </b>and <b>IWiaPreview</b> interfaces are described in the Microsoft Windows SDK documentation.</p>

<p>This method cannot be invoked directly by the application.</p>

<p>The <b>IStream </b>and <b>IWiaPreview</b> interfaces are described in the Microsoft Windows SDK documentation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wia_lh.h (include Wia_lh.h)</dt>
</dl>
</td>
</tr>
</table>