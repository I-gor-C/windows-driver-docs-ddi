---
UID: NE.dxgiddi.DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS
title: DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS
author: windows-driver-content
description: Identifies YUV range and conversion info that describes a multiplane overlay.
old-location: display\dxgi_ddi_multiplane_overlay_ycbcr_flags.htm
old-project: display
ms.assetid: fa915ec0-167f-441c-b2de-0ae2b852c432
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS, DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS
req.alt-loc: Dxgiddi.h
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
---

# DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS enumeration



## -description
Identifies YUV range and conversion info that describes a multiplane overlay.



## -syntax

````
typedef enum DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS { 
  DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE  = 0x1,
  DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709          = 0x2,
  DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC          = 0x4
} DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS;
````


## -enum-fields

### -field DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE

YUV values range from 16 to 235, inclusive, instead of the default range of 0 to 255, inclusive.


### -field DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709

YUV values should be converted using the BT.709 standard, instead of the default BT.601 conversion.


### -field DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC

YUV values contain xvYCC data, instead of conventional YCbCr data.


## -remarks
For more info on how YUV ranges are defined and converted, see <a href="display.yuv_format_ranges">YUV format ranges in Windows 8.1</a>.


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 8.1

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2012 R2

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>