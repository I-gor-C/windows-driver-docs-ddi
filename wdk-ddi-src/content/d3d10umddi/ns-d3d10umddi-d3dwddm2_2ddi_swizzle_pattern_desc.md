---
UID: NS:d3d10umddi.D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
title: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
author: windows-driver-content
description: Describes a swizzle pattern.
old-location: display\d3dwddm2_2ddi_swizzle_pattern_desc.htm
old-project: display
ms.assetid: AD3D5847-862F-41AA-90C0-0F8A1D0A617B
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC structure [Display Devices], d3d10umddi/D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, display.d3dwddm2_2ddi_swizzle_pattern_desc
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
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
-	D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
product: Windows
targetos: Windows
req.typenames: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
---

# D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC structure
Describes a swizzle pattern.

## Syntax
````
typedef struct D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC {
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY InterleavePatternSourceBits[32];
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY InterleavePatternXORSourceBits[32];
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY InterleavePatternXOR2SourceBits[32];
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY InterleavePatternXOR3SourceBits[32];
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY InterleavePatternXOR4SourceBits[32];
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY PostambleXORSourceBits[32];
  D3DWDDM2_0DDI_SWIZZLE_BIT_ENTRY PostambleXOR2SourceBits[32];
  UINT                            PostambleXORImmediate;
  UINT                            Flags;
} D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC;
````

## Members


`InterleavePatternSourceBits`

The interleave pattern source bits.

`InterleavePatternXORSourceBits`

The interleave pattern XOR source bits.

`InterleavePatternXOR2SourceBits`

The interleave pattern second XOR source bits.

`InterleavePatternXOR3SourceBits`

The interleave pattern third XOR source bits.

`InterleavePatternXOR4SourceBits`

The interleave pattern fourth XOR source bits.

`PostambleXORSourceBits`

Postamble XOR source bits.

`PostambleXOR2SourceBits`

Postamble second XOR source bits.

`PostambleXORImmediate`

A postamble XOR immediate value.

`Flags`

Flags. For more information, see the <a href="..\d3d10umddi\ne-d3d10umddi-d3dwddm2_0ddi_swizzle_pattern_flags.md">D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS</a> enumeration.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d10umddi.h |

## See Also

<a href="..\d3d10umddi\ne-d3d10umddi-d3dwddm2_0ddi_swizzle_pattern_flags.md">D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS</a>