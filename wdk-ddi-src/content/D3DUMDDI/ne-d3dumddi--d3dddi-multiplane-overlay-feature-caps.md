---
UID: NE.d3dumddi._D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS
title: D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS
author: windows-driver-content
description: Identifies overlay capabilities.
old-location: display\d3dddi_multiplane_overlay_feature_caps.htm
ms.assetid: 51e44c1c-ca56-4fe3-a27b-d0957df203cf
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS
req.alt-loc: D3dumddi.h
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS enumeration



## -description
<p>Identifies overlay capabilities.</p>


## -syntax

````
typedef enum _D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS { 
  D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_ROTATION         = 0x1,
  D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_VERTICAL_FLIP    = 0x2,
  D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HORIZONTAL_FLIP  = 0x4,
  D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_DEINTERLACE      = 0x8,
  D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_RGB              = 0x10,
  D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_YUV              = 0x20,
  D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_BILINEAR_FILTER  = 0x40,
  D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HIGH_FILTER      = 0x100
} D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS;
````


## -enum-fields
<dl>

### -field <a id="D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_ROTATION"></a><a id="d3dddi_multiplane_overlay_feature_caps_rotation"></a><b>D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_ROTATION</b>

<dd>
<p>The overlay plane can rotate the data 90, 180, and 270 degrees.</p>
</dd>

### -field <a id="D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_VERTICAL_FLIP"></a><a id="d3dddi_multiplane_overlay_feature_caps_vertical_flip"></a><b>D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_VERTICAL_FLIP</b>

<dd>
<p>The overlay plane can flip the data vertically, making it appear upside-down.</p>
</dd>

### -field <a id="D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HORIZONTAL_FLIP"></a><a id="d3dddi_multiplane_overlay_feature_caps_horizontal_flip"></a><b>D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HORIZONTAL_FLIP</b>

<dd>
<p>The overlay plane can flip the data horizontally, making it appear as a right-to-left mirror image.</p>
</dd>

### -field <a id="D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_DEINTERLACE"></a><a id="d3dddi_multiplane_overlay_feature_caps_deinterlace"></a><b>D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_DEINTERLACE</b>

<dd>
<p>Reserved for system use. The user-mode display driver should not use this value.</p>
</dd>

### -field <a id="D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_RGB"></a><a id="d3dddi_multiplane_overlay_feature_caps_rgb"></a><b>D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_RGB</b>

<dd>
<p>The overlay plane supports RGB format.</p>
</dd>

### -field <a id="D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_YUV"></a><a id="d3dddi_multiplane_overlay_feature_caps_yuv"></a><b>D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_YUV</b>

<dd>
<p>The overlay plane supports YUV format.</p>
</dd>

### -field <a id="D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_BILINEAR_FILTER"></a><a id="d3dddi_multiplane_overlay_feature_caps_bilinear_filter"></a><b>D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_BILINEAR_FILTER</b>

<dd>
<p>The overlay plane supports stretching and shrinking using bilinear filtering.</p>
</dd>

### -field <a id="D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HIGH_FILTER"></a><a id="d3dddi_multiplane_overlay_feature_caps_high_filter"></a><b>D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HIGH_FILTER</b>

<dd>
<p>The overlay plane supports stretching and shrinking using filtering that is better than bilinear filtering.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>