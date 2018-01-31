---
UID : NE:d3d12umddi.D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020
title : D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020
author : windows-driver-content
description : Defines the layout in memory of a stereo 3D video frame.
old-location : display\d3d12ddi_video_frame_stereo_format.htm
old-project : display
ms.assetid : 91C5C387-320C-4ABE-98AB-36D2CDE7428F
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : d3d12umddi/D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_VERTICAL, D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_MONO, d3d12umddi/D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020, D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020 enumeration [Display Devices], D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_SEPARATE, D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_VERTICAL, d3d12umddi/D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_MONO, d3d12umddi/D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_SEPARATE, D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_HORIZONTAL, d3d12umddi/D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_HORIZONTAL, display.d3d12ddi_video_frame_stereo_format, D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3d12umddi.h
req.include-header : D3d12umddi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020
---

# D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020 Enumeration
Defines the layout in memory of a stereo 3D video frame.

## Syntax
````
typedef enum D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020 { 
  D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_MONO        = 0,
  D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_HORIZONTAL  = 1,
  D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_VERTICAL    = 2,
  D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_SEPARATE    = 3
} D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020;
````

## Constants

<table>

<tr>
<td>D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_HORIZONTAL</td>
<td>Frame 0 and frame 1 are packed side-by-side, as shown in the following diagram:
<table>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
</table></td>
</tr>

<tr>
<td>D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_MONO</td>
<td>The sample does not contain stereo data. If the stereo format is not specified, this value is the default.</td>
</tr>

<tr>
<td>D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_SEPARATE</td>
<td>Frame 0 and frame 1 are placed in separate resources.</td>
</tr>

<tr>
<td>D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020_VERTICAL</td>
<td>Frame 0 and frame 1 are packed top-to-bottom, as shown in the following diagram:
<table>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
</table></td>
</tr>
</table>

## Remarks

All drivers that support stereo must support all the formats in this enumeration.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |