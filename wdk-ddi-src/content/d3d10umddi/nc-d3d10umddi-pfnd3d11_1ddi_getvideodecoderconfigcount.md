---
UID: NC:d3d10umddi.PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT
title: PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT
author: windows-driver-content
description: Queries the number of video decoder configurations that are supported by the display miniport driver for the specified decoder operation.
old-location: display\getvideodecoderconfigcount.htm
old-project: display
ms.assetid: 5b4cc185-8579-4c13-932f-23065697c4ee
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT, d3d10umddi/pfnGetVideoDecoderConfigCount, display.getvideodecoderconfigcount, pfnGetVideoDecoderConfigCount, pfnGetVideoDecoderConfigCount callback function [Display Devices]
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
-	pfnGetVideoDecoderConfigCount
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT callback function
Queries the number of video decoder configurations that are supported by the display miniport driver for the specified decoder operation.

## Syntax

```
PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT Pfnd3d111DdiGetvideodecoderconfigcount;

void Pfnd3d111DdiGetvideodecoderconfigcount(
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

The Microsoft Direct3D runtime verifies that the <i>pDecodeDesc</i>  parameter data is valid before it calls the <b>GetVideoDecoderConfigCount</b> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh450951">D3D11_1DDI_VIDEO_DECODER_DESC</a>