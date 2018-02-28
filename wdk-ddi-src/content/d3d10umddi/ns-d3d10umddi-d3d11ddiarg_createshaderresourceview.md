---
UID: NS:d3d10umddi.D3D11DDIARG_CREATESHADERRESOURCEVIEW
title: D3D11DDIARG_CREATESHADERRESOURCEVIEW
author: windows-driver-content
description: The D3D11DDIARG_CREATESHADERRESOURCEVIEW structure describes the shader resource view to create.
old-location: display\d3d11ddiarg_createshaderresourceview.htm
old-project: display
ms.assetid: 0271e937-a55d-4153-b1e1-045fef4b76a0
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: D3D11DDIARG_CREATESHADERRESOURCEVIEW, D3D11DDIARG_CREATESHADERRESOURCEVIEW structure [Display Devices], UMDisplayDriver_Dx11param_Structs_e1d9908f-af17-4d66-ba86-4782bb22458e.xml, d3d10umddi/D3D11DDIARG_CREATESHADERRESOURCEVIEW, display.d3d11ddiarg_createshaderresourceview
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D11DDIARG_CREATESHADERRESOURCEVIEW is supported beginning with the Windows 7 operating system.
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
-	D3D11DDIARG_CREATESHADERRESOURCEVIEW
product: Windows
targetos: Windows
req.typenames: D3D11DDIARG_CREATESHADERRESOURCEVIEW
---

# D3D11DDIARG_CREATESHADERRESOURCEVIEW structure
The D3D11DDIARG_CREATESHADERRESOURCEVIEW structure describes the shader resource view to create.

## Syntax
````
typedef struct D3D11DDIARG_CREATESHADERRESOURCEVIEW {
  D3D10DDI_HRESOURCE    hDrvResource;
  DXGI_FORMAT           Format;
  D3D10DDIRESOURCE_TYPE ResourceDimension;
  union {
    D3D10DDIARG_BUFFER_SHADERRESOURCEVIEW    Buffer;
    D3D10DDIARG_TEX1D_SHADERRESOURCEVIEW     Tex1D;
    D3D10DDIARG_TEX2D_SHADERRESOURCEVIEW     Tex2D;
    D3D10DDIARG_TEX3D_SHADERRESOURCEVIEW     Tex3D;
    D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW TexCube;
    D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW  BufferEx;
  };
} D3D11DDIARG_CREATESHADERRESOURCEVIEW;
````

## Members


`Format`

[in] A DXGI_FORMAT-typed value that indicates the pixel format of the view.

`hDrvResource`

[in] A handle to the shader resource.

`ResourceDimension`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff541810">D3D10DDIRESOURCE_TYPE</a>-typed value that indicates the resource type and dimensionality.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | D3D11DDIARG_CREATESHADERRESOURCEVIEW is supported beginning with the Windows 7 operating system. D3D11DDIARG_CREATESHADERRESOURCEVIEW is supported beginning with the Windows 7 operating system. |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_buffer_shaderresourceview.md">D3D10DDIARG_BUFFER_SHADERRESOURCEVIEW</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_createshaderresourceview.md">CreateShaderResourceView(D3D11)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541810">D3D10DDIRESOURCE_TYPE</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10_1ddiarg_texcube_shaderresourceview.md">D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_bufferex_shaderresourceview.md">D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_calcprivateshaderresourceviewsize.md">CalcPrivateShaderResourceViewSize(D3D11)</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_tex3d_shaderresourceview.md">D3D10DDIARG_TEX3D_SHADERRESOURCEVIEW</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_tex1d_shaderresourceview.md">D3D10DDIARG_TEX1D_SHADERRESOURCEVIEW</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_tex2d_shaderresourceview.md">D3D10DDIARG_TEX2D_SHADERRESOURCEVIEW</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11DDIARG_CREATESHADERRESOURCEVIEW structure%20 RELEASE:%20(2/24/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>