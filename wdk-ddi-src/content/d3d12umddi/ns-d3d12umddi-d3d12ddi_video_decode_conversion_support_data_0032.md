---
UID: NS:d3d12umddi.D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032
title: D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032
author: windows-driver-content
description: Video decode conversion support data.
old-location: display\d3d12ddi-video-decode-conversion-support-data-0032.htm
old-project: display
ms.assetid: 1395fe30-9bbf-433c-8696-a0f842bad10e
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032, D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032 structure [Display Devices], d3d12umddi/D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032, display.d3d12ddi-video-decode-conversion-support-data-0032
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
-	D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032
product:
- Windows
targetos: Windows
req.typenames: D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032
---

# D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032 structure
Video decode conversion support data.

## Syntax
```
typedef struct D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032 {
  UINT                                                NodeIndex;
  D3D12DDI_VIDEO_DECODE_CONFIGURATION_0020            Configuration;
  D3D12DDI_VIDEO_SAMPLE_DESCRIPTION_0020              DecodeSample;
  D3D12DDI_VIDEO_FORMAT_DESCRIPTION_0020              OutputFormat;
  DXGI_RATIONAL                                       FrameRate;
  UINT                                                BitRate;
  D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_FLAGS_0020 SupportFlags;
  D3D12DDI_VIDEO_SCALE_SUPPORT_0032                   ScaleSupport;
};
```

## Members


`NodeIndex`

Node index.

`Configuration`

Configuration.

`DecodeSample`

Decode sample.

`OutputFormat`

Output format.

`FrameRate`

Frame rate.

`BitRate`

Bitrate.

`SupportFlags`

Support flags.

`ScaleSupport`

Scale support.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h |