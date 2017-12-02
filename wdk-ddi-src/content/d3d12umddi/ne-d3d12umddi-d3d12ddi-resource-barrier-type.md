---
UID: NE.d3d12umddi.D3D12DDI_RESOURCE_BARRIER_TYPE
title: D3D12DDI_RESOURCE_BARRIER_TYPE
author: windows-driver-content
description: Specifies the type of resource barrier.
old-location: display\d3d12ddi_resource_barrier_type.htm
old-project: display
ms.assetid: 3865DB8A-A920-42AC-B802-E5A3FB02014C
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
req.alt-api: D3D12DDI_RESOURCE_BARRIER_TYPE
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

# D3D12DDI_RESOURCE_BARRIER_TYPE enumeration



## -description
<p>Specifies the type of resource barrier.</p>


## -syntax

````
typedef enum D3D12DDI_RESOURCE_BARRIER_TYPE { 
  D3D12DDI_RESOURCE_BARRIER_TYPE_TRANSITION,
  D3D12DDI_RESOURCE_BARRIER_TYPE_UAV,
  D3D12DDI_RESOURCE_BARRIER_TYPE_0022_RANGED
} D3D12DDI_RESOURCE_BARRIER_TYPE;
````


## -enum-fields
<dl>

### -field D3D12DDI_RESOURCE_BARRIER_TYPE_TRANSITION

<dd>
<p>A transition barrier that indicates a transition of a set of subresources between different usages. </p>
</dd>

### -field D3D12DDI_RESOURCE_BARRIER_TYPE_UAV

<dd>
<p>An unordered access view (UAV) barrier that indicates all UAV accesses to a resource must complete before any future UAV accesses can begin.</p>
</dd>

### -field D3D12DDI_RESOURCE_BARRIER_TYPE_0022_RANGED

<dd>
<p>A ranged resource barrier.</p>
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