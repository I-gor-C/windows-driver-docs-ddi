---
UID: NC:d3dumddi.PFND3DDDI_DESTROYOVERLAY
title: PFND3DDDI_DESTROYOVERLAY
author: windows-driver-content
description: The DestroyOverlay function disables the overlay hardware and frees the overlay handle.
old-location: display\destroyoverlay.htm
old-project: display
ms.assetid: 63004d19-e2cd-462c-8fa5-ea4dd6e29735
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DestroyOverlay, DestroyOverlay callback function [Display Devices], PFND3DDDI_DESTROYOVERLAY, UserModeDisplayDriver_Functions_e3dd8286-aff0-40c0-8cf2-84ecc706df90.xml, d3dumddi/DestroyOverlay, display.destroyoverlay
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
-	DestroyOverlay
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_DESTROYOVERLAY callback function
The <b>DestroyOverlay</b> function disables the overlay hardware and frees the overlay handle.

## Syntax

```
PFND3DDDI_DESTROYOVERLAY Pfnd3dddiDestroyoverlay;

HRESULT Pfnd3dddiDestroyoverlay(
  HANDLE hDevice,
  CONST D3DDDIARG_DESTROYOVERLAY *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<b>DestroyOverlay</b> returns S_OK or an appropriate error result if the overlay hardware is not disabled.

## Remarks

Overlays are independent from the resources that are displayed by using the overlays.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_destroyoverlay.md">D3DDDIARG_DESTROYOVERLAY</a>



<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>