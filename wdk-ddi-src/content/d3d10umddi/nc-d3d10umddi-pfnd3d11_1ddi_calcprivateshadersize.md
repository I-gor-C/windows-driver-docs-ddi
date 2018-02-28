---
UID: NC:d3d10umddi.PFND3D11_1DDI_CALCPRIVATESHADERSIZE
title: PFND3D11_1DDI_CALCPRIVATESHADERSIZE
author: windows-driver-content
description: Determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a shader.
old-location: display\calcprivateshadersize_d3d11_1_.htm
old-project: display
ms.assetid: e23c267f-41df-47a6-ae43-3bbcb48fd300
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: CalcPrivateShaderSize(D3D11_1), CalcPrivateShaderSize(D3D11_1) callback function [Display Devices], PFND3D11_1DDI_CALCPRIVATESHADERSIZE, d3d10umddi/CalcPrivateShaderSize(D3D11_1), display.calcprivateshadersize_d3d11_1_, display.pfncalcprivateshadersize
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
-	CalcPrivateShaderSize(D3D11_1)
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_CALCPRIVATESHADERSIZE callback function
Determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a shader.

## Syntax

```
PFND3D11_1DDI_CALCPRIVATESHADERSIZE Pfnd3d111DdiCalcprivateshadersize;

SIZE_T Pfnd3d111DdiCalcprivateshadersize(
   D3D10DDI_HDEVICE,
  CONST UINT *pShaderCode,
  CONST D3D11_1DDIARG_STAGE_IO_SIGNATURES *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*pShaderCode`

A pointer to an array of CONST UINT tokens that make up the shader code.

`*`




## Return Value

The size of the memory region that the driver requires for creating a shader.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddiarg_stage_io_signatures.md">D3D11_1DDIARG_STAGE_IO_SIGNATURES</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_CALCPRIVATESHADERSIZE callback function%20 RELEASE:%20(2/24/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>