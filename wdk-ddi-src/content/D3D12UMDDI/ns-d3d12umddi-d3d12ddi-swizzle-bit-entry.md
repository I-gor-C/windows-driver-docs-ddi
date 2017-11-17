---
UID: NS.d3d12umddi.D3D12DDI_SWIZZLE_BIT_ENTRY
title: D3D12DDI_SWIZZLE_BIT_ENTRY
author: windows-driver-content
description: Defines a swizzle bit entry.
old-location: display\d3d12ddi_swizzle_bit_entry.htm
ms.assetid: B7FF7AA2-39B2-4D9E-8DDC-0A39FFF49F37
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
req.alt-api: D3D12DDI_SWIZZLE_BIT_ENTRY
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
ms.keywords: D3D12DDI_SWIZZLE_BIT_ENTRY, D3D12DDI_SWIZZLE_BIT_ENTRY
req.iface: 
---

# D3D12DDI_SWIZZLE_BIT_ENTRY structure



## -description
<p>Defines a swizzle bit entry.</p>


## -syntax

````
typedef struct D3D12DDI_SWIZZLE_BIT_ENTRY {
  UINT8 Valid  :1;
  UINT8 ChannelIndex  :2;
  UINT8 SourceBitIndex  :5;
} D3D12DDI_SWIZZLE_BIT_ENTRY;
````


## -struct-fields
<dl>

### -field <b>Valid</b>

<dd>
<p>A valid value.</p>
</dd>

### -field <b>ChannelIndex</b>

<dd>
<p>The channel index. Specify zero (0) for X, one (1) for Y, two (2) for Z, and three (3) for SS.</p>
</dd>

### -field <b>SourceBitIndex</b>

<dd>
<p>Index of source bit address.</p>
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