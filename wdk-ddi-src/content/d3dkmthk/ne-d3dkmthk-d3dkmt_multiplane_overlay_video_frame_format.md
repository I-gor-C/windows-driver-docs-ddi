---
UID: NE.d3dkmthk.D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT
title: D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_multiplane_overlay_video_frame_format.htm
old-project: display
ms.assetid: 0b17bc65-39a3-4aaf-8907-c85919a76b65
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT, D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT
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
req.alt-api: D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT
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

# D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT enumeration



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
typedef enum D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT { 
  D3DKMT_MULIIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_PROGRESSIVE                    = 0,
  D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_INTERLACED_TOP_FIELD_FIRST     = 1,
  D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_INTERLACED_BOTTOM_FIELD_FIRST  = 2
} D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT;
````


## -enum-fields

### -field D3DKMT_MULIIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_PROGRESSIVE


### -field D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_INTERLACED_TOP_FIELD_FIRST


### -field D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_INTERLACED_BOTTOM_FIELD_FIRST


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