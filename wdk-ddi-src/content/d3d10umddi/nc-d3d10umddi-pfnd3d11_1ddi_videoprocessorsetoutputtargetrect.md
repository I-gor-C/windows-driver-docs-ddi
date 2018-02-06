---
UID: NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTTARGETRECT
title: PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTTARGETRECT
author: windows-driver-content
description: Sets the target rectangle for the video processor.
old-location: display\videoprocessorsetoutputtargetrect.htm
old-project: display
ms.assetid: ac1ba2e0-a289-4dee-b739-d3c1ad0970e1
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.videoprocessorsetoutputtargetrect, pfnVideoProcessorSetOutputTargetRect callback function [Display Devices], pfnVideoProcessorSetOutputTargetRect, PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTTARGETRECT, PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTTARGETRECT, d3d10umddi/pfnVideoProcessorSetOutputTargetRect
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
-	pfnVideoProcessorSetOutputTargetRect
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTTARGETRECT callback function
Sets the target rectangle for the video processor.

## Syntax

```
PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTTARGETRECT Pfnd3d111DdiVideoprocessorsetoutputtargetrect;

void Pfnd3d111DdiVideoprocessorsetoutputtargetrect(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSOR,
   BOOL,
  CONST RECT *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSOR`



`BOOL`



`*`




## Return Value

This callback function does not return a value.

## Remarks

The target rectangle is the area within the destination surface where the output will be drawn. The target rectangle is given in pixel coordinates, relative to the destination surface.



If this function is never called, or if the <i>Enable</i> parameter is FALSE, the video processor writes to the entire destination surface.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessor.md">CreateVideoProcessor</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTTARGETRECT callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>