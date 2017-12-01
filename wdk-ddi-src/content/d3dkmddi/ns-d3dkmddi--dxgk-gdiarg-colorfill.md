---
UID: NS.d3dkmddi._DXGK_GDIARG_COLORFILL
title: DXGK_GDIARG_COLORFILL
author: windows-driver-content
description: The DXGK_GDIARG_COLORFILL structure describes the characteristics of a GDI hardware-accelerated color fill operation.
old-location: display\dxgk_gdiarg_colorfill.htm
old-project: display
ms.assetid: f7dad933-31e6-4de2-9753-67c054f44c4a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_GDIARG_COLORFILL, DXGK_GDIARG_COLORFILL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_GDIARG_COLORFILL
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGK_GDIARG_COLORFILL structure



## -description
<p>The DXGK_GDIARG_COLORFILL structure describes the characteristics of a GDI hardware-accelerated color fill operation.</p>


## -syntax

````
typedef struct _DXGK_GDIARG_COLORFILL {
  RECT DstRect;
  UINT DstAllocationIndex;
  UINT NumSubRects;
  RECT *pSubRects;
  UINT Color;
  WORD Rop;
  WORD Rop3;
} DXGK_GDIARG_COLORFILL;
````


## -struct-fields
<dl>

### -field <b>DstRect</b>

<dd>
<p>[in] A <a href="display.rect">RECT</a> structure that defines the rectangular area to be modified. This rectangle is specified in the coordinate system of the destination surface and is defined by two points: upper left and lower right. The rectangle is lower-right exclusive; that is, its lower and right edges are not a part of the bit-block transfer. The two points that define the rectangle are always well ordered. </p>
<p>The destination rectangle defined by <b>DstRect</b> can exceed the bounds of the destination surface, but sub-rectangles cannot. Additionally, all sub-rectangles are guaranteed to fit inside the destination surface. Sub-rectangles can be constrained further by a bounding rectangle that is smaller than the destination rectangle.</p>
</dd>

### -field <b>DstAllocationIndex</b>

<dd>
<p>
      [in] An index of the element in the allocation list that specifies the allocation that is referenced by the <b>DstRect</b> destination rectangle.
     </p>
</dd>

### -field <b>NumSubRects</b>

<dd>
<p>
      [in] The number of sub-rectangles in the destination surface space. The sub-rectangles are not tightly bounded by the <b>DstRect</b> destination rectangle.
     </p>
</dd>

### -field <b>pSubRects</b>

<dd>
<p>
      [in] A pointer to the sub-rectangles in the destination surface space that is bounded by the <b>DstRect</b> destination rectangle.
     </p>
</dd>

### -field <b>Color</b>

<dd>
<p>
      [in] The fill color, in 32-bit ARGB unsigned pixel format (as defined by the D3DDDIFMT_A8R8G8B8 value of the <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a> enumeration).
     </p>
</dd>

### -field <b>Rop</b>

<dd>
<p>
      [in] An 8-bit value that specifies a GDI raster operation (ROP) that is defined by the constant values of the <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-gdirop-colorfill.md">DXGK_GDIROP_COLORFILL</a> enumeration.
     </p>
</dd>

### -field <b>Rop3</b>

<dd>
<p>
      [in] An 8-bit value that specifies a ternary GDI raster operation (ROP3) that combines a brush, a source bitmap, and a destination bitmap in one of 256 possible combinations. This type of raster operation will be processed only if the driver has set the <b>SupportAllBltRops</b> member in the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-presentationcaps.md">DXGK_PRESENTATIONCAPS</a> structure.
     </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="..\d3dkmddi\ne-d3dkmddi--dxgk-gdirop-colorfill.md">DXGK_GDIROP_COLORFILL</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-presentationcaps.md">DXGK_PRESENTATIONCAPS</a>
</dt>
<dt>
<a href="display.rect">RECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_GDIARG_COLORFILL structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
