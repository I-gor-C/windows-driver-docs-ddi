---
UID: NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT
title: PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT
author: windows-driver-content
description: Sets the destination rectangle for an input stream on the video processor.
old-location: display\videoprocessorsetstreamdestrect.htm
old-project: display
ms.assetid: 84AD6C4F-A674-4CCC-B2E9-378E3E55EEF3
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT, d3d10umddi/pfnVideoProcessorSetStreamDestRect, display.videoprocessorsetstreamdestrect, pfnVideoProcessorSetStreamDestRect, pfnVideoProcessorSetStreamDestRect callback function [Display Devices]
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
-	pfnVideoProcessorSetStreamDestRect
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT callback function
Sets the destination rectangle for an input stream on the video processor.

## Syntax

```
PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT Pfnd3d111DdiVideoprocessorsetstreamdestrect;

void Pfnd3d111DdiVideoprocessorsetstreamdestrect(
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

The destination rectangle is the portion of the output surface that receives the bit-block transfer (bitblt) for the specified input stream. The destination rectangle is given in pixel coordinates, relative to the output surface.

The default destination rectangle is an empty rectangle (0, 0, 0, 0). If the <i>VideoProcessorSetStreamDestRect</i> function is never called, or if the <i>Enable</i> parameter is <b>FALSE</b>, no data is written from the specified input stream.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>



<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_dxvahd_createvideoprocessor.md">CreateVideoProcessor</a>