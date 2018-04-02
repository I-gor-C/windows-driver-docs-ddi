---
UID: NS:d3dumddi._DXVADDI_FIXED32
title: "_DXVADDI_FIXED32"
author: windows-driver-content
description: The DXVADDI_FIXED32 structure describes a floating-point number from a 16.16 fixed-point number.
old-location: display\dxvaddi_fixed32.htm
old-project: display
ms.assetid: 4188c488-fda4-4596-96f5-f740a5cc9ffc
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXVA2_Structs_3d19835e-9a75-4d5a-bd6b-451a9978eadb.xml, DXVADDI_FIXED32, DXVADDI_FIXED32 structure [Display Devices], _DXVADDI_FIXED32, d3dumddi/DXVADDI_FIXED32, display.dxvaddi_fixed32
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
-	DXVADDI_FIXED32
product: Windows
targetos: Windows
req.typenames: DXVADDI_FIXED32
---

# _DXVADDI_FIXED32 structure
The DXVADDI_FIXED32 structure describes a floating-point number from a 16.16 fixed-point number.

## Syntax
```
typedef struct _DXVADDI_FIXED32 {
  union {
    struct {
      USHORT Fraction;
      SHORT  Value;
    };
    LONG ll;
  };
} DXVADDI_FIXED32;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff562917">DXVADDI_PROCAMPVALUES</a>