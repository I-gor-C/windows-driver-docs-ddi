---
UID: NS:d3dukmdt._D3DDDI_CREATECONTEXTFLAGS
title: "_D3DDDI_CREATECONTEXTFLAGS"
author: windows-driver-content
description: The D3DDDI_CREATECONTEXTFLAGS structure describes how to create a context in a call to the pfnCreateContextCb function.
old-location: display\d3dddi_createcontextflags.htm
old-project: display
ms.assetid: e450f85c-4c73-44a8-9d0a-da2c212c87c9
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_CREATECONTEXTFLAGS, D3DDDI_CREATECONTEXTFLAGS structure [Display Devices], D3D_other_Structs_e20f9457-1008-4c63-a924-d5fa75929be5.xml, _D3DDDI_CREATECONTEXTFLAGS, d3dukmdt/D3DDDI_CREATECONTEXTFLAGS, display.d3dddi_createcontextflags
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
-	D3DDDI_CREATECONTEXTFLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DDDI_CREATECONTEXTFLAGS
---

# _D3DDDI_CREATECONTEXTFLAGS structure
The D3DDDI_CREATECONTEXTFLAGS structure describes how to create a context in a call to the <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> function.

## Syntax
```
typedef struct _D3DDDI_CREATECONTEXTFLAGS {
  union {
    struct {
      UINT  : 1  NullRendering;
      UINT  : 1  InitialData;
      UINT  : 1  DisableGpuTimeout;
      UINT  : 1  SynchronizationOnly;
      UINT  : 1  HwQueueSupported;
#if ...
      UINT  : 27 Reserved;
#elif
      UINT  : 28 Reserved;
#else
      UINT  : 30 Reserved;
#endif
    };
    UINT Value;
  };
} D3DDDI_CREATECONTEXTFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544143">D3DDDICB_CREATECONTEXT</a>



<a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a>