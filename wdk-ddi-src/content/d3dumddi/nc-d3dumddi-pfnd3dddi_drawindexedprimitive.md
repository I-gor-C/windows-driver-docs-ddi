---
UID: NC:d3dumddi.PFND3DDDI_DRAWINDEXEDPRIMITIVE
title: PFND3DDDI_DRAWINDEXEDPRIMITIVE
author: windows-driver-content
description: The DrawIndexedPrimitive function draws indexed primitives that the Microsoft Direct3D runtime has not transformed the index data in.
old-location: display\drawindexedprimitive.htm
old-project: display
ms.assetid: 12bb6274-d042-43bb-b9f5-1417f42da729
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DrawIndexedPrimitive, DrawIndexedPrimitive callback function [Display Devices], PFND3DDDI_DRAWINDEXEDPRIMITIVE, UserModeDisplayDriver_Functions_427fa7b5-5b52-4314-b097-aea6d27cb535.xml, d3dumddi/DrawIndexedPrimitive, display.drawindexedprimitive
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
-	DrawIndexedPrimitive
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_DRAWINDEXEDPRIMITIVE callback function
The <b>DrawIndexedPrimitive</b> function draws indexed primitives that the Microsoft Direct3D runtime has not transformed the index data in.

## Syntax

```
PFND3DDDI_DRAWINDEXEDPRIMITIVE Pfnd3dddiDrawindexedprimitive;

HRESULT Pfnd3dddiDrawindexedprimitive(
  HANDLE hDevice,
  CONST D3DDDIARG_DRAWINDEXEDPRIMITIVE *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<b>DrawIndexedPrimitive</b> returns S_OK or an appropriate error result if the indexed primitive is not successfully drawn.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_drawindexedprimitive.md">D3DDDIARG_DRAWINDEXEDPRIMITIVE</a>



<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>



<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_drawindexedprimitive2.md">DrawIndexedPrimitive2</a>