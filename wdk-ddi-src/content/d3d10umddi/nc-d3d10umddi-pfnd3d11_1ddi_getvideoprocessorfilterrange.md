---
UID: NC:d3d10umddi.PFND3D11_1DDI_GETVIDEOPROCESSORFILTERRANGE
title: PFND3D11_1DDI_GETVIDEOPROCESSORFILTERRANGE
author: windows-driver-content
description: Queries the range of values that the display miniport driver supports for a specified video processor filter.
old-location: display\getvideoprocessorfilterrange.htm
old-project: display
ms.assetid: ab3f8abb-4735-42c1-9664-8f2f5f7d5da7
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D11_1DDI_GETVIDEOPROCESSORFILTERRANGE, d3d10umddi/pfnGetVideoProcessorFilterRange, display.getvideoprocessorfilterrange, pfnGetVideoProcessorFilterRange, pfnGetVideoProcessorFilterRange callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
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
-	UserDefined
api_location:
-	D3d10umddi.h
api_name:
-	pfnGetVideoProcessorFilterRange
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_GETVIDEOPROCESSORFILTERRANGE callback function
Queries the range of values that the display miniport driver supports for a specified video processor filter.

## Syntax

```
PFND3D11_1DDI_GETVIDEOPROCESSORFILTERRANGE Pfnd3d111DdiGetvideoprocessorfilterrange;

void Pfnd3d111DdiGetvideoprocessorfilterrange(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSORENUM,
   D3D11_1DDI_VIDEO_PROCESSOR_FILTER,
  D3D11_1DDI_VIDEO_PROCESSOR_FILTER_RANGE *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSORENUM`



`D3D11_1DDI_VIDEO_PROCESSOR_FILTER`



`*`




## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ne-d3d10umddi-d3d11_1ddi_video_processor_filter.md">D3D11_1DDI_VIDEO_PROCESSOR_FILTER</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessorenum.md">CreateVideoProcessorEnum</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_processor_filter_range.md">D3D11_1DDI_VIDEO_PROCESSOR_FILTER_RANGE</a>