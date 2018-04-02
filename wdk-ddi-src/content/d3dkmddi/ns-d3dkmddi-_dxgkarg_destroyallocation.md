---
UID: NS:d3dkmddi._DXGKARG_DESTROYALLOCATION
title: "_DXGKARG_DESTROYALLOCATION"
author: windows-driver-content
description: The DXGKARG_DESTROYALLOCATION structure describes how the display miniport driver should release allocations.
old-location: display\dxgkarg_destroyallocation.htm
old-project: display
ms.assetid: 0679ade4-9bbd-4bbc-ad2a-46bf35cac645
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGKARG_DESTROYALLOCATION, DXGKARG_DESTROYALLOCATION structure [Display Devices], DmStructs_94f4c3be-d0fc-4a34-8cf4-976b68f89899.xml, _DXGKARG_DESTROYALLOCATION, d3dkmddi/DXGKARG_DESTROYALLOCATION, display.dxgkarg_destroyallocation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGKARG_DESTROYALLOCATION
product:
- Windows
targetos: Windows
req.typenames: DXGKARG_DESTROYALLOCATION
---

# _DXGKARG_DESTROYALLOCATION structure
The DXGKARG_DESTROYALLOCATION structure describes how the display miniport driver should release allocations.

## Syntax
```
typedef struct _DXGKARG_DESTROYALLOCATION {
  UINT                        NumAllocations;
  CONST HANDLE                *pAllocationList;
  HANDLE                      hResource;
  DXGK_DESTROYALLOCATIONFLAGS Flags;
} DXGKARG_DESTROYALLOCATION;
```

## Members


`NumAllocations`

[in] The number of elements in the array that <b>pAllocationList</b> specifies, which represents the number of allocations to release.

`pAllocationList`

[in] An array of handles to the allocations to release.

`hResource`

[in/out] A handle to a resource. The display miniport driver cleans up this handle if it must release the resource along with the allocations.

`Flags`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561045">DXGK_DESTROYALLOCATIONFLAGS</a> structure that identifies how to release the allocations.

## Remarks
The handles in the array that the <b>pAllocationList</b> member specifies are handles to allocations that the driver's <a href="https://msdn.microsoft.com/a28287d6-4dfa-4db4-92df-bbcd9379a5b2">DxgkDdiCreateAllocation</a> function previously returned in the <b>hAllocation</b> members of <a href="https://msdn.microsoft.com/library/windows/hardware/ff560960">DXGK_ALLOCATIONINFO</a> structures, which are part of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557559">DXGKARG_CREATEALLOCATION</a> structure's <b>pAllocationInfo</b> member. Each allocation handle points to a buffer that contains private driver data for the allocation. The display miniport driver must release the memory for the allocations during the call to <a href="https://msdn.microsoft.com/cade544a-f9c6-4635-ab57-d09d694ca315">DxgkDdiDestroyAllocation</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557559">DXGKARG_CREATEALLOCATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560960">DXGK_ALLOCATIONINFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561045">DXGK_DESTROYALLOCATIONFLAGS</a>



<a href="https://msdn.microsoft.com/a28287d6-4dfa-4db4-92df-bbcd9379a5b2">DxgkDdiCreateAllocation</a>



<a href="https://msdn.microsoft.com/cade544a-f9c6-4635-ab57-d09d694ca315">DxgkDdiDestroyAllocation</a>