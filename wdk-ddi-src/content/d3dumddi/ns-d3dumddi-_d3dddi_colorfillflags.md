---
UID: NS:d3dumddi._D3DDDI_COLORFILLFLAGS
title: "_D3DDDI_COLORFILLFLAGS"
author: windows-driver-content
description: The D3DDDI_COLORFILLFLAGS structure describes how to color-fill a rectangle on a surface.
old-location: display\d3dddi_colorfillflags.htm
old-project: display
ms.assetid: 672baa43-7fa1-4c10-9d60-c7c8a4729f26
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_COLORFILLFLAGS, D3DDDI_COLORFILLFLAGS structure [Display Devices], D3D_other_Structs_555ecebb-bdd8-4c7f-97cd-801216506b9e.xml, _D3DDDI_COLORFILLFLAGS, d3dumddi/D3DDDI_COLORFILLFLAGS, display.d3dddi_colorfillflags
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
-	D3DDDI_COLORFILLFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_COLORFILLFLAGS
---

# _D3DDDI_COLORFILLFLAGS structure
The D3DDDI_COLORFILLFLAGS structure describes how to color-fill a rectangle on a surface.

## Syntax
```
typedef struct _D3DDDI_COLORFILLFLAGS {
  union {
    struct {
      UINT  : 1  PresentToDwm;
      UINT  : 31 Reserved;
    };
    UINT Value;
  };
} D3DDDI_COLORFILLFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/c120421d-6a10-4d37-b936-98dac75e236b">ColorFill</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542907">D3DDDIARG_COLORFILL</a>