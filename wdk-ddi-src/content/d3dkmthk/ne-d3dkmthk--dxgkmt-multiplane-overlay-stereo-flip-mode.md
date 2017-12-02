---
UID: NE.d3dkmthk._DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
title: DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
author: windows-driver-content
description: Reserved for system use. Do not use it in your driver.
old-location: display\dxgkmt_multiplane_overlay_stereo_flip_mode.htm
old-project: display
ms.assetid: 17d77f4f-e1ad-45d6-9cba-1dfcaea2577b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
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
req.iface: 
---

# DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE enumeration



## -description
<p>Reserved for system use. Do not use it in your driver.</p>


## -syntax

````
typedef enum _DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE { 
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE    = 0,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME0  = 1,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME1  = 2
} DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE;
````


## -enum-fields
<dl>

### -field DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE

<dd></dd>

### -field DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME0

<dd></dd>

### -field DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME1

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>