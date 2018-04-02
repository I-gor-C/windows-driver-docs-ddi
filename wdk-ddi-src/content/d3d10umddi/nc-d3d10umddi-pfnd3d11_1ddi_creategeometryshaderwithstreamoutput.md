---
UID: NC:d3d10umddi.PFND3D11_1DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT
title: PFND3D11_1DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT
author: windows-driver-content
description: Creates a geometry shader with stream output.
old-location: display\creategeometryshaderwithstreamoutput_d3d11_1_.htm
old-project: display
ms.assetid: 1d06ef38-4eb9-4129-b409-74bbd1951f92
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateGeometryShaderWithStreamOutput(D3D11_1), CreateGeometryShaderWithStreamOutput(D3D11_1) callback function [Display Devices], PFND3D11_1DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT, d3d10umddi/CreateGeometryShaderWithStreamOutput(D3D11_1), display.creategeometryshaderwithstreamoutput_d3d11_1_, display.pfncreategeometryshaderwithstreamoutput
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
-	CreateGeometryShaderWithStreamOutput(D3D11_1)
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT callback function
Creates a geometry shader with stream output.

## Syntax

```
PFND3D11_1DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT Pfnd3d111DdiCreategeometryshaderwithstreamoutput;

void Pfnd3d111DdiCreategeometryshaderwithstreamoutput(
   D3D10DDI_HDEVICE,
  CONST D3D11DDIARG_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT *,
   D3D10DDI_HSHADER,
   D3D10DDI_HRTSHADER,
  CONST D3D11_1DDIARG_STAGE_IO_SIGNATURES *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HSHADER`



`D3D10DDI_HRTSHADER`



`*`




## Return Value

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/316e30b9-eb06-483c-a124-476b4308cf5f">CalcPrivateGeometryShaderWithStreamOutput(D3D11_1)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542057">D3D11DDIARG_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh406324">D3D11_1DDIARG_STAGE_IO_SIGNATURES</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>