---
UID: NE.d3dumddi._D3DDDI_MULTIPLANE_OVERLAY_FLAGS
title: D3DDDI_MULTIPLANE_OVERLAY_FLAGS
author: windows-driver-content
description: Identifies a flip operation to be performed on an overlay plane.
old-location: display\d3dddi_multiplane_overlay_flags.htm
old-project: display
ms.assetid: b91d87e8-3f63-45ac-919f-3597957ea497
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
req.alt-api: D3DDDI_MULTIPLANE_OVERLAY_FLAGS
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

# D3DDDI_MULTIPLANE_OVERLAY_FLAGS enumeration



## -description
<p>Identifies a flip operation to be performed on an overlay plane.</p>


## -syntax

````
typedef enum _D3DDDI_MULTIPLANE_OVERLAY_FLAGS { 
  D3DDDI_MULTIPLANE_OVERLAY_FLAG_VERTICAL_FLIP    = 0x1,
  D3DDDI_MULTIPLANE_OVERLAY_FLAG_HORIZONTAL_FLIP  = 0x2
} D3DDDI_MULTIPLANE_OVERLAY_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="D3DDDI_MULTIPLANE_OVERLAY_FLAG_VERTICAL_FLIP"></a><a id="d3dddi_multiplane_overlay_flag_vertical_flip"></a><b>D3DDDI_MULTIPLANE_OVERLAY_FLAG_VERTICAL_FLIP</b>

<dd>
<p>The overlay plane should flip the data vertically, making it appear upside-down.</p>
</dd>

### -field <a id="D3DDDI_MULTIPLANE_OVERLAY_FLAG_HORIZONTAL_FLIP"></a><a id="d3dddi_multiplane_overlay_flag_horizontal_flip"></a><b>D3DDDI_MULTIPLANE_OVERLAY_FLAG_HORIZONTAL_FLIP</b>

<dd>
<p>The overlay plane should flip the data horizontally, making it appear as a right-to-left mirror image.</p>
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