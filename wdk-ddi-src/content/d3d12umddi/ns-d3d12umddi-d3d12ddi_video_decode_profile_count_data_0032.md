---
UID : NS:d3d12umddi.D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032
title : D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032
author : windows-driver-content
description : Video decode profile count data.
old-location : display\d3d12ddi-video-decode-profile-count-data-0032.htm
old-project : display
ms.assetid : 8398579d-e8cf-4c58-ac74-eeddf2dca23b
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.d3d12ddi-video-decode-profile-count-data-0032, d3d12umddi/D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032, D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032, D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032 structure [Display Devices]
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
req.typenames : D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032
---

# D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032 structure
Video decode profile count data.

## Syntax
````
typedef struct _D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032 {
  UINT  NodeIndex;
  UINT  ProfileCount;
} D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032, D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032;
````

## Members


`NodeIndex`

Node index.

`ProfileCount`

Profile count.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h |