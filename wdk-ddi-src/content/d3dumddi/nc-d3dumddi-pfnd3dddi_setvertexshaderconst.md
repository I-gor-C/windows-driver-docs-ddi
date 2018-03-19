---
UID: NC:d3dumddi.PFND3DDDI_SETVERTEXSHADERCONST
title: PFND3DDDI_SETVERTEXSHADERCONST
author: windows-driver-content
description: The SetVertexShaderConst function sets one or more vertex shader constant registers with floating-point values.
old-location: display\setvertexshaderconst.htm
old-project: display
ms.assetid: 2dbde343-b10a-4357-a2b7-d6b1b1b868f2
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3DDDI_SETVERTEXSHADERCONST, SetVertexShaderConst, SetVertexShaderConst callback function [Display Devices], UserModeDisplayDriver_Functions_473fa267-d7f2-47b7-bae8-3430d89dd632.xml, d3dumddi/SetVertexShaderConst, display.setvertexshaderconst
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
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
-	d3dumddi.h
api_name:
-	SetVertexShaderConst
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_SETVERTEXSHADERCONST callback function
The <i>SetVertexShaderConst</i> function sets one or more vertex shader constant registers with floating-point values.

## Syntax

```
PFND3DDDI_SETVERTEXSHADERCONST Pfnd3dddiSetvertexshaderconst;

HRESULT Pfnd3dddiSetvertexshaderconst(
  HANDLE hDevice,
  CONST D3DDDIARG_SETVERTEXSHADERCONST *,
  CONST VOID *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`



`*`




## Return Value

<i>SetVertexShaderConst</i> returns S_OK or an appropriate error result if the vertex shader constant registers are not successfully set with floating-point values.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>



<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_setvertexshaderconst.md">D3DDDIARG_SETVERTEXSHADERCONST</a>