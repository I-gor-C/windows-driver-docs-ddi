---
UID : NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE
title : PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE
author : windows-driver-content
description : Sets the alpha fill mode for data that the video processor writes to the render target.
old-location : display\videoprocessorsetoutputalphafillmode.htm
old-project : display
ms.assetid : 0c2cbb8f-d031-4267-b32f-620ed1ad065c
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.videoprocessorsetoutputalphafillmode, pfnVideoProcessorSetOutputAlphaFillMode callback function [Display Devices], pfnVideoProcessorSetOutputAlphaFillMode, PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE, PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE, d3d10umddi/pfnVideoProcessorSetOutputAlphaFillMode
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
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
req.typenames : "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE callback function
Sets the alpha fill mode for data that the video processor writes to the render target.

## Syntax

```
PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE Pfnd3d111DdiVideoprocessorsetoutputalphafillmode;

void Pfnd3d111DdiVideoprocessorsetoutputalphafillmode(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSOR,
   D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE,
   UINT
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSOR`



`D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE`



`UINT`




## Return Value

This callback function does not return a value.

## Remarks

The driver reports its ability to support alpha fill modes in the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_processor_caps.md">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a> structure that is returned through the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorcaps.md">GetVideoProcessorCaps</a> function. If the driver supports the <b>D3D11_1DDI_VIDEO_PROCESSOR_FEATURE_CAPS_ALPHA_FILL</b> capability, it supports all of the alpha fill modes that are defined by the <a href="..\d3d10umddi\ne-d3d10umddi-d3d11_1ddi_video_processor_alpha_fill_mode.md">D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE</a> enumeration. Otherwise, the <i>FillMode</i> parameter must be set to <b>D3D11_VIDEO_PROCESSOR_ALPHA_FILL_MODE_OPAQUE</b>. 


<div class="alert"><b>Note</b>  If the driver does not support the <b>D3D11_1DDI_VIDEO_PROCESSOR_FEATURE_CAPS_ALPHA_FILL</b> capability, the Microsoft Direct3D runtime does not call the <b>VideoProcessorSetOutputAlphaFillMode</b> function.</div><div> </div>The default fill mode is <b>D3D11_VIDEO_PROCESSOR_ALPHA_FILL_MODE_OPAQUE</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessor.md">CreateVideoProcessor</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorcaps.md">GetVideoProcessorCaps</a>

<a href="..\d3d10umddi\ne-d3d10umddi-d3d11_1ddi_video_processor_alpha_fill_mode.md">D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_processor_caps.md">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessorinputview.md">CreateVideoProcessorInputView</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>