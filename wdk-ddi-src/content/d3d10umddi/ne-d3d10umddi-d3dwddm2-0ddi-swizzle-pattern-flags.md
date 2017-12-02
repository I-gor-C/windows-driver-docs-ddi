---
UID: NE.d3d10umddi.D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS
title: D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS
author: windows-driver-content
description: Contains swizzle pattern flag values.
old-location: display\d3dwddm2_0ddi_swizzle_pattern_flags.htm
old-project: display
ms.assetid: 4C3E818B-E265-4AB8-BAAF-D3155578E558
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
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
req.alt-api: D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS
req.alt-loc: d3d10umddi.h
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
req.iface: 
---

# D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS enumeration



## -description
<p>Contains swizzle pattern flag values.</p>


## -syntax

````
typedef enum D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS { 
  D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS_NONE                        = 0,
  D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS_STACK_DEPTH_SLICES          = 1,
  D3DWDDM2_2DDI_SWIZZLE_PATTERN_FLAGS_CONDITIONAL_POSTAMBLE_XORS  = 0x2
} D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS;
````


## -enum-fields
<dl>

### -field D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS_NONE

<dd>
<p>No flags.</p>
</dd>

### -field D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS_STACK_DEPTH_SLICES

<dd>
<p>Stack depth slices. </p>
</dd>

### -field D3DWDDM2_2DDI_SWIZZLE_PATTERN_FLAGS_CONDITIONAL_POSTAMBLE_XORS

<dd>
<p>Conditional post-amble Xors. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h</dt>
</dl>
</td>
</tr>
</table>