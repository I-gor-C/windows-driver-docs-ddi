---
UID: NS:d3d10umddi.D3D10DDIARG_CREATEDEPTHSTENCILVIEW
title: D3D10DDIARG_CREATEDEPTHSTENCILVIEW
author: windows-driver-content
description: The D3D10DDIARG_CREATEDEPTHSTENCILVIEW structure describes the depth stencil view to create.
old-location: display\d3d10ddiarg_createdepthstencilview.htm
old-project: display
ms.assetid: 03851dee-4ed8-484f-8a00-68aca1da19ce
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3D10DDIARG_CREATEDEPTHSTENCILVIEW, D3D10DDIARG_CREATEDEPTHSTENCILVIEW structure [Display Devices], UMDisplayDriver_Dx10param_Structs_7460e9f5-4a7b-469a-8019-cc634f00d4c1.xml, d3d10umddi/D3D10DDIARG_CREATEDEPTHSTENCILVIEW, display.d3d10ddiarg_createdepthstencilview
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
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
-	HeaderDef
api_location:
-	d3d10umddi.h
api_name:
-	D3D10DDIARG_CREATEDEPTHSTENCILVIEW
product: Windows
targetos: Windows
req.typenames: D3D10DDIARG_CREATEDEPTHSTENCILVIEW
---

# D3D10DDIARG_CREATEDEPTHSTENCILVIEW structure
The D3D10DDIARG_CREATEDEPTHSTENCILVIEW structure describes the depth stencil view to create.

## Syntax
````
typedef struct D3D10DDIARG_CREATEDEPTHSTENCILVIEW {
  D3D10DDI_HRESOURCE    hDrvResource;
  DXGI_FORMAT           Format;
  D3D10DDIRESOURCE_TYPE ResourceDimension;
  union {
    D3D10DDIARG_TEX1D_DEPTHSTENCILVIEW   Tex1D;
    D3D10DDIARG_TEX2D_DEPTHSTENCILVIEW   Tex2D;
    D3D10DDIARG_TEXCUBE_DEPTHSTENCILVIEW TexCube;
  };
} D3D10DDIARG_CREATEDEPTHSTENCILVIEW;
````

## Members


`hDrvResource`

[in] A handle to the base depth stencil resource.

`Format`

[in] A DXGI_FORMAT-typed value that indicates the pixel format of the depth stencil view.

`ResourceDimension`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff541810">D3D10DDIRESOURCE_TYPE</a>-typed value that indicates the resource type and dimensionality of the base resource.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_tex1d_depthstencilview.md">D3D10DDIARG_TEX1D_DEPTHSTENCILVIEW</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_calcprivatedepthstencilviewsize.md">CalcPrivateDepthStencilViewSize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541810">D3D10DDIRESOURCE_TYPE</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_createdepthstencilview.md">CreateDepthStencilView</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_tex2d_depthstencilview.md">D3D10DDIARG_TEX2D_DEPTHSTENCILVIEW</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_texcube_depthstencilview.md">D3D10DDIARG_TEXCUBE_DEPTHSTENCILVIEW</a>