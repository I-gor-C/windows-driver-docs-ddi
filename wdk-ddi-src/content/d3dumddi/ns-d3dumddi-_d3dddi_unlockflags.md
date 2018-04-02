---
UID: NS:d3dumddi._D3DDDI_UNLOCKFLAGS
title: "_D3DDDI_UNLOCKFLAGS"
author: windows-driver-content
description: The D3DDDI_UNLOCKFLAGS structure identifies how to unlock a resource.
old-location: display\d3dddi_unlockflags.htm
old-project: display
ms.assetid: f3c3356c-ec7b-4869-896d-9d3b285f0e87
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_UNLOCKFLAGS, D3DDDI_UNLOCKFLAGS structure [Display Devices], D3D_other_Structs_c1133d3b-9330-4278-85c7-4083436278cf.xml, _D3DDDI_UNLOCKFLAGS, d3dumddi/D3DDDI_UNLOCKFLAGS, display.d3dddi_unlockflags
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
-	D3DDDI_UNLOCKFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_UNLOCKFLAGS
---

# _D3DDDI_UNLOCKFLAGS structure
The D3DDDI_UNLOCKFLAGS structure identifies how to unlock a resource.

## Syntax
```
typedef struct _D3DDDI_UNLOCKFLAGS {
  union {
    struct {
      UINT  : 1  NotifyOnly;
      UINT  : 31 Reserved;
    };
    UINT Value;
  };
} D3DDDI_UNLOCKFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543394">D3DDDIARG_UNLOCK</a>