---
UID: NE.d3dumddi._D3DDDI_MULTIPLANE_OVERLAY_FLAGS
title: _D3DDDI_MULTIPLANE_OVERLAY_FLAGS
author: windows-driver-content
description: Identifies a flip operation to be performed on an overlay plane.
old-location: display\d3dddi_multiplane_overlay_flags.htm
old-project: display
ms.assetid: b91d87e8-3f63-45ac-919f-3597957ea497
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _D3DDDI_MULTIPLANE_OVERLAY_FLAGS, D3DDDI_MULTIPLANE_OVERLAY_FLAGS
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
---

# _D3DDDI_MULTIPLANE_OVERLAY_FLAGS enumeration



## -description
Identifies a flip operation to be performed on an overlay plane.


## -syntax

````
typedef enum _D3DDDI_MULTIPLANE_OVERLAY_FLAGS { 
  D3DDDI_MULTIPLANE_OVERLAY_FLAG_VERTICAL_FLIP    = 0x1,
  D3DDDI_MULTIPLANE_OVERLAY_FLAG_HORIZONTAL_FLIP  = 0x2
} D3DDDI_MULTIPLANE_OVERLAY_FLAGS;
````


## -enum-fields

### -field D3DDDI_MULTIPLANE_OVERLAY_FLAG_VERTICAL_FLIP

The overlay plane should flip the data vertically, making it appear upside-down.

### -field D3DDDI_MULTIPLANE_OVERLAY_FLAG_HORIZONTAL_FLIP

The overlay plane should flip the data horizontally, making it appear as a right-to-left mirror image.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8.1
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012 R2
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>