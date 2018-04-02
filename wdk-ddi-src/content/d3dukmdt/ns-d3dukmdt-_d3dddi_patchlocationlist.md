---
UID: NS:d3dukmdt._D3DDDI_PATCHLOCATIONLIST
title: "_D3DDDI_PATCHLOCATIONLIST"
author: windows-driver-content
description: The D3DDDI_PATCHLOCATIONLIST structure describes the location of an allocation to patch (that is, assign a physical address to the allocation).
old-location: display\d3dddi_patchlocationlist.htm
old-project: display
ms.assetid: 88cdbf2d-4b66-47c1-97e1-e3b8377ac526
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_PATCHLOCATIONLIST, D3DDDI_PATCHLOCATIONLIST structure [Display Devices], D3D_other_Structs_30473342-0122-445f-81c0-9cf5c62c771e.xml, _D3DDDI_PATCHLOCATIONLIST, d3dukmdt/D3DDDI_PATCHLOCATIONLIST, display.d3dddi_patchlocationlist
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dukmdt.h
api_name:
-	D3DDDI_PATCHLOCATIONLIST
product:
- Windows
targetos: Windows
req.typenames: D3DDDI_PATCHLOCATIONLIST
---

# _D3DDDI_PATCHLOCATIONLIST structure
The D3DDDI_PATCHLOCATIONLIST structure describes the location of an allocation to patch (that is, assign a physical address to the allocation).

## Syntax
```
typedef struct _D3DDDI_PATCHLOCATIONLIST {
  UINT  AllocationIndex;
  union {
    struct {
      UINT  : 24 SlotId;
      UINT  : 8  Reserved;
    };
    UINT Value;
  };
  UINT  DriverId;
  UINT  AllocationOffset;
  UINT  PatchOffset;
  UINT  SplitOffset;
} D3DDDI_PATCHLOCATIONLIST;
```

## Members


`AllocationIndex`

[in] An index of the element in the allocation list that specifies the allocation that is referenced by the patch location.

`DriverId`

[in/out] The driver-defined identifier of the allocation specification.

`AllocationOffset`

[in/out] The starting offset, in bytes, within the allocation that is referenced.

`PatchOffset`

[in/out] The offset, in bytes, into the DMA buffer that must be patched.

`SplitOffset`

[in/out] The offset, in bytes, where the DMA buffer must be split if the allocation cannot be brought into video memory.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/ce35bdac-af90-471f-af93-0e665be6c7f6">CreateDevice</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542931">D3DDDIARG_CREATEDEVICE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544241">D3DDDICB_RENDER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544375">D3DDDI_ALLOCATIONLIST</a>



<a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a>