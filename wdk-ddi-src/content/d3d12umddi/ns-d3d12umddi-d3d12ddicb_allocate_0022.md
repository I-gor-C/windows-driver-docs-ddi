---
UID: NS:d3d12umddi.D3D12DDICB_ALLOCATE_0022
title: D3D12DDICB_ALLOCATE_0022
author: windows-driver-content
description: Specifies information for use in an allocation callback function.
old-location: display\d3d12ddicb_allocate_0022.htm
old-project: display
ms.assetid: C39262BA-D1CE-4634-974A-ACCE8D321830
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3D12DDICB_ALLOCATE_0022, D3D12DDICB_ALLOCATE_0022 structure [Display Devices], d3d12umddi/D3D12DDICB_ALLOCATE_0022, display.d3d12ddicb_allocate_0022
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
-	D3D12DDICB_ALLOCATE_0022
product: Windows
targetos: Windows
req.typenames: D3D12DDICB_ALLOCATE_0022
---

# D3D12DDICB_ALLOCATE_0022 structure
Specifies information for use in an allocation callback function.

## Syntax
````
typedef struct D3D12DDICB_ALLOCATE_0022 {
  const VOID                    *pPrivateDriverData;
  UINT                          PrivateDriverDataSize;
  HANDLE                        hResource;
  D3DKMT_HANDLE                 hKMResource;
  UINT                          NumAllocations;
  D3D12DDI_ALLOCATION_INFO_0022 *pAllocationInfo;
} D3D12DDICB_ALLOCATE_0022;
````

## Members


`pPrivateDriverData`

A pointer to a buffer that contains optional private driver data.

`PrivateDriverDataSize`

Size of the private driver data.

`hResource`

The handle of a resource.

`hKMResource`

A handle of a kernel resource.

`NumAllocations`

The number of allocations.

`pAllocationInfo`

Allocation as a <a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddi_allocation_info_0022.md">D3D12DDI_ALLOCATION_INFO_0022</a> structure.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |

## See Also

<a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddi_allocation_info_0022.md">D3D12DDI_ALLOCATION_INFO_0022</a>