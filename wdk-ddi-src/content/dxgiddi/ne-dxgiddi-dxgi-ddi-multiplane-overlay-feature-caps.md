---
UID: NE.dxgiddi.DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS
title: DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS
author: windows-driver-content
description: Identifies overlay capabilities.
old-location: display\dxgi_ddi_multiplane_overlay_feature_caps.htm
ms.assetid: f64b3470-b4ae-4d3a-87ac-249429f17dfe
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS
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
ms.keywords: DxApiGetVersion
req.iface: 
---

# DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS enumeration



## -description
<p>Identifies overlay capabilities.</p>


## -syntax

````
typedef enum DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS { 
  DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_ROTATION         = 0x1,
  DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_VERTICAL_FLIP    = 0x2,
  DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HORIZONTAL_FLIP  = 0x4,
  DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_DEINTERLACE      = 0x8,
  DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_STEREO           = 0x10
} DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS;
````


## -enum-fields
<dl>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_ROTATION"></a><a id="dxgi_ddi_multiplane_overlay_feature_caps_rotation"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_ROTATION</b>

<dd>
<p>The overlay plane can rotate the data 90, 180, and 270 degrees.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_VERTICAL_FLIP"></a><a id="dxgi_ddi_multiplane_overlay_feature_caps_vertical_flip"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_VERTICAL_FLIP</b>

<dd>
<p>The overlay plane can flip the data vertically, making it appear upside-down.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HORIZONTAL_FLIP"></a><a id="dxgi_ddi_multiplane_overlay_feature_caps_horizontal_flip"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HORIZONTAL_FLIP</b>

<dd>
<p>The overlay plane can flip the data horizontally, making it appear as a right-to-left mirror image.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_DEINTERLACE"></a><a id="dxgi_ddi_multiplane_overlay_feature_caps_deinterlace"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_DEINTERLACE</b>

<dd>
<p>Reserved for system use. The user-mode display driver should not use this value.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_STEREO"></a><a id="dxgi_ddi_multiplane_overlay_feature_caps_stereo"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_STEREO</b>

<dd>
<p>Reserved for system use. The user-mode display driver should not use this value.</p>
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
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>