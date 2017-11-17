---
UID: NE.d3dkmthk._DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
title: DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
author: windows-driver-content
description: Reserved for system use. Do not use it in your driver.
old-location: display\dxgkmt_multiplane_overlay_stereo_flip_mode.htm
ms.assetid: 17d77f4f-e1ad-45d6-9cba-1dfcaea2577b
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
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
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
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

### -field <a id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE"></a><a id="dxgkmt_multiplane_overlay_stereo_flip_none"></a><b>DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE</b>

<dd></dd>

### -field <a id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME0"></a><a id="dxgkmt_multiplane_overlay_stereo_flip_frame0"></a><b>DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME0</b>

<dd></dd>

### -field <a id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME1"></a><a id="dxgkmt_multiplane_overlay_stereo_flip_frame1"></a><b>DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME1</b>

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