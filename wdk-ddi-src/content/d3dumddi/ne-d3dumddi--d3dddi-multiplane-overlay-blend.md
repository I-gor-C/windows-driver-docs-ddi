---
UID: NE.d3dumddi._D3DDDI_MULTIPLANE_OVERLAY_BLEND
title: D3DDDI_MULTIPLANE_OVERLAY_BLEND
author: windows-driver-content
description: Identifies a blend operation to be performed on an overlay plane.
old-location: display\d3dddi_multiplane_overlay_blend.htm
old-project: display
ms.assetid: 1ee411f2-1779-41bd-808c-40639bb22662
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_MULTIPLANE_OVERLAY_BLEND
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
req.iface: 
---

# D3DDDI_MULTIPLANE_OVERLAY_BLEND enumeration



## -description
<p>Identifies a blend operation to be performed on an overlay plane.</p>


## -syntax

````
typedef enum _D3DDDI_MULTIPLANE_OVERLAY_BLEND { 
  D3DDDI_MULTIPLANE_OVERLAY_BLEND_OPAQUE      = 0x0,
  D3DDDI_MULTIPLANE_OVERLAY_BLEND_ALPHABLEND  = 0x1
} D3DDDI_MULTIPLANE_OVERLAY_BLEND;
````


## -enum-fields
<dl>

### -field D3DDDI_MULTIPLANE_OVERLAY_BLEND_OPAQUE

<dd>
<p>The overlay plane should ignore data in the alpha channel and make the blended plane entirely opaque.</p>
</dd>

### -field D3DDDI_MULTIPLANE_OVERLAY_BLEND_ALPHABLEND

<dd>
<p>The overlay plane should use the pre-multiplied alpha channel in this plane to blend it with the plane beneath.</p>
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