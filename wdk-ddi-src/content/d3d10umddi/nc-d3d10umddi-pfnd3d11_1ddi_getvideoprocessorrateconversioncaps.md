---
UID: NC:d3d10umddi.PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS
title: PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS
author: windows-driver-content
description: Queries a specified group of video processing capabilities that are associated with frame-rate conversion, including deinterlacing and inverse telecine.
old-location: display\getvideoprocessorrateconversioncaps.htm
old-project: display
ms.assetid: c77b722f-e023-4e3e-9dff-616d0ab0a6a2
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.getvideoprocessorrateconversioncaps, pfnGetVideoProcessorRateConversionCaps callback function [Display Devices], pfnGetVideoProcessorRateConversionCaps, PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS, PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS, d3d10umddi/pfnGetVideoProcessorRateConversionCaps
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	D3d10umddi.h
apiname:
-	pfnGetVideoProcessorRateConversionCaps
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS callback function
Queries a specified group of video processing capabilities that are associated with frame-rate conversion, including deinterlacing and inverse telecine.

## Syntax

```
PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS Pfnd3d111DdiGetvideoprocessorrateconversioncaps;

void Pfnd3d111DdiGetvideoprocessorrateconversioncaps(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSORENUM,
   UINT,
  D3D11_1DDI_VIDEO_PROCESSOR_RATE_CONVERSION_CAPS *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSORENUM`



`UINT`



`*`




## Return Value

This callback function does not return a value.

## Remarks

The display miniport driver returns the maximum number of frame-rate conversion capabilities that it supports through the <b>RateConversionCapsCount</b> member of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_processor_caps.md">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a> structure. The driver returns a pointer to this structure through its <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorcaps.md">GetVideoProcessorCaps</a> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessorenum.md">CreateVideoProcessorEnum</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorcaps.md">GetVideoProcessorCaps</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_processor_caps.md">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>