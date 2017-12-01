---
UID: NE.d3d10umddi.D3D10_DDI_BLEND
title: D3D10_DDI_BLEND
author: windows-driver-content
description: The D3D10_DDI_BLEND enumeration type contains values that identify blend modes in a call to the driver's CreateBlendState function.
old-location: display\d3d10_ddi_blend.htm
old-project: display
ms.assetid: 719cd6b3-4f48-4b26-95fe-6f5faac56c06
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10_DDI_BLEND
req.alt-loc: d3d10umddi.h
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
req.iface: 
---

# D3D10_DDI_BLEND enumeration



## -description
<p>The D3D10_DDI_BLEND enumeration type contains values that identify blend modes in a call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createblendstate.md">CreateBlendState</a> function.</p>


## -syntax

````
typedef enum D3D10_DDI_BLEND { 
  D3D10_DDI_BLEND_ZERO             = 1,
  D3D10_DDI_BLEND_ONE              = 2,
  D3D10_DDI_BLEND_SRC_COLOR        = 3,
  D3D10_DDI_BLEND_INV_SRC_COLOR    = 4,
  D3D10_DDI_BLEND_SRC_ALPHA        = 5,
  D3D10_DDI_BLEND_INV_SRC_ALPHA    = 6,
  D3D10_DDI_BLEND_DEST_ALPHA       = 7,
  D3D10_DDI_BLEND_INV_DEST_ALPHA   = 8,
  D3D10_DDI_BLEND_DEST_COLOR       = 9,
  D3D10_DDI_BLEND_INV_DEST_COLOR   = 10,
  D3D10_DDI_BLEND_SRC_ALPHASAT     = 11,
  D3D10_DDI_BLEND_BLEND_FACTOR     = 14,
  D3D10_DDI_BLEND_INVBLEND_FACTOR  = 15,
  D3D10_DDI_BLEND_SRC1_COLOR       = 16,
  D3D10_DDI_BLEND_INV_SRC1_COLOR   = 17,
  D3D10_DDI_BLEND_SRC1_ALPHA       = 18,
  D3D10_DDI_BLEND_INV_SRC1_ALPHA   = 19
} D3D10_DDI_BLEND;
````


## -enum-fields
<dl>

### -field <a id="D3D10_DDI_BLEND_ZERO"></a><a id="d3d10_ddi_blend_zero"></a><b>D3D10_DDI_BLEND_ZERO</b>

<dd>
<p>Blend factor is (0, 0, 0, 0).</p>
</dd>

### -field <a id="D3D10_DDI_BLEND_ONE"></a><a id="d3d10_ddi_blend_one"></a><b>D3D10_DDI_BLEND_ONE</b>

<dd>
<p>Blend factor is (1, 1, 1, 1).</p>
</dd>

### -field <a id="D3D10_DDI_BLEND_SRC_COLOR"></a><a id="d3d10_ddi_blend_src_color"></a><b>D3D10_DDI_BLEND_SRC_COLOR</b>

<dd>
<p>Blend factor is (Rₛ,Gₛ,Bₛ,Aₛ).</p>
</dd>

### -field <a id="D3D10_DDI_BLEND_INV_SRC_COLOR"></a><a id="d3d10_ddi_blend_inv_src_color"></a><b>D3D10_DDI_BLEND_INV_SRC_COLOR</b>

<dd>
<p>Blend factor is (1 - Rₛ, 1 - Gₛ, 1 - Bₛ, 1 - Aₛ). </p>
</dd>

### -field <a id="D3D10_DDI_BLEND_SRC_ALPHA"></a><a id="d3d10_ddi_blend_src_alpha"></a><b>D3D10_DDI_BLEND_SRC_ALPHA</b>

<dd>
<p>Blend factor is (Aₛ, Aₛ, Aₛ, Aₛ). </p>
</dd>

### -field <a id="D3D10_DDI_BLEND_INV_SRC_ALPHA"></a><a id="d3d10_ddi_blend_inv_src_alpha"></a><b>D3D10_DDI_BLEND_INV_SRC_ALPHA</b>

<dd>
<p>Blend factor is ( 1 - Aₛ, 1 - Aₛ, 1 - Aₛ, 1 - Aₛ). </p>
</dd>

### -field <a id="D3D10_DDI_BLEND_DEST_ALPHA"></a><a id="d3d10_ddi_blend_dest_alpha"></a><b>D3D10_DDI_BLEND_DEST_ALPHA</b>

<dd>
<p>
      Blend factor is (A<sub>d</sub>, A<sub>d</sub>, A<sub>d</sub>, A<sub>d</sub>) of the current render target that is being blended. 
     </p>
</dd>

### -field <a id="D3D10_DDI_BLEND_INV_DEST_ALPHA"></a><a id="d3d10_ddi_blend_inv_dest_alpha"></a><b>D3D10_DDI_BLEND_INV_DEST_ALPHA</b>

<dd>
<p>Blend factor is (1 - A<sub>d</sub>, 1 - A<sub>d</sub>, 1 - A<sub>d</sub>, 1 - A<sub>d</sub>) of the current render target that is being blended. </p>
</dd>

### -field <a id="D3D10_DDI_BLEND_DEST_COLOR"></a><a id="d3d10_ddi_blend_dest_color"></a><b>D3D10_DDI_BLEND_DEST_COLOR</b>

<dd>
<p>Blend factor is (R<sub>d</sub>, G<sub>d</sub>, B<sub>d</sub>, A<sub>d</sub>) of the current render target that is being blended. </p>
</dd>

### -field <a id="D3D10_DDI_BLEND_INV_DEST_COLOR"></a><a id="d3d10_ddi_blend_inv_dest_color"></a><b>D3D10_DDI_BLEND_INV_DEST_COLOR</b>

<dd>
<p>Blend factor is (1 - R<sub>d</sub>, 1 - G<sub>d</sub>, 1 - B<sub>d</sub>, 1 - A<sub>d</sub>) of the current render target that is being blended.</p>
</dd>

### -field <a id="D3D10_DDI_BLEND_SRC_ALPHASAT"></a><a id="d3d10_ddi_blend_src_alphasat"></a><b>D3D10_DDI_BLEND_SRC_ALPHASAT</b>

<dd>
<p>Blend factor is (f, f, f, 1); f = min(A, 1 - A<sub>d</sub>). </p>
</dd>

### -field <a id="D3D10_DDI_BLEND_BLEND_FACTOR"></a><a id="d3d10_ddi_blend_blend_factor"></a><b>D3D10_DDI_BLEND_BLEND_FACTOR</b>

<dd>
<p>
      Constant color-blending factor that the frame-buffer blender uses.
     </p>
</dd>

### -field <a id="D3D10_DDI_BLEND_INVBLEND_FACTOR"></a><a id="d3d10_ddi_blend_invblend_factor"></a><b>D3D10_DDI_BLEND_INVBLEND_FACTOR</b>

<dd>
<p>Inverted constant color-blending factor that the frame-buffer blender uses.</p>
</dd>

### -field <a id="D3D10_DDI_BLEND_SRC1_COLOR"></a><a id="d3d10_ddi_blend_src1_color"></a><b>D3D10_DDI_BLEND_SRC1_COLOR</b>

<dd>
<p>Blend factor is the red, green, and blue (RGB) components of a pixel shader output register (PS output o1.rgb). </p>
</dd>

### -field <a id="D3D10_DDI_BLEND_INV_SRC1_COLOR"></a><a id="d3d10_ddi_blend_inv_src1_color"></a><b>D3D10_DDI_BLEND_INV_SRC1_COLOR</b>

<dd>
<p>Blend factor is the inversion of the RGB components of a pixel shader output register (1.0f - PS output o1.rgb). </p>
</dd>

### -field <a id="D3D10_DDI_BLEND_SRC1_ALPHA"></a><a id="d3d10_ddi_blend_src1_alpha"></a><b>D3D10_DDI_BLEND_SRC1_ALPHA</b>

<dd>
<p>Blend factor is the alpha component of a pixel shader output register (PS output o1.a). </p>
</dd>

### -field <a id="D3D10_DDI_BLEND_INV_SRC1_ALPHA"></a><a id="d3d10_ddi_blend_inv_src1_alpha"></a><b>D3D10_DDI_BLEND_INV_SRC1_ALPHA</b>

<dd>
<p>Blend factor is the inversion of the alpha component of a pixel shader output register (1.0f - PS output o1.a). </p>
</dd>
</dl>

## -remarks
<p>A <i>blend mode</i> is an algorithm that is used to determine how a texture is blended with the colors of the surface that the texture is applied to. A <i>blend factor</i> is a description of how each color component is blended in texture blending.</p>

## -requirements
<table>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createblendstate.md">CreateBlendState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_DDI_BLEND enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
