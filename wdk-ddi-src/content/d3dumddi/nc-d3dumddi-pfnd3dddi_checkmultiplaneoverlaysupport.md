---
UID: NC:d3dumddi.PFND3DDDI_CHECKMULTIPLANEOVERLAYSUPPORT
title: PFND3DDDI_CHECKMULTIPLANEOVERLAYSUPPORT
author: windows-driver-content
description: Called by the Microsoft Direct3D runtime to check the details on hardware support for multiplane overlays.
old-location: display\pfncheckmultiplaneoverlaysupport__d3d_.htm
old-project: display
ms.assetid: A439E695-D374-439A-8A69-6D4E247FF134
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3DDDI_CHECKMULTIPLANEOVERLAYSUPPORT, d3dumddi/pfnCheckMultiPlaneOverlaySupport, display.pfncheckmultiplaneoverlaysupport__d3d_, pfnCheckMultiPlaneOverlaySupport, pfnCheckMultiPlaneOverlaySupport callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
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
-	D3dumddi.h
api_name:
-	pfnCheckMultiPlaneOverlaySupport
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_CHECKMULTIPLANEOVERLAYSUPPORT callback function
Called by the Microsoft Direct3D runtime to check the details on hardware support for multiplane overlays.

## Syntax

```
PFND3DDDI_CHECKMULTIPLANEOVERLAYSUPPORT Pfnd3dddiCheckmultiplaneoverlaysupport;

HRESULT Pfnd3dddiCheckmultiplaneoverlaysupport(
  HANDLE hDevice,
  D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

If this routine succeeds, it returns <b>S_OK</b>. Otherwise, it returns an <b>HRESULT</b> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows Server 2012 R2 |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_checkmultiplaneoverlaysupport.md">D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT</a>