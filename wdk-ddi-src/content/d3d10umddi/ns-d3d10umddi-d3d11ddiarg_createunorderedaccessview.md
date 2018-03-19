---
UID: NS:d3d10umddi.D3D11DDIARG_CREATEUNORDEREDACCESSVIEW
title: D3D11DDIARG_CREATEUNORDEREDACCESSVIEW
author: windows-driver-content
description: The D3D11DDIARG_CREATEUNORDEREDACCESSVIEW structure describes the unordered access view to create.
old-location: display\d3d11ddiarg_createunorderedaccessview.htm
old-project: display
ms.assetid: 3c977fe6-d0f9-4edc-abeb-0725d68a482d
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3D11DDIARG_CREATEUNORDEREDACCESSVIEW, D3D11DDIARG_CREATEUNORDEREDACCESSVIEW structure [Display Devices], UMDisplayDriver_Dx11param_Structs_e6b10da8-f790-4182-926a-a7f183dcd59b.xml, d3d10umddi/D3D11DDIARG_CREATEUNORDEREDACCESSVIEW, display.d3d11ddiarg_createunorderedaccessview
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D11DDIARG_CREATEUNORDEREDACCESSVIEW is supported beginning with the Windows 7 operating system.
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
-	D3D11DDIARG_CREATEUNORDEREDACCESSVIEW
product: Windows
targetos: Windows
req.typenames: D3D11DDIARG_CREATEUNORDEREDACCESSVIEW
---

# D3D11DDIARG_CREATEUNORDEREDACCESSVIEW structure
The D3D11DDIARG_CREATEUNORDEREDACCESSVIEW structure describes the unordered access view to create.

## Syntax
````
typedef struct D3D11DDIARG_CREATEUNORDEREDACCESSVIEW {
  D3D10DDI_HRESOURCE    hDrvResource;
  DXGI_FORMAT           Format;
  D3D10DDIRESOURCE_TYPE ResourceDimension;
  union {
    D3D11DDIARG_BUFFER_UNORDEREDACCESSVIEW Buffer;
    D3D11DDIARG_TEX1D_UNORDEREDACCESSVIEW  Tex1D;
    D3D11DDIARG_TEX2D_UNORDEREDACCESSVIEW  Tex2D;
    D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW  Tex3D;
  };
} D3D11DDIARG_CREATEUNORDEREDACCESSVIEW;
````

## Members


`hDrvResource`

[in] A handle to the unordered access block.

`Format`

[in] A DXGI_FORMAT-typed value that indicates the pixel format of the unordered access block.

`ResourceDimension`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff541810">D3D10DDIRESOURCE_TYPE</a>-typed value that indicates the resource type and dimensionality of the unordered access block. The Direct3D runtime will never set <b>ResourceDimension</b> to D3D10DDIRESOURCE_TEXTURECUBE.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | D3D11DDIARG_CREATEUNORDEREDACCESSVIEW is supported beginning with the Windows 7 operating system. D3D11DDIARG_CREATEUNORDEREDACCESSVIEW is supported beginning with the Windows 7 operating system. |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_tex2d_unorderedaccessview.md">D3D11DDIARG_TEX2D_UNORDEREDACCESSVIEW</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_tex3d_unorderedaccessview.md">D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541810">D3D10DDIRESOURCE_TYPE</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_createunorderedaccessview.md">CreateUnorderedAccessView</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_tex1d_unorderedaccessview.md">D3D11DDIARG_TEX1D_UNORDEREDACCESSVIEW</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_calcprivateunorderedaccessviewsize.md">CalcPrivateUnorderedAccessViewSize</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_buffer_unorderedaccessview.md">D3D11DDIARG_BUFFER_UNORDEREDACCESSVIEW</a>