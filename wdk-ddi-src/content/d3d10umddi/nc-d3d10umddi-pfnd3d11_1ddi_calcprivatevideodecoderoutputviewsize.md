---
UID: NC:d3d10umddi.PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE
title: PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE
author: windows-driver-content
description: Returns the number of bytes that the driver requires to store private data for the video decoder view state.
old-location: display\calcprivatevideodecoderoutputviewsize.htm
old-project: display
ms.assetid: d8daa501-13cf-4fba-ab98-b1a2d0325ce1
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: CalcPrivateVideoDecoderOutputViewSize, CalcPrivateVideoDecoderOutputViewSize callback function [Display Devices], PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE, d3d10umddi/CalcPrivateVideoDecoderOutputViewSize, display.calcprivatevideodecoderoutputviewsize
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
-	CalcPrivateVideoDecoderOutputViewSize
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE callback function
Returns the number of bytes that the driver requires to store private data for the video decoder view state.

## Syntax

```
PFND3D11_1DDI_CALCPRIVATEVIDEODECODEROUTPUTVIEWSIZE Pfnd3d111DdiCalcprivatevideodecoderoutputviewsize;

SIZE_T Pfnd3d111DdiCalcprivatevideodecoderoutputviewsize(
   D3D10DDI_HDEVICE,
  CONST D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

The required number of bytes for the video decoder view state.

## Remarks

The runtime will validate the members of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddiarg_createvideodecoderoutputview.md">D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW</a> structure before it calls this function.

This function is not expected to fail.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddiarg_createvideodecoderoutputview.md">D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW</a>