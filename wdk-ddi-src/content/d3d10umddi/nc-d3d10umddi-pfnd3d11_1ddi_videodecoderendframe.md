---
UID : NC:d3d10umddi.PFND3D11_1DDI_VIDEODECODERENDFRAME
title : PFND3D11_1DDI_VIDEODECODERENDFRAME
author : windows-driver-content
description : Completes a DirectX Video Acceleration (DXVA) decoding operation for a video frame.
old-location : display\videodecoderendframe.htm
old-project : display
ms.assetid : f0110435-d060-4f4b-ad29-baaeb8fc2e0e
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.videodecoderendframe, pfnVideoDecoderEndFrame callback function [Display Devices], pfnVideoDecoderEndFrame, PFND3D11_1DDI_VIDEODECODERENDFRAME, PFND3D11_1DDI_VIDEODECODERENDFRAME, d3d10umddi/pfnVideoDecoderEndFrame
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


# PFND3D11_1DDI_VIDEODECODERENDFRAME callback function
Completes a DirectX Video Acceleration (DXVA) decoding operation for a video frame.

## Syntax

```
PFND3D11_1DDI_VIDEODECODERENDFRAME Pfnd3d111DdiVideodecoderendframe;

void Pfnd3d111DdiVideodecoderendframe(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HDECODE
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HDECODE`




## Return Value

This callback function does not return a value.

## Remarks

The <b>VideoDecoderEndFrame</b> completes the decoding operation that was started when the Microsoft Direct3D runtime called <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_videodecoderbeginframe.md">VideoDecoderBeginFrame</a>. <b>VideoDecoderEndFrame</b> signals to the driver that all video data has been submitted for the video frame.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_videodecoderbeginframe.md">VideoDecoderBeginFrame</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideodecoder.md">CreateVideoDecoder</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_VIDEODECODERENDFRAME callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>