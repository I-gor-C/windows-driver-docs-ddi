---
UID: NE.dxgiddi.DXGI_DDI_MULTIPLANE_OVERLAY_FLAGS
title: DXGI_DDI_MULTIPLANE_OVERLAY_FLAGS
author: windows-driver-content
description: Identifies a flip operation to be performed on an overlay plane.
old-location: display\dxgi_ddi_multiplane_overlay_flags.htm
ms.assetid: 74245a8b-1b52-4336-a744-1aedaca0eef5
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
req.alt-api: DXGI_DDI_MULTIPLANE_OVERLAY_FLAGS
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

# DXGI_DDI_MULTIPLANE_OVERLAY_FLAGS enumeration



## -description
<p>Identifies a flip operation to be performed on an overlay plane.</p>


## -syntax

````
typedef enum DXGI_DDI_MULTIPLANE_OVERLAY_FLAGS { 
  DXGI_DDI_MULTIPLANE_OVERLAY_FLAG_VERTICAL_FLIP            = 0x1,
  DXGI_DDI_MULTIPLANE_OVERLAY_FLAG_HORIZONTAL_FLIP          = 0x2,
  DXGI_MULTIPLANE_OVERLAY_FLAG_FULLSCREEN_POST_COMPOSITION  = 0x4
} DXGI_DDI_MULTIPLANE_OVERLAY_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_FLAG_VERTICAL_FLIP"></a><a id="dxgi_ddi_multiplane_overlay_flag_vertical_flip"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_FLAG_VERTICAL_FLIP</b>

<dd>
<p>The overlay plane should flip the data vertically, making it appear upside-down.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_FLAG_HORIZONTAL_FLIP"></a><a id="dxgi_ddi_multiplane_overlay_flag_horizontal_flip"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_FLAG_HORIZONTAL_FLIP</b>

<dd>
<p>The overlay plane should flip the data horizontally, making it appear as a right-to-left mirror image.</p>
</dd>

### -field <a id="DXGI_MULTIPLANE_OVERLAY_FLAG_FULLSCREEN_POST_COMPOSITION"></a><a id="dxgi_multiplane_overlay_flag_fullscreen_post_composition"></a><b>DXGI_MULTIPLANE_OVERLAY_FLAG_FULLSCREEN_POST_COMPOSITION</b>

<dd>
<p>Indicates that the plane is to be stretched using panel fitter hardware.

This should only be set for plane 0.

Composition with other multi-plane overlay planes may be supported, but the ClipRects of those planes must be bound to the SourceRect of this plane.
</p>
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