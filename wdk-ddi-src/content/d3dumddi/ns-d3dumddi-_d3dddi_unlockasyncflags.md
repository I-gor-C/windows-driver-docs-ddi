---
UID: NS:d3dumddi._D3DDDI_UNLOCKASYNCFLAGS
title: "_D3DDDI_UNLOCKASYNCFLAGS"
author: windows-driver-content
description: The D3DDDI_UNLOCKASYNCFLAGS structure identifies how to unlock a resource.
old-location: display\d3dddi_unlockasyncflags.htm
old-project: display
ms.assetid: c31e4a4e-7bc7-43a2-8f86-e79012064fa2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_UNLOCKASYNCFLAGS, D3DDDI_UNLOCKASYNCFLAGS structure [Display Devices], D3D_other_Structs_d42c29f4-23e8-4b5c-8710-2e4153c857bf.xml, _D3DDDI_UNLOCKASYNCFLAGS, d3dumddi/D3DDDI_UNLOCKASYNCFLAGS, display.d3dddi_unlockasyncflags
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
-	D3DDDI_UNLOCKASYNCFLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DDDI_UNLOCKASYNCFLAGS
---

# _D3DDDI_UNLOCKASYNCFLAGS structure
The D3DDDI_UNLOCKASYNCFLAGS structure identifies how to unlock a resource.

## Syntax
```
typedef struct _D3DDDI_UNLOCKASYNCFLAGS {
  union {
    struct {
      UINT  : 1  NotifyOnly;
      UINT  : 31 Reserved;
    };
    UINT Value;
  };
} D3DDDI_UNLOCKASYNCFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543394">D3DDDIARG_UNLOCK</a>