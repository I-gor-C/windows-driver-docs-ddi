---
UID: NE.d3d12umddi.D3D12DDI_SWIZZLE_PATTERN_FLAGS
title: D3D12DDI_SWIZZLE_PATTERN_FLAGS
author: windows-driver-content
description: Specifies swizzle pattern flags.
old-location: display\d3d12ddi_swizzle_pattern_flags.htm
ms.assetid: 613FE631-8381-4EDD-85C9-7B91F9F8B92F
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_SWIZZLE_PATTERN_FLAGS
req.alt-loc: D3d12umddi.h
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
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
req.iface: 
---

# D3D12DDI_SWIZZLE_PATTERN_FLAGS enumeration



## -description
<p>Specifies swizzle pattern flags.</p>


## -syntax

````
typedef enum D3D12DDI_SWIZZLE_PATTERN_FLAGS { 
  D3D12DDI_SWIZZLE_PATTERN_FLAGS_NONE                = 0,
  D3D12DDI_SWIZZLE_PATTERN_FLAGS_STACK_DEPTH_SLICES  = 0x1
} D3D12DDI_SWIZZLE_PATTERN_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDI_SWIZZLE_PATTERN_FLAGS_NONE"></a><a id="d3d12ddi_swizzle_pattern_flags_none"></a><b>D3D12DDI_SWIZZLE_PATTERN_FLAGS_NONE</b>

<dd>
<p>No flag value.</p>
</dd>

### -field <a id="D3D12DDI_SWIZZLE_PATTERN_FLAGS_STACK_DEPTH_SLICES"></a><a id="d3d12ddi_swizzle_pattern_flags_stack_depth_slices"></a><b>D3D12DDI_SWIZZLE_PATTERN_FLAGS_STACK_DEPTH_SLICES</b>

<dd>
<p>Depth slices are treated as being stacked vertically prior to swizzling.</p>
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
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>