---
UID: NS.d3d12umddi.D3D12DDI_SWIZZLE_PATTERN_DESC_0022
title: D3D12DDI_SWIZZLE_PATTERN_DESC_0022
author: windows-driver-content
description: Describes a swizzle pattern.
old-location: display\d3d12ddi_swizzle_pattern_desc_0022.htm
ms.assetid: A52C8293-C037-4062-9A63-AD69237F7B3D
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_SWIZZLE_PATTERN_DESC_0022
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
ms.keywords: D3D12DDI_SWIZZLE_PATTERN_DESC_0022, D3D12DDI_SWIZZLE_PATTERN_DESC_0022
req.iface: 
---

# D3D12DDI_SWIZZLE_PATTERN_DESC_0022 structure



## -description
<p>Describes a swizzle pattern. </p>


## -syntax

````
typedef struct D3D12DDI_SWIZZLE_PATTERN_DESC_0022 {
  D3D12DDI_SWIZZLE_BIT_ENTRY InterleavePatternSourceBits[32];
  D3D12DDI_SWIZZLE_BIT_ENTRY InterleavePatternXORSourceBits[32];
  D3D12DDI_SWIZZLE_BIT_ENTRY InterleavePatternXOR2SourceBits[32];
  D3D12DDI_SWIZZLE_BIT_ENTRY InterleavePatternXOR3SourceBits[32];
  D3D12DDI_SWIZZLE_BIT_ENTRY InterleavePatternXOR4SourceBits[32];
  D3D12DDI_SWIZZLE_BIT_ENTRY PostambleXORSourceBits[32];
  D3D12DDI_SWIZZLE_BIT_ENTRY PostambleXOR2SourceBits[32];
  UINT                       PostambleXORImmediate;
  UINT                       Flags;
} D3D12DDI_SWIZZLE_PATTERN_DESC_0022;
````


## -struct-fields
<dl>

### -field <b>InterleavePatternSourceBits</b>

<dd>
<p>The interleave pattern source bits.</p>
</dd>

### -field <b>InterleavePatternXORSourceBits</b>

<dd>
<p>The interleave pattern XOR source bits.</p>
</dd>

### -field <b>InterleavePatternXOR2SourceBits</b>

<dd>
<p>The interleave pattern second XOR source bits.</p>
</dd>

### -field <b>InterleavePatternXOR3SourceBits</b>

<dd>
<p>The interleave pattern third XOR source bits.</p>
</dd>

### -field <b>InterleavePatternXOR4SourceBits</b>

<dd>
<p>The interleave pattern fourth XOR source bits.</p>
</dd>

### -field <b>PostambleXORSourceBits</b>

<dd>
<p>Postamble XOR source bits.</p>
</dd>

### -field <b>PostambleXOR2SourceBits</b>

<dd>
<p>Postamble second XOR source bits.</p>
</dd>

### -field <b>PostambleXORImmediate</b>

<dd>
<p>A postamble XOR immediate value. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Flags. </p>
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