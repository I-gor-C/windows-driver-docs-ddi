---
UID: NS:d3d10umddi.D3D10DDIARG_CREATESHADERRESOURCEVIEW
title: D3D10DDIARG_CREATESHADERRESOURCEVIEW
author: windows-driver-content
description: The D3D10DDIARG_CREATESHADERRESOURCEVIEW structure describes the shader resource view to create.
old-location: display\d3d10ddiarg_createshaderresourceview.htm
old-project: display
ms.assetid: 60f0019b-ba02-433d-b5a2-f92a43f4d5a8
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D10DDIARG_CREATESHADERRESOURCEVIEW, D3D10DDIARG_CREATESHADERRESOURCEVIEW structure [Display Devices], UMDisplayDriver_Dx10param_Structs_5307f7f2-0e25-4847-b1d4-5300c27320b7.xml, d3d10umddi/D3D10DDIARG_CREATESHADERRESOURCEVIEW, display.d3d10ddiarg_createshaderresourceview
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
-	D3D10DDIARG_CREATESHADERRESOURCEVIEW
product: Windows
targetos: Windows
req.typenames: D3D10DDIARG_CREATESHADERRESOURCEVIEW
---

# D3D10DDIARG_CREATESHADERRESOURCEVIEW structure
The D3D10DDIARG_CREATESHADERRESOURCEVIEW structure describes the shader resource view to create.

## Syntax
```
typedef struct D3D10DDIARG_CREATESHADERRESOURCEVIEW {
  D3D10DDI_HRESOURCE    hDrvResource;
  DXGI_FORMAT           Format;
  D3D10DDIRESOURCE_TYPE ResourceDimension;
  union {
    D3D10DDIARG_BUFFER_SHADERRESOURCEVIEW  Buffer;
    D3D10DDIARG_TEX1D_SHADERRESOURCEVIEW   Tex1D;
    D3D10DDIARG_TEX2D_SHADERRESOURCEVIEW   Tex2D;
    D3D10DDIARG_TEX3D_SHADERRESOURCEVIEW   Tex3D;
    D3D10DDIARG_TEXCUBE_SHADERRESOURCEVIEW TexCube;
  };
};
```

## Members


`hDrvResource`

[in] A handle to the shader resource.

`Format`

[in] A DXGI_FORMAT-typed value that indicates the pixel format of the view.

`ResourceDimension`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff541810">D3D10DDIRESOURCE_TYPE</a>-typed value that indicates the resource type and dimensionality.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/2abf5ca9-974b-40d7-b71c-43c4fb33dd7c">CalcPrivateShaderResourceViewSize</a>



<a href="https://msdn.microsoft.com/3b1c998d-3fde-4712-ba74-7c8033033182">CreateShaderResourceView</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541645">D3D10DDIARG_BUFFER_SHADERRESOURCEVIEW</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541760">D3D10DDIARG_TEX1D_SHADERRESOURCEVIEW</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541773">D3D10DDIARG_TEX2D_SHADERRESOURCEVIEW</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541789">D3D10DDIARG_TEX3D_SHADERRESOURCEVIEW</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541807">D3D10DDIARG_TEXCUBE_SHADERRESOURCEVIEW</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541810">D3D10DDIRESOURCE_TYPE</a>