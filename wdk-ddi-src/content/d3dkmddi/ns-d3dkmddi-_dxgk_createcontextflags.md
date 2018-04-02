---
UID: NS:d3dkmddi._DXGK_CREATECONTEXTFLAGS
title: "_DXGK_CREATECONTEXTFLAGS"
author: windows-driver-content
description: The DXGK_CREATECONTEXTFLAGS structure identifies how to create contexts.
old-location: display\dxgk_createcontextflags.htm
old-project: display
ms.assetid: f7cadf78-c908-4034-889d-b5c7d0ffdaad
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_CREATECONTEXTFLAGS, DXGK_CREATECONTEXTFLAGS structure [Display Devices], DmStructs_19418464-77f9-407f-8b04-c6a35561069b.xml, _DXGK_CREATECONTEXTFLAGS, d3dkmddi/DXGK_CREATECONTEXTFLAGS, display.dxgk_createcontextflags
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
-	DXGK_CREATECONTEXTFLAGS
product:
- Windows
targetos: Windows
req.typenames: DXGK_CREATECONTEXTFLAGS
---

# _DXGK_CREATECONTEXTFLAGS structure
The DXGK_CREATECONTEXTFLAGS structure identifies how to create contexts.

## Syntax
```
typedef struct _DXGK_CREATECONTEXTFLAGS {
  union {
    struct {
      UINT  : 1  SystemContext;
      UINT  : 1  GdiContext;
      UINT  : 1  VirtualAddressing;
      UINT  : 1  SystemProtectedContext;
      UINT  : 1  HwQueueSupported;
#if ...
      UINT  : 27 Reserved;
#elif
      UINT  : 28 Reserved;
#elif
      UINT  : 29 Reserved;
#else
      UINT  : 30 Reserved;
#endif
    };
    UINT Value;
  };
} DXGK_CREATECONTEXTFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557567">DXGKARG_CREATECONTEXT</a>



<a href="https://msdn.microsoft.com/aea21a36-f3d5-4541-bd2d-aa026668c562">DxgkDdiCreateContext</a>