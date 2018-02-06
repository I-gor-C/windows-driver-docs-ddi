---
UID: NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT
title: PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT
author: windows-driver-content
description: Sets the destination rectangle for an input stream on the video processor.
old-location: display\videoprocessorsetstreamdestrect.htm
old-project: display
ms.assetid: 84AD6C4F-A674-4CCC-B2E9-378E3E55EEF3
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.videoprocessorsetstreamdestrect, pfnVideoProcessorSetStreamDestRect callback function [Display Devices], pfnVideoProcessorSetStreamDestRect, PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT, PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT, d3d10umddi/pfnVideoProcessorSetStreamDestRect
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
-	pfnVideoProcessorSetStreamDestRect
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
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
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_dxvahd_createvideoprocessor.md">CreateVideoProcessor</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>