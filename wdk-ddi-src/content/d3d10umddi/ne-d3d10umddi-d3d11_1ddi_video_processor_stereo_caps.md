---
UID: NE:d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS
title: D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS
author: windows-driver-content
description: Defines stereo 3-D capabilities for a Microsoft Direct3D 11 video processor.
old-location: display\d3d11_1ddi_video_processor_stereo_caps.htm
old-project: display
ms.assetid: 02b096be-0f9e-4ea3-a13f-1c6ad7c802c9
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS, D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS enumeration [Display Devices], D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_CHECKERBOARD, D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_COLUMN_INTERLEAVED, D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_FLIP_MODE, D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_MONO_OFFSET, D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_ROW_INTERLEAVED, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_CHECKERBOARD, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_COLUMN_INTERLEAVED, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_FLIP_MODE, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_MONO_OFFSET, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_ROW_INTERLEAVED, display.d3d11_1ddi_video_processor_stereo_caps
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3d10umddi.h
api_name:
-	D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS
product:
- Windows
targetos: Windows
req.typenames: D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS
---

# D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS Enumeration
Defines stereo 3-D capabilities for a Microsoft Direct3D 11 video processor.

## Syntax
```
typedef enum D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS {
  D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_MONO_OFFSET         ,
  D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_ROW_INTERLEAVED     ,
  D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_COLUMN_INTERLEAVED  ,
  D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_CHECKERBOARD        ,
  D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_FLIP_MODE
} ;
```

## Constants

<table>
            
                <tr>
                    <td>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_MONO_OFFSET</td>
                    <td>The video processor supports the <b>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT_MONO_OFFSET</b> format defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451029">D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT</a> enumeration.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_ROW_INTERLEAVED</td>
                    <td>The video processor supports the <b>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT_ROW_INTERLEAVED</b> format.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_COLUMN_INTERLEAVED</td>
                    <td>The video processor supports the <b>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT_COLUMN_INTERLEAVED</b> 
 format.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_CHECKERBOARD</td>
                    <td>The video processor supports the <b>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT_CHECKERBOARD</b> 
format.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS_FLIP_MODE</td>
                    <td>The video processor can flip one or both views. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451025">D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE</a>.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451025">D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451029">D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT</a>