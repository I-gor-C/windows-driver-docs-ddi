---
UID: NS:d3dkmddi._DXGK_ALLOCATIONUSAGEINFO1
title: "_DXGK_ALLOCATIONUSAGEINFO1"
author: windows-driver-content
description: The DXGK_ALLOCATIONUSAGEINFO1 structure describes how an allocation can be used in DMA buffering.
old-location: display\dxgk_allocationusageinfo1.htm
old-project: display
ms.assetid: 6de3363c-fcf8-4350-acee-b401bb3f82a6
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_ALLOCATIONUSAGEINFO1, DXGK_ALLOCATIONUSAGEINFO1 structure [Display Devices], DmStructs_262d3b0f-50c6-429b-9b6e-34963d2ae42b.xml, _DXGK_ALLOCATIONUSAGEINFO1, d3dkmddi/DXGK_ALLOCATIONUSAGEINFO1, display.dxgk_allocationusageinfo1
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
-	DXGK_ALLOCATIONUSAGEINFO1
product: Windows
targetos: Windows
req.typenames: DXGK_ALLOCATIONUSAGEINFO1
---

# _DXGK_ALLOCATIONUSAGEINFO1 structure
The DXGK_ALLOCATIONUSAGEINFO1 structure describes how an allocation can be used in DMA buffering.

## Syntax
```
typedef struct _DXGK_ALLOCATIONUSAGEINFO1 {
  union {
    UINT Value;
    struct {
      UINT  : 1  PrivateFormat;
      UINT  : 1  Swizzled;
      UINT  : 1  MipMap;
      UINT  : 1  Cube;
      UINT  : 1  Volume;
      UINT  : 1  Vertex;
      UINT  : 1  Index;
      UINT  : 25 Reserved;
    };
  } Flags;
  union {
    D3DDDIFORMAT Format;
    UINT         PrivateFormat;
  };
  UINT  SwizzledFormat;
  UINT  ByteOffset;
  UINT  Width;
  UINT  Height;
  UINT  Pitch;
  UINT  Depth;
  UINT  SlicePitch;
} DXGK_ALLOCATIONUSAGEINFO1;
```

## Members


`Flags`

[out] A union that contains either a structure (with the first eight members that are described below) or a 32-bit value (in the <b>Value</b> member) that identifies how the allocation is used:



#### Value

Specifies a member in the union contained in the <b>Flags</b> member that can hold one 32-bit value that identifies how the allocation is used.

`SwizzledFormat`

[out] A swizzled format value for the allocation that is private to a specific vendor.

`ByteOffset`

[out] The offset, in bytes, into the video memory manager's allocation that marks the start of the driver's version of the allocation.

`Width`

[out] The width, in pixels, of the allocation.

`Height`

[out] The height, in number of lines, of the allocation.

`Pitch`

[out] The pitch, in bytes, of the allocation--that is, the distance, in bytes, to the start of the next line.

`Depth`

[out] The depth, in levels, of the allocation (for MIP-mapped and volume textures only).

`SlicePitch`

[out] The slice pitch, in bytes, from level to level (for cube and volume textures only).


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557559">DXGKARG_CREATEALLOCATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560960">DXGK_ALLOCATIONINFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560981">DXGK_ALLOCATIONUSAGEHINT</a>



<a href="https://msdn.microsoft.com/a28287d6-4dfa-4db4-92df-bbcd9379a5b2">DxgkDdiCreateAllocation</a>