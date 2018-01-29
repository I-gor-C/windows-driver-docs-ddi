---
UID : NS:d3d12umddi.D3D12DDI_VIDEO_PROCESS_OUTPUT_STREAM_DESC_0032
title : D3D12DDI_VIDEO_PROCESS_OUTPUT_STREAM_DESC_0032
author : windows-driver-content
description : Describes output stream properties for the video processor.
old-location : display\d3d12ddi_video_process_output_stream_desc_0032.htm
old-project : display
ms.assetid : 5A995E97-4522-44CD-89C3-521724142D7F
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.d3d12ddi_video_process_output_stream_desc_0032, D3D12DDI_VIDEO_PROCESS_OUTPUT_STREAM_DESC_0032 structure [Display Devices], D3D12DDI_VIDEO_PROCESS_OUTPUT_STREAM_DESC_0032, d3d12umddi/D3D12DDI_VIDEO_PROCESS_OUTPUT_STREAM_DESC_0032
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3d12umddi.h
req.include-header : 
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
req.typenames : D3D12DDI_VIDEO_PROCESS_OUTPUT_STREAM_DESC_0032
---

# D3D12DDI_VIDEO_PROCESS_OUTPUT_STREAM_DESC_0032 structure
Describes output stream properties for the video processor.

## Syntax
````
typedef struct _D3D12DDI_VIDEO_PROCESS_OUTPUT_STREAM_DESC_0032 {
  DXGI_FORMAT                                 Format;
  DXGI_COLOR_SPACE_TYPE                       ColorSpace;
  D3D12DDI_VIDEO_PROCESS_ALPHA_FILL_MODE_0020 AlphaFillMode;
  UINT                                        AlphaFillModeSourceStreamIndex;
  FLOAT                                       BackgroundColor[4];
  DXGI_RATIONAL                               FrameRate;
  BOOL                                        EnableStereo;
} D3D12DDI_VIDEO_PROCESS_OUTPUT_STREAM_DESC_0032;
````

## Members


`AlphaFillMode`

The alpha fill mode for data that the video processor writes to the render target.  See D3D12DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE.

`AlphaFillModeSourceStreamIndex`

The zero-based index of an input stream. This parameter is used if AlphaFillMode is D3D12DDI_VIDEO_PROCESS_ALPHA_FILL_MODE_SOURCE_STREAM. Otherwise, the parameter is ignored.

`BackgroundColor`



`ColorSpace`

A DXGI_COLOR_SPACE_TYPE value that specifies the colorspace for the video processor output surface.

`EnableStereo`

If TRUE, stereo output is enabled. Otherwise, the video processor produces mono video frames.

`Format`

The DXGI format of the output texture.

`FrameRate`

The frame rate of the output video stream, specified as a DXGI_RATIONAL structure.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h |