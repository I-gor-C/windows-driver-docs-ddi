---
UID: NS:d3d12umddi.D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032
title: D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032
author: windows-driver-content
description: Video process support data.
old-location: display\d3d12ddi-video-process-support-data-0032.htm
old-project: display
ms.assetid: ea2dabc5-6853-4491-8c1f-f3f5ae516952
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032, D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032 structure [Display Devices], d3d12umddi/D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032, display.d3d12ddi-video-process-support-data-0032
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
-	D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032
product: Windows
targetos: Windows
req.typenames: D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032
---

# D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032 structure
Video process support data.

## Syntax
```
typedef struct D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032 {
  UINT                                              NodeIndex;
  D3D12DDI_VIDEO_SAMPLE_DESCRIPTION_0020            InputSample;
  D3D12DDI_VIDEO_FIELD_TYPE_0020                    InputFieldType;
  D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020           InputStereoFormat;
  DXGI_RATIONAL                                     InputFrameRate;
  D3D12DDI_VIDEO_FORMAT_DESCRIPTION_0020            OutputFormat;
  D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020           OutputStereoFormat;
  DXGI_RATIONAL                                     OutputFrameRate;
  D3D12DDI_VIDEO_PROCESS_SUPPORT_FLAGS_0022         SupportFlags;
  D3D12DDI_VIDEO_SCALE_SUPPORT_0032                 ScaleSupport;
  D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAGS_0020 FeatureSupport;
  D3D12DDI_VIDEO_PROCESS_DEINTERLACE_FLAGS_0020     DeinterlaceSupport;
  D3D12DDI_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS_0022 AutoProcessingSupport;
  D3D12DDI_VIDEO_PROCESS_FILTER_FLAGS_0020          FilterSupport;
  D3D12DDI_VIDEO_PROCESS_FILTER_RANGE_0020          FilterRangeSupport[D3D12DDI_VIDEO_PROCESS_MAX_FILTERS_0020];
};
```

## Members


`NodeIndex`

Node index.

`InputSample`

Input sample.

`InputFieldType`

Input field type.

`InputStereoFormat`

Input stereo format.

`InputFrameRate`

Input frame rate.

`OutputFormat`

Output format.

`OutputStereoFormat`

Output stereo format.

`OutputFrameRate`

Output frame rate.

`SupportFlags`

Support flags.

`ScaleSupport`

Scale support.

`FeatureSupport`

Feature support.

`DeinterlaceSupport`

Deinterlace support.

`AutoProcessingSupport`

Auto processing support.

`FilterSupport`

Filter support.

`FilterRangeSupport`

Filter range support.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h |