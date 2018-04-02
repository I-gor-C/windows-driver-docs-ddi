---
UID: NC:d3dumddi.PFND3DDDI_DRAWINDEXEDPRIMITIVE2
title: PFND3DDDI_DRAWINDEXEDPRIMITIVE2
author: windows-driver-content
description: The DrawIndexedPrimitive2 function draws indexed primitives that the Microsoft Direct3D runtime has transformed the index data in.
old-location: display\drawindexedprimitive2.htm
old-project: display
ms.assetid: f12af70c-a6f2-42da-be62-1cfeb90b6239
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DrawIndexedPrimitive2, DrawIndexedPrimitive2 callback function [Display Devices], PFND3DDDI_DRAWINDEXEDPRIMITIVE2, UserModeDisplayDriver_Functions_55bb1ac5-49e3-428b-9737-ffe0577e6bba.xml, d3dumddi/DrawIndexedPrimitive2, display.drawindexedprimitive2
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
-	DrawIndexedPrimitive2
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_DRAWINDEXEDPRIMITIVE2 callback function
The <b>DrawIndexedPrimitive2</b> function draws indexed primitives that the Microsoft Direct3D runtime has transformed the index data in.

## Syntax

```
PFND3DDDI_DRAWINDEXEDPRIMITIVE2 Pfnd3dddiDrawindexedprimitive2;

HRESULT Pfnd3dddiDrawindexedprimitive2(
  HANDLE hDevice,
  CONST D3DDDIARG_DRAWINDEXEDPRIMITIVE2 *,
   UINT,
  CONST VOID *,
  CONST UINT *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`



`UINT`



`*`



`*`




## Return Value

<b>DrawIndexedPrimitive2</b> returns S_OK or an appropriate error result if the primitive is not successfully drawn.

## Remarks

Stream zero contains transform indices and is the only stream that should be accessed. 

When the Microsoft Direct3D runtime specifies triangle-edge flags in the value that the <i>pFlagBuffer</i> parameter points to, the runtime also specifies to draw only one triangle (that is, the runtime specifies the D3DPT_TRIANGLELIST value in the <b>PrimitiveType</b> member and 0x00000001 in the <b>PrimitiveCount</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543054">D3DDDIARG_DRAWINDEXEDPRIMITIVE2</a> structure that the <i>pData</i> parameter points to).

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543054">D3DDDIARG_DRAWINDEXEDPRIMITIVE2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/12bb6274-d042-43bb-b9f5-1417f42da729">DrawIndexedPrimitive</a>