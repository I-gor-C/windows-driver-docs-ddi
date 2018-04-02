---
UID: NC:d3d10umddi.PFND3D11_1DDI_CREATEHULLSHADER
title: PFND3D11_1DDI_CREATEHULLSHADER
author: windows-driver-content
description: Creates a hull shader.
old-location: display\createhullshader_d3d11_1_.htm
old-project: display
ms.assetid: 5461f9d4-5eff-4ff7-9eeb-cf94bc243dba
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateHullShader(D3D11_1), CreateHullShader(D3D11_1) callback function [Display Devices], PFND3D11_1DDI_CREATEHULLSHADER, d3d10umddi/CreateHullShader(D3D11_1), display.createhullshader_d3d11_1_, display.pfncreatehullshader
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
-	CreateHullShader(D3D11_1)
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_CREATEHULLSHADER callback function
Creates a hull shader.

## Syntax

```
PFND3D11_1DDI_CREATEHULLSHADER Pfnd3d111DdiCreatehullshader;

void Pfnd3d111DdiCreatehullshader(
   D3D10DDI_HDEVICE,
  CONST UINT *pShaderCode,
   D3D10DDI_HSHADER,
   D3D10DDI_HRTSHADER,
  CONST D3D11_1DDIARG_TESSELLATION_IO_SIGNATURES *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*pShaderCode`

A pointer to an array of CONST UINT tokens that form the shader code. The first token in the shader code stream is always the version token. The next token in the stream is the length token that determines the end of the shader code stream. For more information about the format of Direct3D version 11.1 shader code, see the comments inside the D3d11tokenizedprogramformat.hpp header file that is included with the WDK.

`D3D10DDI_HSHADER`



`D3D10DDI_HRTSHADER`



`*`




## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/606b50c0-4070-4694-9299-f20e28743958">CalcPrivateTessellationShaderSize(D3D11_1)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh406326">D3D11_1DDIARG_TESSELLATION_IO_SIGNATURES</a>