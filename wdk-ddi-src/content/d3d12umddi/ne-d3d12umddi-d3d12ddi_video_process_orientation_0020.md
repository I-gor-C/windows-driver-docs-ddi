---
UID : NE:d3d12umddi.D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020
title : D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020
author : windows-driver-content
description : The orientation to be performed by the video processor.
old-location : display\d3d12ddi_video_process_orientation.htm
old-project : display
ms.assetid : 0901AA41-DDA6-46F2-99CA-E45718346A86
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020, D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020
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
req.alt-api : D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020
req.alt-loc : D3d12umddi.h
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
req.typenames : D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020
---

# D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020 Enumeration
The orientation to be performed by the video processor.

## Syntax
````
typedef enum D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020 { 
  D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_DEFAULT                        = 0,
  D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_FLIP_HORIZONTAL                = 1,
  D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_CLOCKWISE_90                   = 2,
  D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_CLOCKWISE_90_FLIP_HORIZONTAL   = 3,
  D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_CLOCKWISE_180                  = 4,
  D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_FLIP_VERTICAL                  = 5,
  D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_CLOCKWISE_180_FLIP_HORIZONTAL  = 5,
  D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_CLOCKWISE_270                  = 6,
  D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_CLOCKWISE_270_FLIP_HORIZONTAL  = 7
} D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020;
````

## Constants

<table>

<tr>
<td>D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_CLOCKWISE_180</td>
<td>Rotate the image clockwise 180 degrees.</td>
</tr>

<tr>
<td>D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_CLOCKWISE_180_FLIP_HORIZONTAL</td>
<td>Rotate the image clockwise 180 degrees and then flip horizontally. This is the same as the <b>D3D12DDI_VIDEO_PROCESS_ORIENTATION_FLIP_VERTICAL</b> constant.</td>
</tr>

<tr>
<td>D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_CLOCKWISE_270</td>
<td>Rotate the image clockwise 270 degrees.</td>
</tr>

<tr>
<td>D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_CLOCKWISE_270_FLIP_HORIZONTAL</td>
<td>Rotate the image clockwise 270 degrees and then flips horizontally.</td>
</tr>

<tr>
<td>D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_CLOCKWISE_90</td>
<td>Rotate the image clockwise 90 degrees.</td>
</tr>

<tr>
<td>D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_CLOCKWISE_90_FLIP_HORIZONTAL</td>
<td>Rotate the image clockwise 90 degrees and then flips it horizontally.</td>
</tr>

<tr>
<td>D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_DEFAULT</td>
<td>No change to the orientation.</td>
</tr>

<tr>
<td>D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_FLIP_HORIZONTAL</td>
<td>Flip the image horizontally.</td>
</tr>

<tr>
<td>D3D12DDI_VIDEO_PROCESS_ORIENTATION_0020_FLIP_VERTICAL</td>
<td>Flip the image vertically. This is the same as the <b>D3D12DDI_VIDEO_PROCESS_ORIENTATION_CLOCKWISE_180_FLIP_HORIZONTAL</b> constant.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |