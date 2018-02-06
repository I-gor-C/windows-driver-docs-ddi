---
UID: NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPIXELASPECTRATIO
title: PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPIXELASPECTRATIO
author: windows-driver-content
description: Sets the pixel aspect ratio for an input stream on the video processor.
old-location: display\videoprocessorsetstreampixelaspectratio.htm
old-project: display
ms.assetid: fe472b54-09f5-4689-a3d1-0985dafa7d4b
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.videoprocessorsetstreampixelaspectratio, pfnVideoProcessorSetStreamPixelAspectRatio callback function [Display Devices], pfnVideoProcessorSetStreamPixelAspectRatio, PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPIXELASPECTRATIO, PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPIXELASPECTRATIO, d3d10umddi/pfnVideoProcessorSetStreamPixelAspectRatio
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
-	pfnVideoProcessorSetStreamPixelAspectRatio
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPIXELASPECTRATIO callback function
Sets the pixel aspect ratio for an input stream on the video processor.

## Syntax

```
PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPIXELASPECTRATIO Pfnd3d111DdiVideoprocessorsetstreampixelaspectratio;

void Pfnd3d111DdiVideoprocessorsetstreampixelaspectratio(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSOR,
   UINT,
   BOOL,
  CONST DXGI_RATIONAL *,
  CONST DXGI_RATIONAL *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSOR`



`UINT`



`BOOL`



`*`



`*`




## Return Value

This callback function does not return a value.

## Remarks

Pixel aspect ratios of the form 0/<i>n</i> and <i>n</i>/0 are not valid.



The default pixel aspect ratio is 1:1 (square pixels).



The driver reports its ability to support the pixel aspect ratio capability in the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_processor_caps.md">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a> structure that is returned through the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorcaps.md">GetVideoProcessorCaps</a> function. If the driver supports the <b>D3D11_1DDI_VIDEO_PROCESSOR_FEATURE_CAPS_PIXEL_ASPECT_RATIO </b> capability, the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamalpha.md">VideoProcessorSetStreamAlpha</a> can be called to set the pixel aspect ratios for an input stream of the video processor.
<div class="alert"><b>Note</b>  If the driver does not support the <b>D3D11_1DDI_VIDEO_PROCESSOR_FEATURE_CAPS_PIXEL_ASPECT_RATIO </b> capability, the Microsoft Direct3D runtime does not call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamalpha.md">VideoProcessorSetStreamAlpha</a> function.</div><div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessor.md">CreateVideoProcessor</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorcaps.md">GetVideoProcessorCaps</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_processor_caps.md">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPIXELASPECTRATIO callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>