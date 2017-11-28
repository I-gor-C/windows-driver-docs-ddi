---
UID: NE.d3d12umddi.D3D12DDI_PREDICATION_OP
title: D3D12DDI_PREDICATION_OP
author: windows-driver-content
description: Contains values for predication operation options.
old-location: display\d3d12ddi_predication_op.htm
old-project: display
ms.assetid: 70676251-BCD7-4996-B5B7-96A8D9B107DB
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
req.alt-api: D3D12DDI_PREDICATION_OP
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

# D3D12DDI_PREDICATION_OP enumeration



## -description
<p>Contains values for predication operation options. </p>


## -syntax

````
typedef enum D3D12DDI_PREDICATION_OP { 
  D3D12DDI_PREDICATION_OP_EQUAL_ZERO      = 0,
  D3D12DDI_PREDICATION_OP_NOT_EQUAL_ZERO  = 1
} D3D12DDI_PREDICATION_OP;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDI_PREDICATION_OP_EQUAL_ZERO"></a><a id="d3d12ddi_predication_op_equal_zero"></a><b>D3D12DDI_PREDICATION_OP_EQUAL_ZERO</b>

<dd>
<p>All the bits in a 64 bit buffer are zero (0).</p>
</dd>

### -field <a id="D3D12DDI_PREDICATION_OP_NOT_EQUAL_ZERO"></a><a id="d3d12ddi_predication_op_not_equal_zero"></a><b>D3D12DDI_PREDICATION_OP_NOT_EQUAL_ZERO</b>

<dd>
<p>Not all of the bits in a 64 bit buffer are zero (0).</p>
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