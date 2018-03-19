---
UID: NE:d3d12umddi.D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAGS_0020
title: D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAGS_0020
author: windows-driver-content
description: Defines the features that video processor supports.
old-location: display\d3d12ddi_video_process_feature_support_flags.htm
old-project: display
ms.assetid: 6DBF48B1-44C7-4C53-8488-F1217E6FAA1C
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAGS_0020, D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAGS_0020 enumeration [Display Devices], D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_ALPHA_BLENDING, D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_ALPHA_FILL, D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_FLIP, D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_LUMA_KEY, D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_PIXEL_ASPECT_RATIO, D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_ROTATION, D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_STEREO, D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0022_NONE, d3d12umddi/D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAGS_0020, d3d12umddi/D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_ALPHA_BLENDING, d3d12umddi/D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_ALPHA_FILL, d3d12umddi/D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_FLIP, d3d12umddi/D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_LUMA_KEY, d3d12umddi/D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_PIXEL_ASPECT_RATIO, d3d12umddi/D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_ROTATION, d3d12umddi/D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_STEREO, d3d12umddi/D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0022_NONE, display.d3d12ddi_video_process_feature_support_flags
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
-	D3d12umddi.h
api_name:
-	D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAGS_0020
product: Windows
targetos: Windows
req.typenames: D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAGS_0020
---

# D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAGS_0020 Enumeration
Defines the features that video processor supports.

## Syntax
````
typedef enum D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAGS_0020 { 
  D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0022_NONE                = 0x0,
  D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_ALPHA_FILL          = 0x1,
  D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_LUMA_KEY            = 0x2,
  D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_STEREO              = 0x4,
  D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_ROTATION            = 0x8,
  D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_FLIP                = 0x10,
  D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_ALPHA_BLENDING      = 0x20,
  D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_PIXEL_ASPECT_RATIO  = 0x40
} D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAGS_0020;
````

## Constants

<table>
            
                <tr>
                    <td>D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0022_NONE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_ALPHA_FILL</td>
                    <td>The video processor can set alpha values on the output pixels. For more information, see the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetoutputalphafillmode.md">SetOutputAlphaFillMode</a> function.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_LUMA_KEY</td>
                    <td>The video processor can perform luma keying.  Luma keying is configured by using the <b>LumaKey</b> member of the <a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddiarg_video_process_input_stream_arguments_0020.md">D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_PARAMETERS</a> structure. For more information, see the <a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddi_video_process_luma_key_0020.md">D3D12DDI_VIDEO_PROCESS_LUMA_KEY</a> structure.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_STEREO</td>
                    <td>The video processor can support 3D stereo video. All drivers that set this capability must support the following stereo formats: <b>D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_HORIZONTAL</b>, <b>D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_VERTICAL</b>, and <b>D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_SEPARATE</b>.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_ROTATION</td>
                    <td>The driver can rotate the input data either 90, 180, or 270 degrees clockwise as part of the video processing operation.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_FLIP</td>
                    <td>The driver can flip the input data horizontally or vertically, together or separately with a video rotation operation.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_ALPHA_BLENDING</td>
                    <td>Alpha blending and a planar alpha may be set in the <b>AlphaBlending</b> member of the <a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddiarg_video_process_input_stream_arguments_0020.md">D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_PARAMETERS</a> structure.  For more information, see the <a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddi_video_process_alpha_blending_0020.md">D3D12DDI_VIDEO_PROCESS_ALPHA_BLENDING</a> structure.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAG_0020_PIXEL_ASPECT_RATIO</td>
                    <td>The driver supports changing the pixel aspect ratio.  If the driver does not report this capability, the <b>SourceAspectRatio</b> and <b>DestinationAspectRatio</b> members of the <a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddiarg_video_process_input_stream_arguments_0020.md">D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_PARAMETERS</a> structure must indicate a 1:1 aspect ratio.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetoutputalphafillmode.md">SetOutputAlphaFillMode</a>



<a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddiarg_video_process_input_stream_arguments_0020.md">D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_PARAMETERS</a>



<a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddi_video_process_alpha_blending_0020.md">D3D12DDI_VIDEO_PROCESS_ALPHA_BLENDING</a>



<a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddi_video_process_luma_key_0020.md">D3D12DDI_VIDEO_PROCESS_LUMA_KEY</a>