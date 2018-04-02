---
UID: NS:d3dkmddi._DXGK_PATCHFLAGS
title: "_DXGK_PATCHFLAGS"
author: windows-driver-content
description: The DXGK_PATCHFLAGS structure identifies, in bit-field flags, information about the direct memory access (DMA) buffer that requires patching.
old-location: display\dxgk_patchflags.htm
old-project: display
ms.assetid: 4052b760-70b0-4418-84f9-1e520a551a03
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_PATCHFLAGS, DXGK_PATCHFLAGS structure [Display Devices], DmStructs_e798cfa4-1915-42c8-87ad-709df6a5555f.xml, _DXGK_PATCHFLAGS, d3dkmddi/DXGK_PATCHFLAGS, display.dxgk_patchflags
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
-	DXGK_PATCHFLAGS
product:
- Windows
targetos: Windows
req.typenames: DXGK_PATCHFLAGS
---

# _DXGK_PATCHFLAGS structure
The DXGK_PATCHFLAGS structure identifies, in bit-field flags, information about the direct memory access (DMA) buffer that requires patching.

## Syntax
```
typedef struct _DXGK_PATCHFLAGS {
  union {
    struct {
      UINT  : 1  Paging;
      UINT  : 1  Present;
      UINT  : 1  RedirectedPresent;
      UINT  : 1  NullRendering;
      UINT  : 28 Reserved;
    };
    UINT Value;
  };
} DXGK_PATCHFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557610">DXGKARG_PATCH</a>



<a href="https://msdn.microsoft.com/363be784-0e3b-4f9a-a643-80857478bbae">DxgkDdiPatch</a>



<a href="https://msdn.microsoft.com/1a46b129-1e78-44e6-a609-59eab206692b">DxgkDdiPresent</a>



<a href="https://msdn.microsoft.com/fd634768-5e1e-4f40-82fd-5ef69148c3d7">DxgkDdiRender</a>