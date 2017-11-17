---
UID: NS.d3d12umddi.D3D12DDIARG_RESOURCE_BARRIER_0022
title: D3D12DDIARG_RESOURCE_BARRIER_0022
author: windows-driver-content
description: Describes a resource barrier.
old-location: display\d3d12ddiarg_resource_barrier_0022.htm
ms.assetid: ED597BB0-F9ED-4311-9E2F-06AEA2755B37
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
ms.keywords: D3D12DDIARG_RESOURCE_BARRIER_0022, D3D12DDIARG_RESOURCE_BARRIER_0022
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

### -field <b>Type</b>

<dd>
<p>The type of resource barrier as a <a href="https://msdn.microsoft.com/3865DB8A-A920-42AC-B802-E5A3FB02014C">D3D12DDI_RESOURCE_BARRIER_TYPE</a> value.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A barrier flag as a <a href="https://msdn.microsoft.com/876ABC9C-F9BE-480F-8641-AE132840F8D5">D3D12DDI_RESOURCE_BARRIER_FLAGS</a> value.</p>
</dd>

### -field <b>    {
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