---
UID: NE.d3dkmddi._DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY
title: DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY
author: windows-driver-content
description: Identifies filtering processes that the hardware should perform when it stretches or shrinks multiplane overlay data.
old-location: display\dxgk_multiplane_overlay_stretch_quality.htm
old-project: display
ms.assetid: 5C995970-59E4-46AD-84CD-0B5675949308
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY
req.alt-loc: D3dkmddi.h
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

# DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY enumeration



## -description
<p>Identifies filtering processes that the hardware should perform when it stretches or shrinks multiplane overlay data.</p>


## -syntax

````
typedef enum _DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY { 
  DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY_BILINEAR  = 0x1,
  DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY_HIGH      = 0x2
} DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY;
````


## -enum-fields
<dl>

### -field DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY_BILINEAR

<dd>
<p>When the hardware stretches or shrinks the data, it should perform bilinear filtering. If the hardware lacks enough resources to perform bilinear shrinking, the user-mode display driver can use point sampling.</p>
</dd>

### -field DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY_HIGH

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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>