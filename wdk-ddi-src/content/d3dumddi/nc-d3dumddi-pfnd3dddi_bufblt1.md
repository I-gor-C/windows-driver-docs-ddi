---
UID: NC:d3dumddi.PFND3DDDI_BUFBLT1
title: PFND3DDDI_BUFBLT1
author: windows-driver-content
description: Performs a bit-block transfer (bitblt) operation from a source vertex or index buffer to a destination vertex or index buffer. Implemented by Windows Display Driver Model (WDDM) 1.2 or later user-mode display drivers.
old-location: display\bufblt1.htm
old-project: display
ms.assetid: 92F2AED7-935F-4E3E-934F-D6DF9AA87495
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: BufBlt1, BufBlt1 callback function [Display Devices], PFND3DDDI_BUFBLT1, d3dumddi/BufBlt1, display.bufblt1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
-	d3dumddi.h
api_name:
-	BufBlt1
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_BUFBLT1 callback function
Performs a bit-block transfer (bitblt) operation from a source vertex or index buffer to a destination vertex or index buffer. Implemented by Windows Display Driver Model (WDDM) 1.2 or later user-mode display drivers.

## Syntax

```
PFND3DDDI_BUFBLT1 Pfnd3dddiBufblt1;

HRESULT Pfnd3dddiBufblt1(
  HANDLE hDevice,
  CONST D3DDDIARG_BUFFERBLT1 *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

Returns S_OK or an appropriate error result if the buffer bitblt operation is not successfully performed.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451069">D3DDDIARG_BUFFERBLT1</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>