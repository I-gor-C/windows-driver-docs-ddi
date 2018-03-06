---
UID: NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCONSTRICTION
title: PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCONSTRICTION
author: windows-driver-content
description: Sets the amount of downsampling to perform on the output.
old-location: display\videoprocessorsetoutputconstriction.htm
old-project: display
ms.assetid: 4b34a76b-2e56-4656-9112-ad2e1d53525d
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCONSTRICTION, d3d10umddi/pfnVideoProcessorSetOutputConstriction, display.videoprocessorsetoutputconstriction, pfnVideoProcessorSetOutputConstriction, pfnVideoProcessorSetOutputConstriction callback function [Display Devices]
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
-	pfnVideoProcessorSetOutputConstriction
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCONSTRICTION callback function
Sets the amount of downsampling to perform on the output.

## Syntax

```
PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCONSTRICTION Pfnd3d111DdiVideoprocessorsetoutputconstriction;

void Pfnd3d111DdiVideoprocessorsetoutputconstriction(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSOR,
   BOOL,
   SIZE
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSOR`



`BOOL`



`SIZE`




## Return Value

This callback function does not return a value.

## Remarks

Downsampling is sometimes used to reduce the quality of premium content when other forms of content protection are not available. 

By default, downsampling is disabled.

If the <i>Enable</i> parameter is TRUE, the display miniport driver downsamples the composed image to the specified size, and then scales it back to the size of the target rectangle.



The width and height of the <i>ConstrictonSize</i> parameter must be greater than zero. If the size is larger than the target rectangle, downsampling does not occur.



The driver reports its ability to support downsampling through the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorcaps.md">GetVideoProcessorCaps</a> function. If the driver supports the <b>D3D11_1DDI_VIDEO_PROCESSOR_FEATURE_CAPS_CONSTRICTION</b> capability, it supports the ability to downsample the composed image.

<div class="alert"><b>Note</b>  If the driver does not support the <b>D3D11_1DDI_VIDEO_PROCESSOR_FEATURE_CAPS_CONSTRICTION</b> capability, the Microsoft Direct3D runtime does not call the <b>VideoProcessorSetOutputConstriction</b> function.</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessor.md">CreateVideoProcessor</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCONSTRICTION callback function%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>