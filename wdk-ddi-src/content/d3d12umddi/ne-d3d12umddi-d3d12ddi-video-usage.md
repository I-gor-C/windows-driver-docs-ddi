---
UID: NE.d3d12umddi.D3D12DDI_VIDEO_USAGE
title: D3D12DDI_VIDEO_USAGE
author: windows-driver-content
description: A hint for the graphics driver to optimize for different scenarios.
old-location: display\d3d12ddi_video_usage.htm
old-project: display
ms.assetid: 663790EE-A9E3-4EBC-93C7-20DE0D759A26
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_VIDEO_USAGE
req.alt-loc: D3d12umddi.h
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

# D3D12DDI_VIDEO_USAGE enumeration



## -description
<p>A hint for the graphics driver to optimize for different scenarios.</p>


## -syntax

````
typedef enum D3D12DDI_VIDEO_USAGE { 
  D3D12DDI_VIDEO_USAGE_NORMAL  = 0,
  D3D12DDI_VIDEO_USAGE_POWER   = 1,
  D3D12_VIDEO_USAGE_QUALITY    = 2
} D3D12DDI_VIDEO_USAGE;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDI_VIDEO_USAGE_NORMAL"></a><a id="d3d12ddi_video_usage_normal"></a><b>D3D12DDI_VIDEO_USAGE_NORMAL</b>

<dd>
<p>Normal video playback.</p>
</dd>

### -field <a id="D3D12DDI_VIDEO_USAGE_POWER"></a><a id="d3d12ddi_video_usage_power"></a><b>D3D12DDI_VIDEO_USAGE_POWER</b>

<dd>
<p>Lower the power usage. This setting can lead to some reduction in video quality.</p>
</dd>

### -field <a id="D3D12_VIDEO_USAGE_QUALITY"></a><a id="d3d12_video_usage_quality"></a><b>D3D12_VIDEO_USAGE_QUALITY</b>

<dd>
<p>The best video quality possible. This setting is appropriate for tasks such as video editing, where quality is more important than speed. It is not appropriate for real-time playback.</p>
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
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>