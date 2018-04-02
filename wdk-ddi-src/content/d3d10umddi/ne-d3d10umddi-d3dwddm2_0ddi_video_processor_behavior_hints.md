---
UID: NE:d3d10umddi.D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS
title: D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS
author: windows-driver-content
description: Describes operations that the video processor can perform more efficiently than VideoProcessorBlt.
old-location: display\d3dwddm2_0ddi_video_processor_behavior_hints.htm
old-project: display
ms.assetid: 1D995AE5-C856-4971-8D51-B06EB32F8C74
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS, D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS enumeration [Display Devices], D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_COLOR_SPACE_CONVERSION, D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_RESIZE, D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_ROTATION, d3d10umddi/D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS, d3d10umddi/D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_COLOR_SPACE_CONVERSION, d3d10umddi/D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_RESIZE, d3d10umddi/D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_ROTATION, display.d3dwddm2_0ddi_video_processor_behavior_hints
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3d10umddi.h
api_name:
-	D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS
product: Windows
targetos: Windows
req.typenames: D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS
---

# D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS Enumeration
Describes operations that the video processor can perform more efficiently than <a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a>.

## Syntax
```
typedef enum D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS {
  D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_ROTATION                ,
  D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_RESIZE                  ,
  D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_COLOR_SPACE_CONVERSION
} ;
```

## Constants

<table>
            
                <tr>
                    <td>D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_ROTATION</td>
                    <td>Indicates that multi-plane overlay hardware can perform the rotation operation more efficiently than <a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a>.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_RESIZE</td>
                    <td>Indicates that the multi-plane overlay hardware can perform the scaling operation more efficiently than <a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a>.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_COLOR_SPACE_CONVERSION</td>
                    <td>Indicates that the multi-plane overlay hardware can perform the colorspace conversion operation more efficiently than <a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a>.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a>