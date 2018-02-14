---
UID: NC:d3dumddi.PFND3DDDI_SETPIXELSHADERCONST
title: PFND3DDDI_SETPIXELSHADERCONST
author: windows-driver-content
description: The SetPixelShaderConst function sets one or more pixel shader constant registers with floating-point values.
old-location: display\setpixelshaderconst.htm
old-project: display
ms.assetid: 02710936-28df-4c8f-aa1e-bdff01155608
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.setpixelshaderconst, SetPixelShaderConst callback function [Display Devices], SetPixelShaderConst, PFND3DDDI_SETPIXELSHADERCONST, PFND3DDDI_SETPIXELSHADERCONST, d3dumddi/SetPixelShaderConst, UserModeDisplayDriver_Functions_be972851-58a6-4f22-aae2-7948679b8bb7.xml
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	d3dumddi.h
apiname:
-	SetPixelShaderConst
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_SETPIXELSHADERCONST callback function
The <i>SetPixelShaderConst</i> function sets one or more pixel shader constant registers with floating-point values.

## Syntax

```
PFND3DDDI_SETPIXELSHADERCONST Pfnd3dddiSetpixelshaderconst;

HRESULT Pfnd3dddiSetpixelshaderconst(
  HANDLE hDevice,
  CONST D3DDDIARG_SETPIXELSHADERCONST *,
  CONST FLOAT *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`



`*`




## Return Value

<i>SetPixelShaderConst</i> returns S_OK or an appropriate error result if the pixel shader constant registers are not successfully set with floating-point values.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>



<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_setpixelshaderconst.md">D3DDDIARG_SETPIXELSHADERCONST</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETPIXELSHADERCONST callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>