---
UID: NS:d3d12umddi.D3D12DDIARG_RESOURCE_BARRIER_0022
title: D3D12DDIARG_RESOURCE_BARRIER_0022
author: windows-driver-content
description: Describes a resource barrier.
old-location: display\d3d12ddiarg_resource_barrier_0022.htm
old-project: display
ms.assetid: ED597BB0-F9ED-4311-9E2F-06AEA2755B37
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D12DDIARG_RESOURCE_BARRIER_0022, D3D12DDIARG_RESOURCE_BARRIER_0022 structure [Display Devices], d3d12umddi/D3D12DDIARG_RESOURCE_BARRIER_0022, display.d3d12ddiarg_resource_barrier_0022
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3d12umddi.h
api_name:
-	D3D12DDIARG_RESOURCE_BARRIER_0022
product: Windows
targetos: Windows
req.typenames: D3D12DDIARG_RESOURCE_BARRIER_0022
---

# D3D12DDIARG_RESOURCE_BARRIER_0022 structure
Describes a resource barrier.

## Syntax
```
typedef struct D3D12DDIARG_RESOURCE_BARRIER_0022 {
  D3D12DDI_RESOURCE_BARRIER_TYPE  Type;
  D3D12DDI_RESOURCE_BARRIER_FLAGS Flags;
  union {
    D3D12DDI_RESOURCE_RANGED_BARRIER_0022     Ranged;
    D3D12DDI_RESOURCE_TRANSITION_BARRIER_0003 Transition;
    D3D12DDI_RESOURCE_UAV_BARRIER             UAV;
  };
};
```

## Members


`Type`

The type of resource barrier as a <a href="https://msdn.microsoft.com/3865DB8A-A920-42AC-B802-E5A3FB02014C">D3D12DDI_RESOURCE_BARRIER_TYPE</a> value.

`Flags`

A barrier flag as a <a href="https://msdn.microsoft.com/876ABC9C-F9BE-480F-8641-AE132840F8D5">D3D12DDI_RESOURCE_BARRIER_FLAGS</a> value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |