---
UID: NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT
title: PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT
author: windows-driver-content
description: Sets the source rectangle for an input stream on the video processor.
old-location: display\videoprocessorsetstreamsourcerect.htm
old-project: display
ms.assetid: 78d62117-260a-46ab-9daa-ee9dcfc7fc1f
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: display.videoprocessorsetstreamsourcerect, pfnVideoProcessorSetStreamSourceRect callback function [Display Devices], pfnVideoProcessorSetStreamSourceRect, PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT, PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT, d3d10umddi/pfnVideoProcessorSetStreamSourceRect
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
-	pfnVideoProcessorSetStreamSourceRect
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
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

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessor.md">CreateVideoProcessor</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT callback function%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>