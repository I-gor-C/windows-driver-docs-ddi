---
UID: NC:d3d10umddi.PFND3D11_1DDI_GETVIDEODECODERBUFFERINFO
title: PFND3D11_1DDI_GETVIDEODECODERBUFFERINFO
author: windows-driver-content
description: Queries the description of a video decoder buffer for a specified video operation.
old-location: display\getvideodecoderbufferinfo.htm
old-project: display
ms.assetid: f129ae04-da7f-4681-a266-ac13317a895d
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D11_1DDI_GETVIDEODECODERBUFFERINFO, d3d10umddi/pfnGetVideoDecoderBufferInfo, display.getvideodecoderbufferinfo, pfnGetVideoDecoderBufferInfo, pfnGetVideoDecoderBufferInfo callback function [Display Devices]
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
-	pfnGetVideoDecoderBufferInfo
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_GETVIDEODECODERBUFFERINFO callback function
Queries the description of a video decoder buffer for a specified video operation.

## Syntax

```
PFND3D11_1DDI_GETVIDEODECODERBUFFERINFO Pfnd3d111DdiGetvideodecoderbufferinfo;

void Pfnd3d111DdiGetvideodecoderbufferinfo(
   D3D10DDI_HDEVICE,
  CONST D3D11_1DDI_VIDEO_DECODER_DESC *,
   UINT,
  D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`UINT`



`*`




## Return Value

This callback function does not return a value.

## Remarks

The Microsoft Direct3D runtime verifies that the <i>pDecodeDesc</i>  and <i>Index</i> parameter data is valid before it calls the <b>GetVideoDecoderBufferInfo</b> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_getvideodecoderbuffertypecount.md">GetVideoDecoderBufferTypeCount</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_decoder_desc.md">D3D11_1DDI_VIDEO_DECODER_DESC</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_decoder_buffer_info.md">D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO</a>