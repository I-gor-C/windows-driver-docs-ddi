---
UID: NE:d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE
title: D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE
author: windows-driver-content
description: For stereo 3-D video, specifies whether the data in frame 0 or frame 1 is flipped, either horizontally or vertically.
old-location: display\d3d11_1ddi_video_processor_stereo_flip_mode.htm
old-project: display
ms.assetid: b385a0fd-6181-45c3-ba6e-e292e0b10e68
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_FRAME0, D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_FRAME1, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_FRAME1, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_FRAME0, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_NONE, D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE, display.d3d11_1ddi_video_processor_stereo_flip_mode, D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_NONE, D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE enumeration [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	D3d10umddi.h
apiname:
-	D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE
product: Windows
targetos: Windows
req.typenames: D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE
---

# D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE Enumeration
For stereo 3-D video, specifies whether the data in frame 0 or frame 1 is flipped, either horizontally or vertically.

## Syntax
````
typedef enum D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE { 
  D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_NONE    = 0,
  D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_FRAME0  = 1,
  D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_FRAME1  = 2
} D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE;
````

## Constants

<table>
            
                <tr>
                    <td>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_FRAME0</td>
                    <td>The data in frame 0 is flipped.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_FRAME1</td>
                    <td>The data in frame 1 is flipped.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_NONE</td>
                    <td>Neither frame is flipped.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |