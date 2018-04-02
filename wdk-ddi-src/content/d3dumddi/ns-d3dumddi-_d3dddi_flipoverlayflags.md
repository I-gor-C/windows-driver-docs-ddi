---
UID: NS:d3dumddi._D3DDDI_FLIPOVERLAYFLAGS
title: "_D3DDDI_FLIPOVERLAYFLAGS"
author: windows-driver-content
description: The D3DDDI_FLIPOVERLAYFLAGS structure identifies how to flip a resource on an overlay.
old-location: display\d3dddi_flipoverlayflags.htm
old-project: display
ms.assetid: 09146e6b-3ac0-422a-addb-831394a15c08
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_FLIPOVERLAYFLAGS, D3DDDI_FLIPOVERLAYFLAGS structure [Display Devices], D3D_other_Structs_a62b399d-d553-4325-9f5a-ceb08287d4f4.xml, _D3DDDI_FLIPOVERLAYFLAGS, d3dumddi/D3DDDI_FLIPOVERLAYFLAGS, display.d3dddi_flipoverlayflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
-	d3dumddi.h
api_name:
-	D3DDDI_FLIPOVERLAYFLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DDDI_FLIPOVERLAYFLAGS
---

# _D3DDDI_FLIPOVERLAYFLAGS structure
The D3DDDI_FLIPOVERLAYFLAGS structure identifies how to flip a resource on an overlay.

## Syntax
```
typedef struct _D3DDDI_FLIPOVERLAYFLAGS {
  union {
    struct {
      UINT  : 1  Even;
      UINT  : 1  Odd;
      UINT  : 30 Reserved;
    };
    UINT Value;
  };
} D3DDDI_FLIPOVERLAYFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543124">D3DDDIARG_FLIPOVERLAY</a>