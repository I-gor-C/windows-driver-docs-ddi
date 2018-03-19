---
UID: NC:d3d10umddi.PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE
title: PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE
author: windows-driver-content
description: Queries a custom frame rate that is associated with a rate conversion capability group.
old-location: display\getvideoprocessorcustomrate.htm
old-project: display
ms.assetid: 49aec00a-8d63-4ec9-966a-0826354fbbe0
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE, d3d10umddi/pfnGetVideoProcessorCustomRate, display.getvideoprocessorcustomrate, pfnGetVideoProcessorCustomRate, pfnGetVideoProcessorCustomRate callback function [Display Devices]
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
-	pfnGetVideoProcessorCustomRate
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE callback function
Queries a custom frame rate that is associated with a rate conversion capability group.

## Syntax

```
PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE Pfnd3d111DdiGetvideoprocessorcustomrate;

void Pfnd3d111DdiGetvideoprocessorcustomrate(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSORENUM,
   UINT,
   UINT,
  D3D11_1DDI_VIDEO_PROCESSOR_CUSTOM_RATE *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSORENUM`



`UINT`



`UINT`



`*`




## Return Value

This callback function does not return a value.

## Remarks

The display miniport driver returns the maximum number of frame-rate conversion capabilities that it supports through the <b>RateConversionCapsCount</b> member of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_processor_caps.md">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a> structure. The driver returns a pointer to this structure through its <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorcaps.md">GetVideoProcessorCaps</a> function. In addition, the attributes of a frame-rate conversion capability group can be queried by calling the <b>GetVideoProcessorCaps</b> function.

The display miniport driver returns the maximum number of custom rates that it supports through the <b>CustomRateCount</b> member of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_processor_rate_conversion_caps.md">D3D11_1DDI_VIDEO_PROCESSOR_RATE_CONVERSION_CAPS</a> structure. The driver returns a pointer to this structure through its <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorcaps.md">GetVideoProcessorCaps</a> function. In addition, the attributes of a frame-rate conversion capability group can be queried by calling the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorrateconversioncaps.md">GetVideoProcessorRateConversionCaps</a> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorrateconversioncaps.md">GetVideoProcessorRateConversionCaps</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorcaps.md">GetVideoProcessorCaps</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessorenum.md">CreateVideoProcessorEnum</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_processor_caps.md">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a>