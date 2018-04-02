---
UID: NE:d3d10umddi.D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS
title: D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS
author: windows-driver-content
description: Contains swizzle pattern flag values.
old-location: display\d3dwddm2_0ddi_swizzle_pattern_flags.htm
old-project: display
ms.assetid: 4C3E818B-E265-4AB8-BAAF-D3155578E558
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS, D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS enumeration [Display Devices], D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS_NONE, D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS_STACK_DEPTH_SLICES, D3DWDDM2_2DDI_SWIZZLE_PATTERN_FLAGS_CONDITIONAL_POSTAMBLE_XORS, d3d10umddi/D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS, d3d10umddi/D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS_NONE, d3d10umddi/D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS_STACK_DEPTH_SLICES, d3d10umddi/D3DWDDM2_2DDI_SWIZZLE_PATTERN_FLAGS_CONDITIONAL_POSTAMBLE_XORS, display.d3dwddm2_0ddi_swizzle_pattern_flags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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
-	D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS
---

# D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS Enumeration
Contains swizzle pattern flag values.

## Syntax
```
typedef enum D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS {
  D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS_NONE                        ,
  D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS_STACK_DEPTH_SLICES          ,
  D3DWDDM2_2DDI_SWIZZLE_PATTERN_FLAGS_CONDITIONAL_POSTAMBLE_XORS
} ;
```

## Constants

<table>
            
                <tr>
                    <td>D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS_NONE</td>
                    <td>No flags.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS_STACK_DEPTH_SLICES</td>
                    <td>Stack depth slices.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_2DDI_SWIZZLE_PATTERN_FLAGS_CONDITIONAL_POSTAMBLE_XORS</td>
                    <td>Conditional post-amble Xors.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d10umddi.h |