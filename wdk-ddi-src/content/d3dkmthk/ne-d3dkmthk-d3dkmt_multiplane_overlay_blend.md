---
UID: NE.d3dkmthk.D3DKMT_MULTIPLANE_OVERLAY_BLEND
title: D3DKMT_MULTIPLANE_OVERLAY_BLEND
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_multiplane_overlay_blend.htm
old-project: display
ms.assetid: f0d181a6-f9cc-4e21-a971-7192e245a5c7
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DKMT_MULTIPLANE_OVERLAY_BLEND, D3DKMT_MULTIPLANE_OVERLAY_BLEND
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_MULTIPLANE_OVERLAY_BLEND
req.alt-loc: D3dkmthk.h
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

# D3DKMT_MULTIPLANE_OVERLAY_BLEND enumeration



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
typedef enum D3DKMT_MULTIPLANE_OVERLAY_BLEND { 
  D3DKMT_MULTIPLANE_OVERLAY_BLEND_OPAQUE      = 0x0,
  D3DKMT_MULTIPLANE_OVERLAY_BLEND_ALPHABLEND  = 0x1
} D3DKMT_MULTIPLANE_OVERLAY_BLEND;
````


## -enum-fields

### -field D3DKMT_MULTIPLANE_OVERLAY_BLEND_OPAQUE


### -field D3DKMT_MULTIPLANE_OVERLAY_BLEND_ALPHABLEND


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>