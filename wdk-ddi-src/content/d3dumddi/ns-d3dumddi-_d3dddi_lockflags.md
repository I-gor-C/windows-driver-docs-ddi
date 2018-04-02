---
UID: NS:d3dumddi._D3DDDI_LOCKFLAGS
title: "_D3DDDI_LOCKFLAGS"
author: windows-driver-content
description: The D3DDDI_LOCKFLAGS structure identifies how to lock a resource.
old-location: display\d3dddi_lockflags.htm
old-project: display
ms.assetid: b9bc6607-3222-45d0-a0d8-18c815a41771
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_LOCKFLAGS, D3DDDI_LOCKFLAGS structure [Display Devices], D3D_other_Structs_1bff30dd-936f-4753-bcbe-e656c454e675.xml, _D3DDDI_LOCKFLAGS, d3dumddi/D3DDDI_LOCKFLAGS, display.d3dddi_lockflags
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
-	D3DDDI_LOCKFLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DDDI_LOCKFLAGS
---

# _D3DDDI_LOCKFLAGS structure
The D3DDDI_LOCKFLAGS structure identifies how to lock a resource.

## Syntax
```
typedef struct _D3DDDI_LOCKFLAGS {
  union {
    struct {
      UINT  : 1  ReadOnly;
      UINT  : 1  WriteOnly;
      UINT  : 1  NoOverwrite;
      UINT  : 1  Discard;
      UINT  : 1  RangeValid;
      UINT  : 1  AreaValid;
      UINT  : 1  BoxValid;
      UINT  : 1  NotifyOnly;
      UINT  : 1  MightDrawFromLocked;
      UINT  : 1  DoNotWait;
      UINT  : 22 Reserved;
    };
    UINT Value;
  };
} D3DDDI_LOCKFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543204">D3DDDIARG_LOCK</a>