---
UID: NE.d3d10umddi.D3D10_DDI_TEXTURE_ADDRESS_MODE
title: D3D10_DDI_TEXTURE_ADDRESS_MODE
author: windows-driver-content
description: The D3D10_DDI_TEXTURE_ADDRESS_MODE enumeration type contains values that identify the texture address mode of a sampler.
old-location: display\d3d10_ddi_texture_address_mode.htm
old-project: display
ms.assetid: 96bbba03-97c1-43f2-bf3e-902de77d5eb9
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
req.alt-api: D3D10_DDI_TEXTURE_ADDRESS_MODE
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

# D3D10_DDI_TEXTURE_ADDRESS_MODE enumeration



## -description
<p>The D3D10_DDI_TEXTURE_ADDRESS_MODE enumeration type contains values that identify the texture address mode of a sampler.</p>


## -syntax

````
typedef enum D3D10_DDI_TEXTURE_ADDRESS_MODE { 
  D3D10_DDI_TEXTURE_ADDRESS_WRAP        = 1,
  D3D10_DDI_TEXTURE_ADDRESS_MIRROR      = 2,
  D3D10_DDI_TEXTURE_ADDRESS_CLAMP       = 3,
  D3D10_DDI_TEXTURE_ADDRESS_BORDER      = 4,
  D3D10_DDI_TEXTURE_ADDRESS_MIRRORONCE  = 5
} D3D10_DDI_TEXTURE_ADDRESS_MODE;
````


## -enum-fields
<dl>

### -field <a id="D3D10_DDI_TEXTURE_ADDRESS_WRAP"></a><a id="d3d10_ddi_texture_address_wrap"></a><b>D3D10_DDI_TEXTURE_ADDRESS_WRAP</b>

<dd>
<p>Tile the texture at every integer junction. For example, for u values between 0 and 3, the texture is repeated three times; no mirroring is performed.</p>
</dd>

### -field <a id="D3D10_DDI_TEXTURE_ADDRESS_MIRROR"></a><a id="d3d10_ddi_texture_address_mirror"></a><b>D3D10_DDI_TEXTURE_ADDRESS_MIRROR</b>

<dd>
<p>Similar to D3D10_DDI_TEXTURE_ADDRESS_WRAP, except that the texture is flipped at every integer junction. For u values between 0 and 1, for example, the texture is addressed normally; between 1 and 2, the texture is flipped (mirrored); and between 2 and 3, the texture is normal again, and so on.</p>
</dd>

### -field <a id="D3D10_DDI_TEXTURE_ADDRESS_CLAMP"></a><a id="d3d10_ddi_texture_address_clamp"></a><b>D3D10_DDI_TEXTURE_ADDRESS_CLAMP</b>

<dd>
<p>Texture coordinates outside the range [0.0, 1.0] are set to the texture color at 0.0 or 1.0, respectively.</p>
</dd>

### -field <a id="D3D10_DDI_TEXTURE_ADDRESS_BORDER"></a><a id="d3d10_ddi_texture_address_border"></a><b>D3D10_DDI_TEXTURE_ADDRESS_BORDER</b>

<dd>
<p>Texture coordinates outside the range [0.0, 1.0] are set to the border color.</p>
</dd>

### -field <a id="D3D10_DDI_TEXTURE_ADDRESS_MIRRORONCE"></a><a id="d3d10_ddi_texture_address_mirroronce"></a><b>D3D10_DDI_TEXTURE_ADDRESS_MIRRORONCE</b>

<dd>
<p>Similar to D3D10_DDI_TEXTURE_ADDRESS_MIRROR and D3D10_DDI_TEXTURE_ADDRESS_CLAMP. Takes the absolute value of the texture coordinate (thus, mirroring around 0), and then clamps to the maximum value. The most common usage of D3D10_DDI_TEXTURE_ADDRESS_MIRRORONCE is for volume textures, where support for the full D3D10_DDI_TEXTURE_ADDRESS_MIRRORONCE texture-addressing mode is not necessary, but the data is symmetric around the one axis.</p>
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
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10-ddi-sampler-desc.md">D3D10_DDI_SAMPLER_DESC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_DDI_TEXTURE_ADDRESS_MODE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
