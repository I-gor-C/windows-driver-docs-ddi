---
UID: NS:d3dkmddi._DXGK_PAGETABLEUPDATEADDRESS
title: "_DXGK_PAGETABLEUPDATEADDRESS"
author: windows-driver-content
description: DXGK_PAGETABLEUPDATEADDRESS contains the address of a page table to update. The member containing the address is defined as part of a DxgkDdiBuildPagingBuffer operation in the DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE structure.
old-location: display\dxgk_pagetableupdateaddress.htm
old-project: display
ms.assetid: 39013276-C76A-4E31-80DD-26C17A020BD6
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGK_PAGETABLEUPDATEADDRESS, DXGK_PAGETABLEUPDATEADDRESS structure [Display Devices], _DXGK_PAGETABLEUPDATEADDRESS, d3dkmddi/DXGK_PAGETABLEUPDATEADDRESS, display.dxgk_pagetableupdateaddress
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_PAGETABLEUPDATEADDRESS
product: Windows
targetos: Windows
req.typenames: DXGK_PAGETABLEUPDATEADDRESS
---

# _DXGK_PAGETABLEUPDATEADDRESS structure
<b>DXGK_PAGETABLEUPDATEADDRESS</b> contains the address of a page table to update. The member containing the address is defined as part of a <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_buildpagingbuffer.md">DxgkDdiBuildPagingBuffer</a> operation in the <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_buildpagingbuffer_updatepagetable.md">DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE</a> structure.

## Syntax
````
typedef struct _DXGK_PAGETABLEUPDATEADDRESS {
  union {
    PVOID                   CpuVirtual;
    D3DGPU_PHYSICAL_ADDRESS GpuPhysical;
    D3DGPU_VIRTUAL_ADDRESS  GpuVirtual;
  };
} DXGK_PAGETABLEUPDATEADDRESS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_buildpagingbuffer_updatepagetable.md">DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_buildpagingbuffer.md">DxgkDdiBuildPagingBuffer</a>