---
UID: NS:d3dkmddi._DXGK_OPENALLOCATIONFLAGS
title: "_DXGK_OPENALLOCATIONFLAGS"
author: windows-driver-content
description: The DXGK_OPENALLOCATIONFLAGS structure identifies the operation to perform for allocations.
old-location: display\dxgk_openallocationflags.htm
old-project: display
ms.assetid: 6dae69b1-ff48-4d43-bc01-e7ad7bb7acc9
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_OPENALLOCATIONFLAGS, DXGK_OPENALLOCATIONFLAGS structure [Display Devices], DmStructs_3b5228f0-93fa-434a-b2ca-9007c372d9ed.xml, _DXGK_OPENALLOCATIONFLAGS, d3dkmddi/DXGK_OPENALLOCATIONFLAGS, display.dxgk_openallocationflags
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
-	DXGK_OPENALLOCATIONFLAGS
product:
- Windows
targetos: Windows
req.typenames: DXGK_OPENALLOCATIONFLAGS
---

# _DXGK_OPENALLOCATIONFLAGS structure
The DXGK_OPENALLOCATIONFLAGS structure identifies the operation to perform for allocations.

## Syntax
```
typedef struct _DXGK_OPENALLOCATIONFLAGS {
  union {
    struct {
      UINT  : 1  Create;
      UINT  : 1  ReadOnly;
      UINT  : 30 Reserved;
    };
    UINT Value;
  };
} DXGK_OPENALLOCATIONFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557609">DXGKARG_OPENALLOCATION</a>