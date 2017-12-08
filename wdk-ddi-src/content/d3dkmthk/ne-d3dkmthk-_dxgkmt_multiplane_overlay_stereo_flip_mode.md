---
UID: NE.d3dkmthk._DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
title: _DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
author: windows-driver-content
description: Reserved for system use. Do not use it in your driver.
old-location: display\dxgkmt_multiplane_overlay_stereo_flip_mode.htm
old-project: display
ms.assetid: 17d77f4f-e1ad-45d6-9cba-1dfcaea2577b
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE, DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
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
req.alt-api: DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
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

# _DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE enumeration



## -description
Reserved for system use. Do not use it in your driver.


## -syntax

````
typedef enum _DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE { 
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE    = 0,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME0  = 1,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME1  = 2
} DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE;
````


## -enum-fields

### -field DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE


### -field DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME0


### -field DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME1


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