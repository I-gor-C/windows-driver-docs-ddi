---
UID: NS:d3dkmddi._DXGK_GDIARG_STRETCHBLT
title: "_DXGK_GDIARG_STRETCHBLT"
author: windows-driver-content
description: The DXGK_GDIARG_STRETCHBLT structure describes the characteristics of a GDI hardware-accelerated stretch bit-block transfer (bitblt) operation.
old-location: display\dxgk_gdiarg_stretchblt.htm
old-project: display
ms.assetid: 11988e4c-9f4b-44cc-bc09-ff6da62f3904
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: BLACKONWHITE, DXGK_GDIARG_STRETCHBLT, DXGK_GDIARG_STRETCHBLT structure [Display Devices], DmStructs_9c8014aa-fdad-474d-a1a1-182020850e17.xml, WHITEONBLACK, _DXGK_GDIARG_STRETCHBLT, d3dkmddi/DXGK_GDIARG_STRETCHBLT, display.dxgk_gdiarg_stretchblt
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_GDIARG_STRETCHBLT
product: Windows
targetos: Windows
req.typenames: DXGK_GDIARG_STRETCHBLT
---

# _DXGK_GDIARG_STRETCHBLT structure
The DXGK_GDIARG_STRETCHBLT structure describes the characteristics of a GDI hardware-accelerated stretch <a href="https://msdn.microsoft.com/bf5fa319-14ec-40df-be7a-89c07ce519ad">bit-block transfer (bitblt)</a> operation.

## Syntax
````
typedef struct _DXGK_GDIARG_STRETCHBLT {
  RECT  SrcRect;
  RECT  DstRect;
  UINT  DstAllocationIndex;
  UINT  SrcAllocationIndex;
  UINT  NumSubRects;
  RECT  *pSubRects;
  union {
    struct {
      UINT Mode  :16;
      UINT MirrorX  :1;
      UINT MirrorY  :1;
    };
    UINT   Flags;
  };
  UINT  SrcPitch;
} DXGK_GDIARG_STRETCHBLT;
````

## Members


`DstAllocationIndex`

[in] An index of the element in the allocation list that specifies the allocation that is referenced by the <b>DstRect</b> destination rectangle.

`DstRect`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure that defines the rectangular area to be modified. This rectangle is specified in the coordinate system of the destination surface and is defined by two points: upper left and lower right. The rectangle is lower-right exclusive; that is, its lower and right edges are not a part of the bit-block transfer. The two points that define the rectangle are always well ordered. 

The destination rectangle defined by <b>DstRect</b> can exceed the bounds of the destination surface, but sub-rectangles cannot. Additionally, all sub-rectangles are guaranteed to fit inside the destination surface. Sub-rectangles can be constrained further by a bounding rectangle that is smaller than the destination rectangle. 

For more information, see the Remarks section.

`NumSubRects`

The number of sub-rectangles in the destination surface space that is bounded by the <b>DstRect</b> destination rectangle.

`pSubRects`

[in] A pointer to the sub-rectangles in the destination surface space that is bounded by the <b>DstRect</b> destination rectangle.

`SrcAllocationIndex`

[in] An index of the element in the allocation list that specifies the allocation that is referenced by the SrcRect source rectangle.

`SrcPitch`

[in] The pitch of the source surface, in bytes.

`SrcRect`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure that defines the rectangular area to be copied. This rectangle is specified in the coordinate system of the source surface and is defined by two points: upper left and lower right. The two points that define the rectangle are always well ordered. 

The source rectangle will never exceed the bounds of the source surface, so it will never overhang the source surface. 

This rectangle is mapped to the destination rectangle defined by <b>DstRect</b>. 

For more information, see the Remarks section.

## Remarks
The x and y stretch ratios are computed respectively as the ratios of the x and y sizes of the <b>DstRect</b> and <b>SrcRect</b> members.

The HALFTONE mode and STRETCH_HALFTONE modes that are defined in <i>Wingdi.h</i> will never be set in the <b>Mode</b> member. The COLORONCOLOR mode can be set in the <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_gdiarg_alphablend.md">DXGK_GDIARG_ALPHABLEND</a> and <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_gdiarg_transparentblt.md">DXGK_GDIARG_TRANSPARENTBLT</a> structures.

When sub-rectangles are transformed to the source surface space, the result is guaranteed to be within the source surface. The transformation of a sub-rectangle's coordinates in the destination surface to coordinates  in the source surface is defined by the following formulas, where

<ul>
<li>(Xd, Yd) is a point inside the sub-rectangle</li>
<li>(Xs, Ys) is a point inside the source rectangle</li>
</ul>
<pre class="syntax" xml:space="preserve"><code>float Ws = SrcRect.right â€“ SrcRect.left;
float Wd = DstRect.right â€“ DstRect.left;
int Xs = round((Xd â€“ DstRect.left + 0.5) * Ws/Wd + SrcRect.left â€“ 0.5)
OR
int Xs = truncate((Xd â€“ DstRect.left + 0.5) * Ws/Wd + SrcRect.left)

float Hs = SrcRect.bottom â€“ SrcRect.top;
float Hd = DstRect.bottom â€“ DstRect.top;
int Ys = round((Yd â€“ DstRect.top + 0.5) * Hs/Hd + SrcRect.top â€“ 0.5)
OR
int Ys = truncate((Yd â€“ DstRect.top + 0.5) * Hs/Hd + SrcRect.top)</code></pre>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of the Windows operating systems. Available in Windows 7 and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_gdiarg_transparentblt.md">DXGK_GDIARG_TRANSPARENTBLT</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_gdiarg_alphablend.md">DXGK_GDIARG_ALPHABLEND</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_presentationcaps.md">DXGK_PRESENTATIONCAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_GDIARG_STRETCHBLT structure%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>