---
UID: NF.wia_lh.IWiaSegmentationFilter.DetectRegions
title: IWiaSegmentationFilter::DetectRegions
author: windows-driver-content
description: The IWiaSegmentationFilter::DetectRegions method determines the subregions of an image laid out on the flatbed platen so that each subregion can be acquired into a separate image item.
old-location: image\iwiasegmentationfilter_detectregions.htm
old-project: image
ms.assetid: 53ad769e-38b5-463d-9fa0-053c2215cc81
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWiaSegmentationFilter, DetectRegions, IWiaSegmentationFilter::DetectRegions
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wia_lh.h
req.include-header: Wia.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaSegmentationFilter.DetectRegions
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
req.iface: IWiaSegmentationFilter
req.product: Windows 10 or later.
---

# IWiaSegmentationFilter::DetectRegions method



## -description
<p>The <b>IWiaSegmentationFilter::DetectRegions</b> method determines the subregions of an image laid out on the flatbed platen so that each subregion can be acquired into a separate image item.</p>


## -syntax

````
HRESULT DetectRegions(
  [in]           LONG      lFlags,
  [in, optional] IStream   *pInputStream ,
  [in, optional] IWiaItem2 *pWiaItem2
);
````


## -parameters
<dl>

### -param lFlags [in]

<dd>
<p>Currently unused. Should be set to zero. </p>
</dd>

### -param pInputStream  [in, optional]

<dd>
<p>Specifies a pointer to the <b>IStream</b> preview image.</p>
</dd>

### -param pWiaItem2 [in, optional]

<dd>
<p>Specifies a pointer to the <b>IWiaItem2</b> item for which <i>pInputStream</i> was acquired. The segmentation filter creates child items for this item. </p>
</dd>
</dl>

## -returns
<p>Returns S_OK if successful, or a standard COM error value otherwise. </p>

## -remarks
<p>This method determines the subregions of the image represented by <i>pInputStream</i>. For each subregion that it detects, it creates a child item for the <b>IWiaItem2</b> item pointed to by the <i>pWiaItem2</i> parameter. For each child item, the segmentation filter must set values for the bounding rectangle of the area to scan, using the following WIA scanner item properties: </p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552663">WIA_IPS_XPOS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552671">WIA_IPS_YPOS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552661">WIA_IPS_XEXTENT</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552669">WIA_IPS_YEXTENT</a>
</p>

<p>A more advanced filter might also require other scanner item properties, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff552581">WIA_IPS_DESKEW_X</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff552587">WIA_IPS_DESKEW_Y</a>, if the driver supports deskewing. </p>

<p>If an application calls <b>IWiaSegmentationFilter::DetectRegions</b> more than once, the application must first delete the child items created by the last call to the <b>IWiaSegmentationFilter::DetectRegions </b>method. </p>

<p>If an application changes any properties into <i>pWiaItem2</i>, between acquiring the image into <i>pInputStream</i> and its call to <b>IWiaSegmentationFilter::DetectRegions</b>, the original property settings (the property settings the item had when the stream was acquired) must be restored. This can be done using <b>IWiaPropertyStorage::GetPropertyStream</b> and <b>IWiaPropertyStorage::SetPropertyStream.</b></p>

<p>The application must reset the <b>IStream </b>preview if its call passes the same stream into the segmentation filter more than once. The application must also reset the stream after the initial download and before calling <b>IWiaSegmentationFilter::DetectRegions</b>.</p>

<p>The <b>IStream,IWiaItem2</b> and <b>IWiaPropertyStorage </b>interfaces are described in the Microsoft Windows SDK documentation.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wia_lh.h (include Wia.h)</dt>
</dl>
</td>
</tr>
</table>