---
UID: NS:d3d12umddi.D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_0032
title: D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_0032
author: windows-driver-content
description: The video process input stream arguments.
old-location: display\d3d12ddiarg-video-process-input-stream-arguments-0032.htm
old-project: display
ms.assetid: b6eafa0c-1b5e-4723-9317-60f1507f12ea
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_0032, D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_0032 structure [Display Devices], d3d12umddi/D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_0032, display.d3d12ddiarg-video-process-input-stream-arguments-0032
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
-	HeaderDef
api_location:
-	d3d12umddi.h
api_name:
-	D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_0032
product: Windows
targetos: Windows
req.typenames: D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_0032
---

# D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_0032 structure
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

The video process input stream arguments.

## Syntax
```
typedef struct D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_0032 {
  D3D12DDI_VIDEO_PROCESS_INPUT_STREAM_0020           InputStream[2];
  D3D12DDI_VIDEO_PROCESS_TRANSFORM_0032              Transform;
  D3D12DDI_VIDEO_PROCESS_INPUT_STREAM_FLAGS_0020     Flags;
  D3D12DDI_VIDEO_PROCESS_INPUT_STREAM_RATE_INFO_0032 RateInfo;
  INT                                                FilterLevels[D3D12DDI_VIDEO_PROCESS_MAX_FILTERS_0020];
  D3D12DDI_VIDEO_PROCESS_ALPHA_BLENDING_0020         AlphaBlending;
};
```

## Members


`InputStream`

The input stream of bytes.

`Transform`

The video process transform.

`Flags`

The video process input stream flags.

`RateInfo`

The rate of the video process input stream.

`FilterLevels`

The video process filter levels.

`AlphaBlending`

The video process alpha blending.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h |