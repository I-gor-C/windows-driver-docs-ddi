---
UID: NC:d3dumddi.PFND3DDDI_SETSTREAMSOURCEUM
title: PFND3DDDI_SETSTREAMSOURCEUM
author: windows-driver-content
description: The SetStreamSourceUM function binds a vertex stream source to a user memory buffer.
old-location: display\setstreamsourceum.htm
old-project: display
ms.assetid: 75a70801-0338-45ed-a691-5f84202575d5
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3DDDI_SETSTREAMSOURCEUM, SetStreamSourceUM, SetStreamSourceUM callback function [Display Devices], UserModeDisplayDriver_Functions_0bea09c2-3bd9-4c60-9688-1c5a687e0dc9.xml, d3dumddi/SetStreamSourceUM, display.setstreamsourceum
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
-	SetStreamSourceUM
product:
- Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_SETSTREAMSOURCEUM callback function
The <i>SetStreamSourceUM</i> function binds a vertex stream source to a user memory buffer.

## Syntax

```
PFND3DDDI_SETSTREAMSOURCEUM Pfnd3dddiSetstreamsourceum;

HRESULT Pfnd3dddiSetstreamsourceum(
  HANDLE hDevice,
  CONST D3DDDIARG_SETSTREAMSOURCEUM *,
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

<i>SetStreamSourceUM</i> returns S_OK or an appropriate error result if the vertex stream source is not successfully bound.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543363">D3DDDIARG_SETSTREAMSOURCEUM</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>