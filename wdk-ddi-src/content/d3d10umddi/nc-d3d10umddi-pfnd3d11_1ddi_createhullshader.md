---
UID : NC:d3d10umddi.PFND3D11_1DDI_CREATEHULLSHADER
title : PFND3D11_1DDI_CREATEHULLSHADER
author : windows-driver-content
description : Creates a hull shader.
old-location : display\createhullshader_d3d11_1_.htm
old-project : display
ms.assetid : 5461f9d4-5eff-4ff7-9eeb-cf94bc243dba
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.createhullshader_d3d11_1_, CreateHullShader(D3D11_1) callback function [Display Devices], CreateHullShader(D3D11_1), PFND3D11_1DDI_CREATEHULLSHADER, PFND3D11_1DDI_CREATEHULLSHADER, d3d10umddi/CreateHullShader(D3D11_1), display.pfncreatehullshader
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



`D3D10DDI_HSHADER`



`D3D10DDI_HRTSHADER`



`*`




## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddiarg_tessellation_io_signatures.md">D3D11_1DDIARG_TESSELLATION_IO_SIGNATURES</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_calcprivatetessellationshadersize.md">CalcPrivateTessellationShaderSize(D3D11_1)</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_CREATEHULLSHADER callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>