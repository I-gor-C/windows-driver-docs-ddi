---
UID: NS.d3dkmddi._DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION
title: DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION
author: windows-driver-content
description: Specifies information about any additional transforms that should occur after the planes are composed.
old-location: display\dxgk_multiplane_overlay_post_composition.htm
ms.assetid: 71D57E42-C1E7-4A0E-80B3-DD39388552C5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION
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
ms.keywords: DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION, DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION
req.iface: 
---

# DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION structure



## -description
<p>Specifies information about any additional transforms that should occur after the planes are composed.</p>


## -syntax

````
typedef struct _DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION {
  DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS        Flags;
  RECT                                                  SrcRect;
  RECT                                                  DstRect;
  D3DDDI_ROTATION                                       Rotation;
} DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>A DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS structure indicating additional transform information.</p>
</dd>

### -field <b>SrcRect</b>

<dd>
<p>Contains the source rect of the virtual mode.</p>
</dd>

### -field <b>DstRect</b>

<dd>
<p>Contains the destination rect of the virtual mode.</p>
</dd>

### -field <b>Rotation</b>

<dd>
<p>Indicates additional rotation that should occur on the final image.</p>
</dd>
</dl>

## -remarks
<p>The source mode contains the virtual mode size and the destination rectangle indicates how the virtual mode maps to the physical mode.

For example, if a 1024x768 virtual mode is used with 1920x1080 physical mode, the following configurations are possible:

</p><dl>
<dd>Stretch mode:
<dl>
<dd>SrcRect = {0, 0, 1024, 768}
</dd>
<dd>DstRect = {0, 0, 1920, 1080}</dd>
</dl>
</dd>
<dd>Centered mode:
<dl>
<dd>SrcRect = {0, 0, 1024, 768}</dd>
<dd>DstRect = {448, 156, 1472, 924}  

</dd>
</dl>
</dd>
<dd>Aspect ratio stretched:
<dl>
<dd>SrcRect = {0, 0, 1024, 768}
</dd>
<dd>DstRect = {240, 0, 1680, 1080}   // 1080p monitor resolution
</dd>
</dl>
</dd>
</dl><dl>
<dd>SrcRect = {0, 0, 1024, 768}
</dd>
<dd>DstRect = {0, 0, 1920, 1080}</dd>
</dl><dl>
<dd>SrcRect = {0, 0, 1024, 768}</dd>
<dd>DstRect = {448, 156, 1472, 924}  

</dd>
</dl><dl>
<dd>SrcRect = {0, 0, 1024, 768}
</dd>
<dd>DstRect = {240, 0, 1680, 1080}   // 1080p monitor resolution
</dd>
</dl>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>