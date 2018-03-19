---
UID: NC:d3dumddi.PFND3DDDI_VALIDATEDEVICE
title: PFND3DDDI_VALIDATEDEVICE
author: windows-driver-content
description: The ValidateDevice function returns the number of passes in which the hardware can perform the blending operations that are specified in the current state.
old-location: display\validatedevice.htm
old-project: display
ms.assetid: 058696e0-be4a-45f3-b3e8-55abccdce3ce
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3DDDI_VALIDATEDEVICE, UserModeDisplayDriver_Functions_37e253ca-1d0f-4896-aaad-4c36053877c5.xml, ValidateDevice, ValidateDevice callback function [Display Devices], d3dumddi/ValidateDevice, display.validatedevice
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
-	ValidateDevice
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_VALIDATEDEVICE callback function
The <i>ValidateDevice</i> function returns the number of passes in which the hardware can perform the blending operations that are specified in the current state.

## Syntax

```
PFND3DDDI_VALIDATEDEVICE Pfnd3dddiValidatedevice;

HRESULT Pfnd3dddiValidatedevice(
  HANDLE hDevice,
  D3DDDIARG_VALIDATETEXTURESTAGESTATE *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<i>ValidateDevice</i> returns S_OK or an appropriate error result if the number of necessary hardware passes is not successfully received.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_validatetexturestagestate.md">D3DDDIARG_VALIDATETEXTURESTAGESTATE</a>



<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>