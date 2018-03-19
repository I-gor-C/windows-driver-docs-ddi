---
UID: NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT
title: PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT
author: windows-driver-content
description: Sets the source rectangle for an input stream on the video processor.
old-location: display\videoprocessorsetstreamsourcerect.htm
old-project: display
ms.assetid: 78d62117-260a-46ab-9daa-ee9dcfc7fc1f
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT, d3d10umddi/pfnVideoProcessorSetStreamSourceRect, display.videoprocessorsetstreamsourcerect, pfnVideoProcessorSetStreamSourceRect, pfnVideoProcessorSetStreamSourceRect callback function [Display Devices]
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
-	pfnVideoProcessorSetStreamSourceRect
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT callback function
Sets the source rectangle for an input stream on the video processor.

## Syntax

```
PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT Pfnd3d111DdiVideoprocessorsetstreamsourcerect;

void Pfnd3d111DdiVideoprocessorsetstreamsourcerect(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSOR,
   UINT,
   BOOL,
  CONST RECT *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSOR`



`UINT`



`BOOL`



`*`




## Return Value

This callback function does not return a value.

## Remarks

The source rectangle is the portion of the input surface from which the video processor performs a bit-block transfer (bitblt) to the destination surface. The source rectangle is given in pixel coordinates, relative to the input surface.



If the <b>VideoProcessorSetStreamSourceRect</b> function is never called, or if the <i>Enable</i> parameter is FALSE, the video processor reads from the entire input surface.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessor.md">CreateVideoProcessor</a>