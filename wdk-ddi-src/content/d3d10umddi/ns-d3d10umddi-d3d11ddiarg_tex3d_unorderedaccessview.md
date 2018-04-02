---
UID: NS:d3d10umddi.D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW
title: D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW
author: windows-driver-content
description: The D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW structure describes a three-dimensional (3-D) texture that is used to create an unordered access view in a call to the CreateUnorderedAccessView function.
old-location: display\d3d11ddiarg_tex3d_unorderedaccessview.htm
old-project: display
ms.assetid: 15b535ab-28ed-41c3-8544-4ccb27a53649
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW, D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW structure [Display Devices], UMDisplayDriver_Dx11param_Structs_0d8a28d7-9bb4-49b9-9ce9-1f290072ba4d.xml, d3d10umddi/D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW, display.d3d11ddiarg_tex3d_unorderedaccessview
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW is supported beginning with the Windows 7 operating system.
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
-	D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW
product:
- Windows
targetos: Windows
req.typenames: D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW
---

# D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW structure
The D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW structure describes a three-dimensional (3-D) texture that is used to create an unordered access view in a call to the <a href="https://msdn.microsoft.com/c5a258e7-6645-46bb-ab2c-a1c8f5e593b7">CreateUnorderedAccessView</a> function.

## Syntax
```
typedef struct D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW {
  UINT MipSlice;
  UINT FirstW;
  UINT WSize;
};
```

## Members


`MipSlice`

[in] The identifier of the MIP-map slice.

`FirstW`

[in] The identifier of the first array slice.

`WSize`

[in] The number of array slices for the texture.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW is supported beginning with the Windows 7 operating system. D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW is supported beginning with the Windows 7 operating system. |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/6aca5d33-c8c6-4c6b-a66a-e28a958cbc2e">CalcPrivateUnorderedAccessViewSize</a>



<a href="https://msdn.microsoft.com/c5a258e7-6645-46bb-ab2c-a1c8f5e593b7">CreateUnorderedAccessView</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542086">D3D11DDIARG_CREATEUNORDEREDACCESSVIEW</a>