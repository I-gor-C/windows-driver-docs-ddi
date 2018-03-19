---
UID: NS:d3d12umddi.D3D12DDI_RESOURCE_ALLOCATION_INFO_0022
title: D3D12DDI_RESOURCE_ALLOCATION_INFO_0022
author: windows-driver-content
description: Specifies information for resource allocation.
old-location: display\d3d12ddi_resource_allocation_info_0022.htm
old-project: display
ms.assetid: 71CDBF47-B32D-4084-B2F6-9F8C037FCB79
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3D12DDI_RESOURCE_ALLOCATION_INFO_0022, D3D12DDI_RESOURCE_ALLOCATION_INFO_0022 structure [Display Devices], d3d12umddi/D3D12DDI_RESOURCE_ALLOCATION_INFO_0022, display.d3d12ddi_resource_allocation_info_0022
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
-	D3D12DDI_RESOURCE_ALLOCATION_INFO_0022
product: Windows
targetos: Windows
req.typenames: D3D12DDI_RESOURCE_ALLOCATION_INFO_0022
---

# D3D12DDI_RESOURCE_ALLOCATION_INFO_0022 structure
Specifies information for resource allocation.

## Syntax
````
typedef struct D3D12DDI_RESOURCE_ALLOCATION_INFO_0022 {
  UINT64                   ResourceDataSize;
  AdditionalDataHeaderSize UINT64;
  UINT64                   AdditionalDataSize;
  UINT32                   ResourceDataAlignment;
  UINT32                   AdditionalDataHeaderAlignment;
  UINT32                   AdditionalDataAlignment;
  D3D12DDI_TEXTURE_LAYOUT  Layout;
  UINT8                    MipLevelSwizzleTransition[5];
  UINT8                    PlaneSliceSwizzleTransition[2];
} D3D12DDI_RESOURCE_ALLOCATION_INFO_0022;
````

## Members


`ResourceDataSize`

The data size of  the resource.

`AdditionalDataHeaderSize`



`AdditionalDataSize`

The additional data size.

`ResourceDataAlignment`

The data alignment of the resource.

`AdditionalDataHeaderAlignment`

The data alignment of the additional header.

`AdditionalDataAlignment`

The additional data alignment.

`Layout`

The texture layout as a <a href="..\d3d12umddi\ne-d3d12umddi-d3d12ddi_texture_layout.md">D3D12DDI_TEXTURE_LAYOUT</a> value.

`MipLevelSwizzleTransition`

The MIP level for a swizzle transition.

`PlaneSliceSwizzleTransition`

The plane slice for a swizzle transition.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |

## See Also

<a href="..\d3d12umddi\ne-d3d12umddi-d3d12ddi_texture_layout.md">D3D12DDI_TEXTURE_LAYOUT</a>