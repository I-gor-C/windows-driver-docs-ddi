---
UID: NC:d3d12umddi.PFND3D12DDI_VIDEO_DECODE_FRAME_0032
title: PFND3D12DDI_VIDEO_DECODE_FRAME_0032
author: windows-driver-content
description: Used to decode a video frame.
old-location: display\pfnd3d12ddi_video_decode_frame_0032.htm
old-project: display
ms.assetid: 0E7DC432-64F9-4EDE-B0FC-5F65EB9E68AD
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D12DDI_VIDEO_DECODE_FRAME_0030, PFND3D12DDI_VIDEO_DECODE_FRAME_0030 callback function [Display Devices], d3d12umddi/PFND3D12DDI_VIDEO_DECODE_FRAME_0030, display.pfnd3d12ddi_video_decode_frame_0032
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: 
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
-	UserDefined
api_location:
-	d3d12umddi.h
api_name:
-	PFND3D12DDI_VIDEO_DECODE_FRAME_0030
product: Windows
targetos: Windows
req.typenames: D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_VIDEO_DECODE_FRAME_0032 callback function
Used to decode a video frame.

## Syntax

```
PFND3D12DDI_VIDEO_DECODE_FRAME_0032 Pfnd3d12ddiVideoDecodeFrame0032;

void Pfnd3d12ddiVideoDecodeFrame0032(
  D3D12DDI_HCOMMANDLIST hDrvCommandList,
  D3D12DDI_HVIDEODECODER_0020 hDrvDecoder,
  const D3D12DDI_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS_0021 *pOutputStreamParameters,
  const D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0032 *pInputStreamParameters
)
{...}
```

## Parameters

`hDrvCommandList`

The command list.

`hDrvDecoder`

The video decoder.

`*pOutputStreamParameters`

The output arguments for the video decode.

`*pInputStreamParameters`

The input arguments for the video decode.


## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h |