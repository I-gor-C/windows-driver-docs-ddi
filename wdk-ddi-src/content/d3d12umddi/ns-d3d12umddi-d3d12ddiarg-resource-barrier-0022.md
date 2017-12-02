---
UID: NS.d3d12umddi.D3D12DDIARG_RESOURCE_BARRIER_0022
title: D3D12DDIARG_RESOURCE_BARRIER_0022
author: windows-driver-content
description: Describes a resource barrier.
old-location: display\d3d12ddiarg_resource_barrier_0022.htm
old-project: display
ms.assetid: ED597BB0-F9ED-4311-9E2F-06AEA2755B37
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDIARG_RESOURCE_BARRIER_0022, D3D12DDIARG_RESOURCE_BARRIER_0022
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDIARG_RESOURCE_BARRIER_0022
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

# D3D12DDIARG_RESOURCE_BARRIER_0022 structure



## -description
<p>Describes a resource barrier.</p>


## -syntax

````
typedef struct D3D12DDIARG_RESOURCE_BARRIER_0022 {
  D3D12DDI_RESOURCE_BARRIER_TYPE  Type;
  D3D12DDI_RESOURCE_BARRIER_FLAGS Flags;
  union      {
        D3D12DDI_RESOURCE_TRANSITION_BARRIER_0003 Transition;
        D3D12DDI_RESOURCE_UAV_BARRIER             UAV;
        D3D12DDI_RESOURCE_RANGED_BARRIER_0022     Ranged;
    };
} D3D12DDIARG_RESOURCE_BARRIER_0022;
````


## -struct-fields
<dl>

### -field Type

<dd>
<p>The type of resource barrier as a <a href="..\d3d12umddi\ne-d3d12umddi-d3d12ddi-resource-barrier-type.md">D3D12DDI_RESOURCE_BARRIER_TYPE</a> value.</p>
</dd>

### -field Flags

<dd>
<p>A barrier flag as a <a href="..\d3d12umddi\ne-d3d12umddi-d3d12ddi-resource-barrier-flags.md">D3D12DDI_RESOURCE_BARRIER_FLAGS</a> value.</p>
</dd>

### -field     {
        D3D12DDI_RESOURCE_TRANSITION_BARRIER_0003 Transition;
        D3D12DDI_RESOURCE_UAV_BARRIER             UAV;
        D3D12DDI_RESOURCE_RANGED_BARRIER_0022     Ranged;
    }</b>

<dd>
<p>A resource barrier.</p>
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