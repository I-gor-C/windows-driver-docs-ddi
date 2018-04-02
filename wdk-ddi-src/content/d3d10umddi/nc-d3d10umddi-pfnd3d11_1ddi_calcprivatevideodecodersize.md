---
UID: NC:d3d10umddi.PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE
title: PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE
author: windows-driver-content
description: Returns the number of bytes that the driver requires to store private data for the video decoder state.
old-location: display\calcprivatevideodecodersize.htm
old-project: display
ms.assetid: a878cba1-589e-4932-9d2b-1abab417660f
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CalcPrivateVideoDecoderSize, CalcPrivateVideoDecoderSize callback function [Display Devices], FND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE, d3d10umddi/CalcPrivateVideoDecoderSize, display.calcprivatevideodecodersize
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
-	CalcPrivateVideoDecoderSize
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE callback function
Returns the number of bytes that the driver requires to store private data for the video decoder state.

## Syntax

```
PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE Pfnd3d111DdiCalcprivatevideodecodersize;

SIZE_T Pfnd3d111DdiCalcprivatevideodecodersize(
   D3D10DDI_HDEVICE,
  CONST D3D11_1DDIARG_CREATEVIDEODECODER *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

The required number of bytes for the video decoder state.

## Remarks

The runtime will validate the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406310">D3D11_1DDIARG_CREATEVIDEODECODER</a> structure before it calls this function.

This function is not expected to fail.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406310">D3D11_1DDIARG_CREATEVIDEODECODER</a>