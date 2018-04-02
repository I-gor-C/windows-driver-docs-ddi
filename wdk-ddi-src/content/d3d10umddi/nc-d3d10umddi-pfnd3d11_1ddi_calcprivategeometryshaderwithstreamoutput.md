---
UID: NC:d3d10umddi.PFND3D11_1DDI_CALCPRIVATEGEOMETRYSHADERWITHSTREAMOUTPUT
title: PFND3D11_1DDI_CALCPRIVATEGEOMETRYSHADERWITHSTREAMOUTPUT
author: windows-driver-content
description: Determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a geometry shader with stream output.
old-location: display\calcprivategeometryshaderwithstreamoutput_d3d11_1_.htm
old-project: display
ms.assetid: 316e30b9-eb06-483c-a124-476b4308cf5f
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CalcPrivateGeometryShaderWithStreamOutput(D3D11_1), CalcPrivateGeometryShaderWithStreamOutput(D3D11_1) callback function [Display Devices], PFND3D11_1DDI_CALCPRIVATEGEOMETRYSHADERWITHSTREAMOUTPUT, d3d10umddi/CalcPrivateGeometryShaderWithStreamOutput(D3D11_1), display.calcprivategeometryshaderwithstreamoutput_d3d11_1_, display.pfncalcprivategeometryshaderwithstreamoutput
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
-	CalcPrivateGeometryShaderWithStreamOutput(D3D11_1)
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_CALCPRIVATEGEOMETRYSHADERWITHSTREAMOUTPUT callback function
Determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a geometry shader with stream output.

## Syntax

```
PFND3D11_1DDI_CALCPRIVATEGEOMETRYSHADERWITHSTREAMOUTPUT Pfnd3d111DdiCalcprivategeometryshaderwithstreamoutput;

SIZE_T Pfnd3d111DdiCalcprivategeometryshaderwithstreamoutput(
   D3D10DDI_HDEVICE,
  CONST D3D11DDIARG_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT *,
  CONST D3D11_1DDIARG_STAGE_IO_SIGNATURES *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`*`




## Return Value

The size of the memory region that the driver requires to create a geometry shader with stream output.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542057">D3D11DDIARG_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh406324">D3D11_1DDIARG_STAGE_IO_SIGNATURES</a>