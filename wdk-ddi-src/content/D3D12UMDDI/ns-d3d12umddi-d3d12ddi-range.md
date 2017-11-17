---
UID: NS.d3d12umddi.D3D12DDI_RANGE
title: D3D12DDI_RANGE
author: windows-driver-content
description: Specifies a range.
old-location: display\d3d12ddi_range.htm
ms.assetid: B3A8F252-D56D-4F20-A0DE-2A29904BC907
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
req.alt-api: D3D12DDI_RANGE
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
ms.keywords: D3D12DDI_RANGE, D3D12DDI_RANGE
req.iface: 
---

# D3D12DDI_RANGE structure



## -description
<p>Specifies a range.</p>


## -syntax

````
typedef struct D3D12DDI_RANGE {
  UINT64 Begin;
  UINT64 End;
} D3D12DDI_RANGE;
````


## -struct-fields
<dl>

### -field <b>Begin</b>

<dd>
<p>The beginning of the range.</p>
</dd>

### -field <b>End</b>

<dd>
<p>A value of one more than the end of the range. Therefore, the value of <i>End</i> minus the value of <i>Begin</i> is the size of the range.</p>
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