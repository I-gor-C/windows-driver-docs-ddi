---
UID: NS.D3DUKMDT._D3DKMDT_3X4_COLORSPACE_TRANSFORM
title: _D3DKMDT_3X4_COLORSPACE_TRANSFORM
author: windows-driver-content
description: Structure to describe the three programmable sub-stages of the 3 by 4 matrix colorspace transform.
old-location: display\D3DKMDT_3X4_COLORSPACE_TRANSFORM.htm
old-project: display
ms.assetid: 7548B626-BEE2-4905-BDCA-14B08DE5DAC8
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _D3DKMDT_3X4_COLORSPACE_TRANSFORM, D3DKMDT_3x4_COLORSPACE_TRANSFORM, *PD3DDDI_3x4_COLORSPACE_TRANSFORM, PD3DDDI_3x4_COLORSPACE_TRANSFORM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_3X4_COLORSPACE_TRANSFORM
req.alt-loc: d3dukmdt.h
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

# _D3DKMDT_3X4_COLORSPACE_TRANSFORM structure



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

Structure to describe the three programmable sub-stages of the 3 by 4 matrix colorspace transform. 



## -syntax

````
typedef struct _D3DDDI_3X4_COLORSPACE_TRANSFORM {
  float           ColorMatrix3x4;
  float           ScalarMultiplier;
  D3DDDI_DXGI_RGB LookupTable1D;
} D3DDDI_3X4_COLORSPACE_TRANSFORM, *PD3DDDI_3X4_COLORSPACE_TRANSFORM;
````


## -struct-fields

### -field ColorMatrix3x4

A 3x3 matrix and 3x1 addition to be applied to each pixel, stored in row-major order. Transforms colors within CIEXYZ.


### -field ScalarMultiplier

A scalar to be multiplied into each element of ColorMatrix3x4.


### -field LookupTable1D

1D look-up table. Transforms colors within the colorspace specified by DXGK_SET_TIMING_PATH_INFO.  


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3dukmdt.h</dt>
</dl>
</td>
</tr>
</table>