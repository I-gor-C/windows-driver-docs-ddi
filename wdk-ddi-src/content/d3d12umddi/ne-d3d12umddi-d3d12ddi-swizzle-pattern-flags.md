---
UID: NE.d3d12umddi.D3D12DDI_SWIZZLE_PATTERN_FLAGS
title: D3D12DDI_SWIZZLE_PATTERN_FLAGS
author: windows-driver-content
description: Specifies swizzle pattern flags.
old-location: display\d3d12ddi_swizzle_pattern_flags.htm
old-project: display
ms.assetid: 613FE631-8381-4EDD-85C9-7B91F9F8B92F
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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

### -field D3D12DDI_SWIZZLE_PATTERN_FLAGS_NONE

<dd>
<p>No flag value.</p>
</dd>

### -field D3D12DDI_SWIZZLE_PATTERN_FLAGS_STACK_DEPTH_SLICES

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