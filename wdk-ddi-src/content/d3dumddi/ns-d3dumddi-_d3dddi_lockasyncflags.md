---
UID: NS:d3dumddi._D3DDDI_LOCKASYNCFLAGS
title: "_D3DDDI_LOCKASYNCFLAGS"
author: windows-driver-content
description: The D3DDDI_LOCKASYNCFLAGS structure identifies how to lock a resource.
old-location: display\d3dddi_lockasyncflags.htm
old-project: display
ms.assetid: 0e6dd14c-5192-4c4b-9dcb-716989d24588
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_LOCKASYNCFLAGS, D3DDDI_LOCKASYNCFLAGS structure [Display Devices], D3D_other_Structs_765c2b3d-14e2-4eaf-978f-764263aa2a99.xml, _D3DDDI_LOCKASYNCFLAGS, d3dumddi/D3DDDI_LOCKASYNCFLAGS, display.d3dddi_lockasyncflags
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
-	D3DDDI_LOCKASYNCFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_LOCKASYNCFLAGS
---

# _D3DDDI_LOCKASYNCFLAGS structure
The D3DDDI_LOCKASYNCFLAGS structure identifies how to lock a resource.

## Syntax
```
typedef struct _D3DDDI_LOCKASYNCFLAGS {
  union {
    struct {
      UINT  : 1  NoOverwrite;
      UINT  : 1  Discard;
      UINT  : 1  RangeValid;
      UINT  : 1  AreaValid;
      UINT  : 1  BoxValid;
      UINT  : 1  NoExistingReferences;
      UINT  : 1  NotifyOnly;
      UINT  : 25 Reserved;
    };
    UINT Value;
  };
} D3DDDI_LOCKASYNCFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543213">D3DDDIARG_LOCKASYNC</a>