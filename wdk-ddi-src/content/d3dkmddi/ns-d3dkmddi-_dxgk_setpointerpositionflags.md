---
UID: NS:d3dkmddi._DXGK_SETPOINTERPOSITIONFLAGS
title: "_DXGK_SETPOINTERPOSITIONFLAGS"
author: windows-driver-content
description: The DXGK_SETPOINTERPOSITIONFLAGS structure identifies, in bit-field flags, information about a mouse pointer.
old-location: display\dxgk_setpointerpositionflags.htm
old-project: display
ms.assetid: c834080a-1a0a-4327-b80b-6e5eb3728605
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_SETPOINTERPOSITIONFLAGS, DXGK_SETPOINTERPOSITIONFLAGS structure [Display Devices], DmStructs_57c5d8e6-b270-4423-8d85-5db8103e2492.xml, _DXGK_SETPOINTERPOSITIONFLAGS, d3dkmddi/DXGK_SETPOINTERPOSITIONFLAGS, display.dxgk_setpointerpositionflags
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
-	DXGK_SETPOINTERPOSITIONFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_SETPOINTERPOSITIONFLAGS
---

# _DXGK_SETPOINTERPOSITIONFLAGS structure
The <b>DXGK_SETPOINTERPOSITIONFLAGS</b> structure identifies, in bit-field flags, information about a mouse pointer.

## Syntax
```
typedef struct _DXGK_SETPOINTERPOSITIONFLAGS {
  union {
    struct {
      UINT  : 1  Visible;
      UINT  : 1  Procedural;
      UINT  : 30 Reserved;
    };
    UINT Value;
  };
} DXGK_SETPOINTERPOSITIONFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557660">DXGKARG_SETPOINTERPOSITION</a>