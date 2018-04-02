---
UID: NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE
title: PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE
author: windows-driver-content
description: Sets the alpha fill mode for data that the video processor writes to the render target.
old-location: display\videoprocessorsetoutputalphafillmode.htm
old-project: display
ms.assetid: 0c2cbb8f-d031-4267-b32f-620ed1ad065c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE, d3d10umddi/pfnVideoProcessorSetOutputAlphaFillMode, display.videoprocessorsetoutputalphafillmode, pfnVideoProcessorSetOutputAlphaFillMode, pfnVideoProcessorSetOutputAlphaFillMode callback function [Display Devices]
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
-	pfnVideoProcessorSetOutputAlphaFillMode
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
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

The driver reports its ability to support alpha fill modes in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450968">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a> structure that is returned through the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451674">GetVideoProcessorCaps</a> function. If the driver supports the <b>D3D11_1DDI_VIDEO_PROCESSOR_FEATURE_CAPS_ALPHA_FILL</b> capability, it supports all of the alpha fill modes that are defined by the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450963">D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE</a> enumeration. Otherwise, the <i>FillMode</i> parameter must be set to <b>D3D11_VIDEO_PROCESSOR_ALPHA_FILL_MODE_OPAQUE</b>. 



<div class="alert"><b>Note</b>  If the driver does not support the <b>D3D11_1DDI_VIDEO_PROCESSOR_FEATURE_CAPS_ALPHA_FILL</b> capability, the Microsoft Direct3D runtime does not call the <b>VideoProcessorSetOutputAlphaFillMode</b> function.</div>
<div> </div>
The default fill mode is <b>D3D11_VIDEO_PROCESSOR_ALPHA_FILL_MODE_OPAQUE</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/741045a2-0a91-490a-907d-5f4900a4a0ae">CreateVideoProcessor</a>



<a href="https://msdn.microsoft.com/f3942c53-e366-41c5-9f43-d093fa6b6ed6">CreateVideoProcessorInputView</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh450963">D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh450968">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451674">GetVideoProcessorCaps</a>