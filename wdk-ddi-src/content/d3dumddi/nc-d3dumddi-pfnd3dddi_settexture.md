---
UID: NC:d3dumddi.PFND3DDDI_SETTEXTURE
title: PFND3DDDI_SETTEXTURE
author: windows-driver-content
description: The SetTexture function inserts a texture at a particular stage in a multiple-texture group.
old-location: display\settexture.htm
old-project: display
ms.assetid: b2ed86c5-cd4f-4aaa-a062-4c7ae4e088df
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3DDDI_SETTEXTURE, SetTexture, SetTexture callback function [Display Devices], UserModeDisplayDriver_Functions_f85a8797-cbcc-40df-a339-af69ce128e95.xml, d3dumddi/SetTexture, display.settexture
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
-	SetTexture
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_SETTEXTURE callback function
The <i>SetTexture</i> function inserts a texture at a particular stage in a multiple-texture group.

## Syntax

```
PFND3DDDI_SETTEXTURE Pfnd3dddiSettexture;

HRESULT Pfnd3dddiSettexture(
  HANDLE hDevice,
   UINT,
   HANDLE
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`UINT`



`HANDLE`




## Return Value

<i>SetTexture</i> returns S_OK or an appropriate error result if the texture is not successfully inserted.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>