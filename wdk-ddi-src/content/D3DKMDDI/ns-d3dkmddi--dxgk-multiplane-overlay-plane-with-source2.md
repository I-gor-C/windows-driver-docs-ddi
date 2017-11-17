---
UID: NS.d3dkmddi._DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE2
title: DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE2
author: windows-driver-content
description: Used in a call to the DxgkDdiCheckMultiPlaneOverlaySupport3 function to check details on hardware support for multi-plane overlays.
old-location: display\dxgk_multiplane_overlay_plane_with_source2.htm
ms.assetid: A9508EBF-0B33-48D7-AD57-31E38D77F5DA
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
req.alt-api: DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE2
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
ms.keywords: DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE2, DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE2
req.iface: 
---

# DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE2 structure



## -description
<p>Used in a call to the <i>DxgkDdiCheckMultiPlaneOverlaySupport3</i> function to check details on hardware support for multi-plane overlays.</p>


## -syntax

````
typedef struct _DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE2 {
  HANDLE                                   hAllocation;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID           VidPnSourceId;
  UINT                                     LayerIndex;
  DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES3      PlaneAttributes;
} DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE2;
````


## -struct-fields
<dl>

### -field <b>hAllocation</b>

<dd>
<p>A handle to the allocation.</p>
</dd>

### -field <b>VidPnSourceId</b>

<dd>
<p>The zero-based video present network (VidPN) source identification number of the input for which the support levels are queried.</p>
</dd>

### -field <b>LayerIndex</b>

<dd>
<p>The zero based index indicating the Z order of the overlay plane.</p>
</dd>

### -field <b>PlaneAttributes</b>

<dd>
<p>A DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES3 structure that specifies overlay plane attributes.</p>
</dd>
</dl>

## -remarks


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