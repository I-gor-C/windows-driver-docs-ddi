---
UID: NC:d3d10umddi.PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE
title: PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE
author: windows-driver-content
description: Returns the number of bytes that the driver requires to store private data for the video processor state.
old-location: display\calcprivatevideoprocessorsize.htm
old-project: display
ms.assetid: a30d98b2-3d39-456a-8363-44ccc71e58ff
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CalcPrivateVideoProcessorSize, CalcPrivateVideoProcessorSize callback function [Display Devices], PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE, d3d10umddi/CalcPrivateVideoProcessorSize, display.calcprivatevideoprocessorsize
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
-	CalcPrivateVideoProcessorSize
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE callback function
Returns the number of bytes that the driver requires to store private data for the video processor state.

## Syntax

```
PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE Pfnd3d111DdiCalcprivatevideoprocessorsize;

SIZE_T Pfnd3d111DdiCalcprivatevideoprocessorsize(
   D3D10DDI_HDEVICE,
  CONST D3D11_1DDIARG_CREATEVIDEOPROCESSOR *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

The required number of bytes for the video processor state.

## Remarks

This function is not expected to fail.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406320">D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW</a>