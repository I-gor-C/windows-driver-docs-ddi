---
UID: NS.d3dkmddi._DXGK_GDIARG_STRETCHBLT
title: DXGK_GDIARG_STRETCHBLT
author: windows-driver-content
description: The DXGK_GDIARG_STRETCHBLT structure describes the characteristics of a GDI hardware-accelerated stretch bit-block transfer (bitblt) operation.
old-location: display\dxgk_gdiarg_stretchblt.htm
old-project: display
ms.assetid: 11988e4c-9f4b-44cc-bc09-ff6da62f3904
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_GDIARG_STRETCHBLT, DXGK_GDIARG_STRETCHBLT
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
req.alt-api: DXGK_GDIARG_STRETCHBLT
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

# DXGK_GDIARG_STRETCHBLT structure



## -description
<p>The DXGK_GDIARG_STRETCHBLT structure describes the characteristics of a GDI hardware-accelerated stretch <a href="wdkgloss.b#wdkgloss.bit_block_transfer#wdkgloss.bit_block_transfer"><i>bit-block transfer (bitblt)</i></a> operation.</p>


## -syntax

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


## -struct-fields
<dl>

### -field <b>SrcRect</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure that defines the rectangular area to be copied. This rectangle is specified in the coordinate system of the source surface and is defined by two points: upper left and lower right. The two points that define the rectangle are always well ordered. </p>
<p>The source rectangle will never exceed the bounds of the source surface, so it will never overhang the source surface. </p>
<p>This rectangle is mapped to the destination rectangle defined by <b>DstRect</b>. </p>
<p>For more information, see the Remarks section.</p>
</dd>

### -field <b>DstRect</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure that defines the rectangular area to be modified. This rectangle is specified in the coordinate system of the destination surface and is defined by two points: upper left and lower right. The rectangle is lower-right exclusive; that is, its lower and right edges are not a part of the bit-block transfer. The two points that define the rectangle are always well ordered. </p>
<p>The destination rectangle defined by <b>DstRect</b> can exceed the bounds of the destination surface, but sub-rectangles cannot. Additionally, all sub-rectangles are guaranteed to fit inside the destination surface. Sub-rectangles can be constrained further by a bounding rectangle that is smaller than the destination rectangle. </p>
<p>For more information, see the Remarks section.</p>
</dd>

### -field <b>DstAllocationIndex</b>

<dd>
<p>
      [in] An index of the element in the allocation list that specifies the allocation that is referenced by the <b>DstRect</b> destination rectangle.
     </p>
</dd>

### -field <b>SrcAllocationIndex</b>

<dd>
<p>
      [in] An index of the element in the allocation list that specifies the allocation that is referenced by the SrcRect source rectangle.
     </p>
</dd>

### -field <b>NumSubRects</b>

<dd>
<p>
      The number of sub-rectangles in the destination surface space that is bounded by the <b>DstRect</b> destination rectangle.
     </p>
</dd>

### -field <b>pSubRects</b>

<dd>
<p>
      [in] A pointer to the sub-rectangles in the destination surface space that is bounded by the <b>DstRect</b> destination rectangle.
     </p>
</dd>

### -field <b>Mode</b>

<dd>
<p>
        [in] Specifies how source pixels are combined to produce output pixels based on whether the following values that are defined in <i>Wingdi.h</i> are set:
		  
        
       </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="BLACKONWHITE"></a><a id="blackonwhite"></a><dl>

### -field <b>BLACKONWHITE</b>

</dl>
</td>
<td width="60%">
<p>On a shrinking bit-block transfer, pixels should be combined with a Boolean <b>AND</b> operation. On a stretching bit-block transfer, pixels should be replicated.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="WHITEONBLACK"></a><a id="whiteonblack"></a><dl>

### -field <b>WHITEONBLACK</b>

</dl>
</td>
<td width="60%">
<p>On a shrinking bit-block transfer, pixels should be combined with a Boolean <b>OR</b> operation. On a stretching bit-block transfer, pixels should be replicated.</p>
</td>
</tr>
</table>
<p> </p>
<p>
        This type of operation will be processed only if the driver has set the <b>SupportMonoStretchBltModes</b> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562004">DXGK_PRESENTATIONCAPS</a> structure.</p>
</dd>

### -field <b>MirrorX</b>

<dd>
<p>
        [in] Specifies whether the stretch bit-block transfer will be performed in mirror mode in the xdirection. This type of operation will be processed only if the value of <b>MirrorX</b> is nonzero and the driver has set the <b>SupportMirrorStretchBlt</b> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562004">DXGK_PRESENTATIONCAPS</a> structure.
       </p>
</dd>

### -field <b>MirrorY</b>

<dd>
<p>
        [in] Specifies whether the stretch bit-block transfer will be performed in mirror mode in the y direction. This type of operation will be processed only if the value of <b>MirrorY</b> is nonzero and the driver has set the <b>SupportMirrorStretchBlt</b> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562004">DXGK_PRESENTATIONCAPS</a> structure.
       </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>
       [in] Optional UINT value that can be used to debug driver code.
      </p>
</dd>

### -field <b>SrcPitch</b>

<dd>
<p>
      [in] The pitch of the source surface, in bytes.
     </p>
</dd>
</dl>

## -remarks
<p>The x and y stretch ratios are computed respectively as the ratios of the x and y sizes of the <b>DstRect</b> and <b>SrcRect</b> members.</p>

<p>The HALFTONE mode and STRETCH_HALFTONE modes that are defined in <i>Wingdi.h</i> will never be set in the <b>Mode</b> member. The COLORONCOLOR mode can be set in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561074">DXGK_GDIARG_ALPHABLEND</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff561091">DXGK_GDIARG_TRANSPARENTBLT</a> structures.</p>

<p>When sub-rectangles are transformed to the source surface space, the result is guaranteed to be within the source surface. The transformation of a sub-rectangle's coordinates in the destination surface to coordinates  in the source surface is defined by the following formulas, where</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561074">DXGK_GDIARG_ALPHABLEND</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561091">DXGK_GDIARG_TRANSPARENTBLT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562004">DXGK_PRESENTATIONCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_GDIARG_STRETCHBLT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
