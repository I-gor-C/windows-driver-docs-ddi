---
UID: NC:d3dumddi.PFND3DDDI_SETINDICESUM
title: PFND3DDDI_SETINDICESUM
author: windows-driver-content
description: The SetIndicesUM function sets the current index buffer to the given user memory buffer.
old-location: display\setindicesum.htm
old-project: display
ms.assetid: 9ca38004-8953-4416-8552-c76813192561
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3DDDI_SETINDICESUM, SetIndicesUM, SetIndicesUM callback function [Display Devices], UserModeDisplayDriver_Functions_f692c944-6130-46e3-8e63-f3dbeb051782.xml, d3dumddi/SetIndicesUM, display.setindicesum
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
-	SetIndicesUM
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_SETINDICESUM callback function
The <i>SetIndicesUM</i> function sets the current index buffer to the given user memory buffer.

## Syntax

```
PFND3DDDI_SETINDICESUM Pfnd3dddiSetindicesum;

HRESULT Pfnd3dddiSetindicesum(
  HANDLE hDevice,
   UINT,
  CONST VOID *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`UINT`



`*`




## Return Value

<i>SetIndicesUM</i> returns S_OK or an appropriate error result if the index buffer is not successfully set to the given user memory buffer.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>