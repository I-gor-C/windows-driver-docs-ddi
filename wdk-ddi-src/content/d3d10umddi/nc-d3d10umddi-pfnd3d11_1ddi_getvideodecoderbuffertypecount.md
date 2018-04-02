---
UID: NC:d3d10umddi.PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT
title: PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT
author: windows-driver-content
description: Queries the number of buffer types that the display miniport driver requires to perform a specified decode operation.
old-location: display\getvideodecoderbuffertypecount.htm
old-project: display
ms.assetid: 3528ac03-55cf-4e02-ae42-69b736684147
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT, d3d10umddi/pfnGetVideoDecoderBufferTypeCount, display.getvideodecoderbuffertypecount, pfnGetVideoDecoderBufferTypeCount, pfnGetVideoDecoderBufferTypeCount callback function [Display Devices]
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
-	pfnGetVideoDecoderBufferTypeCount
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT callback function
Queries the number of buffer types that the display miniport driver requires to perform a specified decode operation.

## Syntax

```
PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT Pfnd3d111DdiGetvideodecoderbuffertypecount;

void Pfnd3d111DdiGetvideodecoderbuffertypecount(
   D3D10DDI_HDEVICE,
  CONST D3D11_1DDI_VIDEO_DECODER_DESC *,
  UINT *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`*`




## Return Value

This callback function does not return a value.

## Remarks

The Microsoft Direct3D runtime verifies that the <i>pDecodeDesc</i>  parameter data is valid before it calls the <b>GetVideoDecoderBufferTypeCount</b> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh450951">D3D11_1DDI_VIDEO_DECODER_DESC</a>