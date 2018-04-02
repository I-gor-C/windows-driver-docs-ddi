---
UID: NS:d3d10umddi.D3D10_DDI_SAMPLER_DESC
title: D3D10_DDI_SAMPLER_DESC
author: windows-driver-content
description: The D3D10_DDI_SAMPLER_DESC structure describes a sampler.
old-location: display\d3d10_ddi_sampler_desc.htm
old-project: display
ms.assetid: 2f65b381-bf81-45b5-9583-793e4ffb453c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D10_DDI_SAMPLER_DESC, D3D10_DDI_SAMPLER_DESC structure [Display Devices], UMDisplayDriver_Dx10param_Structs_3bd0d5fd-417c-43ef-9bdf-0073d8651ced.xml, d3d10umddi/D3D10_DDI_SAMPLER_DESC, display.d3d10_ddi_sampler_desc
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
-	D3D10_DDI_SAMPLER_DESC
product:
- Windows
targetos: Windows
req.typenames: D3D10_DDI_SAMPLER_DESC
---

# D3D10_DDI_SAMPLER_DESC structure
The D3D10_DDI_SAMPLER_DESC structure describes a sampler.

## Syntax
```
typedef struct D3D10_DDI_SAMPLER_DESC {
  D3D10_DDI_FILTER               Filter;
  D3D10_DDI_TEXTURE_ADDRESS_MODE AddressU;
  D3D10_DDI_TEXTURE_ADDRESS_MODE AddressV;
  D3D10_DDI_TEXTURE_ADDRESS_MODE AddressW;
  FLOAT                          MipLODBias;
  UINT                           MaxAnisotropy;
  D3D10_DDI_COMPARISON_FUNC      ComparisonFunc;
  FLOAT                          BorderColor[4];
  FLOAT                          MinLOD;
  FLOAT                          MaxLOD;
};
```

## Members


`Filter`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff541952">D3D10_DDI_FILTER</a>-typed value that indicates the filter property for a sampler.

`AddressU`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff542017">D3D10_DDI_TEXTURE_ADDRESS_MODE</a>-typed value that indicates the texture-address mode for the u coordinate.

`AddressV`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff542017">D3D10_DDI_TEXTURE_ADDRESS_MODE</a>-typed value that indicates the texture-address mode for the v coordinate.

`AddressW`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff542017">D3D10_DDI_TEXTURE_ADDRESS_MODE</a>-typed value that indicates the texture-address mode for the w coordinate.

`MipLODBias`

[in] A single-precision float that affects the level that the driver selects for MIP-map level of detail (LOD).

`MaxAnisotropy`

[in] The maximum valid value for the anisotropy texture-stage state.

`ComparisonFunc`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff541933">D3D10_DDI_COMPARISON_FUNC</a>-typed value that indicates the sampler-comparison function to perform.

`BorderColor`

[in] A four-element array of single-precision float vectors for RGBA, where Red == 0. The border color is used when the D3D10_DDI_TEXTURE_ADDRESS_BORDER value is specified in the <b>AddressU</b>, <b>AddressV</b>, or <b>AddressW</b> member. The float should be converted to the appropriate resource format.

`MinLOD`

[in] A single-precision float vector for the minimum level of detail (LOD) for the sampler.

`MaxLOD`

[in] A single-precision float vector for the maximum level of detail (LOD) for the sampler.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/7231ba65-f6ed-4b00-a61f-21d8fe26398f">CalcPrivateSamplerSize</a>



<a href="https://msdn.microsoft.com/603bb033-390b-4965-b6ea-6acc2c7a8fcf">CreateSampler</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541933">D3D10_DDI_COMPARISON_FUNC</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541952">D3D10_DDI_FILTER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542017">D3D10_DDI_TEXTURE_ADDRESS_MODE</a>