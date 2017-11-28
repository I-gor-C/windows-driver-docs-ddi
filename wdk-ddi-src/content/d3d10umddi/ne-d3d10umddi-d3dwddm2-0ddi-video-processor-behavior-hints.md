---
UID: NE.d3d10umddi.D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS
title: D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS
author: windows-driver-content
description: Describes operations that the video processor can perform more efficiently than VideoProcessorBlt.
old-location: display\d3dwddm2_0ddi_video_processor_behavior_hints.htm
old-project: display
ms.assetid: 1D995AE5-C856-4971-8D51-B06EB32F8C74
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS
req.alt-loc: D3d10umddi.h
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

# D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS enumeration



## -description
<p>Describes operations that the video processor can perform more efficiently than <a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a>.</p>


## -syntax

````
typedef enum D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS { 
  D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_ROTATION                = 0x01,
  D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_RESIZE                  = 0x02,
  D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_COLOR_SPACE_CONVERSION  = 0x04
} D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS;
````


## -enum-fields
<dl>

### -field <a id="D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_ROTATION"></a><a id="d3dwddm2_0ddi_video_processor_behavior_hint_multiplane_overlay_rotation"></a><b>D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_ROTATION</b>

<dd>
<p>Indicates that multi-plane overlay hardware can perform the rotation operation more efficiently than <a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a>. </p>
</dd>

### -field <a id="D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_RESIZE"></a><a id="d3dwddm2_0ddi_video_processor_behavior_hint_multiplane_overlay_resize"></a><b>D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_RESIZE</b>

<dd>
<p>Indicates that the multi-plane overlay hardware can perform the scaling operation more efficiently than <a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a>. </p>
</dd>

### -field <a id="D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_COLOR_SPACE_CONVERSION"></a><a id="d3dwddm2_0ddi_video_processor_behavior_hint_multiplane_overlay_color_space_conversion"></a><b>D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_COLOR_SPACE_CONVERSION</b>

<dd>
<p>Indicates that the multi-plane overlay hardware can perform the colorspace conversion operation more efficiently than <a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a>. </p>
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
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
