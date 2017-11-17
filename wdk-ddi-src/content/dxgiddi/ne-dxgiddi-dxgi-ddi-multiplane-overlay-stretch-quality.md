---
UID: NE.dxgiddi.DXGI_DDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY
title: DXGI_DDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY
author: windows-driver-content
description: Identifies filtering processes that the hardware should perform when it stretches or shrinks multiplane overlay data.
old-location: display\dxgi_ddi_multiplane_overlay_stretch_quality.htm
ms.assetid: 550C09F4-8684-4B6F-BB62-8514721A9B32
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
req.alt-api: DXGI_DDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY
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

# DXGI_DDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY enumeration



## -description
<p>Identifies filtering processes that the hardware should perform when it stretches or shrinks multiplane overlay data.</p>


## -syntax

````
typedef enum DXGI_DDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY { 
  DXGI_DDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY_BILINEAR  = 0x1,
  DXGI_DDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY_HIGH      = 0x2
} DXGI_DDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY;
````


## -enum-fields
<dl>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY_BILINEAR"></a><a id="dxgi_ddi_multiplane_overlay_stretch_quality_bilinear"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY_BILINEAR</b>

<dd>
<p>When the hardware stretches or shrinks the data, it should perform bilinear filtering. If the hardware lacks enough resources to perform bilinear shrinking, the user-mode display driver can use point sampling.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY_HIGH"></a><a id="dxgi_ddi_multiplane_overlay_stretch_quality_high"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY_HIGH</b>

<dd>
<p>When the hardware stretches or shrinks the data, it should perform the highest quality filtering that it supports.</p>
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