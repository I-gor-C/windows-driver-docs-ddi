---
UID: NS:d3dumddi._D3DDDICB_RENDERFLAGS
title: "_D3DDDICB_RENDERFLAGS"
author: windows-driver-content
description: The D3DDDICB_RENDERFLAGS structure identifies information about a command buffer to be rendered.
old-location: display\d3dddicb_renderflags.htm
old-project: display
ms.assetid: 18ae8ec2-a9e9-40e2-8b11-93fd163a801d
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDICB_RENDERFLAGS, D3DDDICB_RENDERFLAGS structure [Display Devices], D3D_other_Structs_559cfa58-5c9b-470e-aa4b-6c145045ed82.xml, _D3DDDICB_RENDERFLAGS, d3dumddi/D3DDDICB_RENDERFLAGS, display.d3dddicb_renderflags
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
-	D3DDDICB_RENDERFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDICB_RENDERFLAGS
---

# _D3DDDICB_RENDERFLAGS structure
The D3DDDICB_RENDERFLAGS structure identifies information about a command buffer to be rendered.

## Syntax
```
typedef struct _D3DDDICB_RENDERFLAGS {
  union {
    struct {
      UINT  : 1  ResizeCommandBuffer;
      UINT  : 1  ResizeAllocationList;
      UINT  : 1  ResizePatchLocationList;
      UINT  : 1  NullRendering;
      UINT  : 28 Reserved;
    };
    UINT Value;
  };
} D3DDDICB_RENDERFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544241">D3DDDICB_RENDER</a>



<a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a>