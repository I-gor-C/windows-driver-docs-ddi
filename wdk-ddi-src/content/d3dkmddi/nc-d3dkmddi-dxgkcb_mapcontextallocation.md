---
UID: NC:d3dkmddi.DXGKCB_MAPCONTEXTALLOCATION
title: DXGKCB_MAPCONTEXTALLOCATION
author: windows-driver-content
description: Maps a graphics processing unit (GPU) virtual address to the specified context allocation.
old-location: display\dxgkcbmapcontextallocation.htm
old-project: display
ms.assetid: 8EAC322D-B666-428A-99A3-96E489611832
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGKCB_MAPCONTEXTALLOCATION, DxgkCbMapContextAllocation, DxgkCbMapContextAllocation callback function [Display Devices], d3dkmddi/DxgkCbMapContextAllocation, display.dxgkcbmapcontextallocation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	UserDefined
api_location:
-	d3dkmddi.h
api_name:
-	DxgkCbMapContextAllocation
product: Windows
targetos: Windows
req.typenames: DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKCB_MAPCONTEXTALLOCATION callback function
Maps a graphics processing unit (GPU) virtual address to the specified context allocation. This device driver interface (DDI) behaves like its user mode counterpart, see <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_mapgpuvirtualaddresscb.md">pfnMapGpuVirtualAddressCb</a> for more details.

## Syntax

```
DXGKCB_MAPCONTEXTALLOCATION DxgkcbMapcontextallocation;

D3DGPU_VIRTUAL_ADDRESS DxgkcbMapcontextallocation(
  IN_CONST_HANDLE hAdapter,
  IN_CONST_PDXGKARGCB_MAPCONTEXTALLOCATION pArgs
)
{...}
```

## Parameters

`hAdapter`

A handle to the display adapter.

`pArgs`

The <a href="..\d3dkmddi\ns-d3dkmddi-_dxgkargcb_mapcontextallocation.md">DXGKARGCB_MAPCONTEXTALLOCATION</a> structure that describes the operation.


## Return Value

Returns a <b>D3DGPU_VIRTUAL_ADDRESS</b> if successful, <b>NULL</b> otherwise.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Desktop |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkargcb_mapcontextallocation.md">DXGKARGCB_MAPCONTEXTALLOCATION</a>



<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_mapgpuvirtualaddresscb.md">pfnMapGpuVirtualAddressCb</a>